#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Die beiden Bereiche unter „Wege in Bewegung“.

Der feminine Ausstieg und Konvaleszenz. Die Texte stammen von den
bisherigen Seiten femininer-ausstieg.at und konvaleszenz.com und sind
unveraendert uebernommen. Preise stehen hier nicht, die gehoeren ins
Gespraech.
"""
from build import *
import json

def bildzeile(bild, alt, inhalt, seite="rechts", ton="on-white"):
    """Ein Bild neben einem Textblock. Auf dem Handy steht das Bild oben."""
    figur = ('<figure class="bz-bild"><img src="assets/bilder/%s" alt="%s" '
             'decoding="async"></figure>') % (bild, alt)
    text = '<div class="bz-text">%s</div>' % inhalt
    reihe = (figur + text) if seite == "links" else (text + figur)
    klasse = "bildzeile" + (" gedreht" if seite == "links" else "")
    return ('<section class="%s"><div class="wrap"><div class="%s">%s</div></div></section>'
            % (ton, klasse, reihe))


# ==================================================================== Ausstieg

BEWERBUNGSFRAGEN = [
    "Wo stehst du gerade, und warum bewirbst du dich genau jetzt?",
    "Welche Entscheidung schiebst du seit Längerem vor dir her?",
    "Was kostet dich dieses Nicht-Handeln heute?",
    "Woran hältst du fest, obwohl du längst weißt, dass es nicht mehr zu dir gehört?",
    "Was würde sich in deinem Leben verändern, wenn du jetzt losgehst?",
    "Bist du bereit, Verantwortung für diesen Schritt zu übernehmen, persönlich, zeitlich und finanziell?",
]

STUFEN = [
    ("Ich entscheide mich", "etwa vier Wochen",
     "Klarheit gewinnen. Wahrheit erkennen. Entscheidung treffen."),
    ("Ich gehe los", "etwa drei Monate",
     "Die ersten Schritte gehen. Vertrauen aufbauen. Das neue Kapitel beginnen."),
    ("Ich lebe mein Leben", "etwa sechs Monate",
     "Das neue Leben konsequent gestalten und dauerhaft verankern."),
]


def ausstieg():
    body = head_block(
        "Wege in Bewegung",
        "Der feminine Ausstieg",
        "Irgendwann ist kein Datum. Wann bist du endlich dran, dein eigenes Leben zu leben?",
        [("index.html", "Apollon"), "Der feminine Ausstieg"])

    body += ('<figure class="breitbild"><img src="assets/bilder/fa-naturweg.webp" '
             'alt="Ein Weg, der durch die Natur führt" loading="eager" decoding="async">'
             '</figure>')

    body += """
<section class="on-white"><div class="wrap narrow gruen">
  <p class="gross">Das Leben wartet nicht auf den perfekten Zeitpunkt. Es wartet auf deine Entscheidung.</p>
  <p style="margin-top:1.6rem"><a class="btn-solid" href="ausstieg-bewerbung.html">Jetzt bewerben</a></p>
</div></section>

<section><div class="wrap narrow">
  <h2>Du musst nicht den ganzen Weg kennen.</h2>
  <p style="margin-top:1rem">Du musst nur den Mut haben, den ersten Schritt zu gehen.</p>
  <p class="zitat" style="margin-top:1.8rem">Du stehst zwischen Abschied und Aufbruch.<br>
  Nicht alles muss heute entschieden werden.<br>
  Aber eines schon:<br>
  Gehst du weiter, oder bleibst du stehen?</p>
</div></section>

"""

    body += bildzeile("fa-marion.webp", "Marion Bernard",
        '<p class="kicker">Marion Bernard</p>'
        '<h2>Ich habe den Weg auch nicht immer gesehen.</h2>'
        '<p style="margin-top:1.2rem">Mit 24 bin ich allein nach Afrika gegangen.<br>'
        'Heute beginne ich mit 60 noch einmal neu.<br>'
        'Nicht, weil ich musste.<br>'
        'Sondern weil ich meinem Leben vertraue.</p>'
        '<p class="gross" style="margin-top:1.6rem">Ich rede nicht über Aufbruch.<br>'
        'Ich lebe ihn.</p>',
        seite="links", ton="on-white")

    body += bildzeile("fa-lavendelfeld.webp", "Ein Lavendelfeld im Licht",
        '<h2>Ein neues Leben beginnt nicht irgendwann.</h2>'
        '<p style="margin-top:1.2rem">Es beginnt mit einer Entscheidung.<br>'
        'Nicht weil alle Fragen beantwortet sind.<br>'
        'Nicht weil die Angst verschwunden ist.<br>'
        'Sondern weil du dir selbst endlich wichtiger wirst.</p>',
        seite="rechts", ton="")

    # Die drei Stufen, ohne Preise
    karten = ""
    for i, (name, dauer, text) in enumerate(STUFEN, 1):
        karten += ('<article class="stufe"><p class="nr">%d</p><h3>%s</h3>'
                   '<p class="dauer">%s</p><p>%s</p>'
                   '<p style="margin-top:1.2rem"><a class="mehr" href="ausstieg-bewerbung.html">'
                   'Ich bin bereit</a></p></article>') % (i, name, dauer, text)

    body += ('<section class="on-white"><div class="wrap">'
             '<p class="kicker">Wo stehst du heute?</p>'
             '<h2>Drei Wege, je nachdem, wie weit du schon bist.</h2>'
             '<div class="stufen">' + karten + '</div>'
             '<p class="leise" style="margin-top:1.6rem;max-width:38rem">Was ein Weg umfasst und '
             'was er kostet, besprechen wir persönlich. Das hängt davon ab, wo du stehst, und '
             'lässt sich nicht auf einer Seite beantworten.</p>'
             '</div></section>')

    body += ('<section class="on-white"><div class="wrap narrow prose eigen gruen">'
             '<!--eigen:ausstieg-frei--><!--/eigen:ausstieg-frei-->'
             '</div></section>')

    body += """
<section><div class="wrap narrow">
  <p class="kicker">Noch nicht sicher?</p>
  <h2>Beginne mit meinem Buch.</h2>
  <p style="margin-top:1.2rem">Wenn eine Bewerbung dir gerade zu groß ist, ist das Buch der leisere
  erste Schritt. Dieselbe Haltung, in deinem eigenen Tempo.</p>
  <p style="margin-top:1.4rem"><a class="btn-outline" href="buch.html">Zum Buch</a>
  <a class="btn-outline" href="ausstieg-impulsbuch.html" style="margin-left:.6rem">Zum Impulsbuch</a></p>
</div></section>

<section class="on-navy"><div class="wrap narrow" style="text-align:center">
  <p class="gross">Du hast nur dieses eine Leben.<br>Lebe es.</p>
  <p style="margin-top:1.6rem"><a class="btn-light" href="ausstieg-bewerbung.html">Ich bin bereit</a></p>
  <p class="leise" style="margin-top:1.6rem;color:rgba(255,255,255,.7)">Ich arbeite nur mit Frauen,
  bei denen ich spüre: Jetzt ist ihre Zeit.</p>
</div></section>
"""

    page("ausstieg.html", "Der feminine Ausstieg | Apollon",
         "Souveränität statt Abhängigkeit. Begleitung von Marion Bernard für Frauen, die den "
         "Schritt in ihr eigenes Leben gehen.", body)


def ausstieg_bewerbung():
    body = head_block(
        "Der feminine Ausstieg",
        "Deine Entscheidung beginnt jetzt.",
        "Bevor wir miteinander sprechen, nimm dir bitte etwa zehn Minuten Zeit und beantworte die "
        "folgenden Fragen ehrlich. Es gibt keine richtigen oder falschen Antworten. Sie helfen mir "
        "zu erkennen, ob ich die richtige Begleiterin für deinen Weg bin.",
        [("index.html", "Apollon"), ("ausstieg.html", "Der feminine Ausstieg"), "Bewerbung"])

    felder = ""
    for i, frage in enumerate(BEWERBUNGSFRAGEN, 1):
        felder += ('<div class="frage"><label for="f%d"><span class="zahl">%d</span>%s</label>'
                   '<textarea id="f%d" name="frage%d" rows="4" required></textarea></div>'
                   % (i, i, frage, i, i))

    body += ('<section class="on-white"><div class="wrap narrow">'
             '<form class="apo gruen" method="post" action="formular.php">'
             '<input type="hidden" name="formular" value="Bewerbung, Der feminine Ausstieg">'
             '<p class="netz" aria-hidden="true"><label>Bitte freilassen'
             '<input type="text" name="webseite" tabindex="-1" autocomplete="off"></label></p>'
             + felder +
             '<h2 style="margin-top:2.4rem">Fast geschafft, wie erreiche ich dich?</h2>'
             '<div class="zwei">'
             '<div><label for="vn">Vorname</label>'
             '<input id="vn" name="name" type="text" required></div>'
             '<div><label for="em">E-Mail</label>'
             '<input id="em" name="email" type="email" required></div>'
             '</div>'
             '<div><label for="tel">Telefon</label>'
             '<input id="tel" name="telefon" type="tel"></div>'
             '<div class="check" style="margin-top:1.2rem">'
             '<input id="dsg" name="datenschutz" type="checkbox" required>'
             '<label for="dsg">Ich habe die <a href="datenschutz.html">Datenschutzerklärung</a> '
             'gelesen und stimme der Verarbeitung meiner Daten zur Bearbeitung meiner Bewerbung zu.</label>'
             '</div>'
             '<div class="check" style="margin-top:.8rem">'
             '<input id="mn" name="mensch" type="checkbox" required>'
             '<label for="mn">Ich bin ein Mensch.</label></div>'
             '<div style="margin-top:1.6rem"><button class="btn-solid" type="submit">'
             'Bewerbung absenden</button></div>'
             '<p class="leise" style="margin-top:1rem">Wenn es passt, melde ich mich für ein '
             'persönliches Telefonat bei dir.</p>'
             '</form></div></section>')

    page("ausstieg-bewerbung.html", "Bewerbung, Der feminine Ausstieg | Apollon",
         "Sechs Fragen vor dem ersten Gespräch. Bewirb dich für die Begleitung im femininen Ausstieg.",
         body)


def ausstieg_impulsbuch():
    # Der Wortlaut stammt von femininer-ausstieg.at und ist von Marion.
    # Er wird nicht umgeschrieben, nur gesetzt.
    body = head_block(
        "Der feminine Ausstieg",
        "Ein Brief für dich.",
        "Vielleicht ist irgendwann tatsächlich kein Datum.",
        [("index.html", "Apollon"), ("ausstieg.html", "Der feminine Ausstieg"), "Impulsbuch"])

    body += ('<section class="on-white"><div class="wrap narrow">'
             '<p class="lead">Vielleicht beginnt dein neues Kapitel genau heute.<br>'
             'Ich habe einen kleinen Brief für dich geschrieben.<br>'
             'Er erinnert dich an das, was längst in dir angelegt ist.<br>'
             'Wenn du magst, schicke ich ihn dir.<br>'
             'Von Herzen.</p>'
             '<form class="apo gruen" method="post" action="formular.php" style="margin-top:2rem">'
             '<input type="hidden" name="formular" value="Impulsbuch, Der feminine Ausstieg">'
             '<p class="netz" aria-hidden="true"><label>Bitte freilassen'
             '<input type="text" name="webseite" tabindex="-1" autocomplete="off"></label></p>'
             '<div class="zwei">'
             '<div><label for="ivn">Vorname</label><input id="ivn" name="name" type="text" required></div>'
             '<div><label for="iem">E-Mail</label><input id="iem" name="email" type="email" required></div>'
             '</div>'
             '<div class="check" style="margin-top:1.2rem">'
             '<input id="idsg" name="datenschutz" type="checkbox" required>'
             '<label for="idsg">Ich möchte das Impulsbuch erhalten und bin einverstanden, dass '
             'mir Marion Bernard per E-Mail weitere Impulse sendet. Die '
             '<a href="datenschutz.html">Datenschutzerklärung</a> habe ich gelesen. Ich kann mich '
             'jederzeit wieder abmelden.</label></div>'
             '<div class="check" style="margin-top:.8rem">'
             '<input id="imn" name="mensch" type="checkbox" required>'
             '<label for="imn">Ich bin ein Mensch.</label></div>'
             '<div style="margin-top:1.6rem"><button class="btn-solid" type="submit">'
             'Impulsbuch kostenlos lesen</button></div>'
             '<p class="leise" style="margin-top:1rem">Ich schicke dir den Brief persönlich an '
             'diese Adresse. Du kannst dich jederzeit wieder abmelden.</p>'
             '</form></div></section>')

    body += ('<section><div class="wrap narrow" style="text-align:center">'
             '<p>Lieber der ganze Weg? <a class="mehr" href="ausstieg-bewerbung.html">'
             'Zur Bewerbung</a></p></div></section>')



    page("ausstieg-impulsbuch.html", "Impulsbuch, Der feminine Ausstieg | Apollon",
         "Das kostenlose Impulsbuch von Marion Bernard. Der leisere erste Schritt.", body)


# ================================================================ Konvaleszenz

STIMMEN = [
    ("Miriam", "Lehrerin", "kv-miriam.webp",
     "Mit den liebevollen Empfehlungen durch die Fußlesung konnte ich meine Lebensenergie "
     "zurückgewinnen."),
    ("André", "Videocreator", "kv-andre.webp",
     "Der Verein inspiriert Menschen mit Hilfe des Werkzeugs „Füße lesen“ ins Handeln zu kommen."),
    ("Christian", "Fotograf", "kv-christian.webp",
     "Auf der stetigen Suche nach der Selbstoptimierung und Ursachenforschung hat mich die "
     "Erkenntnis durch das Lesen weitergebracht mit der mir bis dato unbekannten Technik "
     "„Füße lesen“."),
    # Wortlaut von konvaleszenz.com, ungekuerzt.
    ("Stefan", "Pilot", "kv-stefan.webp",
     "Mir wurde geholfen, meine Leidenschaft zur Berufung zu machen. Meine Leidenschaft ist die "
     "Fliegerei. Seit meinem sechzehnten Lebensjahr sitze ich hinter dem Steuerknüppel. Damals "
     "begann ich meine Flugausbildung im Segelflugzeug. Erst mit 18 begann ich, Motorflugzeuge "
     "zu fliegen. Aus gesundheitlichen Gründen musste ich meine Pläne, eine Karriere als "
     "Berufspilot, aufgeben. Da brach eine Welt in mir zusammen, denn mein Traum ließ sich nicht "
     "mehr realisieren. So geriet der Wunsch, die Fliegerei beruflich zunutze zu machen, in den "
     "Hintergrund. Marion Bernard begutachtete meine Fußsohlen. Dabei kam heraus, dass ich "
     "beruflich einen völlig falschen Weg eingeschlagen habe. In vielen Gesprächen wuchs eine "
     "neue Idee! Es geht darum, Menschen die Flugangst zu nehmen. Wir haben ein erfolgreiches "
     "Konzept entwickelt. Marion Bernard berät mich bis heute. Ihre Erfahrung, ihr Humor, ihre "
     "Geradlinigkeit und Bestimmtheit haben mir meine Trägheit ausgetrieben. Ich kann Marion "
     "Bernard nur weiterempfehlen. Ihre Empathie und Vertrautheit schaffen eine Atmosphäre, sich "
     "zu öffnen, um eine Persönlichkeitsweiterempfehlung zu fördern."),
]


def konvaleszenz():
    body = head_block(
        "Wege in Bewegung",
        "Konvaleszenz",
        "Wenn dein Körper dich hierher gerufen hat, bist du richtig.",
        [("index.html", "Apollon"), "Konvaleszenz"])

    body += ('<figure class="breitvideo">'
             '<video autoplay muted loop playsinline poster="assets/bilder/kv-steine.webp" '
             'aria-label="Ein Steinstapel am Meer, umspült von Wellen">'
             '<source src="assets/video/kv-steine.webm" type="video/webm">'
             '<source src="assets/video/kv-steine.mp4" type="video/mp4">'
             '</video></figure>')

    body += """
<section class="on-white"><div class="wrap narrow warm">
  <p class="zitat">„Behandle die Ursache, nicht die Wirkung.“<br>
  <span class="leise">Dr. Edward Bach</span></p>
  <p style="margin-top:1.8rem">Konvaleszenz schaut auf die Ursachen von Schmerzen, Problemen und
  dem, was sich in deinem Leben festgefahren anfühlt oder fehlt.</p>
  <p>Unser Werkzeug ist der Blick auf deine Füße. Nicht als Methode, sondern als Zugang.</p>
  <p>Deine Fußsohlen zeigen, wie dein Körper Belastungen verarbeitet, wo Spannung entsteht und wie
  dein ganz persönlicher Zustand aussieht. So individuell, wie du es bist.</p>
  <p class="gross" style="margin-top:1.6rem">Deine Füße lügen nicht.<br>
  Sie zeigen deinen körperlichen, geistigen, seelischen Zustand, nicht ein Modell.</p>
</div></section>

"""

    body += bildzeile("kv-meer.webp", "Das Meer, weit und ruhig",
        '<h2>Die Fußlesung</h2>'
        '<p style="margin-top:1rem">Die Fußlesung ist ein erster klarer Blick auf deinen aktuellen '
        'Zustand. Sie macht sichtbar, wo Druck entstanden ist, was dich innerlich blockiert und '
        'warum dein Körper genau so reagiert.</p>'
        '<p>Ohne Bewertung. Ohne Einordnung in richtig oder falsch. Sondern so, wie es sich bei dir '
        'zeigt. Nicht allgemein, nicht vergleichend, sondern bezogen auf dich.</p>'
        '<p>Du erlebst hier zum ersten Mal Klarheit statt Vermutungen. Die Fußlesung ist kein '
        'Versprechen auf Lösung. Sie ist eine Einladung zur Wahrheit, deiner Wahrheit, und damit '
        'der Anfang von Veränderung. Nicht, weil etwas kaputt ist, sondern weil es zu lange '
        'getragen, verdrängt oder aus falschen Entscheidungen heraus zurückgestellt wurde.</p>'
        '<p style="margin-top:1.4rem">Es richtet sich an Menschen, die bereit sind, Verantwortung '
        'für sich zu übernehmen und ihren Zustand nicht delegieren, sondern verstehen wollen. Wer '
        'eine schnelle Lösung sucht, ist hier nicht richtig. Wer Klarheit sucht, findet hier einen '
        'Anfang.</p>'
        '<p style="margin-top:1.6rem"><a class="btn-solid" href="gespraech.html">Nimm Kontakt auf</a></p>',
        seite="links", ton="")

    body += bildzeile("kv-steine.webp", "Aufeinandergeschichtete Steine, die im Gleichgewicht stehen",
        '<h2>Und wenn klar wird, dass es tiefer geht</h2>'
        '<p style="margin-top:1rem">Manchmal zeigt sich, dass es nicht um ein einzelnes Thema geht, '
        'sondern um ein ganzes Gefüge aus Verantwortung, Druck und Erwartungen. Dann beginnt das '
        'Mentoring.</p>'
        '<p>Keine Therapie. Kein Programm. Sondern eine Begleitung, die Ordnung zurückbringt, im '
        'Denken, im Körper und im Leben. Nicht schneller. Sondern tragfähiger.</p>',
        seite="rechts", ton="on-white")

    # Der Hinweis, wortgleich von der bisherigen Seite
    body += ('<section><div class="wrap narrow"><div class="wichtig">'
             '<p class="kicker">Wichtig</p>'
             '<p>Konvaleszenz ersetzt keine medizinische oder therapeutische Behandlung und gibt '
             'keine Heilversprechen.</p>'
             '<p>Konvaleszenz ist ein Raum für Menschen, die verstehen wollen, warum ihr Körper '
             'reagiert, statt ihn weiter zu bekämpfen.</p>'
             '<!--eigen:konvaleszenz-grundlage--><!--/eigen:konvaleszenz-grundlage-->'
             '<p>Ich stelle keine Diagnosen. Ich ordne ein. Damit du in deinem Tempo, in eigener '
             'Verantwortung, klarere Entscheidungen treffen kannst.</p>'
             '</div></div></section>')

    body += ('<section><div class="wrap">'
             '<p class="kicker">Deine Vorteile</p>'
             '<div class="vorteile">'
             '<article><h3>Zufriedenheit</h3><p>Verborgene Interessen und Fähigkeiten aufdecken.</p></article>'
             '<article><h3>Gesundheit</h3><p>Gezielt können Ernährungsumstellungen ausgesprochen werden.</p></article>'
             '<article><h3>Lebensziele</h3><p>Neue Ausrichtung durch Leben deines Seelenplans.</p></article>'
             '</div></div></section>')

    body += ('<section class="on-white"><div class="wrap narrow">'
             '<h2>Wachse an und mit deiner Vision, werde die beste Ausführung von dir selbst</h2>'
             '<p style="margin-top:1.2rem">Selbstheilung geschieht durch Konfliktlösung. Keine '
             'sogenannte Krankheit kommt von außen. Beginne mit der Innenschau und wachse in deine '
             'eigenen Schuhe. Gehe den ersten Schritt und nimm Kontakt auf, wir helfen dir, zu '
             'transformieren, zu dem Menschen, der du sein sollst.</p>'
             '<p class="themen">'
             '<span>Beziehungen</span><span>Führung</span><span>Krankheit</span>'
             '<span>Einsamkeit</span><span>Gesundheit</span></p>'
             '<p style="margin-top:1.6rem">Wenn du bereit bist, dich für dich zu öffnen und in die '
             'Erfüllung all deiner Träume zu gelangen, dann bist du hier richtig.</p>'
             '</div></section>')

    body += ('<figure class="breitbild"><img src="assets/bilder/kv-hinweis.webp" '
             'alt="Ein gedeckter Tisch an einem See vor Bergen" decoding="async"></figure>')

    body += ('<section class="on-white"><div class="wrap narrow">'
             '<p class="kicker">Projektleitung von Konvaleszenz</p>'
             '<h2>Warum ich tue, was ich tue</h2>'
             '<p style="margin-top:1.2rem">Ich arbeite mit dir, weil ich weiß, wie leicht man sich '
             'selbst verliert, während man funktioniert, trägt, durchhält.</p>'
             '<p>Vielleicht kennst du das: Du machst alles richtig, und trotzdem fühlt sich etwas '
             'nicht stimmig an.</p>'
             '<p>Mich treibt die Erfahrung, dass dein Körper oft früher weiß, was aus dem '
             'Gleichgewicht geraten ist, als dein Kopf es zulässt. Er speichert, was du übergehst. '
             'Er hält fest, was du lange getragen hast.</p>'
             '<p>Ich habe gelernt, diese Sprache zu verstehen. Still, ohne Bewertung, ohne '
             'Zielvorgaben. Besonders dort, wo sie sichtbar wird: an deinen Füßen.</p>'
             '<p>Ich liebe diese Arbeit, weil ich immer wieder sehe, wie viel Entlastung entsteht, '
             'wenn du erkennst, warum dein Körper reagiert und was du nicht länger ausgleichen '
             'musst.</p>'
             '<p>Bei Konvaleszenz geht es nicht darum, dich zu verändern. Es geht darum, dass du '
             'dich wieder wahrnimmst. Klar. Erdverbunden. In deinem Tempo.</p>'
             '<p>Ich begleite dich, damit du verstehst, was dich belastet, und damit dein System '
             'wieder tragen kann, ohne ständig gegen sich selbst zu arbeiten.</p>'
             '<div class="byline" style="margin-top:2rem"><span>Marion Bernard, '
             '<a href="bodenplatte.html">mehr über die Arbeit dahinter</a></span></div>'
             '</div></section>')

    # Erfahrungsberichte
    karten = ""
    for name, beruf, bild, text in STIMMEN:
        oben = ('<div class="stimme-bild"><img src="assets/bilder/%s" alt="%s" '
                'decoding="async"></div>') % (bild, name) if bild else ''
        karten += ('<figure class="stimme%s">%s<div class="stimme-text">'
                   '<blockquote>%s</blockquote>'
                   '<figcaption><strong>%s</strong><span>%s</span></figcaption>'
                   '</div></figure>'
                   % ("" if bild else " ohnebild", oben, text, name, beruf))
    body += ('<section><div class="wrap">'
             '<p class="kicker">Erfahrungsberichte</p>'
             '<h2>Was Menschen danach gesagt haben</h2>'
             '<div class="stimmen">' + karten + '</div></div></section>')

    body += ('<section><div class="wrap narrow prose eigen">'
             '<!--eigen:konvaleszenz-frei--><!--/eigen:konvaleszenz-frei-->'
             '</div></section>')

    body += ('<section class="on-white"><div class="wrap narrow">'
             '<h2>Der nächste Schritt</h2>'
             '<p style="margin-top:1rem">Wenn du spürst, dass dein Körper dich nicht quält, sondern '
             'auf etwas Wesentliches hinweist, ist die Fußlesung ein ruhiger, klärender Einstieg.</p>'
             '<figure class="randbild"><img src="assets/bilder/kv-weg.webp" '
             'alt="Ein Pfad, der bergauf führt" loading="lazy" decoding="async"></figure>'
             '<p style="margin-top:1.4rem"><a class="btn-solid" href="gespraech.html">'
             'Nimm Kontakt auf</a></p>'
             '<p class="leise" style="margin-top:1.2rem">Konvaleszenz ist ein Projekt des '
             'Wirtschaftsvereins Apollon, Prinz-Eugen-Straße 68, 1040 Wien.</p>'
             '<p class="kicker" style="margin-top:2rem">Wo wir sonst noch sind</p>'
             '<p class="kanaele">'
             '<a href="https://www.linkedin.com/in/mentorin-marion-bernard/" target="_blank" rel="noopener">LinkedIn</a>'
             '<a href="https://de.pinterest.com/konvaleszenz/" target="_blank" rel="noopener">Pinterest</a>'
             '<a href="https://t.me/konvaleszenz" target="_blank" rel="noopener">Telegram</a>'
             '</p>'
             '</div></section>')

    page("konvaleszenz.html", "Konvaleszenz, Fußlesung und Mentoring in Wien | Apollon",
         "Konvaleszenz schaut auf die Ursachen. Fußlesung und Mentoring bei Marion Bernard in Wien.",
         body)


if __name__ == "__main__":
    ausstieg()
    ausstieg_bewerbung()
    ausstieg_impulsbuch()
    konvaleszenz()
    print("WIB-Bereich gebaut: ausstieg, bewerbung, impulsbuch, konvaleszenz")
