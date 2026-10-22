# -*- coding: utf-8 -*-
"""
English (General American) IPA for glossary terms.
Words come from the CMU Pronouncing Dictionary (pip install cmudict) at BUILD time only;
acronyms are spelled by letter names; the few words the dictionary lacks are listed in OVERRIDES.
"""
import re

try:
    import cmudict
    CMU = cmudict.dict()
except Exception:                       # build-time dependency only
    CMU = {}

ARPA = {
    "AA": "ɑː", "AE": "æ", "AO": "ɔː", "AW": "aʊ", "AY": "aɪ", "B": "b", "CH": "tʃ", "D": "d", "DH": "ð",
    "EH": "ɛ", "EY": "eɪ", "F": "f", "G": "ɡ", "HH": "h", "IH": "ɪ", "JH": "dʒ", "K": "k", "L": "l",
    "M": "m", "N": "n", "NG": "ŋ", "OW": "oʊ", "OY": "ɔɪ", "P": "p", "R": "r", "S": "s", "SH": "ʃ",
    "T": "t", "TH": "θ", "UH": "ʊ", "V": "v", "W": "w", "Y": "j", "Z": "z", "ZH": "ʒ",
}
VOWELS = {"AA", "AE", "AH", "AO", "AW", "AY", "EH", "ER", "EY", "IH", "IY", "OW", "OY", "UH", "UW"}
VALID_ONSETS = {
    "st", "sp", "sk", "str", "spr", "skr", "tr", "pr", "kr", "br", "dr", "ɡr", "fr", "θr", "ʃr",
    "pl", "bl", "kl", "ɡl", "fl", "sl", "sm", "sn", "sw", "tw", "kw", "dw", "ɡw", "spl", "pj", "bj", "kj", "mj", "fj", "vj", "hj", "nj", "tj", "dj",
}
LETTERS = {
    "A": "eɪ", "B": "biː", "C": "siː", "D": "diː", "E": "iː", "F": "ɛf", "G": "dʒiː", "H": "eɪtʃ", "I": "aɪ",
    "J": "dʒeɪ", "K": "keɪ", "L": "ɛl", "M": "ɛm", "N": "ɛn", "O": "oʊ", "P": "piː", "Q": "kjuː", "R": "ɑːr",
    "S": "ɛs", "T": "tiː", "U": "juː", "V": "viː", "W": "ˈdʌbəl juː", "X": "ɛks", "Y": "waɪ", "Z": "ziː",
}
DIGITS = {"0": "oʊ", "1": "wʌn", "2": "tuː", "3": "θriː", "4": "fɔːr", "5": "faɪv", "6": "sɪks", "7": "ˈsɛvən", "8": "eɪt", "9": "naɪn"}

# words that are NOT in the dictionary (or acronyms that are said as words)
OVERRIDES = {
    "bert": "ˈbɜːrt", "mum": "mʌm", "rag": "ræɡ", "serp": "sɜːrp", "umap": "ˈjuːmæp", "silo": "ˈsaɪloʊ",
    "geo": "ˌdʒiː iː ˈoʊ",
    "robots.txt": "ˈroʊbɑːts tɛkst",
    "llm": "ˌɛl ɛl ˈɛm", "llmo": "ˌɛl ɛl ɛm ˈoʊ",
    "pagespeed": "ˈpeɪdʒ spiːd", "genai": "ˈdʒɛn eɪ aɪ", "javascript": "ˈdʒɑːvəskrɪpt",
    "e‑e‑a‑t": "ˌiː iː eɪ ˈtiː", "e-e-a-t": "ˌiː iː eɪ ˈtiː",
    "tf-idf": "ˌtiː ɛf aɪ diː ˈɛf",
    "eav": "ˌiː eɪ ˈviː", "sdi": "ˌɛs diː ˈaɪ",
    "gsc": "ˌdʒiː ɛs ˈsiː",
    "dom": "ˌdiː oʊ ˈɛm",
    "cls": "ˌsiː ɛl ˈɛs", "crp": "ˌsiː ɑːr ˈpiː", "fcp": "ˌɛf siː ˈpiː", "inp": "ˌaɪ ɛn ˈpiː", "lcp": "ˌɛl siː ˈpiː",
    "cwv": "ˌsiː ˈdʌbəl juː ˈviː",
    "paa": "ˌpiː eɪ ˈeɪ", "pbn": "ˌpiː biː ˈɛn", "nlp": "ˌɛn ɛl ˈpiː", "abc": "ˌeɪ biː ˈsiː", "aeo": "ˌeɪ iː ˈoʊ",
    "eta": "ˌiː tiː ˈeɪ", "ai": "ˌeɪ ˈaɪ",
    "async": "ˈeɪsɪŋk", "defer": "dɪˈfɜːr",
    "de-index": "diː ˈɪndɛks",
    "genai)": "ˈdʒɛn eɪ aɪ",
    "hreflang": "ˈeɪtʃ rɛf læŋ",
    "agentic": "eɪˈdʒɛntɪk", "chunking": "ˈtʃʌŋkɪŋ", "citability": "ˌsaɪtəˈbɪləti", "cosine": "ˈkoʊsaɪn",
    "multimodal": "ˌmʌltiˈmoʊdəl", "sitemap": "ˈsaɪtmæp", "upsell": "ˈʌpsɛl", "vitals": "ˈvaɪtəlz",
    "lead": "liːd", "increase": "ˈɪnkriːs", "intent": "ɪnˈtɛnt", "internal": "ɪnˈtɜːrnəl", "query": "ˈkwɪri",
    "contentful": "kənˈtɛntfəl", "engineering": "ˌɛndʒəˈnɪrɪŋ",
    "ahrefs": "ˈeɪrɛfs", "autocomplete": "ˈɔːtoʊkəmˌpliːt", "backlink": "ˈbæklɪŋk", "backlinks": "ˈbæklɪŋks",
    "benchmarking": "ˈbɛntʃmɑːrkɪŋ", "breadcrumbs": "ˈbrɛdkrʌmz", "canonicalization": "kəˌnɑːnəkələˈzeɪʃən",
    "cctld": "ˌsiː siː ˌtiː ɛl ˈdiː", "chatbot": "ˈtʃætbɑːt", "devtools": "ˈdɛv tuːlz", "crawlability": "ˌkrɔːləˈbɪləti",
    "dofollow": "ˈduːˌfɑːloʊ", "googlebot": "ˈɡuːɡəl bɑːt", "gptbot": "ˌdʒiː piː ˈtiː bɑːt", "gtmetrix": "ˌdʒiː tiː ˈmɛtrɪks",
    "heatmap": "ˈhiːtmæp", "hotjar": "ˈhɑːtdʒɑːr", "indexability": "ˌɪndɛksəˈbɪləti", "indexnow": "ˈɪndɛks naʊ",
    "linkable": "ˈlɪŋkəbəl", "listicle": "ˈlɪstɪkəl", "llms.txt": "ˌɛl ɛl ˈɛmz dɑːt ˌtiː ɛks ˈtiː", "mangools": "ˈmæŋɡuːlz",
    "minification": "ˌmɪnəfəˈkeɪʃən", "moz": "mɑːz", "multiregional": "ˌmʌltiˈriːdʒənəl", "nofollow": "ˈnoʊˌfɑːloʊ",
    "noindex": "ˈnoʊˌɪndɛks", "onboarding": "ˈɑːnˌbɔːrdɪŋ", "preload": "ˈpriːloʊd", "prioritization": "praɪˌɔːrətəˈzeɪʃən",
    "rankbrain": "ˈræŋkbreɪn", "regex": "ˈrɛdʒɛks", "rel": "rɛl", "schema.org": "ˈskiːmə dɑːt ɔːrɡ", "copywriting": "ˈkɑːpiˌraɪtɪŋ",
    "semrush": "ˈsɛmrʌʃ", "shopify": "ˈʃɑːpɪfaɪ", "sitebulb": "ˈsaɪtbʌlb", "sitelinks": "ˈsaɪtlɪŋks", "spammy": "ˈspæmi",
    "subdirectory": "ˈsʌbdəˌrɛktəri", "subdomain": "ˈsʌbdoʊˌmeɪn", "touchpoint": "ˈtʌtʃpɔɪnt", "transactional": "trænˈzækʃənəl",
    "transcreation": "ˌtrænskriˈeɪʃən", "unlinked": "ʌnˈlɪŋkt", "upselling": "ˈʌpˌsɛlɪŋ", "wayback": "ˈweɪbæk",
    "webp": "ˈwɛb piː", "whitepaper": "ˈwaɪtˌpeɪpər",
    "a/b": "eɪ biː", "ga4": "ˌdʒiː eɪ ˈfɔːr", "json": "ˈdʒeɪsən", "prospecting": "ˈprɑːspɛktɪŋ",
    "yoy": "ˌwaɪ oʊ ˈwaɪ", "mom": "ˌɛm oʊ ˈɛm", "reconsideration": "ˌriːkənˌsɪdəˈreɪʃən",
    "of": "əv", "for": "fər", "in": "ɪn", "to": "tuː", "out": "aʊt", "up": "ʌp", "and": "ænd",
}
OVERRIDES["robots.txt"] = "ˈroʊbɑːts dɑːt ˌtiː ɛks ˈtiː"


def spell(word):
    return " ".join(LETTERS[c] for c in word.upper() if c in LETTERS)


def arpa_to_ipa(phones):
    # syllable nuclei
    items = []
    for p in phones:
        m = re.match(r"([A-Z]+)(\d?)$", p)
        items.append((m.group(1), m.group(2)))
    out, i, n = [], 0, len(items)
    # find vowel indices
    vidx = [k for k, (b, s) in enumerate(items) if b in VOWELS]
    onset_start = {}
    for vi, k in enumerate(vidx):
        # consonants between previous vowel and this one
        prev = vidx[vi - 1] if vi else -1
        cons = list(range(prev + 1, k))
        if vi == 0:
            start = cons[0] if cons else k
        else:
            # choose the longest valid onset suffix of the cluster (at least 1 consonant)
            start = k
            for j in range(len(cons)):
                chunk = "".join(ARPA[items[c][0]] for c in cons[j:])
                if j == len(cons) - 1 or chunk in VALID_ONSETS:
                    start = cons[j]; break
            if not cons:
                start = k
        onset_start[k] = start
    marks = {}
    for k in vidx:
        s = items[k][1]
        if s == "1": marks[onset_start[k]] = "ˈ"
        elif s == "2": marks[onset_start[k]] = "ˌ"
    res = []
    for k, (b, s) in enumerate(items):
        if k in marks and res:
            res.append(marks[k])
        elif k in marks:
            res.append(marks[k])
        if b == "AH":
            res.append("ʌ" if s in ("1", "2") else "ə")
        elif b == "ER":
            res.append("ɜːr" if s in ("1", "2") else "ər")
        elif b == "IY":
            res.append("iː" if s in ("1", "2") else "i")
        elif b == "UW":
            res.append("uː")
        else:
            res.append(ARPA[b])
    return "".join(res)


def word_ipa(w):
    if w == "Geo":                      # "Geo-targeting" is a word, GEO is spelled out
        return "ˈdʒiːoʊ"
    lw = w.lower()
    if lw in OVERRIDES:
        return OVERRIDES[lw]
    if re.fullmatch(r"\d+", w):
        return " ".join(DIGITS.get(c, c) for c in w)
    if re.fullmatch(r"[A-Z]{2,6}", w):
        return spell(w)                       # unknown capitalised acronym → letter by letter
    if re.fullmatch(r"[A-Za-z]\d", w):        # H1
        return spell(w[0]) + " " + DIGITS[w[1]]
    clean = re.sub(r"[^a-z']", "", lw)
    prons = CMU.get(clean)
    if prons:
        ph = prons[0]
        ipa = arpa_to_ipa(ph)
        if sum(1 for p in ph if re.sub(r"\d", "", p) in VOWELS) == 1:
            ipa = ipa.replace("ˈ", "").replace("ˌ", "")
        return ipa
    return None


def _phrase(ch, missing):
    words = [w for w in ch.split() if w]
    parts = []
    for w in words:
        if w.lower() in OVERRIDES:
            sub = [w]
        else:
            sub = [x for x in re.split(r"(?<=[A-Za-z0-9])-(?=[A-Za-z0-9])", w) if x]
        for x in sub:
            ip = word_ipa(x.strip(".,;:"))
            if ip is None:
                missing.append(x)
                ip = "?"
            parts.append(ip)
    return " ".join(parts)


def _segment(seg, missing):
    """One 'a / b' free segment, with optional Latin parenthetical: 'Core Web Vitals (CWV)'."""
    seg = seg.strip()
    paren = [p for p in re.findall(r"\(([^)]*)\)", seg) if not re.search(r"[А-Яа-яЁё]", p)]
    main = re.sub(r"\([^)]*\)", "", seg).strip()
    out = "/" + _phrase(main, missing) + "/"
    for p in paren:
        out += " (/" + _phrase(p, missing) + "/)"
    return out


def term_ipa(term):
    """'/…/' ; alternatives joined with ' · ' ; 'ACR — Long Name' → '/…/ — /…/'. Returns (text, missing_words)."""
    missing = []
    halves = re.split(r"\s+[—–]\s+", term.strip())
    rendered = []
    for half in halves:
        chunks = [c for c in re.split(r"\s+/\s+", half) if c.strip()]
        rendered.append(" · ".join(_segment(c, missing) for c in chunks))
    return " — ".join(rendered), missing


# ---------------------------------------------------------------- Russian practical transcription (from IPA)
_CYR_TOKENS = [
    ("tʃ", "ч"), ("dʒ", "дж"), ("aɪ", "ай"), ("aʊ", "ау"), ("eɪ", "эй"), ("oʊ", "оу"), ("ɔɪ", "ой"),
    ("ɜːr", "ёр"), ("ər", "ер"), ("ɑːr", "ар"), ("ɔːr", "ор"), ("ɑː", "о"), ("ɔː", "о"), ("iː", "и"), ("uː", "у"),
    ("æ", "э"), ("ɛ", "э"), ("ʌ", "а"), ("ə", "э"), ("ɪ", "и"), ("i", "и"), ("ʊ", "у"),
    ("θ", "ф"), ("ð", "з"), ("ʃ", "ш"), ("ʒ", "ж"), ("ŋ", "нг"),
    ("p", "п"), ("b", "б"), ("t", "т"), ("d", "д"), ("k", "к"), ("ɡ", "г"), ("f", "ф"), ("v", "в"),
    ("s", "с"), ("z", "з"), ("h", "х"), ("m", "м"), ("n", "н"), ("l", "л"), ("r", "р"), ("w", "в"), ("j", "й"),
]


def ipa_word_to_cyr(w):
    w = w.replace("ˈ", "").replace("ˌ", "")
    out, i = [], 0
    while i < len(w):
        ch = w[i]
        if ch == " ":
            out.append(" "); i += 1; continue
        if ch == "j" and w[i + 1:i + 2] == "ə" and out and out[-1] not in " -":   # kjə → кью (document, cumulative)
            out.append("ью"); i += 2; continue
        if ch == "j" and w[i + 1:i + 3] == "uː":          # kjuː → кью, jуː → ю
            out.append("ю" if (not out or out[-1] in " -") else "ью"); i += 3; continue
        for tok, cyr in _CYR_TOKENS:
            if w.startswith(tok, i):
                out.append(cyr); i += len(tok); break
        else:
            out.append(ch); i += 1
    s = "".join(out)
    s = s.replace("нгк", "нк")                              # ŋk → нк (think)
    return s


def _phrase_cyr(ch, missing):
    words = [w for w in ch.split() if w]
    parts = []
    for w in words:
        if w.lower() in OVERRIDES:
            sub = [w]
        else:
            sub = [x for x in re.split(r"(?<=[A-Za-z0-9])-(?=[A-Za-z0-9])", w) if x]
        cy = []
        for x in sub:
            ip = word_ipa(x.strip(".,;:"))
            if ip is None:
                missing.append(x); ip = "?"
            cy.append(ipa_word_to_cyr(ip))
        parts.append("-".join(cy))
    s = " ".join(parts)
    # подряд идущие нули в числах: «500» → «файв о-о», а не «оу оу»
    s = re.sub(r"оу(?: оу)+", lambda m: "-".join(["о"] * (m.group(0).count("оу"))), s)
    return s


def _segment_cyr(seg, missing):
    seg = seg.strip()
    paren = [p for p in re.findall(r"\(([^)]*)\)", seg) if not re.search(r"[А-Яа-яЁё]", p)]
    main = re.sub(r"\([^)]*\)", "", seg).strip()
    out = "/" + _phrase_cyr(main, missing) + "/"
    for p in paren:
        out += " (/" + _phrase_cyr(p, missing) + "/)"
    return out


def term_cyr(term):
    """Practical Cyrillic transcription, e.g. 'Add-on service' → '/эд-он сёрвис/'."""
    missing = []
    halves = re.split(r"\s+[—–]\s+", term.strip())
    rendered = []
    for half in halves:
        chunks = [c for c in re.split(r"\s+/\s+", half) if c.strip()]
        rendered.append(" · ".join(_segment_cyr(c, missing) for c in chunks))
    return " — ".join(rendered), missing
