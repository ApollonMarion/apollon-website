#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from build import *

def artlist(items):
    # Sind alle Artikel fertig, verschwinden die Markierungen. Sie helfen nur solange, wie noch etwas fehlt.
    alle_fertig = all(isinstance(t, tuple) for t in items)
    out = ['<ul class="artlist">']
    for t in items:
        if isinstance(t, tuple):
            titel, href = t
            marke = '' if alle_fertig else '<span class="soon" style="color:var(--gold);border-color:#E4D2AC">fertig</span>'
            out.append('<li><a href="%s">%s</a>%s</li>' % (href, titel, marke))
        else:
            out.append('<li><span style="color:var(--ink-soft)">%s</span><span class="soon">in Arbeit</span></li>' % t)
    out.append('</ul>')
    return "".join(out)

def faq(pairs):
    out = ['<div style="margin-top:1.4rem">']
    for q, a in pairs:
        out.append('<details class="faq"><summary>%s</summary><p>%s</p></details>' % (q, a))
    out.append('</div>')
    return "".join(out)

def faq_schema(pairs):
    import json
    d = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
        {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in pairs]}
    return '<script type="application/ld+json">%s</script>' % json.dumps(d, ensure_ascii=False)

# ============================================================ WISSEN, ÜBERSICHT
body = head_block("Wissen", "Alles, was wir wissen, steht offen da.",
  "Weil Wissen, das in einem Kopf bleibt, mit diesem Kopf verschwindet.",
  [("index.html","Apollon"), "Wissen"]) + """
<section class="on-white"><div class="wrap">
  <p class="lead" style="max-width:40rem">Wir erfinden nichts Neues. Wir arbeiten mit Werkzeugen, die es seit Ewigkeiten gibt, und wir wissen, wie man sie richtig benutzt.</p>
  <div class="three" style="margin-top:2.4rem">
    <article class="card"><h3>Der Verein als Werkzeug</h3><p>Gründung, Statuten, Organe, Rechnungen, Gemeinnützigkeit. Erklärt so, wie man es einem Menschen erklärt und nicht einer Behörde.</p><a class="more" href="wissen-verein.html">Zum Vereinswissen</a></article>
    <article class="card"><h3>Die EWIV, verständlich</h3><p>Die Europäische wirtschaftliche Interessenvereinigung. Ein mächtiges Werkzeug, über das kaum jemand verständlich schreibt.</p><a class="more" href="wissen-ewiv.html">Zur EWIV</a></article>
    <article class="card"><h3>Der Körper liest mit</h3><p>Was Druck, Haltung und Füße über einen Menschen erzählen. Die Grundlage der Arbeit in der Konvaleszenz.</p><a class="more" href="wissen-koerper.html">Zum Körperwissen</a></article>
  </div>
</div></section>

<section><div class="wrap">
  <h2 style="max-width:22ch">Denkmodelle</h2>
  <p style="max-width:38rem;margin-top:1rem">Ein Denkmodell ist ein Bild, das etwas Kompliziertes in einem Moment verständlich macht. Es ist der Teil des Wissens, den Menschen weitererzählen.</p>
  <div class="two" style="margin-top:2rem">
    <article class="card"><h3>Die Bodenplatte</h3><p>Warum zuerst der Boden kommt und dann das Haus. Und woran man merkt, dass unter dem eigenen Unternehmen keiner liegt.</p><a class="more" href="bodenplatte.html">Zum Modell</a></article>
    <article class="card"><h3>Preis, Wert und Rückfluss</h3><p>Drei Begriffe, die ständig verwechselt werden. Wer sie auseinanderhält, rechnet anders und arbeitet ruhiger.</p><a class="more" href="#">In Arbeit</a></article>
  </div>
</div></section>

<section class="on-white"><div class="wrap">
  <h2>Journal und Videos</h2>
  <p style="max-width:38rem;margin-top:1rem">Im Journal steht, was zuletzt dazugekommen ist, chronologisch. In der Mediathek liegen die Videos, fünf bis zehn Minuten, unscripted, jedes mit Transkript, damit gesprochenes Wissen auffindbar wird.</p>
  <div class="note"><strong>Im Aufbau:</strong> Journal und Mediathek folgen, sobald die ersten Artikel und Videos stehen. Die Struktur ist angelegt.</div>
</div></section>
"""
page("wissen.html", "Wissen | Apollon",
     "Vereinswesen, EWIV und das Wissen über den Körper. Verständlich erklärt, offen zugänglich.", body)

# ============================================================ PILLAR 1, VEREIN
pairs = [
 ("Darf ein Verein Rechnungen schreiben?",
  "Ja. Ein Verein ist rechtsfähig und kann Leistungen gegen Entgelt anbieten, solange das vom Vereinszweck gedeckt ist und die Statuten es zulassen. Bei umfangreicher wirtschaftlicher Tätigkeit sind Steuerpflicht und Gemeinnützigkeit gesondert zu prüfen."),
 ("Wie viele Personen braucht man für eine Vereinsgründung?",
  "In Österreich genügen zwei Personen für die Gründung. In Deutschland braucht ein eingetragener Verein sieben Gründungsmitglieder. Die genauen Anforderungen ergeben sich aus dem jeweils geltenden Vereinsrecht."),
 ("Muss ein Verein gemeinnützig sein?",
  "Nein. Gemeinnützigkeit ist eine steuerliche Einstufung, keine Voraussetzung. Ein Verein kann auch wirtschaftlich tätig sein, ohne gemeinnützig zu sein."),
 ("Wie zahlt ein Verein jemanden aus?",
  "Über anerkannte Wege wie Werkverträge, freie Dienstverträge, Anstellung oder Aufwandsentschädigungen. Welcher Weg passt, hängt von Tätigkeit, Umfang und Regelmäßigkeit ab."),
 ("Wie lange dauert eine Vereinsgründung?",
  "Nach Einreichung der Errichtungsanzeige entscheidet die Behörde. In der Praxis vergehen meist wenige Wochen. Die Vorbereitung der Statuten ist der Teil, der Sorgfalt braucht."),
]
body = head_block("Apollon", "Verein",
  "Menschen haben sich schon immer zusammengeschlossen, wenn sie gemeinsam etwas erreichen wollten. Der Verein gibt diesem gemeinsamen Willen eine Struktur.",
  [("index.html","Apollon"), ("wissen.html","Wissen"), "Verein"]) + """
<section class="on-white"><div class="wrap">
  <div class="prose">
    <p class="auftakt">Was einer allein schwer tragen kann, können viele gemeinsam tragen. Das ist die ursprüngliche Idee hinter dem Verein.</p>
    <p class="leise" style="font-size:.93rem">Bevor es um die Form geht, geht es um die Entscheidung. Wenn Sie noch davorstehen, beginnen Sie hier: <a href="entscheidung.html">Wenn eine Entscheidung ansteht</a>.</p>
    <p>Menschen verbinden Wissen, Fähigkeiten, Vermögen, Verantwortung und Möglichkeiten, um einen gemeinsamen Zweck zu verwirklichen. Sie sorgen füreinander vor. Sie teilen Risiken. Sie bewahren Werte. Sie entwickeln Projekte. Sie schaffen etwas, das über den Einzelnen hinaus wirken kann.</p>
  </div>
</div></section>

<section><div class="wrap">
  <h2>Eine alte Idee mit erstaunlich modernen Möglichkeiten</h2>
  <div class="prose" style="margin-top:1.2rem">
    <p>Die Geschichte gemeinschaftlicher Zusammenschlüsse reicht weit zurück. Bereits Gilden und Zünfte organisierten gemeinsame Interessen, Unterstützung und Vorsorge. Im 19. Jahrhundert entstanden aus dem Gedanken der gegenseitigen Unterstützung Strukturen, deren Nachfolger teilweise bis heute bestehen.</p>
  </div>
  <ul class="zeitleiste" style="max-width:38rem">
    <li><span class="jahr">Mittelalter</span><span class="was">Gilden und Zünfte organisieren gemeinsame Interessen, Unterstützung und Vorsorge.</span></li>
    <li><span class="jahr">1820, Gotha</span><span class="was">Eine Feuerversicherung nach dem Gegenseitigkeitsprinzip entsteht.</span></li>
    <li><span class="jahr">1824, Österreich</span><span class="was">Gründung der Wechselseitigen k. k. priv. Brandschaden-Versicherungs-Anstalt.</span></li>
    <li><span class="jahr">1828, Graz</span><span class="was">Unter Erzherzog Johann entsteht die Grazer Wechselseitige.</span></li>
    <li><span class="jahr">1896, Westfalen</span><span class="was">Landwirte gründen einen Versicherungsverein, aus dem die heutige LVM hervorging.</span></li>
    <li><span class="jahr">Heute</span><span class="was">Dieselbe Idee, neue Vorhaben.</span></li>
  </ul>
  <div class="prose" style="margin-top:1.6rem">
    <p>Die Herausforderungen waren unterschiedlich. Der zugrunde liegende Gedanke war ähnlich: Menschen hatten ein gemeinsames Anliegen und schufen dafür eine gemeinsame Struktur.</p>
  </div>
</div></section>

<section class="on-white"><div class="wrap">
  <div class="prose">
    <h2>Gemeinsam Möglichkeiten schaffen</h2>
    <p style="margin-top:1rem">Der Verein ist eine eigene Rechtspersönlichkeit. Damit kann er selbst Träger von Rechten und Pflichten sein und, im Rahmen seiner konkreten rechtlichen Ausgestaltung, Verträge schließen, Konten führen, Eigentum halten, Mitarbeiter beschäftigen, Projekte durchführen und Einnahmen erzielen.</p>
    <p>Dadurch eröffnet sich eine entscheidende Perspektive: Der Verein kann Dinge tragen, die Menschen gemeinsam verwirklichen möchten.</p>
    <p>Genau deshalb betrachten wir bei Apollon einen Verein als Werkzeug. Die entscheidende Frage lautet:</p>
    <p class="auftakt">Was möchten Sie damit möglich machen?</p>
  </div>
</div></section>

<section><div class="wrap">
  <div class="prose">
    <h2>Der Zweck bestimmt die Struktur</h2>
    <p style="margin-top:1rem">Jeder Verein beginnt mit einem Zweck. Und genau dieser Zweck verdient besondere Aufmerksamkeit. Er beschreibt, wofür der Verein geschaffen wird, was die Beteiligten miteinander verwirklichen möchten und in welchem Rahmen der Verein tätig werden soll.</p>
    <p>Deshalb beginnt unsere Arbeit mit dem Vorhaben:</p>
    <ul>
      <li>Was soll entstehen?</li>
      <li>Was soll erhalten werden?</li>
      <li>Welche Menschen sollen miteinander wirken?</li>
      <li>Welche Projekte sollen umgesetzt werden?</li>
      <li>Welche Ressourcen sollen gemeinsam genutzt werden?</li>
      <li>Welche Werte sollen weitergetragen werden?</li>
      <li>Welche Aufgaben soll der Verein übernehmen?</li>
    </ul>
    <p>Aus diesen Antworten entwickelt sich die Struktur. Die Statuten geben diesem Vorhaben anschließend seinen Rahmen.</p>

    <h2 style="margin-top:2.6rem">Jeder Verein trägt seine eigene Idee</h2>
    <p style="margin-top:1rem">Jedes Projekt ist anders. Jeder Verein entsteht aus einer eigenen Ausgangssituation. Menschen, Ziele, vorhandene Strukturen, Projekte und zukünftige Entwicklungen unterscheiden sich.</p>
    <p>Deshalb entwickeln wir Statuten aus dem jeweiligen Vorhaben heraus. Besondere Bedeutung hat dabei die Formulierung des Vereinszwecks. Er soll das Vorhaben so beschreiben, dass die Struktur heute trägt und gleichzeitig Raum für die geplante Entwicklung bietet.</p>
    <p>Für uns sind Statuten deshalb weit mehr als ein Dokument für die Gründung. Sie bilden die Bodenplatte, auf der der Verein anschließend arbeiten kann.</p>
  </div>
</div></section>

<section class="on-white"><div class="wrap">
  <div class="prose">
    <h2>Ein Verein kann wirtschaftlich tätig sein</h2>
    <p style="margin-top:1rem">Ein Verein kann Einnahmen erzielen, Leistungen anbieten, Rechnungen stellen, Projekte betreiben und Menschen für ihre Tätigkeit bezahlen. Entscheidend ist die konkrete Ausgestaltung des Vereins und seines Zwecks.</p>
    <p>Damit eröffnet der Verein Möglichkeiten, die weit über das verbreitete Bild von Vereinsfest, Ehrenamt und Freizeitgestaltung hinausgehen. Er kann Wissen vermitteln, Projekte entwickeln, Infrastruktur bereitstellen, Veranstaltungen durchführen, Vermögen halten und unterschiedliche Menschen oder Kompetenzen unter einem gemeinsamen Zweck verbinden.</p>
    <p>Die konkrete Tätigkeit ergibt sich aus dem jeweiligen Vorhaben und der dafür geschaffenen Struktur.</p>
  </div>
</div></section>

<section><div class="wrap">
  <div class="prose">
    <h2>Vermögen kann einem Zweck dienen</h2>
    <p style="margin-top:1rem">Ein weiterer wichtiger Gedanke entsteht dort, wo Menschen über längere Zeiträume und Generationen denken. Immobilien. Grundstücke. Unternehmensbeteiligungen. Wertpapiere. Sachwerte. Andere Vermögenswerte.</p>
    <p>Ein Verein besitzt als eigene Rechtspersönlichkeit eigenes Vereinsvermögen. Damit entsteht die Möglichkeit, Vermögenswerte innerhalb einer auf Dauer angelegten Struktur zu halten und einem gemeinsamen Zweck zuzuordnen.</p>
    <p>Gerade bei Familien, Unternehmern und Menschen mit langfristig aufgebautem Vermögen entstehen daraus interessante Fragen:</p>
    <ul>
      <li>Was soll mit diesem Vermögen langfristig geschehen?</li>
      <li>Was soll erhalten bleiben?</li>
      <li>Welchem Zweck soll es künftig dienen?</li>
      <li>Wie soll es über Generationen weiterwirken?</li>
      <li>Welche Struktur kann dieses Ziel tragen?</li>
    </ul>
    <p>Diese Fragen verdienen eine individuelle Betrachtung.</p>

    <h2 style="margin-top:2.6rem">Familie ist bereits Gemeinschaft</h2>
    <p style="margin-top:1rem">Viele Menschen verbinden einen Verein zunächst mit einer größeren Gruppe. Dabei beginnt Gemeinschaft häufig viel früher: in der Familie.</p>
    <p>Auch Familien verfolgen gemeinsame Ziele, besitzen Vermögen, entwickeln Projekte, tragen Verantwortung und beschäftigen sich mit der Frage, was für kommende Generationen erhalten bleiben soll.</p>
    <p>Ein Verein kann deshalb auch im familiären Zusammenhang eine interessante Struktur sein, wenn Menschen einen gemeinsamen Zweck dauerhaft organisieren möchten.</p>
    <p class="leise" style="font-size:.93rem;margin-top:1.2rem">Dass der Zusammenschluss von Menschen mit einem gemeinsamen Ziel ein tragfähiger Weg ist, sieht man nicht nur bei uns. Die Bertelsmann Stiftung beschreibt im Magazin <em>Change</em>, wie eine Vereinsgründung Schritt für Schritt abläuft: <a href="https://www.change-magazin.de/de/verein-gruenden" target="_blank" rel="noopener">Verein gründen: In fünf Schritten zum eingetragenen Verein</a>.</p>
  </div>
</div></section>

<section class="on-white"><div class="wrap">
  <div class="prose">
    <h2>Unternehmertum über Generationen denken</h2>
    <p style="margin-top:1rem">Ein Unternehmen beantwortet viele Fragen des täglichen Wirtschaftens. Uns interessiert zusätzlich die langfristige Perspektive:</p>
    <ul>
      <li>Was soll bleiben?</li>
      <li>Was soll wachsen?</li>
      <li>Was soll weitergegeben werden?</li>
      <li>Welche Werte sollen erhalten werden?</li>
      <li>Welche Projekte sollen auch in Zukunft weiterleben können?</li>
      <li>Und welche Struktur dient diesem Ziel?</li>
    </ul>
    <p>Verein, Unternehmen, <a href="wissen-ewiv.html">EWIV</a> und Stiftung können dabei unterschiedliche Werkzeuge innerhalb einer größeren Architektur sein. Die Ausgangsfrage bleibt immer dieselbe: Was möchten Sie erreichen?</p>
  </div>
</div></section>

<section><div class="wrap">
  <div class="prose">
    <h2>Die richtige Entscheidung beginnt mit Verstehen</h2>
    <p style="margin-top:1rem">Menschen sprechen über ihre Pläne. Mit Familienmitgliedern. Mit Freunden. Mit Geschäftspartnern. Mit Menschen, die eigene Erfahrungen gemacht haben.</p>
    <p>Diese Erfahrungen gehören zu deren Geschichte, deren Verein und deren Ausgangssituation. Ihre Entscheidung betrifft jedoch Ihr Vorhaben. Und Sie tragen die Konsequenzen dieser Entscheidung.</p>
    <p>Deshalb ist es sinnvoll, zunächst die eigenen Möglichkeiten zu verstehen:</p>
    <ul>
      <li>Welche Konsequenzen entstehen, wenn Sie handeln?</li>
      <li>Welche Konsequenzen entstehen, wenn Sie eine Entscheidung verschieben?</li>
      <li>Welche Struktur passt zu Ihrem Ziel?</li>
      <li>Welche Alternativen gibt es?</li>
      <li>Was soll langfristig erreicht werden?</li>
    </ul>
    <p class="auftakt" style="margin-top:1.6rem">Aus Wissen entsteht Klarheit. Aus Klarheit entsteht Entscheidungsfähigkeit.</p>
  </div>
</div></section>

<section class="on-white"><div class="wrap">
  <div class="prose">
    <h2>Ist der Verein das richtige Werkzeug?</h2>
    <p style="margin-top:1rem">Genau diese Frage steht bei uns am Anfang. Menschen kommen mit einer Herausforderung, einer Idee oder einem Ziel. Manchmal denken sie bereits an einen Verein. Manchmal entsteht diese Möglichkeit erst während der Betrachtung.</p>
    <p>Gemeinsam schauen wir auf das gesamte Vorhaben. Auf die Menschen. Auf vorhandene Unternehmen. Auf Vermögen. Auf Projekte. Auf die Zukunft. Auf das, was erhalten werden soll. Und auf das, was neu entstehen darf.</p>
    <p>Daraus ergibt sich die entscheidende Frage: Ist der Verein für das, was Sie erreichen möchten, das passende Werkzeug? Diese Entscheidung braucht Wissen, Erfahrung und Gespür für das gesamte Vorhaben.</p>

    <h2 style="margin-top:2.6rem">Von der Idee zur gelebten Struktur</h2>
    <p style="margin-top:1rem">Eine Vereinsgründung beginnt mit dem Verstehen des Vorhabens. Daraus entwickeln sich Zweck, Statuten und Struktur. Und danach beginnt das Entscheidende: Der Verein wird mit Leben gefüllt.</p>
    <p>Projekte entstehen. Menschen arbeiten miteinander. Ressourcen werden eingesetzt. Wissen wird weitergegeben. Werte können erhalten werden. Der Verein erfüllt den Zweck, für den er geschaffen wurde.</p>
    <p>Genau dort wird aus einem Stück Papier ein Werkzeug.</p>
  </div>
</div></section>

<section><div class="wrap">
  <h2>Die Artikel zu diesem Thema</h2>
  <p style="max-width:38rem;margin-top:.8rem">Jeder beantwortet genau eine Frage.</p>
  """ + artlist([
   ("Darf ein Verein Rechnungen schreiben?", "wissen-verein-rechnungen.html"),
   ("Was kostet eine Vereinsgründung in Österreich?", "wissen-verein-kosten-oesterreich.html"),
   ("Wie viele Personen braucht man für eine Vereinsgründung?", "wissen-verein-personen.html"),
   ("Verein oder Einzelunternehmen: was passt wann?", "wissen-verein-oder-einzelunternehmen.html"),
   ("Verein oder GmbH: der ehrliche Vergleich", "wissen-verein-oder-gmbh.html"),
   ("Was gehört in Vereinsstatuten, und was besser nicht?", "wissen-verein-statuten.html"),
   ("Muss ein Verein gemeinnützig sein?", "wissen-verein-gemeinnuetzig.html"),
   ("Wie zahlt ein Verein jemanden aus?", "wissen-verein-auszahlen.html"),
   ("Welche Organe braucht ein Verein wirklich?", "wissen-verein-organe.html"),
   ("Was passiert bei einer Vereinsprüfung?", "wissen-verein-pruefung.html"),
   ("Verein gründen in Deutschland oder Österreich: der Unterschied", "wissen-verein-deutschland-oesterreich.html"),
   ("Wie aus einem Verein ein wirtschaftlich tragender Betrieb wird", "wissen-verein-tragender-betrieb.html"),
  ]) + """
</div></section>

<section class="on-white"><div class="wrap narrow">
  <h2>Häufige Fragen</h2>""" + faq(pairs) + """
</div></section>

<section class="on-navy"><div class="wrap narrow" style="text-align:center">
  <p class="kicker">Was möchten Sie möglich machen?</p>
  <h2>Vielleicht haben Sie bereits eine Vorstellung.</h2>
  <p style="margin-top:1.2rem">Vielleicht besitzen Sie Immobilien oder andere Vermögenswerte und denken über deren Zukunft nach. Vielleicht möchten Sie gemeinsam mit Ihrer Familie etwas erhalten oder entwickeln. Vielleicht möchten Sie ein Projekt aufbauen. Oder Sie möchten zunächst verstehen, welche Möglichkeiten ein Verein überhaupt eröffnet.</p>
  <p style="margin-top:1.2rem">Dann beginnt unser gemeinsames Gespräch bei Ihrem Vorhaben. Bei dem, was bereits vorhanden ist. Bei dem, was entstehen soll.</p>
  <p style="margin-top:1.6rem"><a class="btn-light" href="gespraech.html">Was möchten Sie möglich machen?</a></p>
</div></section>
"""
page("wissen-verein.html", "Verein | Apollon",
     "Menschen schließen sich zusammen, um gemeinsam zu tragen, was einer allein nicht trägt. Was ein Verein möglich macht und wie aus einem Vorhaben eine tragfähige Struktur wird.",
     body, faq_schema(pairs))

# ============================================================ EWIV
pairs2 = [
 ("Was ist eine EWIV?",
  "Die Europäische wirtschaftliche Interessenvereinigung ist eine Rechtsform der Europäischen Union für die Zusammenarbeit über Ländergrenzen hinweg. Unternehmen, Vereine und selbstständig tätige Menschen aus verschiedenen Mitgliedstaaten verbinden darin Wissen, Fähigkeiten, Ressourcen und Projekte, ohne ihre Eigenständigkeit aufzugeben."),
 ("Was bedeutet die Abkürzung EWIV?",
  "EWIV steht für Europäische wirtschaftliche Interessenvereinigung. Im europäischen Sprachgebrauch findet sich auch die Bezeichnung EEIG für European Economic Interest Grouping."),
 ("Welche Möglichkeiten bietet eine EWIV?",
  "Sie gibt grenzüberschreitender Zusammenarbeit eine eigene Struktur. Beteiligte können gemeinsam entwickeln, gemeinsam anbieten, Wissen und Erfahrungen teilen, Ressourcen bündeln und Projekte über Ländergrenzen hinweg umsetzen. Welche Möglichkeiten im Einzelfall entstehen, ergibt sich aus dem Vorhaben."),
 ("Für wen kann eine EWIV interessant sein?",
  "Für Unternehmer, Vereine und Organisationen, die mit Partnern in anderen europäischen Ländern zusammenarbeiten möchten und dafür eine tragfähige gemeinsame Form suchen. Und für alle, die eine bestehende Struktur europäisch erweitern wollen."),
 ("Welche Bedeutung hat der europäische Binnenmarkt für eine EWIV?",
  "Der Binnenmarkt ist die Grundlage. Er erlaubt es Menschen, Unternehmen, Waren, Leistungen und Kapital, sich innerhalb Europas frei zu bewegen. Die EWIV ist die Rechtsform, die dieser Freiheit eine unternehmerische Form gibt."),
 ("Wie funktioniert grenzüberschreitende Zusammenarbeit mit einer EWIV?",
  "Die Beteiligten bringen ein, was bereits vorhanden ist: Wissen, Infrastruktur, Kontakte, Märkte, Erfahrungen, Fähigkeiten. Die Vereinigung wird zum gemeinsamen Raum dafür. Jeder bleibt dabei eigenständig."),
 ("Wie können bestehende Unternehmen, Vereine und Projekte miteinander verbunden werden?",
  "Über die gemeinsame Aufgabe. Zuerst wird geklärt, was gemeinsam entstehen soll und was jeder Beteiligte mitbringt. Daraus ergibt sich, welche Aufgabe die Vereinigung übernimmt und wie sie mit den bestehenden Strukturen zusammenwirkt."),
 ("Welche Rolle kann eine EWIV innerhalb einer größeren Unternehmensstruktur übernehmen?",
  "Sie kann der europäische Teil einer größeren Architektur sein. Unternehmen, Verein, EWIV und Stiftung übernehmen dabei unterschiedliche Aufgaben. Welche Struktur welche Aufgabe trägt, ergibt sich aus dem Ziel."),
 ("Warum beginnt die Entwicklung einer Struktur mit dem unternehmerischen Ziel?",
  "Weil eine Struktur nur dann trägt, wenn sie zu dem passt, was sie tragen soll. Wer mit der Rechtsform beginnt, sucht anschließend eine Aufgabe für ein Werkzeug. Wer mit dem Ziel beginnt, findet das passende Werkzeug."),
]
body = head_block("Apollon", "EWIV",
  "Europa ist ein Binnenmarkt. Wir sind der Binnenmarkt.",
  [("index.html","Apollon"), ("wissen.html","Wissen"), "EWIV"]) + """
<section class="on-navy"><div class="wrap narrow" style="text-align:center">
  <p class="auftakt" style="color:#fff;max-width:none;margin:0">Europa ist ein Binnenmarkt.<br>Wir sind der Binnenmarkt.</p>
</div></section>

<section class="on-white"><div class="wrap">
  <div class="prose">
    <p>Der europäische Binnenmarkt besteht aus Menschen, Unternehmen und Organisationen, die miteinander handeln, Wissen teilen, Leistungen erbringen, Projekte entwickeln und über Grenzen hinweg zusammenarbeiten. Wir sind diejenigen, die ihn mit Leben füllen.</p>
    <p>Genau hier setzt die Europäische wirtschaftliche Interessenvereinigung an, kurz EWIV. Sie gibt grenzüberschreitender Zusammenarbeit eine Struktur und eröffnet die Möglichkeit, Wissen, Fähigkeiten, Ressourcen, Unternehmen und Projekte miteinander zu verbinden.</p>
    <p class="leise" style="font-size:.93rem">Bevor es um die Form geht, geht es um die Entscheidung. Wenn Sie noch davorstehen, beginnen Sie hier: <a href="entscheidung.html">Wenn eine Entscheidung ansteht</a>.</p>
  </div>
</div></section>

<section><div class="wrap">
  <div class="prose">
    <h2>Gemeinsam entsteht mehr</h2>
    <p style="margin-top:1rem">Was geschieht, wenn mehrere Unternehmer ihre Möglichkeiten miteinander verbinden?</p>
    <p>Der eine verfügt über Wissen. Ein anderer über Infrastruktur. Ein weiterer über Kontakte, Märkte oder Erfahrungen. Andere bringen Fähigkeiten, Netzwerke, Ressourcen oder Projekte ein.</p>
    <p>Jeder bringt das ein, was bereits vorhanden ist. Aus der Verbindung dieser Möglichkeiten kann etwas entstehen, das den Handlungsspielraum aller Beteiligten erweitert.</p>
    <p class="auftakt">Für uns ist das europäisches Unternehmertum: Kooperation schafft Möglichkeiten.</p>
  </div>
</div></section>

<section class="on-white"><div class="wrap">
  <div class="prose">
    <h2>Die EWIV ist ein Werkzeug</h2>
    <p style="margin-top:1rem">Bei uns beginnt die Beschäftigung mit einer EWIV mit einer unternehmerischen Frage: Was möchten Sie damit möglich machen?</p>
    <ul>
      <li>Was soll gemeinsam entstehen?</li>
      <li>Welche Unternehmen, Vereine oder Menschen sollen zusammenarbeiten?</li>
      <li>Was bringt jeder Beteiligte mit?</li>
      <li>Welche Ressourcen stehen bereits zur Verfügung?</li>
      <li>Welche Fähigkeiten ergänzen sich?</li>
      <li>Welche Aufgaben können gemeinsam übernommen werden?</li>
      <li>Welchen Nutzen soll die Zusammenarbeit für die Beteiligten schaffen?</li>
    </ul>
    <p>Aus den Antworten auf diese Fragen entwickelt sich die Struktur.</p>

    <h2 style="margin-top:2.6rem">Die Idee bestimmt die Struktur</h2>
    <p style="margin-top:1rem">Eine tragfähige Struktur entsteht aus dem Vorhaben, das sie tragen soll. Deshalb betrachten wir zuerst das Ziel.</p>
    <p>Wir sehen uns bestehende Unternehmen, Vereine, Projekte, Fähigkeiten, Wissen und Ressourcen an. Wir verbinden Perspektiven. Wir entwickeln Möglichkeiten. Und wir fragen: Was möchten Sie künftig anders, größer oder gemeinsam gestalten?</p>
    <p>Damit bekommt die Struktur eine Aufgabe. Sie dient dem Vorhaben.</p>
  </div>
</div></section>

<section><div class="wrap">
  <div class="prose">
    <h2>Eine europäische Möglichkeit, die viele Unternehmer gerade erst entdecken</h2>
    <p style="margin-top:1rem">Die EWIV besteht seit Jahrzehnten. Gleichzeitig ist sie im unternehmerischen Alltag vergleichsweise wenig bekannt. Dabei eröffnet gerade der europäische Binnenmarkt interessante Möglichkeiten für Zusammenarbeit.</p>
    <ul>
      <li>Unternehmen können Wissen miteinander verbinden.</li>
      <li>Erfahrungen können weitergegeben werden.</li>
      <li>Ressourcen können gemeinsam genutzt werden.</li>
      <li>Projekte können grenzüberschreitend entwickelt werden.</li>
      <li>Kontakte und Netzwerke können sich ergänzen.</li>
    </ul>
    <p>Aus einzelnen Unternehmen und Organisationen kann eine Zusammenarbeit wachsen, von der die Beteiligten profitieren und in der ihre jeweilige Eigenständigkeit erhalten bleibt.</p>
    <p>Die entscheidende Frage lautet: Was können die Beteiligten gemeinsam daraus entwickeln?</p>

    <h3 style="margin-top:2.2rem">Eine Frage, die wir offen stellen</h3>
    <p>Wenn diese Form seit Jahrzehnten besteht und so viel ermöglicht, warum kennt sie dann kaum jemand?</p>
    <p>Ein Teil der Antwort ist unspektakulär: Sie ist eine Nische, sie steht in keinem Lehrplan, und Beraterinnen und Berater empfehlen in aller Regel das, womit sie selbst täglich arbeiten.</p>
    <p>Ob das die ganze Antwort ist, mag jeder für sich beurteilen. Uns interessiert an dieser Stelle etwas anderes: Wissen, das niemand weitergibt, wirkt wie Wissen, das es nicht gibt. Deshalb geben wir es weiter.</p>
  </div>
</div></section>

<section class="on-white"><div class="wrap">
  <div class="prose">
    <h2>Unternehmertum über Generationen denken</h2>
    <p style="margin-top:1rem">Unternehmerische Entscheidungen reichen häufig weit über das aktuelle Geschäftsjahr hinaus. Irgendwann entstehen andere Fragen:</p>
    <ul>
      <li>Was soll erhalten bleiben?</li>
      <li>Was soll weitergegeben werden?</li>
      <li>Wie können Wissen und Erfahrungen weiterleben?</li>
      <li>Wie können Projekte weiterentwickelt werden?</li>
      <li>Wie können bestehende Werte und wirtschaftliche Substanz auch künftig wirken?</li>
    </ul>
    <p>Genau deshalb betrachten wir unternehmerische Strukturen im Zusammenhang. Unternehmen, <a href="wissen-verein.html">Verein</a>, EWIV und Stiftung können unterschiedliche Aufgaben innerhalb einer größeren unternehmerischen Architektur übernehmen. Welche Struktur sinnvoll ist, ergibt sich aus dem jeweiligen Ziel.</p>
  </div>
</div></section>

<section><div class="wrap">
  <div class="prose">
    <h2>Wissen erweitert den Handlungsspielraum</h2>
    <p style="margin-top:1rem">Wer viele Möglichkeiten kennt, kann aus einem größeren Handlungsspielraum heraus entscheiden. Deshalb beginnt unternehmerische Entscheidungsfreiheit mit Wissen und Verständnis.</p>
    <p>Wir machen Zusammenhänge verständlich: Was ist eine EWIV? Welche Möglichkeiten eröffnet sie? Wie kann grenzüberschreitende Zusammenarbeit gestaltet werden? Wie können bestehende Unternehmen, Vereine und Projekte miteinander verbunden werden? Welche Aufgabe könnte eine EWIV innerhalb einer größeren Struktur übernehmen? Was möchten Sie damit erreichen?</p>
    <p class="auftakt">Aus Wissen entsteht Verständnis. Aus Verständnis entstehen Möglichkeiten. Aus Möglichkeiten entstehen bewusste Entscheidungen.</p>
  </div>
</div></section>

<section class="on-white"><div class="wrap">
  <div class="prose">
    <h2>Von der Idee zur gelebten Struktur</h2>
    <p style="margin-top:1rem">Eine EWIV zu kennen, ist der Anfang. Spannend wird sie dort, wo wir betrachten, was sie für das eigene Vorhaben ermöglichen kann.</p>
    <p>Wir vermitteln Wissen und Erfahrung rund um die EWIV und entwickeln gemeinsam mit Unternehmern Ideen, Ausrichtungen und Modelle für europäische Zusammenarbeit. Wir betrachten dazu die vorhandene Situation: Unternehmen und Organisationen. Menschen und Fähigkeiten. Projekte und Ideen. Wissen und Erfahrungen. Ressourcen und Möglichkeiten. Und vor allem das Ziel, das erreicht werden soll.</p>
    <p>So entsteht aus einer europäischen Rechtsform eine unternehmerisch gedachte und praktisch nutzbare Struktur.</p>
  </div>
</div></section>

<section><div class="wrap narrow">
  <h2>Häufige Fragen zur EWIV</h2>""" + faq(pairs2) + """
</div></section>

<section class="on-navy"><div class="wrap narrow" style="text-align:center">
  <p class="kicker">Was möchten Sie möglich machen?</p>
  <h2>Vielleicht haben Sie bereits von einer EWIV gehört.</h2>
  <p style="margin-top:1.2rem">Vielleicht beschäftigen Sie sich schon länger mit europäischen Strukturen. Vielleicht suchen Sie eine Möglichkeit, mehrere Unternehmen, Vereine, Projekte oder Kompetenzen sinnvoll miteinander zu verbinden. Oder Sie möchten zunächst entdecken, welche Möglichkeiten Ihnen zur Verfügung stehen.</p>
  <p style="margin-top:1.2rem">Dann beginnt unser gemeinsames Gespräch genau dort: bei Ihrer Ausgangssituation, bei Ihrer Idee, bei dem, was Sie erreichen möchten.</p>
  <p style="margin-top:1.6rem"><a class="btn-light" href="gespraech.html">EWIV-Beratung</a></p>
</div></section>
"""
page("wissen-ewiv.html", "EWIV: Europäische wirtschaftliche Interessenvereinigung | Apollon",
     "Die EWIV gibt grenzüberschreitender Zusammenarbeit in Europa eine Struktur. Was sie ist, welche Möglichkeiten sie eröffnet und wie aus einem unternehmerischen Ziel eine tragfähige europäische Struktur wird.",
     body, faq_schema(pairs2))

# ============================================================ PILLAR 3, KÖRPER
pairs3 = [
 ("Was ist eine Fußlesung?",
  "Ein Blick auf die Fußsohlen, aus dem sich Spannungen, Belastungen und Muster ablesen lassen. Sie dient dem Verstehen von Zusammenhängen und ersetzt keine ärztliche Diagnose."),
 ("Ist das eine medizinische Behandlung?",
  "Nein. Es handelt sich um eine Beobachtung und Begleitung, nicht um Heilkunde. Bei gesundheitlichen Beschwerden ist ärztlicher Rat einzuholen."),
 ("Für wen ist das nichts?",
  "Für Menschen, die eine schnelle Lösung suchen. Die Arbeit setzt voraus, dass jemand bereit ist, Ursachen anzusehen statt Symptome wegzuräumen."),
]
body = head_block("Wissen", "Der Körper liest mit",
  "Was Druck, Haltung und Füße über einen Menschen erzählen, lange bevor er es selbst in Worte fasst.",
  [("index.html","Apollon"), ("wissen.html","Wissen"), "Der Körper"]) + """
<section class="on-white"><div class="wrap">
  <div class="kurz"><strong>Kurz gesagt</strong><p>Der Körper zeigt an, was ein Mensch trägt. Die Fußlesung ist ein Weg, diese Zeichen zu lesen, um Ursachen statt Symptome zu betrachten. Sie ist keine medizinische Diagnose und ersetzt keine ärztliche Behandlung, sondern dient dem Verstehen von Zusammenhängen.</p></div>
  <div class="prose">
    <p>Wer über Jahre gegen sich selbst arbeitet, sieht irgendwann anders aus. Das ist keine Esoterik, das ist Statik. Der Körper verteilt Lasten um, und diese Umverteilung hinterlässt Spuren.</p>
    <h3>Warum die Füße</h3>
    <p>Weil dort alles ankommt. Sie tragen das ganze Gewicht, den ganzen Tag, ein Leben lang. Was an Druck entsteht, wird dort sichtbar, bevor es woanders wehtut.</p>
    <h3>Was daraus wird</h3>
    <p>Kein Befund und keine Diagnose, sondern ein Gespräch. Über das, was ein Mensch trägt, warum er es trägt und was passieren müsste, damit er es ablegen kann.</p>
    <h3>Für wen es nichts ist</h3>
    <p>Für Menschen, die eine schnelle Lösung suchen. Wer die Ursache nicht ansehen will, wird mit dem Symptom weiter zu tun haben.</p>
    <p style="font-size:.9rem;color:var(--ink-faint)">Diese Arbeit ersetzt keine ärztliche oder psychotherapeutische Behandlung. Bei gesundheitlichen Beschwerden wenden Sie sich bitte an eine Ärztin oder einen Arzt.</p>
  </div>
</div></section>

<section><div class="wrap">
  <h2>Die Artikel zu diesem Thema</h2>
  """ + artlist([
   ("Was ist eine Fußlesung?", "wissen-koerper-fusslesung.html"),
   ("Was der Körper über Druck erzählt", "wissen-koerper-druck.html"),
   ("Warum Symptome bekämpfen selten hilft", "wissen-koerper-symptome.html"),
  ]) + """
</div></section>

<section class="on-white"><div class="wrap narrow">
  <h2>Häufige Fragen</h2>""" + faq(pairs3) + """
  <p style="margin-top:2rem"><a class="btn-solid" href="konvaleszenz.html">Zur Konvaleszenz</a></p>
</div></section>
"""
page("wissen-koerper.html", "Der Körper liest mit | Apollon",
     "Was Druck, Haltung und Füße über einen Menschen erzählen. Die Grundlage der Arbeit in der Konvaleszenz.",
     body, faq_schema(pairs3))

# ============================================================ FEMININER AUSSTIEG
body = head_block("Wege in Bewegung", "Der feminine Ausstieg",
  "Souveränität statt Abhängigkeit. Für Frauen im Übergang zwischen Abschied und Aufbruch.",
  [("index.html","Apollon"), "Der feminine Ausstieg"]) + """
<section class="on-white"><div class="wrap two">
  <div>
    <p class="quote">&bdquo;Irgendwann ist kein Datum.&ldquo;</p>
    <p style="margin-top:1.6rem;max-width:32rem">Handeln braucht eine Entscheidung, keine Perfektion. Die meisten warten nicht auf mehr Klarheit, sondern auf einen Moment, der von allein nie kommt.</p>
  </div>
  <div class="body-col">
    <div class="kurz"><strong>Kurz gesagt</strong><p>Der feminine Ausstieg ist ein begleitetes Programm für Frauen, die einen Neuanfang gestalten wollen. Es führt in drei Stufen von der Entscheidung über die ersten Schritte bis zur Verankerung im neuen Alltag. Der Zugang läuft über eine Bewerbung, nicht über eine Buchung.</p></div>
    <p>Gemeint ist nicht zwingend der berufliche Ausstieg. Gemeint ist der Schritt in die eigene Zuständigkeit. Weg von Verhältnissen, in denen andere über den eigenen Alltag entscheiden.</p>
    <p>Das ist selten ein einzelner Tag. Es ist ein Übergang, und Übergänge sind die Phase, in der die meisten umkehren.</p>
  </div>
</div></section>

<section><div class="wrap">
  <h2>Die drei Stufen</h2>
  <ol class="steps" style="margin-top:2rem">
    <li><p class="dur">Etwa vier Wochen</p><h3>Entscheidung</h3><p>Klarheit gewinnen, Wahrheit erkennen. Was ist tatsächlich der Fall, was ist Gewohnheit und was ist Angst. Am Ende steht eine Entscheidung, die trägt.</p></li>
    <li><p class="dur">Etwa drei Monate</p><h3>Aktion</h3><p>Die ersten Schritte werden umgesetzt. Nicht alle auf einmal, sondern in der Reihenfolge, die zur Lage passt.</p></li>
    <li><p class="dur">Etwa sechs Monate</p><h3>Verankerung</h3><p>Das Neue wird Alltag. Aus Absicht wird Gewohnheit, aus Gewohnheit wird Selbstverständlichkeit.</p></li>
  </ol>
</div></section>

<section class="on-white"><div class="wrap two">
  <div>
    <h2>Der leisere erste Schritt</h2>
    <p style="margin-top:1.2rem">Wer sich noch nicht bewerben möchte, kann mit dem Impulsbuch beginnen. Es ist ein Kapitel aus &bdquo;Erste Person&ldquo; und bringt ziemlich genau auf den Punkt, worum es geht.</p>
    <p style="margin-top:1.4rem"><a class="btn-outline" href="buch.html">Zum Buch</a></p>
  </div>
  <div class="body-col">
    <h2>Bewerbung</h2>
    <p style="margin-top:1.2rem">Die Zusammenarbeit beginnt mit einer Bewerbung und einem Gespräch. Über Umfang und Kosten sprechen wir dort, weil beides von Ihrer Lage abhängt.</p>
    <p style="margin-top:1.4rem"><a class="btn-solid" href="gespraech.html">Gespräch vereinbaren</a></p>
  </div>
</div></section>

<section><div class="wrap"><div class="note"><strong>Umzug:</strong> Die bestehenden Inhalte von femininer-ausstieg.at werden hierher übernommen, inklusive Erfahrungsberichten und Impulsbuch-Strecke. Danach wird die alte Adresse seitengenau hierher weitergeleitet.</div></div></section>
"""
page("ausstieg.html", "Der feminine Ausstieg | Apollon",
     "Begleitung für Frauen im Übergang. Drei Stufen von der Entscheidung bis zur Verankerung. Souveränität statt Abhängigkeit.", body)

# ============================================================ KONVALESZENZ
body = head_block("Wege in Bewegung", "Konvaleszenz",
  "Fußlesung und Mentoring in Wien. Für Menschen, die Ursachen verstehen wollen, statt Symptome zu bekämpfen.",
  [("index.html","Apollon"), "Konvaleszenz"]) + """
<section class="on-white"><div class="wrap two">
  <div>
    <p class="quote">&bdquo;Wer eine schnelle Lösung sucht, ist hier nicht richtig.&ldquo;</p>
    <p style="margin-top:1.6rem;max-width:32rem">Konvaleszenz heißt Genesung. Gemeint ist nicht das Verschwinden eines Symptoms, sondern der Weg zurück in die eigene Zuständigkeit für den eigenen Zustand.</p>
  </div>
  <div class="body-col">
    <div class="kurz"><strong>Kurz gesagt</strong><p>Konvaleszenz verbindet die Fußlesung als ersten Blick mit einer anschließenden Begleitung. Die Fußlesung zeigt Spannungen und Muster, das Mentoring arbeitet an dem, was dahintersteht. Angeboten wird beides in Wien. Es ist keine medizinische Behandlung.</p></div>
    <p>Am Anfang steht ein Blick auf die Fußsohlen. Was sich dort zeigt, ist selten überraschend, wenn man es ausgesprochen hört. Es ist nur meistens noch nie ausgesprochen worden.</p>
    <p>Daraus wird ein Gespräch über Verantwortung, Druck und Erwartungen. Und, wenn es passt, eine längere Begleitung.</p>
  </div>
</div></section>

<section><div class="wrap">
  <h2>Wie gearbeitet wird</h2>
  <div class="two" style="margin-top:2rem">
    <article class="card"><h3>Die Fußlesung</h3><p>Der erste Termin. Ein Blick auf das, was der Körper trägt, und ein Gespräch darüber, was daraus folgt. Dazu Hinweise zu Ernährung und Alltag, wenn sie sich aus dem Gesehenen ergeben.</p></article>
    <article class="card"><h3>Das Mentoring</h3><p>Die längere Begleitung. Hier geht es um die Zusammenhänge zwischen Verantwortung, Druck und den Erwartungen, die ein Mensch an sich selbst stellt.</p></article>
  </div>
  <p style="margin-top:2rem;max-width:38rem;font-size:.92rem;color:var(--ink-faint)">Diese Arbeit ersetzt keine ärztliche oder psychotherapeutische Behandlung. Bei gesundheitlichen Beschwerden wenden Sie sich bitte an eine Ärztin oder einen Arzt.</p>
  <p style="margin-top:1.6rem"><a class="btn-solid" href="gespraech.html">Termin anfragen</a> <a class="btn-outline" href="wissen-koerper.html" style="margin-left:.6rem">Das Wissen dahinter</a></p>
</div></section>

<section class="on-white"><div class="wrap"><div class="note"><strong>Umzug:</strong> Blogartikel, Erfahrungsberichte und News von konvaleszenz.com werden hierher übernommen. Die Artikel wandern in das Journal und in den Wissensbereich, die Erfahrungsberichte auf diese Seite.</div></div></section>
"""
page("konvaleszenz.html", "Konvaleszenz, Fußlesung und Mentoring in Wien | Apollon",
     "Fußlesung und Mentoring in Wien. Ursachen verstehen statt Symptome bekämpfen.", body)

# ============================================================ GESPRÄCH
body = head_block("Der nächste Schritt", "Ein Gespräch.",
  "Kein Verkaufstermin und kein Vortrag. Sie erzählen, was gerade ansteht, und wir sagen Ihnen ehrlich, wie wir Ihnen dabei helfen können.",
  [("index.html","Apollon"), "Gespräch"]) + """
<section class="on-white"><div class="wrap narrow">
  <p class="lead">Sagen Sie uns vorab kurz, worum es geht. Dann gehen wir vorbereitet in das Gespräch, und Sie müssen nicht bei null anfangen.</p>
  <form class="apo" method="post" action="formular.php" style="margin-top:2rem">
    <input type="hidden" name="formular" value="Gespräch vereinbaren">
    <div style="position:absolute;left:-9999px" aria-hidden="true"><label for="hp2">Bitte leer lassen</label><input id="hp2" type="text" name="webseite" tabindex="-1" autocomplete="off"></div>
    <fieldset><legend>Sie</legend>
      <div><label for="n">Name</label><input id="n" name="name" type="text" required></div>
      <div style="margin-top:1rem"><label for="e">E-Mail</label><input id="e" name="email" type="email" required></div>
      <div style="margin-top:1rem"><label for="t">Telefon</label><input id="t" name="telefon" type="tel"><p class="hint">Freiwillig. Manchmal ist ein Anruf schneller.</p></div>
    </fieldset>
    <fieldset><legend>Ihr Anliegen</legend>
      <div><label for="u">Ihr Unternehmen oder Ihre Tätigkeit, in einem Satz</label><input id="u" name="unternehmen" type="text"></div>
      <div style="margin-top:1rem"><label for="w">Womit können wir Ihnen helfen?</label><textarea id="w" name="anliegen" required></textarea>
        <p class="hint">Schreiben Sie einfach frei heraus, worum es geht. Zwei, drei Sätze genügen. Ehrlich ist wichtiger als vollständig.</p></div>
      <div style="margin-top:1rem"><label for="z">Was wäre für Sie ein gutes Ergebnis?</label><textarea id="z" name="ziel" style="min-height:5.5rem"></textarea>
        <p class="hint">Freiwillig. Muss noch nicht fertig gedacht sein.</p></div>
    </fieldset>
    <div class="check"><input id="mensch" name="mensch" type="checkbox" required><label for="mensch">Ich bin ein Mensch.</label></div>
    <div><button class="btn-solid" type="submit">Absenden</button></div>
    <p class="hint">Ihre Angaben werden ausschließlich zur Bearbeitung Ihrer Anfrage verwendet und nicht weitergegeben. Siehe <a href="datenschutz.html">Datenschutz</a>.</p>
  </form>
</div></section>

<section><div class="wrap narrow">
  <h2>Oder direkt</h2>
  <p style="margin-top:1rem">Wirtschaftsverein Apollon<br>Prinz-Eugen-Straße 68, 1040 Wien</p>
  <p>Telefon <a href="tel:+436766269486">+43 676 626 9486</a><br>E-Mail <a href="mailto:kontakt@apollon.eu.com">kontakt@apollon.eu.com</a></p>
</div></section>
"""
page("gespraech.html", "Gespräch vereinbaren | Apollon",
     "Ein Gespräch mit Apollon. Sagen Sie vorab kurz, worum es geht.", body)

# ============================================================ IMPRESSUM
body = head_block("Rechtliches", "Impressum",
  "Angaben gemäß § 5 ECG und § 25 Mediengesetz.", [("index.html","Apollon"), "Impressum"]) + """
<section class="on-white"><div class="wrap narrow legalprose">
  <h3>Medieninhaber und Betreiber</h3>
  <p>Wirtschaftsverein Apollon<br>Prinz-Eugen-Straße 68<br>1040 Wien, Österreich</p>
  <h3>Vertretungsberechtigt</h3>
  <p>Obfrau: Marion Bernard</p>
  <h3>Kontakt</h3>
  <p>Telefon: +43 676 626 9486<br>E-Mail: kontakt@apollon.eu.com</p>
  <h3>ZVR-Zahl</h3>
  <p>1719735645</p>
  <h3>Vereinszweck</h3>
  <p>Ideelle und wirtschaftliche Förderung der Mitglieder sowie Bildungs- und Entwicklungsarbeit für Unternehmer und Menschen in Veränderungsprozessen.</p>
  <h3>Bildnachweis</h3>
  <p>Eigene Aufnahmen. Ergänzend Pixabay und Adobe Stock.</p>
  <h3>Haftung für Inhalte</h3>
  <p>Die Inhalte dieser Seiten wurden mit Sorgfalt erstellt. Für die Richtigkeit, Vollständigkeit und Aktualität wird keine Gewähr übernommen. Rechtliche Ausführungen ersetzen keine Rechtsberatung im Einzelfall.</p>
  <h3>Haftung für Links</h3>
  <p>Für die Inhalte verlinkter externer Seiten sind ausschließlich deren Betreiber verantwortlich.</p>
  <div class="note"><strong>Zu prüfen:</strong> Der Vereinszweck ist sinngemäß formuliert und sollte durch den Wortlaut aus den Statuten ersetzt werden. Falls eine UID-Nummer besteht, gehört sie ebenfalls hierher.</div>
</div></section>
"""
page("impressum.html", "Impressum | Apollon", "Impressum des Wirtschaftsvereins Apollon, Wien.", body)

# ============================================================ DATENSCHUTZ
body = head_block("Rechtliches", "Datenschutzerklärung",
  "Welche Daten wir verarbeiten, warum, und welche Rechte Sie haben.", [("index.html","Apollon"), "Datenschutz"]) + """
<section class="on-white"><div class="wrap narrow legalprose">
  <h3>Verantwortlicher</h3>
  <p>Wirtschaftsverein Apollon, Prinz-Eugen-Straße 68, 1040 Wien. Kontakt: kontakt@apollon.eu.com</p>
  <h3>Aufruf dieser Website</h3>
  <p>Beim Aufruf werden technisch notwendige Daten verarbeitet: IP-Adresse, Datum und Uhrzeit, aufgerufene Seite, Browsertyp. Rechtsgrundlage ist das berechtigte Interesse an einem sicheren Betrieb nach Art. 6 Abs. 1 lit. f DSGVO. Die Speicherung erfolgt für längstens sieben Tage.</p>
  <h3>Keine Cookies zur Auswertung</h3>
  <p>Diese Website verwendet keine Cookies zu Analyse- oder Werbezwecken und bindet keine Dienste Dritter ein, die personenbezogene Daten übertragen. Schriften und alle weiteren Bestandteile werden vom eigenen Server ausgeliefert. Deshalb ist kein Einwilligungsbanner erforderlich.</p>
  <h3>Formulare</h3>
  <p>Wenn Sie ein Kontakt- oder Bewerbungsformular ausfüllen, verarbeiten wir die angegebenen Daten ausschließlich zur Bearbeitung Ihrer Anfrage. Rechtsgrundlage ist Art. 6 Abs. 1 lit. b DSGVO. Die Daten werden gelöscht, sobald der Zweck entfallen ist und keine Aufbewahrungspflicht entgegensteht.</p>
  <h3>Newsletter</h3>
  <p>Ein Newsletter wird nur nach ausdrücklicher Einwilligung versendet. Die Einwilligung kann jederzeit widerrufen werden, ein Abmeldelink steht in jeder Nachricht.</p>
  <h3>Empfänger</h3>
  <p>Hostingdienstleister in Österreich, auf Grundlage eines Auftragsverarbeitungsvertrages. Eine Übermittlung in Drittstaaten findet nicht statt.</p>
  <h3>Speicherdauer</h3>
  <p>Wir speichern personenbezogene Daten nur so lange, wie es für den jeweiligen Zweck erforderlich ist oder gesetzliche Aufbewahrungsfristen dies verlangen.</p>
  <h3>Ihre Rechte</h3>
  <ul>
    <li>Auskunft über die verarbeiteten Daten</li>
    <li>Berichtigung unrichtiger Daten</li>
    <li>Löschung und Einschränkung der Verarbeitung</li>
    <li>Datenübertragbarkeit</li>
    <li>Widerspruch gegen die Verarbeitung</li>
    <li>Beschwerde bei der Österreichischen Datenschutzbehörde</li>
  </ul>
  <div class="note"><strong>Zu prüfen:</strong> Dies ist ein sorgfältiger Entwurf, keine Rechtsberatung. Sobald feststeht, welche Dienste tatsächlich eingebunden werden, ergänze ich die entsprechenden Abschnitte.</div>
</div></section>
"""
page("datenschutz.html", "Datenschutz | Apollon", "Datenschutzerklärung von Apollon. Keine Cookies zur Auswertung, keine Dienste Dritter.", body)

print("Teil 2 gebaut.")


# ============================================================ DANKE
body = head_block("Angekommen", "Danke.",
  "Ihre Nachricht ist bei uns. Wir melden uns.",
  [("index.html","Apollon"), "Danke"]) + """
<section class="on-white"><div class="wrap narrow">
  <p class="lead">Wir lesen jede Nachricht selbst.</p>
  <p>In der Regel melden wir uns innerhalb weniger Tage. Wenn es dringend ist, rufen Sie an: <a href="tel:+436766269486">+43 676 626 9486</a>.</p>
  <p style="margin-top:2rem"><a class="btn-solid" href="index.html">Zur Startseite</a> <a class="btn-outline" href="wissen.html" style="margin-left:.6rem">Zum Wissen</a></p>
</div></section>
"""
page("danke.html", "Danke | Apollon", "Ihre Nachricht ist angekommen.", body)

print("Dankeseite gebaut.")
