#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from build import *

# ============================================================ STARTSEITE
swan_uri = "assets/schwan.svg"

start_body = """
<div class="hero wrap">
  <img class="swan" src="assets/schwan.svg" alt="Apollon" width="200" height="200">
  <p class="wordmark">APOLLON</p>
  <div class="rule"></div>
  <p class="slogan">Entwicklung beginnt beim Menschen.</p>
</div>
<div class="divider"></div>

<section><div class="wrap narrow" style="text-align:center">
  <p class="kicker">Wenn eine Entscheidung ansteht</p>
  <h2 style="max-width:22ch;margin:0 auto">Ihre Entscheidung braucht keine Mehrheit.</h2>
  <p class="lead" style="margin-top:1.2rem">Die Menschen, die Ihnen ihre Meinung geben, tragen die Konsequenzen in der Regel nicht. Sie selbst tragen sie.</p>
  <p style="max-width:38rem;margin:0 auto">Und auch nicht zu entscheiden ist eine Entscheidung. Nur trifft sie dann jemand anderes.</p>
  <p style="margin-top:1.6rem"><a class="btn-outline" href="entscheidung.html">Wenn eine Entscheidung ansteht</a></p>
</div></section>

<div class="divider"></div>

<section class="on-white">
  <div class="wrap two">
    <div><p class="kicker">Die Bodenplatte</p><h2>Ihr Unternehmen läuft. Und trotzdem stimmt etwas nicht.</h2></div>
    <div class="body-col">
      <p class="lead">Meistens liegt es nicht an dem, was oben sichtbar ist. Es liegt an dem, was darunter fehlt.</p>
      <p>Bevor man ein Haus baut, zieht man eine Bodenplatte ein. Bei Unternehmen macht das fast niemand. Man gründet, wächst, stellt ein, und irgendwann trägt die Konstruktion das nicht mehr, was auf ihr steht.</p>
      <p>Das liegt selten daran, dass jemand etwas falsch gemacht hätte. Es liegt an dem, was im Alltag liegen geblieben ist. Aufgeschoben, vertagt, im Lärm der nächsten Woche untergegangen.</p>
      <p>Wir schauen uns Ihre Situation an. Und wenn Sie mögen, ziehen wir in drei bis vier Stunden eine Bodenplatte aus Wissen bei Ihnen ein. Danach können Sie in Ruhe entscheiden, ob alles so bleiben soll, wie es ist, oder ob Sie etwas verändern wollen.</p>
      <p style="margin-top:1.6rem"><a class="btn-outline" href="bodenplatte.html">Die Bodenplatte</a></p>
    </div>
  </div>
</section>

<section>
  <div class="wrap"><div class="denkkreis">
    <p class="kicker">Der Denkkreis</p>
    <p class="teaser">Manche Gespräche verändern ein Unternehmen. Andere verändern den Unternehmer.</p>
    <div class="rule"></div>
    <ul class="facts"><li>16. und 17. Oktober 2026</li><li>Lengede</li><li>Zwölf Plätze</li><li>Bewerbung</li></ul>
    <p style="max-width:36rem;margin:0 auto 1.8rem">Kein Seminar. Kein Programm, das wir hier ausbreiten. Zwölf Unternehmer, zwei Tage, ein Haus. Hier wird nicht zugehört und wieder vergessen, hier wird miteinander gearbeitet. Was in diesen zwei Tagen entsteht, ist zu kostbar, um es vorher zu erklären.</p>
    <a class="btn-light" href="denkkreis.html">Bewerben</a>
  </div></div>
</section>

<section class="on-white">
  <div class="wrap">
    <p class="kicker pill">Wissen</p>
    <h2 style="max-width:20ch">Alles, was wir wissen, steht offen da.</h2>
    <p class="lead" style="max-width:40rem;margin-top:1rem">Weil Wissen, das in einem Kopf bleibt, mit diesem Kopf verschwindet.</p>
    <p style="max-width:40rem">Wir erfinden dabei nichts Neues. Wir arbeiten mit Werkzeugen, die es seit Ewigkeiten gibt, und wir wissen, wie man sie richtig benutzt.</p>
    <div class="three" style="margin-top:2.4rem">
      <article class="card"><h3>Der Verein als Werkzeug</h3><p>Gründung, Statuten, Organe, Rechnungen, Gemeinnützigkeit. Erklärt so, wie man es einem Menschen erklärt und nicht einer Behörde.</p><a class="more" href="wissen-verein.html">Zum Vereinswissen</a></article>
      <article class="card"><h3>Die EWIV, verständlich</h3><p>Die Europäische wirtschaftliche Interessenvereinigung. Ein mächtiges Werkzeug, über das kaum jemand verständlich schreibt.</p><a class="more" href="wissen-ewiv.html">Zur EWIV</a></article>
      <article class="card"><h3>Der Körper liest mit</h3><p>Was Druck, Haltung und Füße über einen Menschen erzählen. Die Grundlage der Arbeit in der Konvaleszenz.</p><a class="more" href="wissen-koerper.html">Zum Körperwissen</a></article>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <p class="kicker">Das Vereinsheim</p>
    <h2 style="max-width:24ch">Es gibt Räume, in denen man arbeitet. Und Räume, in denen man denkt.</h2>
    <p class="lead" style="max-width:40rem;margin-top:1rem">Unser Haus in Lengede ist das zweite. Kein Tagungshotel, sondern ein Ort mit einem langen Holztisch und einer Glasfront zum Garten.</p>
    <div style="margin-top:2rem">GALLERY</div>
    <p style="margin-top:1.6rem"><a class="btn-outline" href="vereinsheim.html">Zum Vereinsheim</a> <span style="color:var(--ink-faint);font-size:.9rem;margin-left:.6rem">250 &euro; pro Tag</span></p>
  </div>
</section>

<section class="on-white">
  <div class="wrap two">
    <div>BOOKCOVER</div>
    <div class="body-col">
      <p class="kicker">Das Buch</p>
      <h2>Erste Person</h2>
      <p class="lead" style="margin-top:1rem">Warum wir uns selbst verlassen und wie wir zurückkehren.</p>
      <p>Marion Bernard beobachtet darin, wie Menschen sich den ganzen Tag lang selbst moderieren. Wie sie sich zurechtlegen, anpassen, erklären. Und was passiert, wenn sie damit aufhören.</p>
      <p style="margin-top:1.4rem"><a class="btn-outline" href="buch.html">Zum Buch</a></p>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <p class="kicker">Wege in Bewegung</p>
    <h2 style="max-width:24ch">Der Wirtschaftsverein Apollon hat zurzeit zwei Großprojekte.</h2>
    <div class="two" style="margin-top:2.2rem">
      <article class="card"><h3>Der feminine Ausstieg</h3><p>Für Frauen im Übergang zwischen Abschied und Aufbruch. Souveränität statt Abhängigkeit, in drei Stufen begleitet, von der Entscheidung bis zur Verankerung.</p><p style="margin-top:.8rem;font-style:italic;color:var(--navy);font-family:var(--f-d);font-size:1.2rem">&bdquo;Irgendwann ist kein Datum.&ldquo;</p><a class="more" href="ausstieg.html">Zum femininen Ausstieg</a></article>
      <article class="card"><h3>Konvaleszenz</h3><p>Fußlesung und Mentoring in Wien. Für Menschen, die verstehen wollen, was hinter einem Symptom steckt, statt es zu bekämpfen.</p><p style="margin-top:.8rem;font-style:italic;color:var(--navy);font-family:var(--f-d);font-size:1.2rem">&bdquo;Wer eine schnelle Lösung sucht, ist hier nicht richtig.&ldquo;</p><a class="more" href="konvaleszenz.html">Zur Konvaleszenz</a></article>
    </div>
  </div>
</section>

<section class="on-navy">
  <div class="wrap narrow" style="text-align:center">
    <p class="kicker">Der nächste Schritt</p>
    <h2>Ein Gespräch.</h2>
    <p style="margin-top:1.2rem">Kein Verkaufstermin und kein Vortrag. Sie erzählen, was gerade ansteht, und wir sagen Ihnen ehrlich, wie wir Ihnen dabei helfen können.</p>
    <p style="margin-top:1.6rem"><a class="btn-light" href="gespraech.html">Gespräch vereinbaren</a></p>
    <p style="margin-top:1.4rem;font-size:.86rem;color:#93A6BC">Sagen Sie vorab kurz, worum es geht. Dann gehen wir vorbereitet in das Gespräch.</p>
  </div>
</section>
"""

BOOKCOVER = """<a href="https://www.amazon.de/dp/369635953X" target="_blank" rel="noopener" style="display:block;text-decoration:none;max-width:300px">
<img src="assets/bilder/buchcover.jpg" alt="Buchcover: Erste Person von Marion Bernard" width="300" height="425" style="border-radius:3px;box-shadow:0 18px 40px -22px rgba(2,33,68,.65)">
</a>"""

start_body = start_body.replace("GALLERY", gallery()).replace("BOOKCOVER", BOOKCOVER)
page("index.html", "Apollon | Entwicklung beginnt beim Menschen",
     "Apollon entwickelt Unternehmer. Wissen über Verein, EWIV und tragfähige Strukturen, der Denkkreis und ein Haus, in dem gearbeitet wird.",
     start_body, ORG_SCHEMA, LIGHTBOX)

# ============================================================ ENTSCHEIDUNG
body = head_block("Wenn eine Entscheidung ansteht", "Ihre Entscheidung braucht keine Mehrheit.",
  "Wir holen Menschen in dem Moment ab, in dem etwas Weitreichendes ansteht. Bevor fremde Meinungen, Unsicherheit oder Aufschieben sie von ihrem eigentlichen Vorhaben entfernen.",
  [("index.html","Apollon"), "Wenn eine Entscheidung ansteht"]) + """
<section class="on-white"><div class="wrap">
  <div class="prose">
    <p>Manchmal wissen wir längst, dass sich etwas verändern muss.</p>
    <p>Ein Unternehmen soll anders aufgestellt werden. Vermögen soll erhalten bleiben. Eine Nachfolge steht an. Immobilien sollen sinnvoll strukturiert werden. Verantwortung soll neu verteilt werden. Oder es soll eine Lösung entstehen, die auch für die nächste Generation noch trägt.</p>
    <p>Und dann beginnen wir zu fragen. Familie, Freunde, Geschäftspartner, Berater. Aus einer zunächst klaren Wahrnehmung entstehen unterschiedliche Meinungen, persönliche Erfahrungen und Befürchtungen.</p>
    <p>Diese Perspektiven können hilfreich sein. Entscheidend bleibt jedoch etwas anderes.</p>
    <p class="auftakt">Die Menschen, die Ihnen ihre Meinung geben, tragen die Konsequenzen Ihrer Entscheidung in der Regel nicht. Sie selbst tragen sie.</p>
  </div>
</div></section>

<section><div class="wrap">
  <div class="prose">
    <h2>Wir beginnen deshalb mit einer anderen Frage</h2>
    <p class="auftakt" style="margin-top:1.2rem">Was wollen Sie wirklich erreichen?</p>
    <p>Erst wenn das klar ist, beschäftigen wir uns mit dem Weg dorthin.</p>
  </div>
</div></section>

<section class="on-white"><div class="wrap">
  <div class="prose">
    <h2>Nicht die Struktur steht am Anfang</h2>
    <p style="margin-top:1rem">Ein <a href="wissen-verein.html">Verein</a> kann ein hervorragendes Werkzeug sein. Eine <a href="wissen-ewiv.html">EWIV</a> ebenfalls. Eine GmbH, eine Stiftung oder eine andere Struktur kann in einer anderen Situation die richtige Antwort sein.</p>
    <p class="auftakt">Aber ein Werkzeug ist noch keine Entscheidung.</p>
    <p>Wir betrachten zuerst die Ausgangssituation, das Unternehmen, das Vermögen, Familie und Nachfolge, bestehende Strukturen und die Vorstellung davon, wie Zukunft aussehen soll. Daraus entsteht Orientierung. Erst danach wird entschieden, welcher Weg dazu passt.</p>
  </div>
</div></section>

<section><div class="wrap">
  <div class="prose">
    <h2>Was kostet es, keine Entscheidung zu treffen?</h2>
    <p style="margin-top:1rem">Auch Abwarten hat Konsequenzen. Und es gibt einen Punkt, den man sich klarmachen sollte:</p>
    <p class="auftakt">Nicht zu entscheiden ist ebenfalls eine Entscheidung. Nur trifft sie dann jemand anderes.</p>
    <p>Die Zeit, die Umstände, ein Gericht, eine Behörde, die Erben, der Markt. Wer eine Frage lange genug offen lässt, bekommt irgendwann eine Antwort, die nicht seine eigene ist.</p>
    <p>Unternehmen verändern sich. Menschen werden älter. Familienkonstellationen verändern sich. Vermögen geht irgendwann in die nächste Generation. Rahmenbedingungen und Gestaltungsmöglichkeiten können sich verändern. Eine Entscheidung, die heute möglich ist, kann später unter völlig anderen Voraussetzungen getroffen werden müssen.</p>
    <p class="auftakt" style="margin-top:1.6rem">Sie sollten sich immer darüber im Klaren sein, welche Konsequenzen es hat, wenn Sie etwas tun. Und ebenso, welche es hat, wenn Sie es lassen.</p>
  </div>
</div></section>

<section class="on-white"><div class="wrap">
  <div class="prose">
    <h2>Was wir an dieser Stelle anbieten</h2>
    <p style="margin-top:1rem">Nicht: „Wir gründen Ihnen einen Verein."</p>
    <p>Nicht: „Wir kennen die eine richtige Lösung."</p>
    <p class="auftakt">Sondern Klarheit vor einer weitreichenden Entscheidung.</p>
    <p>Wir wollen niemanden zu einer bestimmten Lösung überreden. Wir führen Informationen, Erfahrungen und Perspektiven so zusammen, dass Sie selbst erkennen können, welche Entscheidung für Sie trägt.</p>
    <p>Aus einem solchen Gespräch kann eine Beratung entstehen, eine Begleitung, eine Vereins- oder EWIV-Struktur oder eine ganz andere Lösung. Der erste Schritt bleibt derselbe: verstehen, was erreicht werden soll.</p>
  </div>
</div></section>

<section><div class="wrap">
  <h2>Die Haltung dahinter</h2>
  <div class="two" style="margin-top:2rem">
    <article class="card"><h3>Orientierung statt fremder Meinung</h3><p>Wer die Folgen trägt, entscheidet. Alle anderen geben Perspektiven, und die sind wertvoll, solange sie nicht die Entscheidung ersetzen.</p></article>
    <article class="card"><h3>Information statt Bevormundung</h3><p>Wir sagen Ihnen, was möglich ist und was es kostet, in beide Richtungen. Was Sie daraus machen, bleibt Ihre Sache.</p></article>
    <article class="card"><h3>Eigenverantwortung statt Abhängigkeit</h3><p>Sie sollen am Ende verstehen, warum Ihre Struktur so aussieht, wie sie aussieht. Nicht uns fragen müssen.</p></article>
    <article class="card"><h3>Entscheidung statt Aufschieben</h3><p>Auch ein bewusstes Nein ist ein Ergebnis. Ein unbewusstes Vielleicht ist keines.</p></article>
  </div>
</div></section>

<section class="on-navy"><div class="wrap narrow" style="text-align:center">
  <p class="kicker">Wenn eine Entscheidung ansteht</p>
  <h2>Meine Situation besprechen.</h2>
  <p style="margin-top:1.2rem">Sie erzählen, was gerade ansteht. Wir hören zu, ordnen ein und sagen Ihnen ehrlich, welche Möglichkeiten Sie haben und was jede davon bedeutet.</p>
  <p style="margin-top:1.6rem"><a class="btn-light" href="gespraech.html">Klarheit für meine Entscheidung gewinnen</a></p>
</div></section>
"""
page("entscheidung.html", "Wenn eine Entscheidung ansteht | Apollon",
     "Vor jeder Rechtsform steht eine Entscheidung. Warum sie keine Mehrheit braucht, was Abwarten kostet und wie aus Orientierung Entscheidungsfähigkeit wird.",
     body)

# ============================================================ BODENPLATTE
body = head_block("Die Bodenplatte", "Erst der Boden. Dann das Haus.",
  "Eine Beratung, nach der Sie auf festem Grund entscheiden können, ob alles so bleiben soll, wie es ist.",
  [("index.html","Apollon"), "Die Bodenplatte"]) + """
<section class="on-white"><div class="wrap">
  <div class="kurz"><strong>Kurz gesagt</strong><p>Die Bodenplatte ist eine Beratung von drei bis vier Stunden, in der Idee, Ziele, Beteiligte und die bestehende unternehmerische Struktur geklärt werden. Danach wissen Sie, welche Form zu Ihrem Vorhaben passt und ob Sie etwas verändern wollen. Ein Verein kann das Ergebnis sein, muss es aber nicht.</p></div>
  <div class="prose">
    <p>Die Bodenplatte ist eine Wissensgrundlage, auf der Sie entscheiden können. Sie beantwortet drei Fragen: Habe ich die richtige Rechtsform? Bin ich sattelfest darin, was ich damit tun kann und was nicht? Und wenn ich etwas verändern will, wie geht das?</p>
    <p>Sie gilt für alles, was schon da ist. Soll die GmbH bleiben? Soll die UG aufgelöst werden? Wie ist die Haftung geregelt, und will ich das so? Am Ende steht entweder die Entscheidung, dass alles bleibt, wie es ist, oder ein klarer Weg zur Veränderung: mehr Erleichterung, eine Positionierung und eine Ausrichtung, die auch in einer Krise trägt.</p>
    <p>Die meisten Unternehmen wachsen schneller, als ihre Struktur mitwächst. Man gründet, weil etwas dringend ist. Man stellt ein, weil die Arbeit da ist. Man verschiebt die Fragen, die keine Frist haben. Und irgendwann sitzt man in einer Konstruktion, die man selbst nicht mehr erklären kann.</p>
    <p>Wir setzen uns davor.</p>
  </div>
</div></section>

<section><div class="wrap">
  <h2 style="max-width:20ch">Wie es abläuft</h2>
  <ol class="steps" style="margin-top:2rem">
    <li>
      <p class="dur">Drei bis vier Stunden</p>
      <h3>Die Beratung: Wir ziehen die Bodenplatte ein</h3>
      <p>Wir erfassen Ihre Idee, Ihre Ziele, die Beteiligten und die bestehende unternehmerische Struktur. Wir klären, welche Form für Ihr Vorhaben sinnvoll ist und wie sie konkret gestaltet werden sollte.</p>
      <p>Sie bekommen Klarheit über Zweck, Projekte, Einnahmemöglichkeiten, Rollen und den Weg der Umsetzung. Danach entscheiden Sie auf einer soliden Grundlage.</p>
    </li>
    <li>
      <h3>Die Errichtung: Sie folgen einem klaren Ablauf</h3>
      <p>Wenn Sie sich für einen Verein entscheiden, schreiben wir die Statuten passend zu Ihrem tatsächlichen Vorhaben. Sie bekommen sie zugeschickt und wir lesen sie gemeinsam in einem eigenen Termin.</p>
      <p>Wir bereiten die Vereinserrichtungsanzeige für Deutschland und Österreich vor und begleiten Sie bis zur Eintragung. Danach bekommen Sie Entwürfe der zentralen Formulare, die Ihr Verein im Alltag braucht.</p>
      <p>Und wir bringen Ihnen bei, wie der Verein Projekte generiert und durchführt.</p>
      <p>Sie erledigen nur die Schritte, die Sie von uns vorbereitet zugespielt bekommen.</p>
    </li>
    <li>
      <h3>Die gelebte Praxis: Aus der Struktur wird ein Unternehmen</h3>
      <p>Sie lernen, wie aus Ideen konkrete Projekte entstehen und wie daraus Einnahmen werden. Sie entwickeln ein Verständnis für Preis, Wert und Rückfluss, damit Ihre Arbeit sich trägt.</p>
      <p>Sie erfahren, wie ein Verein professionell kommuniziert und als ernstzunehmender wirtschaftlicher Akteur sichtbar wird. Und Sie lernen Wege kennen, ihn sinnvoll mit vorhandenen Strukturen zu verbinden.</p>
    </li>
  </ol>
</div></section>

<section class="on-white"><div class="wrap two">
  <div>
    <h2>Ihr Ergebnis</h2>
    <p class="quote" style="margin-top:1.4rem">Eine Struktur, die schützt, ermöglicht und wirtschaftlich trägt.</p>
  </div>
  <div class="body-col">
    <p>Mit klarer Ordnung, praxistauglichen Unterlagen und dem Wissen, sie erfolgreich mit Leben zu füllen.</p>
    <p>Und mit einer Entscheidung, die Sie selbst getroffen haben, nicht eine, die Ihnen jemand verkauft hat.</p>
    <p style="margin-top:1.6rem"><a class="btn-solid" href="gespraech.html">Gespräch vereinbaren</a></p>
  </div>
</div></section>

<section><div class="wrap narrow">
  <h2>Häufige Fragen</h2>
  <div style="margin-top:1.4rem">
  <details class="faq"><summary>Muss am Ende ein Verein stehen?</summary><p>Nein. Der Verein ist eine mögliche Bauform, kein Ziel. Manchmal ist die richtige Antwort, dass alles bleibt, wie es ist, und nur zwei Dinge geordnet werden.</p></details>
  <details class="faq"><summary>Was kostet die Beratung?</summary><p>Das besprechen wir im Gespräch, weil es davon abhängt, was Sie vorhaben. Auf dieser Seite steht bewusst kein Preis, damit die erste Frage nicht der Preis ist, sondern die Sache.</p></details>
  <details class="faq"><summary>Geht das auch für Deutschland?</summary><p>Ja. Wir bereiten die Errichtung für Deutschland und für Österreich vor.</p></details>
  <details class="faq"><summary>Wie schnell geht das?</summary><p>Die Beratung selbst dauert drei bis vier Stunden. Wie lange die Umsetzung dauert, hängt von der Behörde ab und davon, wie schnell Sie die vorbereiteten Schritte erledigen.</p></details>
  </div>
</div></section>
"""
page("bodenplatte.html", "Die Bodenplatte | Apollon",
     "Eine Beratung von drei bis vier Stunden, nach der Sie auf festem Grund entscheiden, ob Ihre Struktur bleibt oder sich verändert.", body)

# ============================================================ DENKKREIS
body = """
<section style="padding-top:clamp(2.4rem,6vw,4rem)"><div class="wrap"><div class="denkkreis">
  <p class="kicker">Der Denkkreis</p>
  <p class="teaser">Manche Gespräche verändern ein Unternehmen. Andere verändern den Unternehmer.</p>
  <div class="rule"></div>
  <ul class="facts"><li>16. und 17. Oktober 2026</li><li>Lengede</li><li>Zwölf Plätze</li><li>Bewerbung</li></ul>
</div></div></section>

<section class="on-white"><div class="wrap narrow">
  <p class="lead">Kein Seminar. Kein Programm, das wir hier ausbreiten.</p>
  <p>Zwölf Unternehmer, zwei Tage, ein Haus. Hier wird nicht zugehört und wieder vergessen. Hier wird miteinander gearbeitet.</p>
  <p>Wir schreiben an dieser Stelle absichtlich nicht, was in diesen zwei Tagen passiert. Nicht aus Koketterie, sondern weil das, was dort entsteht, nicht in einen Ablaufplan passt. Wer alles vorher wissen möchte, um es dann abzuhaken, ist nicht gemeint. Wer neugierig geworden ist, schon.</p>
  <p>Was wir sagen können: Es geht um anders denken und anders handeln. Darum, für die nächste Krise gewappnet zu sein, statt ihr ausgeliefert. Und darum, dass zwölf Menschen, die etwas unternehmen, in zwei Tagen mehr voneinander lernen als in einem Jahr Fachliteratur.</p>
  <p style="margin-top:2rem"><a class="btn-solid" href="#bewerbung">Bewerben</a></p>
</div></section>

<section><div class="wrap narrow" id="bewerbung">
  <p class="kicker">Bewerbung</p>
  <h2>Erzählen Sie uns kurz von sich.</h2>
  <p style="margin-top:1rem;max-width:34rem">Wir lesen jede Bewerbung selbst und melden uns innerhalb weniger Tage. Es gibt zwölf Plätze, deshalb entscheiden wir, wer dazupasst.</p>
  <form class="apo" style="margin-top:2rem" method="post" action="formular.php">
    <input type="hidden" name="formular" value="Denkkreis, Bewerbung">
    <div style="position:absolute;left:-9999px" aria-hidden="true"><label for="hp1">Bitte leer lassen</label><input id="hp1" type="text" name="webseite" tabindex="-1" autocomplete="off"></div>
    <div><label for="n">Name</label><input id="n" name="name" type="text" required></div>
    <div><label for="e">E-Mail</label><input id="e" name="email" type="email" required></div>
    <div><label for="t">Telefon</label><input id="t" name="telefon" type="tel"></div>
    <div><label for="u">Ihr Unternehmen, in einem Satz</label><input id="u" name="unternehmen" type="text" required></div>
    <div><label for="w">Woran arbeiten Sie gerade, das Sie nicht loslässt?</label><textarea id="w" name="thema" required></textarea>
      <p class="hint">Zwei, drei Sätze genügen. Ehrlich ist wichtiger als vollständig.</p></div>
    <div class="check"><input id="mensch" name="mensch" type="checkbox" required><label for="mensch">Ich bin ein Mensch.</label></div>
    <div><button class="btn-solid" type="submit">Bewerbung senden</button></div>
    <p class="hint">Ihre Angaben werden ausschließlich zur Bearbeitung dieser Bewerbung verwendet. Siehe <a href="datenschutz.html">Datenschutz</a>.</p>
  </form>
  <p class="hint" style="margin-top:1.6rem">Den genauen Ort, die Uhrzeiten und alles Weitere erfahren Sie, sobald Sie dabei sind.</p>
</div></section>

<section class="on-navy"><div class="wrap narrow" style="text-align:center">
  <p class="kicker">Bleiben Sie in der Nähe</p>
  <h2>Apollon Denkkreise</h2>
  <p style="margin-top:1rem">Im Telegram-Kanal erscheinen die Einladungen zu den kommenden Denkkreisen. Sonst nichts.</p>
  <p style="margin-top:1.6rem"><a class="btn-light" href="https://t.me/apollondenkkreise" target="_blank" rel="noopener">Zum Kanal</a></p>
</div></section>
"""
EVENT = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"Event","name":"Apollon Denkkreis","startDate":"2026-10-16","endDate":"2026-10-17",
"eventAttendanceMode":"https://schema.org/OfflineEventAttendanceMode","eventStatus":"https://schema.org/EventScheduled",
"location":{"@type":"Place","name":"Vereinsheim Apollon","address":{"@type":"PostalAddress","addressLocality":"Lengede","addressCountry":"DE"}},
"maximumAttendeeCapacity":12,
"description":"Zwölf Unternehmer, zwei Tage, ein Haus. Anders denken und anders handeln.",
"organizer":{"@type":"Organization","name":"Apollon"}}
</script>"""
page("denkkreis.html", "Der Denkkreis | Apollon",
     "16. und 17. Oktober 2026 in Lengede. Zwölf Unternehmer, zwei Tage, ein Haus. Bewerbung statt Buchung.", body, EVENT)

# ============================================================ VEREINSHEIM
body = head_block("Das Vereinsheim", "Es gibt Räume, in denen man arbeitet. Und Räume, in denen man denkt.",
  "Unser Haus in Lengede ist das zweite. Seit Kurzem auch von außen buchbar.",
  [("index.html","Apollon"), "Vereinsheim"]) + """
<section class="on-white"><div class="wrap">
  <div class="kurz"><strong>Kurz gesagt</strong><p>Das Vereinsheim Apollon in Lengede ist ein Haus für kleine Gruppen, die konzentriert arbeiten wollen. Seminarraum mit langem Holztisch und Flipchart, Wohnbereich mit Glasfront zum Garten, Küche und Bad. Der Tagessatz beträgt 250 Euro. Buchbar auch für Externe.</p></div>
  """ + gallery() + """
</div></section>

<section><div class="wrap two">
  <div>
    <h2>Kein Tagungshotel</h2>
    <p class="quote" style="margin-top:1.4rem">Wer eine Pause braucht, geht zwei Schritte und steht draußen.</p>
  </div>
  <div class="body-col">
    <p>Der Seminarraum hat einen massiven Holztisch, Tageslicht von zwei Seiten und ein Flipchart. Nebenan der Wohnbereich mit einer großen Glasfront zum Garten, offen zur Terrasse.</p>
    <p>Genau das macht den Unterschied zwischen einem Tag, der zäh wird, und einem, der trägt. Kein grauer Teppich, kein Neonlicht, keine Kaffeekanne auf einem Rollwagen.</p>
    <p>Dazu eine Küche, ein modernes Bad, Parkplätze direkt am Haus und WLAN.</p>
  </div>
</div></section>

<section class="on-white"><div class="wrap">
  <h2 style="max-width:22ch">Wofür das Haus gemacht ist</h2>
  <div class="three" style="margin-top:2rem">
    <article class="card"><h3>Konzentriert arbeiten</h3><p>Strategietage, Klausuren, Workshops, Team-Retreats. Alles, wofür der Besprechungsraum im Büro zu eng ist.</p></article>
    <article class="card"><h3>Begleiten und lernen</h3><p>Coachings, Schulungen, Aufstellungsarbeit, kleine Seminare. Räume, die nicht nach Prüfungssaal aussehen.</p></article>
    <article class="card"><h3>Vorträge im kleinen Kreis</h3><p>Abende, an denen jemand etwas erzählt und danach noch geblieben wird.</p></article>
  </div>
</div></section>

<section><div class="wrap narrow">
  <h2>Konditionen</h2>
  <ul class="facts dark" style="justify-content:flex-start;margin-top:1.4rem">
    <li>250 &euro; pro Tag</li><li>2 bis 8 Personen</li><li>Lengede</li><li>Parkplätze am Haus</li><li>WLAN</li>
  </ul>
  <p style="margin-top:1.6rem">Die Küche ist vollständig eingerichtet, es kann also selbst gekocht werden. Übernachtet wird im Haus nicht, es ist ein Ort für den Tag.</p>
  <p style="margin-top:1rem">Schreiben Sie uns kurz, worum es geht und für wie viele Menschen. Dann sagen wir Ihnen, ob das Haus dafür passt.</p>
  <p style="margin-top:1.4rem"><a class="btn-solid" href="vereinsheim-anfrage.html">Location anfragen</a></p>
</div></section>
"""
PLACE = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"EventVenue","name":"Vereinsheim Apollon",
"address":{"@type":"PostalAddress","addressLocality":"Lengede","addressCountry":"DE"},
"description":"Seminarhaus für kleine Gruppen mit Seminarraum, Wohnbereich, Küche und Garten."}
</script>"""
page("vereinsheim.html", "Das Vereinsheim | Apollon",
     "Seminarhaus in Lengede für kleine Gruppen. Holztisch, Flipchart, Garten. 250 Euro pro Tag, auch für Externe buchbar.", body, PLACE, LIGHTBOX)

# ============================================================ ANFRAGE VEREINSHEIM
body = head_block("Das Vereinsheim", "Das Haus anfragen.",
  "Sagen Sie uns, wer Sie sind und was Sie vorhaben. Dann sagen wir Ihnen, ob das Haus dafür passt und ob es frei ist.",
  [("index.html","Apollon"), ("vereinsheim.html","Vereinsheim"), "Anfrage"]) + """
<section class="on-white"><div class="wrap narrow">
  <form class="apo" method="post" action="formular.php" style="margin-top:1rem">
    <input type="hidden" name="formular" value="Vereinsheim, Anfrage">
    <div style="position:absolute;left:-9999px" aria-hidden="true"><label for="hp3">Bitte leer lassen</label><input id="hp3" type="text" name="webseite" tabindex="-1" autocomplete="off"></div>
    <fieldset><legend>Wer fragt an</legend>
      <div><label for="fa">Firma oder Organisation</label><input id="fa" name="firma" type="text" required></div>
      <div style="margin-top:1rem"><label for="an">Ansprechpartner</label><input id="an" name="ansprechpartner" type="text" required></div>
      <div style="margin-top:1rem"><label for="ae">E-Mail</label><input id="ae" name="email" type="email" required></div>
      <div style="margin-top:1rem"><label for="at">Telefon</label><input id="at" name="telefon" type="tel"><p class="hint">Freiwillig. Für Rückfragen zum Termin oft der schnellere Weg.</p></div>
      <div style="margin-top:1rem"><label for="aw">Webadresse</label><input id="aw" name="web" type="text" placeholder="beispiel.at"><p class="hint">Freiwillig. Hilft uns einzuschätzen, worum es geht.</p></div>
    </fieldset>
    <fieldset><legend>Das Vorhaben</legend>
      <div><label for="av">Was haben Sie vor?</label><textarea id="av" name="vorhaben" required></textarea>
        <p class="hint">Seminar, Klausur, Workshop, Retreat, Dreh. Zwei, drei Sätze genügen.</p></div>
      <div style="margin-top:1rem"><label for="ap">Wie viele Menschen?</label><input id="ap" name="personen" type="text" required></div>
      <div style="margin-top:1rem"><label for="ad">Wann, und für wie lange?</label><input id="ad" name="zeitraum" type="text" required><p class="hint">Auch ein grober Zeitraum reicht für den Anfang.</p></div>
      <div style="margin-top:1rem"><label for="ab">Sonstiges, das wir wissen sollten</label><textarea id="ab" name="sonstiges" style="min-height:5.5rem"></textarea>
        <p class="hint">Freiwillig. Etwa Übernachtung, Verpflegung, besondere Technik.</p></div>
    </fieldset>
    <div class="check"><input id="mensch3" name="mensch" type="checkbox" required><label for="mensch3">Ich bin ein Mensch.</label></div>
    <div><button class="btn-solid" type="submit">Anfrage senden</button></div>
    <p class="hint">Ihre Angaben werden ausschließlich zur Bearbeitung Ihrer Anfrage verwendet und nicht weitergegeben. Siehe <a href="datenschutz.html">Datenschutz</a>.</p>
  </form>
  <p style="margin-top:2rem"><a class="zurueck" href="vereinsheim.html">Zurück zum Vereinsheim</a></p>
</div></section>
"""
page("vereinsheim-anfrage.html", "Das Vereinsheim anfragen | Apollon",
     "Anfrage für das Vereinsheim Apollon in Lengede: Firma, Ansprechpartner, Vorhaben, Zeitraum und Gruppengröße.", body)

# ============================================================ BUCH
body = head_block("Das Buch", "Erste Person",
  "Warum wir uns selbst verlassen und wie wir zurückkehren.",
  [("index.html","Apollon"), "Buch"]) + """
<section class="on-white"><div class="wrap two">
  <div>""" + BOOKCOVER + """</div>
  <div class="body-col">
    <div class="kurz"><strong>Kurz gesagt</strong><p>&bdquo;Erste Person&ldquo; von Marion Bernard ist 2026 bei Books on Demand erschienen, hat 126 Seiten und trägt die ISBN 978-3-696-35953-9. Das Buch handelt davon, wie Menschen sich den ganzen Tag lang selbst moderieren, und was geschieht, wenn sie damit aufhören.</p></div>
    <p>&bdquo;Irgendwann beginnt der Moment, in dem du spürst, dass du dich selbst zu lange mit einem Bild verglichen hast, das nie wirklich deines war. Dieses Buch ist eine Einladung, damit aufzuhören.&ldquo;</p>
    <p>Zurück zur eigenen Wahrnehmung. Zurück zu Entscheidungen, die sich nicht nach Druck anfühlen, sondern nach Wahrheit. Die eigene Geschichte hat einen Menschen geprägt, aber sie legt ihn nicht fest.</p>
    <p>Manche verstehen erst nach diesem Buch, worum es hier eigentlich geht.</p>
    <p style="font-size:.9rem;color:var(--ink-faint);margin-top:1.4rem">126 Seiten, Books on Demand, 11. Mai 2026. ISBN 978-3-696-35953-9. Überall erhältlich, wo es Bücher gibt.</p>
    <p style="margin-top:1.4rem"><a class="btn-solid" href="https://www.amazon.de/dp/369635953X" target="_blank" rel="noopener">Zum Buch bei Amazon</a></p>
  </div>
</div></section>

<section><div class="wrap narrow">
  <h2>Über die Autorin</h2>
  <p style="margin-top:1.2rem">Marion Bernard steht für ein Leben in Selbstbestimmung und innerer Klarheit. Sie beschäftigt sich damit, wie Menschen sich aus innerem Druck, Erwartungen und Anpassung lösen und wieder in Verbindung mit ihrer eigenen Wahrheit kommen.</p>
  <p>Ihre Arbeit ist geprägt von der Überzeugung, dass jeder Mensch die Fähigkeit in sich trägt, stimmige Entscheidungen zu treffen und den eigenen Weg bewusst zu gestalten. Dieselbe Haltung liegt der Arbeit von Apollon zugrunde.</p>
</div></section>
"""
BOOK = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"Book","name":"Erste Person",
"alternativeHeadline":"Warum wir uns selbst verlassen und wie wir zurückkehren",
"author":{"@type":"Person","name":"Marion Bernard"},"isbn":"9783696359539",
"numberOfPages":126,"datePublished":"2026-05-11","publisher":{"@type":"Organization","name":"Books on Demand"},
"inLanguage":"de"}
</script>"""
page("buch.html", "Erste Person, das Buch von Marion Bernard | Apollon",
     "Erste Person. Warum wir uns selbst verlassen und wie wir zurückkehren. Das Buch von Marion Bernard, 126 Seiten, ISBN 978-3-696-35953-9.", body, BOOK)

print("Teil 1 gebaut.")
