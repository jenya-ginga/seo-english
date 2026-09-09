import os

ROOT = os.path.dirname(os.path.abspath(__file__))

HEAD_FONTS = '''<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;0,900;1,600&family=PT+Serif:ital,wght@0,400;0,700;1,400&family=Fraunces:opsz,wght@9..144,450;9..144,560;9..144,620;9..144,680&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/style.css">'''

def page(title, desc, brand, eyebrow, h1, lede, navlinks, body, prev_href, prev_label, next_href, next_label, extra_head_hero=""):
    nav_html = "\n      ".join(f'<a class="navlink" href="{href}">{label}</a>' for href, label in navlinks)
    return f'''<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
{HEAD_FONTS}
</head>
<body>

<nav class="topnav">
  <div class="wrap">
    <a href="/" class="brand"><span class="dot"></span>{brand}</a>
    <div class="navlinks">
      {nav_html}
    </div>
  </div>
</nav>

<header class="hero">
  <div class="wrap">
    <div class="eyebrow">{eyebrow}</div>
    <h1>{h1}</h1>
    <p class="lede">{lede}</p>
    {extra_head_hero}
  </div>
</header>

{body}

<footer>
  <div class="wrap footer-row">
    <a href="{prev_href}" class="footer-back">{prev_label}</a>
    <a href="{next_href}" class="footer-next">{next_label}</a>
  </div>
</footer>

</body>
</html>
'''

def section(id_, h2, kicker, inner):
    return f'''<section id="{id_}">
  <div class="wrap">
    <h2>{h2}</h2>
    <p class="section-kicker">{kicker}</p>
    {inner}
  </div>
</section>'''

def info_card(title, sub, chip, idea, en, ru, tags):
    tag_html = "".join(f"<span>{t}</span>" for t in tags)
    return f'''<div class="info-card">
      <div class="info-head"><h3>{title}<small>{sub}</small></h3><span class="chip">{chip}</span></div>
      <p class="idea">{idea}</p>
      <div class="example-block"><span class="en">{en}</span><span class="ru">{ru}</span></div>
      <div class="chips">{tag_html}</div>
    </div>'''

def phrase_card(title, pairs):
    items = "".join(f'<li><span class="en">{en}</span><span class="ru">— {ru}</span></li>' for en, ru in pairs)
    return f'''<div class="phrase-card"><h4>{title}</h4><ul class="phrase-list">{items}</ul></div>'''

def phrase_grid(cards_html_list):
    return f'<div class="phrase-grid">{"".join(cards_html_list)}</div>'

def compare_card(rows):
    # rows: list of (tag, cls, en, ru)
    rows_html = "".join(
        f'<div class="compare-row"><span class="compare-tag {cls}">{tag}</span><span><span class="en">{en}</span><span class="ru">{ru}</span></span></div>'
        for tag, cls, en, ru in rows
    )
    return f'<div class="compare-card">{rows_html}</div>'

def accordion(items, single=False, first_open=True):
    # items: list of dict(title, sub, body_html)
    grid_class = "accordion-grid single" if single else "accordion-grid"
    cards = []
    for i, it in enumerate(items):
        num = f"{i+1:02d}"
        open_attr = " open" if (first_open and i == 0) else ""
        cards.append(f'''<details class="xcard"{open_attr}>
      <summary>
        <span class="xcard-index">{num}</span>
        <span class="xcard-heading"><span class="xcard-title">{it['title']}</span><span class="xcard-sub">{it.get('sub','')}</span></span>
        <span class="xcard-chevron">⌄</span>
      </summary>
      <div class="xcard-body">{it['body']}</div>
    </details>''')
    return f'<div class="{grid_class}">{"".join(cards)}</div>'

def table_scroll(headers, rows):
    th = "".join(f"<th>{h}</th>" for h in headers)
    trs = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="table-scroll"><table><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div>'

def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", path, len(content), "bytes")
