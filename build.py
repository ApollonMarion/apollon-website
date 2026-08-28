#!/usr/bin/env python3
# Baut die Apollon-Seiten aus einer gemeinsamen Vorlage.
import os, io, base64, shutil
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = HERE

# Schriften liegen auf dem eigenen Server. Keine Verbindung zu Google,
# deshalb auch kein Cookie-Banner noetig.
FONTS = ('<link rel="stylesheet" href="assets/schriften.css">'
         '<link rel="preload" href="assets/fonts/karla-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>'
         '<link rel="preload" href="assets/fonts/cormorant-garamond-latin-600-normal.woff2" as="font" type="font/woff2" crossorigin>')

NAV = [
    ("wissen.html", "Wissen", []),
    ("blog.html", "Blog", []),
    ("entscheidung.html", "Apollon", [("entscheidung.html", "Wenn eine Entscheidung ansteht"), ("bodenplatte.html", "Die Bodenplatte"), ("denkkreis.html", "Der Denkkreis")]),
    ("vereinsheim.html", "Vereinsheim", []),
    ("buch.html", "Buch", []),
    ("ausstieg.html", "WIB", [("ausstieg.html", "Der feminine Ausstieg"),
                              ("ausstieg-bewerbung.html", "Bewerbung"),
                              ("ausstieg-impulsbuch.html", "Impulsbuch"),
                              ("konvaleszenz.html", "Konvaleszenz")]),
]

def nav_mobil(current):
    """Dasselbe Menue fuer das Handy, flach untereinander."""
    out = []
    for href, label, kids in NAV:
        cur = ' aria-current="page"' if current == href else ''
        if kids:
            out.append('<span class="gruppe">%s</span>' % label)
            for k_href, k_label in kids:
                c = ' aria-current="page"' if current == k_href else ''
                out.append('<a class="unter" href="%s"%s>%s</a>' % (k_href, c, k_label))
        else:
            out.append('<a href="%s"%s>%s</a>' % (href, cur, label))
    out.append('<a class="hervor" href="gespraech.html">Gespräch vereinbaren</a>')
    return "".join(out)


def nav_html(current):
    out = []
    for href, label, kids in NAV:
        cur = ' aria-current="page"' if current in [href] + [k[0] for k in kids] else ''
        if kids:
            sub = "".join('<a href="%s">%s</a>' % k for k in kids)
            out.append('<span class="item has"><a class="link" href="%s"%s>%s</a><span class="submenu">%s</span></span>' % (href, cur, label, sub))
        else:
            out.append('<span class="item"><a class="link" href="%s"%s>%s</a></span>' % (href, cur, label))
    return "".join(out)

def _v(pfad):
    """Kurzer Stempel aus dem Dateiinhalt, damit Browser Aenderungen sofort sehen."""
    import hashlib
    try:
        with open(os.path.join(OUT, pfad), "rb") as f:
            return hashlib.md5(f.read()).hexdigest()[:8]
    except OSError:
        return "1"


HEAD = """<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="assets/apollon.css?v={vcss}">
<link rel="icon" href="favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="assets/favicon-32.png">
<link rel="icon" type="image/png" sizes="16x16" href="assets/favicon-16.png">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<meta name="theme-color" content="#022144">
{fonts}
{schema}
</head>
<body>
<div class="topbar"><div class="inner">
  <a class="brandmark" href="index.html"><img src="assets/schwan.svg" alt="" width="34" height="34"><span class="wm">APOLLON</span></a>
  <nav class="main" aria-label="Hauptnavigation">{nav}</nav>
  <button class="burger" type="button" aria-expanded="false" aria-controls="handymenu" aria-label="Menü öffnen"><span></span><span></span><span></span></button>
  <a class="cta-btn" href="gespraech.html">Gespräch vereinbaren</a>
</div>
<nav class="handymenu" id="handymenu" aria-label="Menü">{navmobil}</nav>
</div>
<script>
(function(){{
  var k = document.querySelector('.burger'), m = document.getElementById('handymenu');
  if (!k || !m) return;
  k.addEventListener('click', function(){{
    var offen = m.classList.toggle('offen');
    k.classList.toggle('zu', offen);
    k.setAttribute('aria-expanded', offen ? 'true' : 'false');
    k.setAttribute('aria-label', offen ? 'Menü schließen' : 'Menü öffnen');
  }});
  document.addEventListener('keydown', function(e){{
    if (e.key === 'Escape' && m.classList.contains('offen')) k.click();
  }});
}})();
</script>
<main>
"""

FOOT = """</main>
<footer><div class="wrap">
  <div class="footcols">
    <div>
      <h4 style="letter-spacing:.24em;font-size:1rem">APOLLON</h4>
      <p style="margin-top:.6rem;max-width:26rem">Entwicklung beginnt beim Menschen.</p>
    </div>
    <div>
      <h4>Seiten</h4>
      <ul class="footlinks">
        <li><a href="wissen.html">Wissen</a></li>
        <li><a href="blog.html">Blog</a></li>
        <li><a href="bodenplatte.html">Die Bodenplatte</a></li>
        <li><a href="denkkreis.html">Der Denkkreis</a></li>
        <li><a href="vereinsheim.html">Vereinsheim</a></li>
        <li><a href="buch.html">Buch</a></li>
      </ul>
    </div>
    <div>
      <h4>Wege in Bewegung</h4>
      <ul class="footlinks">
        <li><a href="ausstieg.html">Der feminine Ausstieg</a></li>
        <li><a href="ausstieg-impulsbuch.html">Das Impulsbuch</a></li>
        <li><a href="konvaleszenz.html">Konvaleszenz</a></li>
        <li><a href="https://t.me/apollondenkkreise" target="_blank" rel="noopener">Telegram: Apollon Denkkreise</a></li>
        <li><a href="gespraech.html">Kontakt</a></li>
      </ul>
    </div>
  </div>
  <div class="legal">
    <a href="impressum.html">Impressum</a><a href="datenschutz.html">Datenschutz</a>
    <span style="margin-left:auto">Wirtschaftsverein Apollon, Wien</span>
  </div>
</div></footer>
</body></html>
"""

LIGHTBOX = """
<div class="lb" id="lb" role="dialog" aria-modal="true" aria-label="Große Bildansicht">
  <button class="x" type="button" aria-label="Schließen">&#10005;</button>
  <button class="nav prev" type="button" aria-label="Vorheriges Bild">&#8249;</button>
  <img alt=""><button class="nav next" type="button" aria-label="Nächstes Bild">&#8250;</button>
  <div class="cap"></div>
</div>
<script>
(function(){var b=[].slice.call(document.querySelectorAll('.gallery button')),l=document.getElementById('lb');
if(!l||!b.length)return;var im=l.querySelector('img'),c=l.querySelector('.cap'),i=0;
function s(n){i=(n+b.length)%b.length;var x=b[i].querySelector('img');im.src=x.src;im.alt=x.alt;
c.textContent=b[i].closest('figure').querySelector('figcaption').textContent;l.classList.add('open');}
b.forEach(function(x,n){x.addEventListener('click',function(){s(n);});});
l.querySelector('.x').addEventListener('click',function(){l.classList.remove('open');});
l.querySelector('.prev').addEventListener('click',function(e){e.stopPropagation();s(i-1);});
l.querySelector('.next').addEventListener('click',function(e){e.stopPropagation();s(i+1);});
l.addEventListener('click',function(e){if(e.target===l)l.classList.remove('open');});
document.addEventListener('keydown',function(e){if(!l.classList.contains('open'))return;
if(e.key==='Escape')l.classList.remove('open');if(e.key==='ArrowRight')s(i+1);if(e.key==='ArrowLeft')s(i-1);});})();
</script>
"""

def page(slug, title, desc, body, schema="", extra=""):
    html = HEAD.format(title=title, desc=desc, fonts=FONTS, nav=nav_html(slug),
                       navmobil=nav_mobil(slug), schema=schema,
                       vcss=_v("assets/apollon.css")) + body + extra + FOOT
    with open(os.path.join(OUT, slug), "w", encoding="utf-8") as f:
        f.write(html)

def head_block(kicker, h1, intro, crumbs=None):
    cr = ''
    if crumbs:
        cr = '<p class="crumbs">' + ' &rsaquo; '.join(
            ('<a href="%s">%s</a>' % c if isinstance(c, tuple) else c) for c in crumbs) + '</p>'
    return ('<div class="pagehead"><div class="wrap">%s<p class="kicker">%s</p><h1>%s</h1>'
            '<p class="intro">%s</p></div></div>' % (cr, kicker, h1, intro))

# ---------------------------------------------------------------- Bilder
def datauri(path, maxw=1200, q=76):
    im = Image.open(path).convert("RGB")
    if im.width > maxw:
        im = im.resize((maxw, round(im.height * maxw / im.width)), Image.LANCZOS)
    b = io.BytesIO(); im.save(b, "JPEG", quality=q, optimize=True, progressive=True)
    return "data:image/jpeg;base64," + base64.b64encode(b.getvalue()).decode()

BILD = os.path.join(ROOT, "Bilder_Vereinsheim")
IMGS = [
    ("vereinsheim_aussen.jpg", "Das Vereinsheim von außen", "Das Haus"),
    ("vereinsheim_seminarraum.jpg", "Seminarraum mit langem Holztisch und Flipchart", "Der Seminarraum"),
    ("vereinsheim_wohnraum.jpg", "Wohnbereich mit Fensterfront zum Garten", "Der Wohnbereich"),
    ("vereinsheim_badezimmer.png", "Badezimmer", "Das Bad"),
]

def _prep_images():
    os.makedirs(os.path.join(OUT, "assets", "bilder"), exist_ok=True)
    names = []
    for f, alt, cap in IMGS:
        base = os.path.splitext(f)[0] + ".jpg"
        dst = os.path.join(OUT, "assets", "bilder", base)
        im = Image.open(os.path.join(BILD, f)).convert("RGB")
        if im.width > 1600:
            im = im.resize((1600, round(im.height*1600/im.width)), Image.LANCZOS)
        im.save(dst, "JPEG", quality=82, optimize=True, progressive=True)
        names.append(("assets/bilder/" + base, alt, cap))
    return names

def gallery():
    out = ['<div class="gallery">']
    for src_, alt, cap in _prep_images():
        out.append('<figure><button type="button"><img src="%s" alt="%s" loading="lazy"></button><figcaption>%s</figcaption></figure>' % (src_, alt, cap))
    out.append('</div><p style="margin-top:.9rem;font-size:.85rem;color:var(--ink-faint)">Bild anklicken f\u00fcr die gro\u00dfe Ansicht.</p>')
    return "".join(out)

# Schwan als eigene Datei ablegen
os.makedirs(os.path.join(OUT, "assets"), exist_ok=True)
shutil.copy(os.path.join(ROOT, "APOLLON_Schwan.svg"), os.path.join(OUT, "assets", "schwan.svg"))

ORG_SCHEMA = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"Organization","name":"Apollon","slogan":"Entwicklung beginnt beim Menschen.",
"parentOrganization":{"@type":"Organization","name":"Wirtschaftsverein Apollon",
"address":{"@type":"PostalAddress","streetAddress":"Prinz-Eugen-Straße 68","postalCode":"1040","addressLocality":"Wien","addressCountry":"AT"},
"telephone":"+43 676 626 9486","email":"info@konvaleszenz.com"}}
</script>"""

print("Vorlage bereit.")
