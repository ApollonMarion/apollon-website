#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Der Blogbereich.

Die Texte stammen von Marion. Sie liegen als Textdateien in ../marion und
werden hier unveraendert uebernommen. Wir setzen nur die Absaetze und
Ueberschriften, wir schreiben nichts um.
"""
from build import *
import json, os, re

MARION = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "marion")


# ---------------------------------------------------------------- Umwandlung
def aus_text(pfad):
    """Macht aus Marions Text HTML. Ueberschriften, Absaetze, Zeilenumbrueche.

    Der Wortlaut bleibt, wie er ist. Wir entscheiden nur, was Absatz und was
    Ueberschrift wird, und wir lassen die Quellenangaben weg, die kommen
    getrennt in den Quellenblock.
    """
    with open(pfad, encoding="utf-8") as f:
        roh = f.read()

    # Der Quellenteil wird gesondert behandelt
    quellen = []
    teil = re.split(r"\n## Woher die Zahlen stammen\s*\n", roh)
    roh = teil[0]
    if len(teil) > 1:
        for name, url in re.findall(r"([^\n]+)\n(https?://\S+)", teil[1]):
            quellen.append((name.strip(), url.strip()))

    # Titelzeile und Datumszeile heraustrennen
    zeilen = roh.split("\n")
    if zeilen and zeilen[0].startswith("# "):
        zeilen = zeilen[1:]
    roh = "\n".join(zeilen)
    roh = re.sub(r"^\s*(MONTAG|DIENSTAG|MITTWOCH|DONNERSTAG|FREITAG|SAMSTAG|SONNTAG),[^\n]*\n", "", roh)

    aus = []
    cta = None
    for block in re.split(r"\n\s*\n", roh.strip()):
        block = block.strip()
        if not block:
            continue
        if block.startswith("### "):
            aus.append("<h3>%s</h3>" % block[4:].strip())
        elif block.startswith("## "):
            aus.append("<h2>%s</h2>" % block[3:].strip())
        elif block.startswith("CTA:"):
            cta = block[4:].strip()
        elif block.startswith("---"):
            continue
        else:
            aus.append("<p>%s</p>" % "<br>".join(z.strip() for z in block.split("\n")))
    return "".join(aus), quellen, cta


# ---------------------------------------------------------------- Bausteine
BYLINE = ('<div class="byline"><span>Geschrieben von <strong>Marion Bernard</strong>. '
          'Sie begleitet Unternehmer dabei, ihre Struktur tragfähig zu machen, und errichtet '
          'seit Jahren Vereine, Stiftungen und EWIV. '
          '<a href="bodenplatte.html">Mehr über die Arbeit dahinter</a></span></div>')


def quellenblock(liste):
    if not liste:
        return ""
    out = ['<div class="quellen"><h3>Woher die Zahlen stammen</h3><ul>']
    for text, url in liste:
        out.append('<li><a href="%s" target="_blank" rel="noopener">%s</a></li>' % (url, text))
    out.append('</ul></div>')
    return "".join(out)


def artikel_schema(titel, beschreibung, slug, datum_iso):
    d = {"@context": "https://schema.org", "@type": "BlogPosting", "headline": titel,
         "description": beschreibung, "inLanguage": "de-AT",
         "author": {"@type": "Person", "name": "Marion Bernard"},
         "publisher": {"@type": "Organization", "name": "Apollon"},
         "datePublished": datum_iso, "dateModified": datum_iso,
         "mainEntityOfPage": "https://apollon.eu.com/" + slug}
    return '<script type="application/ld+json">%s</script>' % json.dumps(d, ensure_ascii=False)


def cta_block(knopf="Gespräch vereinbaren"):
    return ('<section class="on-navy"><div class="wrap narrow" style="text-align:center">'
            '<p class="kicker">Kein fertiger Plan nötig</p>'
            '<h2>Ein Gespräch.</h2>'
            '<p style="margin-top:1.2rem">Sie erzählen, wo Sie stehen. Wir schauen gemeinsam '
            'darauf, was bereits da ist und was daraus entstehen kann.</p>'
            '<p style="margin-top:1.6rem"><a class="btn-light" href="gespraech.html">'
            + knopf + '</a></p></div></section>')


# ---------------------------------------------------------------- die Beiträge
BEITRAEGE = [
    dict(
        slug="blog-loesung-gefragt.html",
        quelle="artikel-01-loesung-gefragt.md",
        datum="Mittwoch, 26. August 2026",
        datum_iso="2026-08-26",
        titel="Ist meine Lösung heute überhaupt noch gefragt?",
        vorspann=("Es gibt Fragen, die stellt man sich gerne. Und es gibt Fragen, "
                  "die sollte man sich stellen."),
        teaser=("1.444 Insolvenzverfahren wurden in Österreich im ersten Halbjahr gar nicht "
                "erst eröffnet, weil kein Vermögen mehr da war. Über die Frage, die man sich "
                "früher stellen sollte als die nach dem nächsten Auftrag."),
        beschreibung=("Marion Bernard über die Frage, die vor der nächsten Krise schützt: "
                      "Braucht der Markt das, was ich anbiete, heute überhaupt noch in dieser Form?"),
    ),
]

# Der Beitrag dieser Woche. Er wurde Donnerstag frueh zur Durchsicht geschickt
# und geht nach Marions Freigabe online. Bis dahin liegt er unter dem Namen in
# "dateiname" und taucht nirgends auf.
BEITRAEGE.insert(1, dict(
    slug="blog-fuenf-betriebe.html",
    dateiname="vorschau-fertig-fuenf-betriebe.html",
    warten=True,
    quelle="artikel-03-fuenf-betriebe.md",
    datum="Donnerstag, 27. August 2026",
    datum_iso="2026-08-27",
    titel="Fünf Betriebe wollen zusammenarbeiten. Wie fängt man an?",
    vorspann=("Über den ersten Schritt, an dem die meisten Kooperationen scheitern, "
              "bevor sie begonnen haben."),
    teaser=("Alle nicken, alle finden es richtig, und dann passiert drei Monate lang nichts. "
            "Über die drei Fragen, die vor jeder Rechtsform kommen."),
    beschreibung=("Marion Bernard über den ersten Schritt einer Zusammenarbeit zwischen "
                  "Betrieben und darüber, warum die Rechtsform zuletzt kommt."),
))

APOLLON_REIHE      = "Blog &middot; Apollon"
KONVALESZENZ_REIHE = "Blog &middot; Konvaleszenz"
AUSSTIEG_REIHE     = "Blog &middot; Der feminine Ausstieg"


def marke(b):
    """Die Zeile ueber der Ueberschrift. Ohne ausdrueckliche Angabe: Apollon."""
    reihe = b.get("reihe") or APOLLON_REIHE
    return reihe + (" &middot; " + b["datum"] if b.get("datum") else "")


BEITRAEGE += [
    dict(slug="blog-selbst-denken.html", quelle="kv-01-selbst-denken.md",
         reihe=KONVALESZENZ_REIHE,
         titel="Wenn du nicht selbst denkst, denkt jemand anderes für dich",
         vorspann="Über einen Arzt, der unbequem war, und über die Frage, welche Spur du selbst hinterlässt.",
         teaser=("Ein Mensch, der versteht, ist nicht steuerbar. Über Verantwortung, "
                 "Bequemlichkeit und die Frage, ob wir noch selbst denken."),
         beschreibung="Marion Bernard über Eigenverantwortung, Souveränität und die Frage, ob wir noch selbst denken."),

    dict(slug="blog-warum-reagierst-du.html", quelle="kv-02-warum-reagierst-du.md",
         reihe=KONVALESZENZ_REIHE,
         titel="Warum reagierst du eigentlich auf ein Leben, das du nie gewählt hast?",
         vorspann="Noch bevor der erste Kaffee getrunken ist, bestimmen bereits andere über den Verlauf des Tages.",
         teaser=("Wir reagieren auf Termine, Rechnungen, Krankheiten, Konflikte. Doch wann hast du "
                 "das letzte Mal etwas getan, weil du es wirklich wolltest?"),
         beschreibung="Marion Bernard über den Unterschied zwischen Reagieren und Gestalten, und was die Füße dazu zeigen."),

    dict(slug="blog-entscheidung-nach-der-entscheidung.html",
         quelle="kv-03-entscheidung-nach-der-entscheidung.md",
         reihe=KONVALESZENZ_REIHE,
         titel="Die Entscheidung nach der Entscheidung",
         vorspann="Warum Vertrauen oft erst beginnt, nachdem Klarheit bereits da war.",
         teaser=("Die Entscheidung ist gefallen, und trotzdem taucht sie abends wieder auf. "
                 "Über die feine Grenze zwischen Reflektion und gedanklicher Schleife."),
         beschreibung="Marion Bernard über Klarheit vor der Entscheidung und Vertrauen danach."),

    dict(slug="blog-alte-strukturen.html", quelle="kv-04-alte-strukturen.md",
         reihe=KONVALESZENZ_REIHE,
         titel="Wenn alte Strukturen den gleichen Fehler wiederholen",
         vorspann="Du siehst, was nicht funktioniert. Und irgendwann erkennst du: Das liegt nicht an dir.",
         teaser=("Strukturen ändern sich nicht. Menschen ändern sich. Über den Moment, in dem "
                 "nicht mehr die Struktur entscheidet, sondern du."),
         beschreibung="Marion Bernard über den Schmerz, klarer zu sehen als das Umfeld, und über den Mut, etwas Neues zu bauen."),

    dict(slug="blog-geld-und-wahrheit.html", quelle="kv-05-geld-und-wahrheit.md",
         reihe=KONVALESZENZ_REIHE,
         titel="Geld, Wahrheit und der Moment, in dem ein Mensch sich selbst verliert",
         vorspann="Viele glauben, Geld sei das Hindernis. Aber das ist es nie.",
         teaser=("Ein Termin, der alles hätte verändern können. Über Geld als Spiegel und "
                 "darüber, was Heilung wirklich braucht."),
         beschreibung="Marion Bernard darüber, warum Menschen fliehen, wenn es ernst wird, und was Heilung wirklich verlangt."),

    dict(slug="blog-wenn-sich-erfuellt.html", quelle="kv-06-wenn-sich-erfuellt.md",
         reihe=KONVALESZENZ_REIHE,
         titel="Wenn sich erfüllt, wovon du träumst",
         vorspann="Kein Feuerwerk, keine Fanfaren, sondern ein leises, warmes Ja.",
         teaser=("Erfüllung ist kein Ziel, sondern ein Zustand. Über den Weg dorthin und "
                 "darüber, was der Körper dabei zeigt."),
         beschreibung="Marion Bernard über Erfüllung als inneres Ankommen und über die Verantwortung, die damit beginnt."),

    dict(slug="blog-hinhoeren.html", quelle="kv-07-hinhoeren.md",
         reihe=KONVALESZENZ_REIHE,
         titel="Hinhören, und was es verändert",
         vorspann="Hinhören beginnt oft dort, wo Worte enden.",
         teaser=("Solange unser Inneres laut ist, können wir das Äußere nicht wirklich hören. "
                 "Über Zuhören in Beziehungen, im Körper und in den Füßen."),
         beschreibung="Marion Bernard über echtes Zuhören, was es in Beziehungen verändert und was die Füße dazu erzählen."),
]


def bauen():
    for i, b in enumerate(BEITRAEGE):
        koerper, quellen, cta = aus_text(os.path.join(MARION, b["quelle"]))

        body = head_block("Blog", b["titel"], b["vorspann"],
                          [("index.html", "Apollon"), ("blog.html", "Blog"), "Beitrag"])
        body += ('<div class="wrap" style="padding-top:1.4rem">'
                 '<a class="zurueck" href="blog.html">Zurück zur Übersicht</a></div>')
        body += '<section class="on-white" style="padding-top:1.6rem"><div class="wrap">'
        body += '<p class="stand">%s</p>' % marke(b)
        body += '<div class="prose">' + koerper + '</div>'
        body += quellenblock(quellen)
        body += BYLINE
        body += '</div></section>'

        andere = [x for x in BEITRAEGE if x["slug"] != b["slug"] and not x.get("warten")]
        if andere:
            links = "".join('<a href="%s">%s</a>' % (x["slug"], x["titel"]) for x in andere[:3])
            body += ('<section><div class="wrap narrow">'
                     '<h3 style="font-family:var(--f-b);font-size:.8rem;letter-spacing:.12em;'
                     'text-transform:uppercase;color:var(--gold);margin:0 0 .8rem">Weiterlesen</h3>'
                     '<div class="weiter">' + links + '</div></div></section>')

        body += cta_block(cta.title() if cta else "Gespräch vereinbaren")
        page(b.get("dateiname", b["slug"]), b["titel"] + " | Apollon", b["beschreibung"], body,
             artikel_schema(b["titel"], b["beschreibung"], b["slug"],
                            b.get("datum_iso", "2026-08-26")))

    # ------------------------------------------------------------ Übersicht
    body = head_block("Blog", "Gedanken aus der Arbeit",
                      "Jede Woche ein Text von Marion Bernard. Über das, was Unternehmern gerade "
                      "wirklich unter den Nägeln brennt, und über die Fragen, die davor kommen.",
                      [("index.html", "Apollon"), "Blog"])
    body += '<section class="on-white"><div class="wrap">'
    body += ('<div class="beitragsliste eigenliste">'
             '<!--eigen:blogliste--><!--/eigen:blogliste-->'
             '</div>')
    body += '<div class="beitragsliste">'
    for b in BEITRAEGE:
        if b.get("warten"):
            continue
        zeile = marke(b)
        body += ('<article class="beitrag">'
                 '<p class="stand">%s</p>'
                 '<h2><a href="%s">%s</a></h2>'
                 '<p>%s</p>'
                 '<p><a class="mehr" href="%s">Weiterlesen</a></p>'
                 '</article>') % (zeile, b["slug"], b["titel"], b["teaser"], b["slug"])
    body += '</div></div></section>'
    body += cta_block()
    page("blog.html", "Blog | Apollon",
         "Jede Woche ein Text von Marion Bernard über Unternehmertum, Struktur und die Fragen, "
         "die vor der nächsten Krise kommen.", body)

    print("Blog gebaut: %d Beitrag(e) plus Übersicht" % len(BEITRAEGE))


if __name__ == "__main__":
    bauen()
