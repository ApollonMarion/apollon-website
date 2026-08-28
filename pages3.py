#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Die Wissensartikel zum Thema Verein.
from build import *
import json

STAND = "24. August 2026"

def faq_block(pairs):
    out = ['<div style="margin-top:1.2rem">']
    for q, a in pairs:
        out.append('<details class="faq"><summary>%s</summary><p>%s</p></details>' % (q, a))
    out.append('</div>')
    return "".join(out)

def faq_schema(pairs):
    d = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in pairs]}
    return '<script type="application/ld+json">%s</script>' % json.dumps(d, ensure_ascii=False)

def artikel_schema(titel, beschreibung, slug):
    d = {"@context": "https://schema.org", "@type": "Article", "headline": titel,
         "description": beschreibung, "inLanguage": "de-AT",
         "author": {"@type": "Person", "name": "Marion Bernard"},
         "publisher": {"@type": "Organization", "name": "Apollon"},
         "datePublished": "2026-08-24", "dateModified": "2026-08-24",
         "mainEntityOfPage": "https://apollon.eu.com/" + slug}
    return '<script type="application/ld+json">%s</script>' % json.dumps(d, ensure_ascii=False)

def quellen(liste):
    out = ['<div class="quellen"><h3>Woher die Angaben stammen</h3><ul>']
    for text, url in liste:
        out.append('<li><a href="%s" target="_blank" rel="noopener">%s</a></li>' % (url, text))
    out.append('</ul></div>')
    return "".join(out)

def weiter(links):
    out = ['<h3 style="font-family:var(--f-b);font-size:.8rem;letter-spacing:.12em;text-transform:uppercase;color:var(--gold);margin:2.4rem 0 0">Weiterlesen</h3><div class="weiter">']
    for text, href in links:
        out.append('<a href="%s">%s</a>' % (href, text))
    out.append('</div>')
    return "".join(out)

BYLINE = ('<div class="byline"><span>Geschrieben von <strong>Marion Bernard</strong>. '
          'Sie errichtet seit Jahren Vereine und begleitet Unternehmer dabei, ihre Struktur tragfähig zu machen. '
          '<a href="bodenplatte.html">Mehr über die Arbeit dahinter</a></span></div>')

RECHTSHINWEIS = ('<p class="hinweis">Dieser Text gibt den Stand vom ' + STAND + ' wieder und ersetzt keine '
                 'Rechts- oder Steuerberatung im Einzelfall. Im Zweifel gilt die jeweils geltende Fassung '
                 'der genannten Gesetze.</p>')

CTA = ('<section class="on-navy"><div class="wrap narrow" style="text-align:center">'
       '<p class="kicker">Ihre Lage ist anders als jede Checkliste</p>'
       '<h2>Ein Gespräch.</h2>'
       '<p style="margin-top:1.2rem">Sie erzählen, was gerade ansteht, und wir sagen Ihnen ehrlich, wie wir Ihnen dabei helfen können.</p>'
       '<p style="margin-top:1.6rem"><a class="btn-light" href="gespraech.html">Gespräch vereinbaren</a></p>'
       '</div></section>')

def artikel(slug, titel, h1, intro, kurz, koerper, faqs, quellenliste, weiterlinks, beschreibung):
    body = head_block("Wissen &middot; Der Verein", h1, intro,
                      [("index.html", "Apollon"), ("wissen.html", "Wissen"),
                       ("wissen-verein.html", "Der Verein"), "Artikel"])
    body += '<div class="wrap" style="padding-top:1.4rem"><a class="zurueck" href="wissen-verein.html">Zurück zur Übersicht: Der Verein als Werkzeug</a></div>'
    body += '<section class="on-white" style="padding-top:1.6rem"><div class="wrap">'
    body += '<p class="stand">Stand: ' + STAND + '</p>'
    body += '<div class="kurz"><strong>Kurz gesagt</strong><p>' + kurz + '</p></div>'
    body += '<div class="prose">' + koerper + '</div>'
    body += RECHTSHINWEIS
    body += quellen(quellenliste)
    body += BYLINE
    body += '</div></section>'
    body += '<section><div class="wrap narrow"><h2>Häufige Fragen</h2>' + faq_block(faqs)
    body += weiter(weiterlinks)
    body += ('<div class="zurueck-fuss">'
             '<a class="zurueck" href="wissen-verein.html">Zurück zur Übersicht: Der Verein</a>'
             '<a class="zurueck" href="wissen.html">Zurück zum Wissensbereich</a>'
             '<a class="zurueck" href="index.html">Zurück zur Startseite</a></div>')
    body += '</div></section>'
    body += CTA
    schema = artikel_schema(titel, beschreibung, slug) + faq_schema(faqs)
    page(slug, titel, beschreibung, body, schema)


# ==================================================================== 1
Q_GV = ("Vereinsgründung auf oesterreich.gv.at", "https://www.oesterreich.gv.at/themen/reisen_und_freizeit/vereine.html")
Q_WKO = ("Der Verein als Unternehmer, WKO", "https://www.wko.at/wirtschaftsrecht/der-verein-als-unternehmer")
Q_USP_KU = ("Kleinunternehmerregelung, Unternehmensserviceportal", "https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/weitere-informationen-zur-umsatzsteuer/weitere-steuertatbestaende-und-befreiungen/kleinunternehmen.html")
Q_USP_UST = ("Umsatzsteuer für Vereine, Unternehmensserviceportal", "https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/weitere-informationen-zur-umsatzsteuer/weitere-steuertatbestaende-und-befreiungen/umsatzsteuer-fuer-vereine.html")

artikel(
 "wissen-verein-rechnungen.html",
 "Darf ein Verein Rechnungen schreiben? | Apollon",
 "Darf ein Verein Rechnungen schreiben?",
 "Ja. Und das ist einer der am hartnäckigsten missverstandenen Punkte im Vereinswesen.",
 "Ja, ein Verein darf Rechnungen schreiben. Er ist rechtsfähig, kann Leistungen anbieten und dafür Entgelt verlangen. Die Voraussetzung ist, dass die Tätigkeit vom Vereinszweck gedeckt ist und die Statuten sie abbilden.",
 """
<p>Die Frage kommt in fast jedem ersten Gespräch. Meistens in dieser Form: „Ein Verein darf doch nichts verdienen, oder?“ Die Antwort ist ein klares Nein, dieser Satz stimmt so nicht.</p>

<h3>Warum der Verein Rechnungen schreiben darf</h3>
<p>Ein Verein ist eine eigene Rechtsperson. Er kann Verträge schließen, ein Konto führen, Eigentum besitzen und Menschen beschäftigen. Alles, was daraus folgt, folgt daraus auch beim Geld: Wer eine Leistung erbringt, darf sie in Rechnung stellen.</p>
<p>Was das Vereinsgesetz verbietet, ist etwas anderes. Der Verein darf nicht <em>auf Gewinn gerichtet</em> sein. Das heißt nicht, dass er keinen Überschuss erwirtschaften darf. Es heißt, dass dieser Überschuss nicht an die Mitglieder ausgeschüttet werden darf, sondern dem Vereinszweck zufließen muss.</p>
<p>Die Wirtschaftskammer formuliert es so: Ein Verein darf sich erwerbswirtschaftlich betätigen und sogar Gewinne erzielen, solange diese nicht an die Mitglieder gehen, sondern dem ideellen Zweck dienen. In der Fachsprache heißt das Nebenzweckprivileg.</p>

<h3>Die eine Bedingung, an der es scheitert</h3>
<p>Alles, was der Verein tut, muss vom Vereinszweck gedeckt sein und in den Statuten vorkommen. Das ist keine Formalie, das ist die eigentliche Arbeit.</p>
<p>Jedes Vorhaben braucht seine eigenen Statuten. Sie müssen zu dem passen, was die Menschen mit diesem Verein tatsächlich erreichen wollen, und nicht zu einem anderen Verein, der zufällig ein Muster hinterlassen hat.</p>
<p>Deshalb ist § 2, die Formulierung des Vereinszwecks, der wichtigste Absatz der gesamten Statuten.</p>

<h3>Was auf der Rechnung stehen muss</h3>
<p>Dieselben Angaben wie bei jedem anderen Unternehmen: vollständiger Name und Anschrift des Vereins, Name und Anschrift des Empfängers, Menge und Bezeichnung der Leistung, Datum, fortlaufende Nummer, Entgelt. Kommt Umsatzsteuer dazu, zusätzlich der Steuersatz, der Steuerbetrag und die UID-Nummer.</p>
<p>Praktischer Hinweis aus der Erfahrung: Die ZVR-Zahl des Vereins gehört ebenfalls darauf. Sie ist zwar nicht überall zwingend, aber sie macht sofort klar, wer da Rechnung stellt, und erspart Rückfragen.</p>

<h3>Wo es wirklich eng wird</h3>
<p>Nicht bei der Rechnung, sondern bei zwei anderen Punkten.</p>
<p><strong>Die Gewerbeberechtigung.</strong> Wer wirtschaftlich tätig wird, braucht sie unter Umständen auch als Verein. Das wird gern übersehen, weil man mit dem Wort Verein etwas Privates verbindet.</p>
<p><strong>Die Gemeinnützigkeit.</strong> Wenn der Verein steuerlich begünstigt ist, kann ein zu großer wirtschaftlicher Betrieb diese Begünstigung gefährden. Es gibt dafür abgestufte Kategorien, von unentbehrlich über entbehrlich bis begünstigungsschädlich. Wer in diese Nähe kommt, sollte es vorher wissen und nicht hinterher.</p>

<h3>Der Grund, warum das alles geht</h3>
<p>Der Verein ist eine eigene Rechtspersönlichkeit. Genau das ermöglicht es Menschen, ihre Vorhaben als Projekte umzusetzen: mit einem eigenen Namen, einem eigenen Konto, eigenen Verträgen und eigenen Rechnungen.</p>
 """,
 [("Darf ein Verein Gewinn machen?",
   "Ja, aber der Gewinn darf nicht an die Mitglieder ausgeschüttet werden. Er muss dem Vereinszweck zufließen. Eine ausschließlich gewinnorientierte Tätigkeit ist mit der Vereinsform nicht vereinbar."),
  ("Wie stellt ein Verein seine Leistungen in Rechnung?",
   "So wie jedes andere Unternehmen auch: mit vollständigen Angaben zu Leistung, Empfänger, Datum und fortlaufender Nummer. Welche steuerlichen Angaben im Einzelfall dazugehören, klären wir im Gespräch, weil es von der Tätigkeit und vom Gegenüber abhängt."),
  ("Muss die ZVR-Zahl auf die Rechnung?",
   "Zwingend vorgeschrieben ist sie nicht auf jeder Rechnung, sie gehört aber in die Geschäftskorrespondenz und schafft Klarheit. Wir empfehlen, sie immer anzugeben."),
  ("Was passiert, wenn die Statuten die Tätigkeit nicht abdecken?",
   "Dann handelt der Verein außerhalb seines Zwecks. Das kann vereinsrechtliche und steuerliche Folgen haben. Die Statuten lassen sich ändern, das ist der übliche Weg."),
  ],
 [Q_WKO, Q_USP_KU, Q_USP_UST],
 [("Was gehört in Vereinsstatuten, und was besser nicht?", "wissen-verein.html"),
  ("Was kostet eine Vereinsgründung in Österreich?", "wissen-verein-kosten-oesterreich.html"),
  ("Verein oder Einzelunternehmen: was passt wann?", "wissen-verein-oder-einzelunternehmen.html"),
  ("Zurück zur Übersicht: Der Verein als Werkzeug", "wissen-verein.html")],
 "Ein Verein darf Rechnungen schreiben, wenn die Tätigkeit vom Vereinszweck gedeckt ist. Was auf die Rechnung gehört und ab wann Umsatzsteuer anfällt."
)

# ==================================================================== 2
artikel(
 "wissen-verein-kosten-oesterreich.html",
 "Was kostet eine Vereinsgründung in Österreich? | Apollon",
 "Was kostet eine Vereinsgründung in Österreich?",
 "Die Behörde ist billig. Teuer wird, was danach kommt, wenn man es falsch aufsetzt.",
 "Die Gründung eines Vereins in Österreich kostet an Bundesgebühren 21 Euro für die Errichtungsanzeige plus 6 Euro je Bogen der beigelegten Statuten, höchstens 36 Euro. Ein Bescheid auf Antrag kostet 6,50 Euro. Registerauszüge sind gebührenfrei. Die Gebühren werden erst nach Abschluss des Verfahrens fällig, nicht im Voraus.",
 """
<p>Wer diese Frage stellt, meint fast immer zwei verschiedene Dinge auf einmal: Was zahle ich dem Staat, und was zahle ich sonst noch. Die erste Antwort ist erfreulich klein, die zweite hängt von Ihnen ab.</p>

<h3>Was der Staat verlangt</h3>
<p>Für die Errichtungsanzeige fallen 21 Euro Bundesgebühr an. Für die Statuten, die als Beilage mitgehen, kommen 6 Euro je Bogen dazu, gedeckelt bei 36 Euro. Wer einen Bescheid beantragt, zahlt dafür 6,50 Euro, sofern er positiv ausfällt. Ein negativer Bescheid ist kostenlos, was in dem Fall ein schwacher Trost ist.</p>
<p>Kopien und Auszüge aus dem Vereinsregister sind gebührenfrei. Die Gebühren werden nach Abschluss des Verfahrens fällig, nicht im Voraus. Nach der Eintragung kommt die Einladung zur Aufnahme der Vereinstätigkeit in Papierform an den Präsidenten, und dann wird gezahlt.</p>
<p>Danach lässt sich jederzeit ein aktueller Auszug beim Bundesministerium für Inneres abrufen: <a href="https://citizen.bmi.gv.at/at.gv.bmi.fnsweb-p/zvn/public/Registerauszug" target="_blank" rel="noopener">Registerauszug online</a>.</p>

<h3>Was der Staat nicht verlangt</h3>
<p>Es braucht keinen Notar. Es braucht kein Stammkapital. Es braucht keinen Rechtsanwalt. Es braucht auch keine Bank, die vorher etwas bestätigt.</p>
<p>Das ist der eigentliche Grund, warum der Verein für viele Vorhaben die zugänglichste Rechtsform in Österreich ist. Man kann mit zwei Personen und einem gut geschriebenen Dokument beginnen.</p>

<h3>Was tatsächlich Geld kostet</h3>
<p>Die Statuten. Nicht als Gebühr, sondern als Arbeit.</p>
<p>Eine Vorlage aus dem Internet kostet nichts und passt in den meisten Fällen nicht. Sie beschreibt einen Verein, den jemand anderer gegründet hat, für ein Vorhaben, das mit Ihrem nichts zu tun hat. Solange nichts passiert, merkt das niemand. Wenn etwas passiert, ist es das erste Dokument, das jemand liest.</p>
<p>Was danach folgt, kostet ebenfalls: das Konto, die Buchhaltung, gegebenenfalls eine Gewerbeberechtigung, gegebenenfalls die steuerliche Begleitung. Nichts davon ist dramatisch, aber es ist eben nicht null.</p>

<h3>Wie lange es dauert</h3>
<p>Nach Eingang der Errichtungsanzeige hat die Behörde vier Wochen Zeit. Bestehen Bedenken gegen die Gesetzmäßigkeit, kann sie auf längstens sechs Wochen verlängern. Untersagt sie nichts, entsteht der Verein mit Ablauf der Frist von selbst. Man muss also nicht auf ein Ja warten, sondern auf das Ausbleiben eines Nein.</p>
<p>In der Praxis geht es meistens schneller, weil viele Behörden vorher einen positiven Bescheid ausstellen, wenn man ihn beantragt.</p>

<h3>Und in Deutschland?</h3>
<p>Dort ist der Weg anders und etwas teurer. Ein eingetragener Verein braucht sieben Mitglieder. Für die Eintragung gehen Statuten, Gründungsprotokoll und Mitgliederliste in unterschriebener Form an das Amtsgericht.</p>
<p>Ein Punkt wird dabei regelmäßig falsch erzählt, auch von Fachleuten: Beglaubigt werden muss nicht das ganze Paket, sondern die Unterschrift. § 77 BGB verlangt für die Anmeldung eine öffentlich beglaubigte Erklärung der Vorstandsmitglieder in vertretungsberechtigter Zahl. Der Notar bestätigt also nur, dass die Unterschrift echt ist. Er beurkundet nicht den Inhalt, und genau darin liegt der Unterschied zwischen einer zweistelligen und einer dreistelligen Rechnung. Seit August 2023 geht diese Beglaubigung auch per Videokommunikation.</p>
<p>Dazu kommt die Eintragungsgebühr des Amtsgerichts. Die Größenordnung liegt insgesamt bei rund hundert bis zweihundert Euro, je nach Notar und Bundesland.</p>

<h3>Was wir daraus machen</h3>
<p>Zu uns kommt niemand mit dem Wunsch nach einem Verein. Es kommt jemand mit einer Herausforderung, die gelöst werden soll.</p>
<p>Der Verein ist für sehr vieles gut, und genau deshalb steht am Anfang eine andere Frage: Ist er hier das richtige Werkzeug? Das lässt sich nicht am Formular entscheiden. Es braucht Wissen und vor allem Gespür, und zwar auf beiden Seiten, bei dem, der fragt, und bei dem, der antwortet.</p>
<p>Statuten von irgendjemandem zu kopieren ist keine Lösung. Das eigene Vorhaben so aufzuschreiben, dass es trägt, ist eine.</p>
<p>Und noch etwas, das wir oft erleben: Menschen, die schlechte Erfahrungen mit oder durch Vereine gemacht haben, werden häufig zu Ratgebern und verunsichern andere. Das ist verständlich und trotzdem der falsche Maßstab. Holen Sie sich lieber eine eigene Einschätzung bei jemandem, der täglich damit umgeht, und entscheiden Sie dann.</p>
 """,
 [("Braucht man für eine Vereinsgründung einen Notar?",
   "In Österreich nicht. Die Statuten werden von den Gründern vereinbart und unterschrieben, die Errichtung wird der Vereinsbehörde angezeigt. In Deutschland braucht es einen Notar nur für die Beglaubigung der Unterschrift unter der Anmeldung, nicht für die Beurkundung der Unterlagen selbst."),
  ("Braucht ein Verein Startkapital?",
   "Nein. Anders als bei der GmbH gibt es kein Mindestkapital. Sinnvoll ist trotzdem, von Anfang an zu klären, wovon der Verein seine laufenden Kosten trägt."),
  ("Wie lange dauert die Gründung?",
   "Die Behörde hat vier Wochen Zeit, in Zweifelsfällen bis zu sechs. Untersagt sie den Verein nicht, entsteht er mit Fristablauf. Die Vorbereitung der Statuten braucht meist länger als das Verfahren selbst."),
  ("Kann man einen Verein auch ohne Sitz in Österreich gründen?",
   "Die Gründer müssen keine österreichischen Staatsbürger sein. Der Verein braucht aber einen Sitz in Österreich, und danach richtet sich die zuständige Behörde."),
  ],
 [Q_GV, Q_WKO],
 [("Wie viele Personen braucht man für eine Vereinsgründung?", "wissen-verein-personen.html"),
  ("Darf ein Verein Rechnungen schreiben?", "wissen-verein-rechnungen.html"),
  ("Verein oder GmbH: der ehrliche Vergleich", "wissen-verein-oder-gmbh.html"),
  ("Die Bodenplatte: erst der Boden, dann das Haus", "bodenplatte.html")],
 "Was eine Vereinsgründung in Österreich wirklich kostet: 21 Euro Bundesgebühr, 6 Euro je Statutenbogen, kein Notar, kein Stammkapital."
)

# ==================================================================== 3
artikel(
 "wissen-verein-personen.html",
 "Wie viele Personen braucht man für eine Vereinsgründung? | Apollon",
 "Wie viele Personen braucht man für eine Vereinsgründung?",
 "In Österreich zwei. In Deutschland sieben. Und das ist nicht der einzige Unterschied.",
 "In Österreich genügen zwei Personen, um einen Verein zu gründen. Sie vereinbaren die Statuten und zeigen die Errichtung der Vereinsbehörde an. In Deutschland verlangt § 56 BGB für die Eintragung eines Vereins mindestens sieben Mitglieder. Das Leitungsorgan muss in Österreich aus mindestens zwei Personen bestehen.",
 """
<p>Diese Frage entscheidet öfter über die Rechtsform, als man denkt. Wer zu zweit etwas aufbauen will, hat in Österreich einen Weg, den es in Deutschland so nicht gibt.</p>

<h3>Österreich: zwei genügen</h3>
<p>Zwei Personen vereinbaren die Statuten, unterschreiben eigenhändig und zeigen die Errichtung der Vereinsbehörde an. Gründer können natürliche oder juristische Personen sein. Eine österreichische Staatsbürgerschaft ist nicht erforderlich.</p>
<p>Die Statuten müssen klar formuliert und auf Deutsch abgefasst sein. Das klingt nach einer Kleinigkeit und ist es nicht: Unklare Statuten sind der häufigste Grund, warum eine Behörde nachfragt.</p>

<h3>Wer danach welche Rolle hat</h3>
<p>Ein Verein braucht Organe, und die brauchen Menschen.</p>
<p><strong>Die Mitgliederversammlung</strong> ist zumindest alle fünf Jahre einzuberufen. Sie ist der Ort der gemeinsamen Willensbildung.</p>
<p><strong>Das Leitungsorgan</strong> muss aus mindestens zwei Personen bestehen und führt die Geschäfte.</p>
<p><strong>Zwei Rechnungsprüfer</strong> sind zu bestellen. Sie prüfen die Ordnungsmäßigkeit der Rechnungslegung und berichten innerhalb von vier Monaten.</p>
<p>Damit ist klar, warum zwei Personen zwar rechtlich reichen, praktisch aber knapp sind. Rechnungsprüfer sollen unabhängig sein, und wer alles selbst macht, prüft am Ende sich selbst.</p>
<p>Unsere Erfahrung: Vier bis fünf Menschen sind die Zahl, bei der ein Verein arbeitsfähig wird, ohne schwerfällig zu sein.</p>

<h3>Deutschland: sieben für die Eintragung</h3>
<p>§ 56 BGB sagt es knapp: „Die Eintragung soll nur erfolgen, wenn die Zahl der Mitglieder mindestens sieben beträgt.“</p>
<p>Gemeint ist die Eintragung ins Vereinsregister, also der Schritt zum eingetragenen Verein. Ein nicht eingetragener Verein kann auch mit weniger bestehen, ist aber in der Praxis unhandlich, weil die Haftungslage eine andere ist.</p>
<p>Sinkt die Mitgliederzahl später deutlich unter diese Schwelle, kann dem Verein die Rechtsfähigkeit entzogen werden. Wer in Deutschland gründet, sollte die sieben also nicht als einmalige Hürde verstehen, sondern als Dauerzustand.</p>

<h3>Was das für die Entscheidung bedeutet</h3>
<p>Wenn Sie zu zweit oder zu dritt sind und einen Verein wollen, ist Österreich der einfachere Weg. Das ist kein Trick und kein Schlupfloch, es ist schlicht unterschiedliches Recht.</p>
<p>Die eigentliche Frage bleibt trotzdem dieselbe: Wollen Sie überhaupt einen Verein, oder wollen Sie eine Struktur, und der Verein ist nur die erste Form, die Ihnen eingefallen ist? Darüber sprechen wir lieber vorher als nachher.</p>
 """,
 [("Reichen wirklich zwei Personen?",
   "Für die Gründung in Österreich ja. Das Leitungsorgan muss aus mindestens zwei Personen bestehen, und zusätzlich sind zwei Rechnungsprüfer zu bestellen. Praktisch arbeitet ein Verein ab etwa vier bis fünf Menschen am besten."),
  ("Können auch Firmen einen Verein gründen?",
   "Ja. Gründer können natürliche oder juristische Personen sein."),
  ("Muss man österreichischer Staatsbürger sein?",
   "Nein. Die Staatsbürgerschaft spielt keine Rolle. Der Verein braucht aber einen Sitz in Österreich."),
  ("Was passiert in Deutschland, wenn Mitglieder wegfallen?",
   "Fällt die Mitgliederzahl deutlich unter die gesetzliche Schwelle, kann dem eingetragenen Verein die Rechtsfähigkeit entzogen werden. Die sieben Mitglieder sind also kein einmaliger Gründungsakt."),
  ],
 [Q_GV, ("§ 56 BGB bei Gesetze im Internet", "https://www.gesetze-im-internet.de/bgb/__56.html")],
 [("Was kostet eine Vereinsgründung in Österreich?", "wissen-verein-kosten-oesterreich.html"),
  ("Welche Organe braucht ein Verein wirklich?", "wissen-verein.html"),
  ("Verein oder Einzelunternehmen: was passt wann?", "wissen-verein-oder-einzelunternehmen.html"),
  ("Zurück zur Übersicht: Der Verein als Werkzeug", "wissen-verein.html")],
 "In Österreich genügen zwei Personen für eine Vereinsgründung, in Deutschland verlangt § 56 BGB sieben Mitglieder für die Eintragung."
)

# ==================================================================== 4
artikel(
 "wissen-verein-oder-einzelunternehmen.html",
 "Verein oder Einzelunternehmen: was passt wann? | Apollon",
 "Verein oder Einzelunternehmen: was passt wann?",
 "Die Frage ist nicht, was günstiger ist. Die Frage ist, wem das Ergebnis gehören soll.",
 "Ein Einzelunternehmen gehört einer Person, ist schnell angemeldet und haftet mit dem Privatvermögen. Ein Verein gehört sich selbst, braucht mindestens zwei Gründer und haftet mit dem Vereinsvermögen. Die Entscheidung hängt weniger an den Kosten als an der Frage, ob das Vorhaben an einer Person hängen soll oder nicht.",
 """
<h3>Das Einzelunternehmen in einem Absatz</h3>
<p>Eine Person, eine Gewerbeanmeldung, sofort arbeitsfähig. Kein Kapital, kein Notar, kein Gesellschaftsvertrag. Der Gewinn gehört Ihnen, die Steuer zahlen Sie über die Einkommensteuer, die Sozialversicherung läuft über die SVS.</p>
<p>Der Preis dafür ist die Haftung. Sie haften mit Ihrem gesamten Vermögen, also auch mit dem, was mit dem Geschäft nichts zu tun hat.</p>

<h3>Der Verein in einem Absatz</h3>
<p>Mindestens zwei Personen, Statuten, Anzeige bei der Behörde. Kein Kapital, kein Notar. Der Verein ist eine eigene Rechtsperson und haftet mit seinem Vermögen, nicht mit dem der Mitglieder. Überschüsse bleiben im Verein und dienen dem Zweck.</p>
<p>Der Preis dafür ist Struktur. Es gibt Organe, Zuständigkeiten, eine Mitgliederversammlung und Rechnungsprüfer. Sie entscheiden nicht mehr allein.</p>
<p>Ein Punkt, der dabei fast immer übersehen wird: Der Verein kann Vermögen halten, und zwar auch größeres. Er kann Immobilien besitzen, er kann sie geschenkt bekommen, und er kann sie erben. Vereinsvermögen gehört dem Verein, nicht seinen Mitgliedern, und es bleibt dort, auch wenn Menschen kommen und gehen. Für Vorhaben, die über eine Generation hinausdenken, ist das oft der eigentliche Grund für diese Rechtsform.</p>

<h3>Die drei Fragen, an denen es sich entscheidet</h3>
<p><strong>Erstens: Soll das Vorhaben an Ihnen hängen?</strong> Wenn ja, ist das Einzelunternehmen ehrlich. Wenn nein, wenn es also weiterlaufen soll, auch wenn Sie einmal ausfallen oder aussteigen, dann brauchen Sie eine Form, die Sie überlebt.</p>
<p><strong>Zweitens: Was passiert mit dem Überschuss?</strong> Beim Einzelunternehmen ist er Ihr Einkommen. Im Verein bleibt er im Verein. Das kann ein Nachteil sein, wenn Sie davon leben wollen. Es kann ein großer Vorteil sein, wenn Sie aufbauen wollen.</p>
<p><strong>Drittens: Wie viel Risiko liegt in der Sache?</strong> Wer berät, unterrichtet oder vermittelt, trägt ein anderes Risiko als wer baut, veranstaltet oder mit Menschen körperlich arbeitet. Je größer das Risiko, desto wichtiger die Trennung zwischen Vorhaben und Privatvermögen.</p>

<h3>Was viele nicht wissen</h3>
<p>Es ist kein Entweder-oder. In der Praxis existieren beide Formen sehr oft nebeneinander: das Einzelunternehmen für das, was persönlich an Sie gebunden ist, der Verein für das, was gemeinsam getragen wird und wachsen soll.</p>
<p>Diese Kombination ist zulässig und häufig sinnvoll. Sie will nur sauber aufgesetzt sein, damit klar bleibt, welche Leistung wo erbracht und wo abgerechnet wird. Wer das vermischt, bekommt später Fragen, die er nicht beantworten kann.</p>

<h3>Ein Satz zur Ehrlichkeit</h3>
<p>Der Verein ist kein Steuersparmodell. Wer ihn dafür hält, hat ihn missverstanden und wird damit auf Dauer nicht glücklich. Er ist ein Werkzeug für Vorhaben, die mehreren gehören und länger dauern sollen als die Aufmerksamkeitsspanne einer Person.</p>
 """,
 [("Kann ich beides haben, Einzelunternehmen und Verein?",
   "Ja, das ist zulässig und in der Praxis häufig. Wichtig ist eine saubere Trennung: welche Leistung wird wo erbracht und wo abgerechnet."),
  ("Hafte ich als Vereinsvorstand privat?",
   "Grundsätzlich haftet der Verein mit seinem Vermögen. Bei Pflichtverletzungen, etwa bei nicht abgeführten Abgaben, kann jedoch eine persönliche Haftung der Organe entstehen. Das ist einer der Punkte, die man vorher besprechen sollte."),
  ("Kann ich aus einem Einzelunternehmen einen Verein machen?",
   "Nicht durch Umwandlung im engeren Sinn. Man gründet den Verein neu und überträgt, was übertragbar ist. Wie das sauber geht, hängt vom Einzelfall ab."),
  ("Ist der Verein billiger?",
   "In der Gründung ja, im laufenden Betrieb nicht unbedingt. Der Unterschied liegt weniger im Geld als in der Struktur."),
  ],
 [Q_GV, Q_WKO],
 [("Verein oder GmbH: der ehrliche Vergleich", "wissen-verein-oder-gmbh.html"),
  ("Darf ein Verein Rechnungen schreiben?", "wissen-verein-rechnungen.html"),
  ("Die Bodenplatte: erst der Boden, dann das Haus", "bodenplatte.html"),
  ("Zurück zur Übersicht: Der Verein als Werkzeug", "wissen-verein.html")],
 "Verein oder Einzelunternehmen: Haftung, Überschuss, Struktur. Die drei Fragen, an denen sich die Rechtsform wirklich entscheidet."
)

# ==================================================================== 5
artikel(
 "wissen-verein-oder-gmbh.html",
 "Verein oder GmbH: der ehrliche Vergleich | Apollon",
 "Verein oder GmbH: der ehrliche Vergleich",
 "Beide begrenzen die Haftung. Der Unterschied liegt woanders, nämlich beim Eigentum.",
 "Eine GmbH in Österreich braucht seit 2024 mindestens 10.000 Euro Stammkapital, davon 5.000 Euro bar, einen Notariatsakt und die Eintragung ins Firmenbuch. Ein Verein braucht zwei Personen, Statuten und eine Anzeige bei der Behörde. Der entscheidende Unterschied: Die GmbH gehört ihren Gesellschaftern, der Verein gehört sich selbst.",
 """
<p>Wer diese Frage stellt, hat meistens schon verstanden, dass er die Haftung begrenzen will. Das können beide Formen. Die Entscheidung fällt an einer anderen Stelle.</p>

<h3>Was die GmbH kostet und verlangt</h3>
<p>Seit 1. Jänner 2024 liegt das Mindeststammkapital bei 10.000 Euro, davon sind mindestens 5.000 Euro bar einzuzahlen. Davor waren es 35.000 Euro, das ist der Grund, warum ältere Quellen andere Zahlen nennen.</p>
<p>Dazu kommen der Gesellschaftsvertrag als Notariatsakt, die Eintragung ins Firmenbuch und meist eine steuerliche Begleitung beim Start. In Summe liegen die Gründungskosten üblicherweise zwischen zweitausend und fünftausend Euro, ohne das Stammkapital selbst. Die Eintragungsgebühr beim Firmenbuch kann über das Neugründungsförderungsgesetz entfallen, wenn man die Bestätigung rechtzeitig einholt.</p>
<p>Gerechnet in Wochen: zwei bis sechs, je nach Firmenbuchgericht.</p>

<h3>Was der Verein kostet und verlangt</h3>
<p>Zwei Personen, Statuten, Errichtungsanzeige. An Gebühren fallen 21 Euro plus höchstens 36 Euro für die Statutenbeilagen an. Kein Notar, kein Kapital. Die Behörde hat vier Wochen Zeit, in Zweifelsfällen sechs.</p>

<h3>Der eigentliche Unterschied</h3>
<p>Nicht das Geld. Das Eigentum.</p>
<p><strong>Eine GmbH gehört ihren Gesellschaftern.</strong> Anteile lassen sich verkaufen, vererben, verpfänden. Gewinne können ausgeschüttet werden. Wer Wert aufbaut, baut ihn für sich auf, und kann ihn eines Tages zu Geld machen.</p>
<p><strong>Ein Verein gehört niemandem.</strong> Es gibt keine Anteile. Niemand kann seinen Verein verkaufen. Überschüsse bleiben im Verein und dienen dem Zweck. Wenn der Verein aufgelöst wird, geht das Vermögen dorthin, wo die Statuten es hinschicken, nicht an die Mitglieder.</p>
<p>Das ist der Punkt, an dem sich die Entscheidung entscheidet. Alles andere ist Beiwerk.</p>

<h3>Wann welche Form passt</h3>
<p><strong>Die GmbH passt</strong>, wenn Sie ein Unternehmen bauen, das Ihnen gehören soll, das Gewinne ausschütten oder verkauft werden soll, das Investoren aufnehmen könnte, oder das nach außen die Erwartung erfüllen muss, ein Unternehmen zu sein.</p>
<p><strong>Der Verein passt</strong>, wenn mehrere gemeinsam etwas tragen, wenn das Vorhaben länger bestehen soll als die Beteiligten, wenn der Zweck wichtiger ist als der Ertrag, oder wenn Sie eine vorhandene Struktur sinnvoll ergänzen wollen.</p>

<h3>Und die Kombination</h3>
<p>In der Praxis stehen beide oft nebeneinander. Die GmbH macht das Geschäft, der Verein trägt den Teil, der gemeinschaftlich ist, etwa Bildung, Forschung, ein Haus, ein Netzwerk. Das ist zulässig und häufig die klügste Lösung.</p>
<p>Sie verlangt allerdings Sorgfalt: Beide müssen tatsächlich getrennte Aufgaben haben, mit eigenen Verträgen, eigener Abrechnung, nachvollziehbaren Leistungen. Wer sie vermischt, hat am Ende beide Nachteile und keinen Vorteil.</p>

<h3>Der Satz, den wir am häufigsten sagen</h3>
<p>Die Rechtsform ist nicht der Anfang. Der Anfang ist die Frage, was Sie eigentlich vorhaben und wem das Ergebnis gehören soll. Wenn das klar ist, ergibt sich die Form fast von selbst.</p>
 """,
 [("Wie viel Stammkapital braucht eine GmbH in Österreich?",
   "Seit 1. Jänner 2024 mindestens 10.000 Euro, davon 5.000 Euro bar eingezahlt. Zuvor lag das Mindeststammkapital bei 35.000 Euro."),
  ("Kann ein Verein Gewinne ausschütten?",
   "Nein. Überschüsse müssen dem Vereinszweck zufließen. Eine Ausschüttung an Mitglieder ist mit der Vereinsform nicht vereinbar."),
  ("Kann man einen Verein verkaufen?",
   "Nein. Es gibt keine Anteile. Das ist der grundlegende Unterschied zur GmbH."),
  ("Darf ein Verein eine GmbH halten?",
   "Grundsätzlich ja. Ob es im Einzelfall sinnvoll und steuerlich unbedenklich ist, hängt von Zweck, Umfang und Gemeinnützigkeit ab."),
  ],
 [Q_GV, Q_WKO, ("Gründungskosten im Überblick, WKO", "https://www.wko.at/gruendung/gruendungskosten")],
 [("Verein oder Einzelunternehmen: was passt wann?", "wissen-verein-oder-einzelunternehmen.html"),
  ("Was kostet eine Vereinsgründung in Österreich?", "wissen-verein-kosten-oesterreich.html"),
  ("Die Bodenplatte: erst der Boden, dann das Haus", "bodenplatte.html"),
  ("Zurück zur Übersicht: Der Verein als Werkzeug", "wissen-verein.html")],
 "Verein oder GmbH in Österreich: Stammkapital, Kosten, Haftung und der entscheidende Unterschied beim Eigentum."
)

print("Fünf Artikel gebaut.")
