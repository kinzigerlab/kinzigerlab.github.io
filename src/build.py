#!/usr/bin/env python3
"""Build the Kinziger Lab website as one self-contained page.

    python3 build.py            -> site/index.html   (publish it together with site/img/)
    python3 build.py --preview  -> also preview/index.html with local font files
    python3 build.py --release  -> also release/, the public copy with every draft note and tag removed
    python3 src/build.py --repo -> in the website repository, where this file sits in src/: rewrites
                                   index.html at the repository root (photographs live in img/ there)

All text, people and publications live in content.py.
"""
import html
import pathlib
import re
import shutil
import sys
from urllib.parse import quote

import content as C

ROOT = pathlib.Path(__file__).parent


# ----------------------------------------------------------------- helpers
def esc(s):
    return html.escape(str(s), quote=True)


def _link(m):
    label, url = m.group(1), m.group(2)
    rel = ' rel="noopener"' if url.startswith("http") else ""
    return f'<a href="{url}"{rel}>{label}</a>'


def inline(s):
    """Escape, then apply the tiny markup: [label](url), **bold**, *italic*."""
    s = esc(s)
    s = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", _link, s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\*([^*]+)\*", r"<i>\1</i>", s)
    return s


def paras(items, cls=""):
    c = f' class="{cls}"' if cls else ""
    return "\n".join(f"<p{c}>{inline(p)}</p>" for p in items)


def note(text):
    if not text:
        return ""
    return f'<p class="note"><strong>Draft note.</strong> {inline(text)}</p>'


def caption(f):
    where = f'<span class="where">{esc(f["where"])}</span> ' if f.get("where") else ""
    credit = f' <span class="credit">Photo: {esc(f["credit"])}</span>' if f.get("credit") else ""
    return f'{where}{inline(f["caption"])}{credit}'


def img(f, lazy=True, cls=""):
    c = f' class="{cls}"' if cls else ""
    load = ' loading="lazy"' if lazy else ""
    return (f'<img{c} src="img/{esc(f["src"])}" width="{f["w"]}" height="{f["h"]}" '
            f'alt="{esc(f["alt"])}"{load} decoding="async">')


def figure(f, cls="fig"):
    n = note(f["note"]) if f.get("note") else ""
    return f'<figure class="{cls}">{img(f)}<figcaption>{caption(f)}</figcaption>{n}</figure>'


def slot(text):
    """A photo still to come.  Shows only while draft notes are on."""
    return f'<p class="photo-slot is-placeholder"><strong>Photo to come.</strong> {inline(text)}</p>'


def ext(label, url, cls=""):
    c = f' class="{cls}"' if cls else ""
    return f'<a href="{esc(url)}" rel="noopener"{c}>{inline(label)}</a>'


def doi_url(doi):
    return "https://doi.org/" + quote(doi, safe="/:;().-_")


TAGS = {"edna": ("eDNA", "edna"), "gen": ("Genetics", "gen")}


def tag(key):
    label, cls = TAGS[key]
    return f'<span class="tag tag--{cls}">{label}</span>'


def initials(name):
    words = [w for w in re.sub(r"[^A-Za-z .]", "", name).replace(".", " ").split() if w]
    words = [w for w in words if w not in ("Ph", "D", "Dr")]
    return (words[0][0] + words[-1][0]).upper() if len(words) > 1 else words[0][0].upper()


# ----------------------------------------------------------------- icons
ICONS = [
    # bottle of water
    '<path d="M20 6h8M21.5 6v7l-5 7v19a3 3 0 0 0 3 3h9a3 3 0 0 0 3-3V20l-5-7V6"/><path d="M16.5 29c2.6-2 5 2 7.5 0s5-2 7.5 0"/>',
    # filter funnel
    '<path d="M9 8h30L29 22H19L9 8z"/><path d="M19 22v6h10v-6"/><path d="M14 28h20"/><path d="M24 33v3M24 40v2"/>',
    # tube
    '<path d="M14 9h20"/><path d="M17 9v19l7 13 7-13V9"/><path d="M17 25h14"/>',
    # amplification curve
    '<path d="M8 6v34h34"/><path d="M8 36c11 0 13-1 17-12s7-13 17-13"/><path d="M8 25h34" stroke-dasharray="2 3.5"/>',
    # detection history grid
    '<rect x="8" y="8" width="8" height="8" fill="currentColor"/><rect x="20" y="8" width="8" height="8"/><rect x="32" y="8" width="8" height="8" fill="currentColor"/>'
    '<rect x="8" y="20" width="8" height="8"/><rect x="20" y="20" width="8" height="8" fill="currentColor"/><rect x="32" y="20" width="8" height="8" fill="currentColor"/>'
    '<rect x="8" y="32" width="8" height="8" fill="currentColor"/><rect x="20" y="32" width="8" height="8"/><rect x="32" y="32" width="8" height="8"/>',
]


def icon(i):
    return f'<svg viewBox="0 0 48 48" aria-hidden="true" focusable="false">{ICONS[i]}</svg>'


# ----------------------------------------------------------------- publications
KINZIGER_FORMS = [
    "Andrew P Kinziger", "Andrew Kinziger", "Kinziger, A. P.", "Kinziger, A.P.", "Kinziger AP",
    "A.P. Kinziger", "A. P. Kinziger", "A. Kinziger", "Kinziger, A.",
]
ALUM_RE = re.compile(r"\b(Fong|Martel|Sutter|Parker|Wiesenfeld|Schmelzle|Hellmair|McCraney|Hearsey|Goodman|Bandy|Keel|Coyne|Boche|Whitmore|Reneski|Newell|Hinterman|Malakauskas|McGourty|Bridegum|Richardson)\b")
THEME = {k: (label, fam) for k, label, fam in C.THEMES}


def fmt_authors(a):
    s = esc(a)
    for form in KINZIGER_FORMS:
        f = esc(form)
        if f in s:
            s = s.replace(f, f"<strong>{f}</strong>", 1)
            break
    else:
        s = s.replace("Kinziger", "<strong>Kinziger</strong>", 1)
    return ALUM_RE.sub(r'<span class="alum">\1</span>', s)


def pub_link(p):
    if p.get("doi"):
        return f'<a href="{esc(doi_url(p["doi"]))}" rel="noopener">doi:{esc(p["doi"])}</a>'
    if p.get("url"):
        label = "PDF" if p["url"].lower().endswith(".pdf") or "FileHandler" in p["url"] else "Article"
        return ext(label, p["url"])
    return ""


def pub_item(p, first):
    label, fam = THEME[p["theme"]]
    authors = fmt_authors(p["a"])
    stop = "" if p["a"].rstrip().endswith(".") else "."
    details = f' {esc(p["d"])}' if p.get("d") else ""
    meta = [f'<span class="tag tag--{fam}">{label}</span>']
    link = pub_link(p)
    if link:
        meta.append(link)
    for lab, url in p.get("extra", []):
        meta.append(ext(lab, url))
    if p.get("press"):
        press = ", ".join(ext(lab, url) for lab, url in p["press"])
        meta.append(f'<span class="press">In the news: {press}</span>')
    cls = "pub first-of-year" if first else "pub"
    return (
        f'<li class="{cls}" data-theme="{p["theme"]}" data-year="{p["y"]}">'
        f'<span class="pub-year">{p["y"]}</span>'
        f'<div class="pub-body">'
        f'<p class="pub-title">{inline(p["t"])}</p>'
        f'<p class="pub-cite"><span class="pub-authors">{authors}{stop}</span> {p["y"]}. '
        f'<i>{esc(p["j"])}</i>{details}.</p>'
        f'<p class="pub-meta">{" ".join(meta)}</p>'
        f"</div></li>"
    )


def pubs_html():
    out, prev = [], None
    for p in C.PUBLICATIONS:
        out.append(pub_item(p, p["y"] != prev))
        prev = p["y"]
    return "\n".join(out)


def chips_html():
    n = len(C.PUBLICATIONS)
    chips = [f'<button type="button" class="chip" data-filter="all" aria-pressed="true">All<span class="n">{n}</span></button>']
    for key, label, _fam in C.THEMES:
        k = sum(1 for p in C.PUBLICATIONS if p["theme"] == key)
        chips.append(f'<button type="button" class="chip" data-filter="{key}" aria-pressed="false">{label}<span class="n">{k}</span></button>')
    return "\n".join(chips)


# ----------------------------------------------------------------- sections
def home():
    grads = f"{len(C.ALUMNI)} since {min(a['year'] for a in C.ALUMNI)}"
    label_rows = "".join(f"<dt>{esc(k)}</dt><dd>{esc(v or grads)}</dd>" for k, v in C.LABEL)
    steps = []
    for i, (title, text) in enumerate(C.WORKFLOW):
        seq = ""
        if title == "Amplify":
            seq = f'<span class="seq">{esc(C.PRIMER[1])}<code>{esc(C.PRIMER[0])}</code></span>'
        steps.append(
            f'<li class="step"><div class="step-icon">{icon(i)}</div><div class="step-text">'
            f'<h3><span class="n">{i + 1}</span>{esc(title)}</h3><p>{esc(text)}{seq}</p></div></li>'
        )
    pillars = []
    for p in C.PILLARS:
        pillars.append(
            f'<div class="pillar pillar--{p["key"]}"><h3>{esc(p["title"])}</h3><p>{esc(p["text"])}</p>'
            f'<p><a class="link-strong" href="{p["link"][1]}">{esc(p["link"][0])}</a></p></div>'
        )
    places = []
    for name, text, tags, _ in C.PLACES:
        places.append(
            f'<li><span class="place">{esc(name)}</span><p>{esc(text)}</p>'
            f'<span class="tags">{"".join(tag(t) for t in tags)}</span></li>'
        )
    latest = []
    for p in C.PUBLICATIONS[:5]:
        href = doi_url(p["doi"]) if p.get("doi") else p.get("url", "#publications")
        latest.append(
            f'<li><a href="{esc(href)}" rel="noopener">{inline(p["t"])}</a>'
            f'<span class="meta"><i>{esc(p["j"])}</i>, {p["y"]}</span></li>'
        )
    theses = []
    for a in C.ALUMNI[:4]:
        theses.append(
            f'<li><a href="{esc(a["url"])}" rel="noopener">{inline(a["thesis"])}</a>'
            f'<span class="meta">{esc(a["name"])}, M.S. {a["year"]}</span></li>'
        )
    return f"""
<section class="view" id="home" data-view="home" aria-label="Home">
  <div class="wrap hero">
    <div>
      <h1>{esc(C.HERO["h1"])}</h1>
      <p class="lede">{esc(C.HERO["lede"])}</p>
      <p class="actions"><a class="btn" href="#research">See our research</a> <a class="link-strong" href="#join">Join the lab</a></p>
    </div>
    <div class="label-card">
      <p class="org">Cal Poly Humboldt</p>
      <p class="dept">Department of Fisheries Biology</p>
      <dl>{label_rows}</dl>
    </div>
  </div>

  <figure class="photo-band">
    {img(C.HOME_PHOTO, lazy=False)}
    <figcaption class="wrap"><p>{caption(C.HOME_PHOTO)}</p>{note(C.HOME_PHOTO.get("note"))}</figcaption>
  </figure>

  <div class="flow">
    <div class="wrap">
      <div class="flow-head">
        <h2>How environmental DNA works</h2>
        <p class="lede">{esc(C.WORKFLOW_INTRO)}</p>
      </div>
      <ol class="steps">
        {"".join(steps)}
      </ol>
    </div>
  </div>

  <div class="wrap">
    <div class="band">
      <div class="band-head"><h2>What we study</h2></div>
      <div class="pillars">{"".join(pillars)}</div>
    </div>

    <div class="band">
      <div class="band-head"><h2>Where we work</h2><p>{esc(C.PLACES_SUB)}</p></div>
      <div>
        <ul class="places">{"".join(places)}</ul>
        {note(C.PLACES_NOTE)}
      </div>
    </div>

    <div class="band">
      <div class="band-head"><h2>Recent work</h2></div>
      <div class="cols-2">
        <div class="mini"><h3>Latest papers</h3><ul>{"".join(latest)}</ul>
          <p class="more"><a class="link-strong" href="#publications">All publications</a></p></div>
        <div class="mini"><h3>Recently finished theses</h3><ul>{"".join(theses)}</ul>
          <p class="more"><a class="link-strong" href="#alumni">All lab alumni</a></p></div>
      </div>
    </div>

    <div class="band">
      <div class="band-head"><h2>Prospective students</h2></div>
      <div class="prose">
        <p class="lede">Applications for fall admission to the Natural Resources M.S. program close on February 1. If your research interests match the lab's work, let Andrew know.</p>
        <p><a class="btn" href="#join">How to join the lab</a></p>
      </div>
    </div>
  </div>
</section>"""


def strip(f):
    """Three photographs in sequence, each with a step name, under one caption."""
    items = "".join(
        f'<li>{img(p)}<span class="strip-step">{esc(p["step"])}</span></li>' for p in f["photos"]
    )
    credit = f' <span class="credit">Photos: {esc(f["credit"])}</span>' if f.get("credit") else ""
    n = note(f["note"]) if f.get("note") else ""
    return (f'<figure class="strip"><ol>{items}</ol>'
            f'<figcaption>{inline(f["caption"])}{credit}</figcaption>{n}</figure>')


def topic_html(t):
    refs = ", ".join(ext(lab, url) for lab, url in t["refs"])
    n = note(t["note"]) if t.get("note") else ""
    pic = figure(t["figure"]) if t.get("figure") else ""
    pic += slot(t["slot"]) if t.get("slot") else ""
    return (
        f'<article class="topic"><h3>{esc(t["title"])}</h3><div class="topic-body">'
        f'{pic}{paras(t["body"])}{n}<p class="refs">Read more: {refs}</p></div></article>'
    )


def research():
    current = "".join(f"<li>{esc(x)}</li>" for x in C.CURRENT)
    partners = "".join(f"<li>{esc(x)}</li>" for x in C.PARTNERS)
    tools = "".join(f"<li>{esc(x)}</li>" for x in C.TOOLS)
    return f"""
<section class="view" id="research" data-view="research" aria-label="Research">
  <div class="wrap">
    <div class="page-head head-split">
      <div>
        <h1>Research</h1>
        <p class="lede">{esc(C.RESEARCH_INTRO)}</p>
        <p class="jump">Jump to <a href="#edna">environmental DNA</a>, <a href="#genetics">conservation genetics and genomics</a> or <a href="#partners">working with us</a>.</p>
      </div>
      <div class="now">
        <h2>Under way now</h2>
        <ul>{current}</ul>
        {note(C.CURRENT_NOTE)}
      </div>
    </div>

    <div class="part part--edna" id="edna">
      <h2>Environmental DNA</h2>
      <p class="lede">{esc(C.EDNA_LEDE)}</p>
      {strip(C.EDNA_STRIP)}
    </div>
    {"".join(topic_html(t) for t in C.EDNA_TOPICS)}

    <div class="part part--gen" id="genetics">
      <h2>Conservation genetics and genomics</h2>
      <p class="lede">{esc(C.GEN_LEDE)}</p>
    </div>
    {"".join(topic_html(t) for t in C.GEN_TOPICS)}

    <div class="part part--plain" id="partners">
      <h2>Working with us</h2>
    </div>
    <article class="topic">
      <h3>For agencies, Tribes and organizations</h3>
      <div class="topic-body">
        {paras(C.PARTNER_TEXT)}
        <p><a class="link-strong" href="#contact">Contact the lab</a></p>
      </div>
    </article>
    <article class="topic">
      <h3>Partners and funders</h3>
      <div class="topic-body">
        <ul class="plain-list">{partners}</ul>
        {note(C.PARTNER_NOTE)}
      </div>
    </article>
    <article class="topic">
      <h3>In the lab</h3>
      <div class="topic-body"><ul class="plain-list">{tools}</ul></div>
    </article>
  </div>
</section>"""


def people():
    pi = C.PI
    roles = "".join(f"<li>{esc(r)}</li>" for r in pi["roles"])
    edu = "".join(f"<dt>{esc(k)}</dt><dd>{esc(v)}</dd>" for k, v in pi["education"])
    courses = "".join(f"<li>{esc(c)}</li>" for c in pi["courses"])
    c = C.CONTACT
    rooms = "".join(f"<li>{esc(k)}: {esc(v)}</li>" for k, v in c["rooms"])
    members = []
    for m in C.MEMBERS:
        ph = m["status"] == "placeholder"
        chip = '<span class="confirm">confirm</span>' if m["status"] == "confirm" else ""
        mono = "" if ph else initials(m["name"])
        members.append(
            f'<li class="{"is-placeholder" if ph else ""}"><span class="mono" aria-hidden="true">{mono}</span>'
            f'<span><span class="name">{esc(m["name"])}{chip}</span><span class="role">{esc(m["role"])}</span></span>'
            f'<span class="proj">{esc(m["project"])}</span></li>'
        )
    alumni = []
    dots = {"edna": ("dot dot--edna", "eDNA thesis"), "gen": ("dot dot--gen", "Genetics thesis"), "": ("dot", "")}
    for a in C.ALUMNI:
        dcls, dlabel = dots[a["theme"]]
        sr = f'<span class="sr">{dlabel}: </span>' if dlabel else ""
        after = esc(a["after"])
        who = '<span class="confirm">confirm</span>' if a.get("confirm") else ""
        if a.get("after_confirm"):
            after += '<span class="confirm">confirm</span>'
        alumni.append(
            f'<li><span class="yr">{a["year"]}</span><span class="name">{esc(a["name"])}{who}</span>'
            f'<span class="thesis"><span class="{dcls}" aria-hidden="true"></span>{sr}'
            f'<a href="{esc(a["url"])}" rel="noopener">{inline(a["thesis"])}</a></span>'
            f'<span class="after">{after}</span></li>'
        )
    return f"""
<section class="view" id="people" data-view="people" aria-label="People">
  <div class="wrap">
    <div class="page-head">
      <h1>People</h1>
      <p class="lede">A principal investigator, graduate students in the Natural Resources M.S. program, and undergraduates who learn the lab from the bench up.</p>
      {note(C.PEOPLE_NOTE)}
    </div>

    <div class="band pi">
      <figure class="portrait">{img(pi["photo"])}<figcaption>Photo: {esc(pi["photo"]["credit"])}</figcaption></figure>
      <div>
        <h2>{esc(pi["name"])}</h2>
        <ul class="roles">{roles}</ul>
        <div class="prose">{paras(pi["bio"])}</div>
        <div class="facts">
          <div><h3>Education</h3><dl>{edu}</dl></div>
          <div><h3>Courses</h3><ul>{courses}</ul></div>
          <div><h3>Contact</h3><ul><li><a href="mailto:{esc(c["email"])}">{esc(c["email"])}</a></li><li>{esc(c["phone"])}</li>{rooms}</ul></div>
        </div>
      </div>
    </div>

    <div class="band">
      <div class="band-head"><h2>Current members</h2></div>
      <div>
        {note(C.MEMBERS_NOTE)}
        <ul class="roster">{"".join(members)}</ul>
      </div>
    </div>

    <div class="band" id="alumni">
      <div class="band-head"><h2>Lab alumni</h2>
        <p>{len(C.ALUMNI)} M.S. graduates, newest first.</p>
        <p class="legend"><span class="dot dot--edna" aria-hidden="true"></span>eDNA thesis<br><span class="dot dot--gen" aria-hidden="true"></span>Genetics thesis</p>
      </div>
      <div>
        {note(C.ALUMNI_NOTE)}
        <ul class="alumni">
          <li class="alumni-head" aria-hidden="true"><span>Year</span><span>Graduate</span><span>Thesis</span><span>After the lab</span></li>
          {"".join(alumni)}
        </ul>
      </div>
    </div>
  </div>
</section>"""


def publications():
    n = len(C.PUBLICATIONS)
    return f"""
<section class="view" id="publications" data-view="publications" aria-label="Publications">
  <div class="wrap">
    <div class="page-head">
      <h1>Publications</h1>
      <p class="lede">{n} papers since 1997. <span class="alum">Underlined</span> names are students and alumni of the lab.</p>
      {note(C.PUBS_NOTE)}
    </div>

    <div class="pub-tools">
      <div class="chips" role="group" aria-label="Filter by theme">
        {chips_html()}
      </div>
      <label class="pub-search" for="pubq">Search <input id="pubq" type="search" placeholder="goby, lamprey, Klamath" autocomplete="off"></label>
    </div>
    <p class="pub-count" id="pubcount" aria-live="polite">Showing all {n} papers</p>
    <p class="pub-empty" id="pubempty" hidden>No papers match. Clear the search or choose All.</p>
    <ol class="pubs" id="publist">
      {pubs_html()}
    </ol>

    <p class="more">Student theses are listed with <a href="#alumni">lab alumni</a>.</p>
  </div>
</section>"""


def join():
    steps = "".join(f"<li><h3>{esc(t)}</h3><p>{inline(x)}</p></li>" for t, x in C.JOIN_STEPS)
    rows = "".join(f'<tr><th scope="row">{esc(k)}</th><td>{esc(v)}</td></tr>' for k, v in C.DEADLINES)
    return f"""
<section class="view" id="join" data-view="join" aria-label="Join the lab">
  <div class="wrap">
    <div class="page-head head-split">
      <div>
        <h1>Join the lab</h1>
        <p class="lede">{esc(C.JOIN_INTRO)}</p>
      </div>
      {figure(C.JOIN_PHOTO)}
    </div>

    <div class="band">
      <div class="band-head"><h2>Graduate students</h2></div>
      <div>
        <ul class="join-list">{steps}</ul>
      </div>
    </div>

    <div class="band">
      <div class="band-head"><h2>Deadlines</h2></div>
      <div>
        <table class="deadlines"><tbody>{rows}</tbody></table>
        <p class="refs">Source: {ext(C.DEADLINES_SRC[0], C.DEADLINES_SRC[1])}</p>
      </div>
    </div>

    <div class="band">
      <div class="band-head"><h2>Funding</h2></div>
      <div class="prose"><p>{esc(C.FUNDING)}</p>{note(C.JOIN_NOTE)}</div>
    </div>

    <div class="band">
      <div class="band-head"><h2>Undergraduates</h2></div>
      <div class="prose"><p>{esc(C.UNDERGRAD)}</p></div>
    </div>
  </div>
</section>"""


def footer():
    c = C.CONTACT
    lines = "".join(f"<p>{esc(x)}</p>" for x in c["lines"])
    rooms = "".join(f"<p>{esc(k)}: {esc(v)}</p>" for k, v in c["rooms"])
    links = "".join(f"<li>{ext(lab, url)}</li>" for lab, url in c["links"])
    return f"""
<footer class="site-footer" id="contact">
  <div class="wrap">
    <div>
      <h2>Contact</h2>
      <p>{esc(c["name"])}</p>
      {lines}
    </div>
    <div>
      <h3>Find us</h3>
      {rooms}
      <p>Phone: {esc(c["phone"])}</p>
      <p>Email: <a href="mailto:{esc(c["email"])}">{esc(c["email"])}</a></p>
    </div>
    <div>
      <h3>At Cal Poly Humboldt</h3>
      <ul>{links}</ul>
    </div>
    <p class="fine">The Kinziger Lab, Department of Fisheries Biology, Cal Poly Humboldt. Last updated {esc(C.UPDATED)}.</p>
  </div>
</footer>"""


# ----------------------------------------------------------------- page shell
CSS = (ROOT / "style.css").read_text()
JS = (ROOT / "site.js").read_text()

FONT_LINKS = """<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Libre+Caslon+Display&amp;family=Libre+Caslon+Text:ital,wght@0,400;0,700;1,400&amp;family=Libre+Franklin:ital,wght@0,300..700;1,300..700&amp;display=swap">"""

F = (ROOT / "fonts" / "node_modules").as_uri()
FONT_LOCAL = f"""<style>
@font-face{{font-family:"Libre Caslon Text";font-style:normal;font-weight:400;src:url("{F}/@fontsource/libre-caslon-text/files/libre-caslon-text-latin-400-normal.woff2") format("woff2")}}
@font-face{{font-family:"Libre Caslon Text";font-style:italic;font-weight:400;src:url("{F}/@fontsource/libre-caslon-text/files/libre-caslon-text-latin-400-italic.woff2") format("woff2")}}
@font-face{{font-family:"Libre Caslon Text";font-style:normal;font-weight:700;src:url("{F}/@fontsource/libre-caslon-text/files/libre-caslon-text-latin-700-normal.woff2") format("woff2")}}
@font-face{{font-family:"Libre Caslon Display";font-style:normal;font-weight:400;src:url("{F}/@fontsource/libre-caslon-display/files/libre-caslon-display-latin-400-normal.woff2") format("woff2")}}
@font-face{{font-family:"Libre Franklin";font-style:normal;font-weight:100 900;src:url("{F}/@fontsource-variable/libre-franklin/files/libre-franklin-latin-wght-normal.woff2") format("woff2")}}
@font-face{{font-family:"Libre Franklin";font-style:italic;font-weight:100 900;src:url("{F}/@fontsource-variable/libre-franklin/files/libre-franklin-latin-wght-italic.woff2") format("woff2")}}
</style>"""

NAV = [("research", "Research"), ("people", "People"), ("publications", "Publications"), ("join", "Join the lab")]


COUNTER_FILE = "count.v5.js"   # GoatCounter's counter script, version 5, kept beside index.html


def counter_tag(on):
    """The visit counter. Only the public copy in the repository carries it; drafts and previews do not."""
    code = getattr(C, "GOATCOUNTER", "")
    if not (on and code):
        return ""
    assert re.fullmatch(r"[a-z0-9][a-z0-9-]*", code), code
    return (f'<script data-goatcounter="https://{code}.goatcounter.com/count" '
            f"data-goatcounter-settings='{{\"no_onload\": true}}' async src=\"{COUNTER_FILE}\"></script>\n")


def page(fonts, counter=False):
    nav = "".join(f'<li><a href="#{k}" data-nav="{k}">{esc(v)}</a></li>' for k, v in NAV)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light dark">
<title>The Kinziger Lab</title>
<meta name="description" content="The Kinziger Lab at Cal Poly Humboldt uses environmental DNA and genetics to monitor and conserve the fishes of California's North Coast.">
{fonts}
<script>document.documentElement.classList.add("js");</script>
<style>
{CSS}
</style>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="draftbar" id="draftbar">
  <div class="wrap">
    <p><strong>Draft for review.</strong> Amber notes mark things to confirm. They are not part of the site.</p>
    <button type="button" id="notes-toggle" aria-pressed="true">Hide notes</button>
  </div>
</div>
<header class="site-header">
  <div class="wrap">
    <a class="wordmark" href="#home" data-nav="home">The Kinziger Lab<small>eDNA and fish conservation genetics</small></a>
    <nav aria-label="Main"><ul class="nav">{nav}</ul></nav>
  </div>
</header>
<main id="main">
{home()}
{research()}
{people()}
{publications()}
{join()}
</main>
{footer()}
<script>
{JS}
</script>
{counter_tag(counter)}</body>
</html>
"""


def strip_draft(h):
    """The public copy: no draft bar, no notes, no confirm tags, no photo slots."""
    h, n = re.subn(r'<div class="draftbar" id="draftbar">.*?</div>\s*</div>\s*', "", h, count=1, flags=re.S)
    assert n == 1, "draft bar not found"
    h = re.sub(r'\s*<p class="note">.*?</p>', "", h, flags=re.S)
    h = re.sub(r'\s*<span class="confirm">.*?</span>', "", h, flags=re.S)
    h = re.sub(r'\s*<p class="photo-slot is-placeholder">.*?</p>', "", h, flags=re.S)
    for marker in ('class="note"', 'class="confirm"', 'id="draftbar"', 'id="notes-toggle"', "Draft note", "Draft for review"):
        assert marker not in h, marker
    return h


def main():
    if "--repo" in sys.argv:
        # Repository layout: this file sits in src/ and the website is the repository root.
        top = ROOT.parent
        public = strip_draft(page(FONT_LINKS, counter=True))
        (top / "index.html").write_text(public, encoding="utf-8")
        (top / ".nojekyll").write_text("", encoding="utf-8")   # GitHub Pages: serve the files as they are
        used = sorted(set(re.findall(r'src="img/([^"]+)"', public)))
        missing = [n for n in used if not (top / "img" / n).exists()]
        if COUNTER_FILE in public and not (top / COUNTER_FILE).exists():
            missing.append(COUNTER_FILE + " (beside index.html)")
        print(f"wrote {top / 'index.html'}  ({len(public) / 1024:.0f} KB); photographs used: {len(used)}; "
              f"missing from img/: {', '.join(missing) if missing else 'none'}")
        return
    out = ROOT / "site" / "index.html"
    out.parent.mkdir(exist_ok=True)
    html_out = page(FONT_LINKS)
    clean = 'class="note"' not in html_out and 'class="confirm"' not in html_out
    if clean:
        html_out = strip_draft(html_out)   # nothing left to review, so no draft bar either
    out.write_text(html_out, encoding="utf-8")
    print(f"wrote {out}  ({out.stat().st_size / 1024:.0f} KB)" + ("  [no draft notes left]" if clean else ""))
    if "--preview" in sys.argv:
        prev = ROOT / "preview" / "index.html"
        prev.parent.mkdir(exist_ok=True)
        prev.write_text(strip_draft(page(FONT_LOCAL)) if clean else page(FONT_LOCAL), encoding="utf-8")
        link = prev.parent / "img"
        if not link.exists():
            link.symlink_to(out.parent / "img", target_is_directory=True)
        print(f"wrote {prev}")
    if "--release" in sys.argv:
        rel = ROOT / "release"
        (rel / "img").mkdir(parents=True, exist_ok=True)
        public = strip_draft(page(FONT_LINKS))
        (rel / "index.html").write_text(public, encoding="utf-8")
        (rel / ".nojekyll").write_text("", encoding="utf-8")   # GitHub Pages: serve the files as they are
        used = set(re.findall(r'src="img/([^"]+)"', public))
        for old in (rel / "img").iterdir():
            if old.name not in used:
                old.unlink()
        for name in sorted(used):
            shutil.copy2(out.parent / "img" / name, rel / "img" / name)
        print(f"wrote {rel}/index.html  ({len(public) / 1024:.0f} KB) and {len(used)} images")
        if "--preview" in sys.argv:
            (ROOT / "preview" / "release.html").write_text(strip_draft(page(FONT_LOCAL)), encoding="utf-8")


if __name__ == "__main__":
    main()
