"""Единая шапка сайта. Используется build.page(), gen_home и CLI-скриптом:
    python3 generator/sitenav.py   — переписывает шапку во всех готовых *.html
"""
import os, re, sys

MAIN = [
    ("/#lessons", "Уроки", "/lessons/"),
    ("/glossary/", "Глоссарий", "/glossary/"),
    ("/phrasebook/", "Разговорник", "/phrasebook/"),
    ("/games/", "Игровая", "/games/"),
    ("/game/", "Тренажёр", "/game/"),
]
BRAND = "Global English для SEO"


def site_head(path, sub=()):
    """path — URL страницы ('/', '/glossary/', '/lessons/3/'); sub — [(href, label)] якоря внутри страницы."""
    links = []
    for href, label, prefix in MAIN:
        h = href[1:] if (path == "/" and href.startswith("/#")) else href
        cur = ' aria-current="page"' if (path != "/" and path.startswith(prefix)) else ""
        links.append(f'<a class="navlink" href="{h}"{cur}>{label}</a>')
    nav = "\n      ".join(links)
    subnav = ""
    if len(sub) >= 2:  # одна ссылка-якорь не нужна
        items = "\n      ".join(f'<a href="{h}">{l}</a>' for h, l in sub)
        subnav = f'''
  <nav class="subnav" aria-label="На этой странице">
    <div class="wrap wide">
      {items}
    </div>
  </nav>'''
    return f'''<div class="site-head">
  <nav class="topnav">
    <div class="wrap wide">
      <a href="/" class="brand"><span class="dot"></span>{BRAND}</a>
      <div class="navlinks">
      {nav}
      </div>
    </div>
  </nav>{subnav}
</div>'''


NAV_RE = re.compile(r'(?:<div class="site-head">\s*)?<nav class="topnav">.*?</nav>(?:\s*<nav class="subnav".*?</nav>)?(?:\s*</div>)?', re.S)


def main(root):
    n = 0
    for dp, dn, fn in os.walk(root):
        if ".git" in dp or "node_modules" in dp:
            continue
        for f in fn:
            if f != "index.html":
                continue
            p = os.path.join(dp, f)
            t = open(p, encoding="utf-8").read()
            m = re.search(r'<nav class="topnav">.*?</nav>', t, re.S)
            if not m:
                continue
            old = m.group(0)
            sub = re.findall(r'<a class="navlink" href="(#[^"]+)">([^<]+)</a>', old)
            sm = re.search(r'<nav class="subnav".*?</nav>', t, re.S)
            if sm:
                sub = re.findall(r'<a href="(#[^"]+)">([^<]+)</a>', sm.group(0))
            rel = os.path.relpath(dp, root).replace(os.sep, "/")
            path = "/" if rel == "." else f"/{rel}/"
            if path in ("/", "/gazette/"):
                sub = []  # главная и газета: меню уже глобальное
            # старый блок (включая уже применённую шапку) -> новый
            t2 = re.sub(r'<div class="site-head">.*?</nav>\s*(?:<nav class="subnav".*?</nav>\s*)?</div>', "@@HEAD@@", t, count=1, flags=re.S)
            if "@@HEAD@@" not in t2:
                t2 = t.replace(old, "@@HEAD@@", 1)
            t2 = t2.replace("@@HEAD@@", site_head(path, sub), 1)
            if t2 != t:
                open(p, "w", encoding="utf-8").write(t2)
                n += 1
    print("шапка обновлена в", n, "файлах")


if __name__ == "__main__":
    main(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
