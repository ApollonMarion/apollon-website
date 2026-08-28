#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Wissensartikel zum Körper.
from build import *
from pages3 import (STAND, faq_block, faq_schema, artikel_schema,
                    quellen, weiter, CTA)

GESUNDHEITSHINWEIS = ('<p class="hinweis">Dieser Text dient der Information. Er ersetzt keine ärztliche '
                      'Untersuchung, keine Diagnose und keine Behandlung. Die hier beschriebene Arbeit ist '
                      'keine Heilbehandlung im medizinischen Sinn. Bei Schmerzen, Beschwerden oder '
                      'Veränderungen am Körper wenden Sie sich bitte an eine Ärztin oder einen Arzt. '
                      'Stand: ' + STAND + '.</p>')

BYLINE_K = ('<div class="byline"><span>Aus der Arbeit von <strong>Marion Bernard</strong>. '
            'Sie arbeitet seit Jahren mit Menschen, die sich über lange Zeit übergangen haben, und '
            'begleitet sie zurück in ein tragfähiges Maß. '
            '<a href="konvaleszenz.html">Mehr über die Konvaleszenz</a></span></div>')


def artikel_k(slug, titel, h1, intro, kurz, koerper, faqs, quellenliste, weiterlinks, beschreibung):
    body = head_block("Wissen &middot; Der Körper", h1, intro,
                      [("index.html", "Apollon"), ("wissen.html", "Wissen"),
                       ("wissen-koerper.html", "Der Körper"), "Artikel"])
    body += '<div class="wrap" style="padding-top:1.4rem"><a class="zurueck" href="wissen-koerper.html">Zurück zur Übersicht: Der Körper</a></div>'
    body += '<section class="on-white" style="padding-top:1.6rem"><div class="wrap">'
    body += '<p class="stand">Stand: ' + STAND + '</p>'
    body += '<div class="kurz"><strong>Kurz gesagt</strong><p>' + kurz + '</p></div>'
    body += '<div class="prose">' + koerper + '</div>'
    body += GESUNDHEITSHINWEIS
    if quellenliste:
        body += quellen(quellenliste)
    body += BYLINE_K
    body += '</div></section>'
    body += '<section><div class="wrap narrow"><h2>Häufige Fragen</h2>' + faq_block(faqs)
    body += weiter(weiterlinks)
    body += ('<div class="zurueck-fuss">'
             '<a class="zurueck" href="wissen-koerper.html">Zurück zur Übersicht: Der Körper</a>'
             '<a class="zurueck" href="wissen.html">Zurück zum Wissensbereich</a>'
             '<a class="zurueck" href="index.html">Zurück zur Startseite</a></div>')
    body += '</div></section>'
    body += CTA
    schema = artikel_schema(titel, beschreibung, slug) + faq_schema(faqs)
    page(slug, titel, beschreibung, body, schema)


# ---------------------------------------------------------------- Quellen30489-6/fulltext")


# ==================================================================== 1
artikel_k(
 "wissen-koerper-fusslesung.html",
 "Was ist eine Fußlesung? | Apollon",
 "Was ist eine Fußlesung?",
 "Ein Blick auf die Füße und ein Gespräch darüber, was ein Mensch trägt. Keine Untersuchung, kein Befund, keine Behandlung.",
 "Bei einer Fußlesung werden die Füße angesehen: Stellung der Zehen, Hornhaut, Gewölbe, Haut, Haltung im Stand. Daraus entsteht kein Befund, sondern ein Gespräch über Belastung und Gewohnheiten. Nachprüfbar ist der mechanische Teil, denn Hornhaut entsteht dort, wo wiederholt Druck wirkt. Alles Weitere ist Deutung und wird auch so benannt. Eine Fußlesung ist keine medizinische Diagnose und ersetzt keine ärztliche Abklärung.",
 """
<p>Der Begriff klingt nach Handlesen, und schon ist die halbe Leserschaft weg. Verständlich. Deshalb hier die nüchterne Version, mit einer klaren Trennung zwischen dem, was messbar ist, dem, was Deutung ist, und dem, was in die Hände einer Ärztin gehört.</p>

<h3>Die kurze Antwort</h3>
<p>Jemand sieht sich Ihre Füße an und stellt Fragen. Aus dem, was zu sehen ist, und aus dem, was Sie erzählen, entsteht ein Gespräch über Belastung: worauf Sie stehen, wie lange schon, und was Sie dabei mit sich machen.</p>
<p>Kein Gerät, kein Befund, kein Rezept. Ein Gespräch, das an einem ungewöhnlichen Punkt ansetzt.</p>

<h3>Woher das kommt</h3>
<p>Die Vorstellung, dass sich am Fuß etwas über den ganzen Menschen ablesen lässt, stammt aus traditionellen Heilsystemen, vor allem aus dem Ayurveda und der chinesischen Medizin, die den Fuß als eine Art Karte des Organismus verstehen. Aus dieser Tradition kommen auch die bekannteren Verwandten wie die Fußreflexzonenarbeit.</p>
<p>Diese Systeme sind alt und in sich stimmig, aber sie sind nicht durch kontrollierte Studien belegt. Wer etwas anderes behauptet, verkauft Ihnen etwas. Wir sagen es deshalb lieber selbst, bevor es jemand anders tut.</p>

<h3>Worauf geschaut wird</h3>
<p>In der Praxis geht es um sichtbare Dinge: die Stellung und Form der Zehen, wo sich Hornhaut gebildet hat und wo nicht, wie das Gewölbe steht, wie sich das Gewicht im Stand verteilt, wie die Haut aussieht, wie die Füße gehalten werden, wenn niemand hinsieht.</p>
<p>Dazu, oft aufschlussreicher als alles andere, ein Paar getragene Schuhe. Sohlen lügen nicht.</p>

<h3>Was daran nachprüfbar ist</h3>
<p>Ein Teil dieser Beobachtungen steht auf festem Boden.</p>
<p>Hornhaut entsteht dort, wo wiederholt Druck und Reibung wirken. Das ist keine Deutung, das ist Physiologie. Und der Zusammenhang ist gut untersucht: In einer Studie an diabetischen Patienten sanken die Spitzendrücke unter den Vorfußballen nach dem Abtragen der Schwielen um sechsundzwanzig Prozent, von durchschnittlich 14,2 auf 10,3 Kilogramm pro Quadratzentimeter. Die Autoren beschrieben die Hornhaut als eine Art Fremdkörper, der den Druck zusätzlich erhöht.</p>
<p>Wo Hornhaut ist, war also Belastung. In der Diabetesversorgung wird genau daraus eine ernste Konsequenz gezogen, weil erhöhter plantarer Druck ein Risikofaktor für Fußgeschwüre ist.</p>
<p>Die Füße halten fest, wie jemand steht und geht. Das ist der harte Kern, auf den sich alles Weitere stützt.</p>

<h3>Was daran Deutung ist</h3>
<p>Der Sprung von „hier war Belastung“ zu „deshalb ist dieser Mensch so und so“ ist kein Messvorgang. Er ist eine Deutung.</p>
<p>Das ist kein Makel, solange man es sagt. Ein guter Handwerker deutet ständig, eine erfahrene Ärztin auch. Der Unterschied zwischen seriös und unseriös liegt nicht darin, ob gedeutet wird, sondern ob die Deutung als solche benannt wird und ob sie im Gespräch überprüfbar bleibt.</p>
<p>Deshalb ist eine Fußlesung, die gut gemacht ist, immer ein Dialog. Es wird etwas beobachtet, es wird eine Frage daraus, und Sie sagen, ob das stimmt. Wenn nicht, wird die Deutung fallen gelassen, nicht Sie.</p>

<h3>Was eine Fußlesung ausdrücklich nicht ist</h3>
<p>Sie ist keine Diagnose. In Österreich ist die Feststellung von Krankheiten Ärzten vorbehalten, und das Berufsbild der Humanenergetik hält ausdrücklich fest, dass diese Tätigkeit keine Heilbehandlung im Sinn einer Krankheitsbehandlung darstellt.</p>
<p>Die Standesregeln gehen weiter: keine Diagnosen, keine Therapien im medizinischen Sinn, keine unseriösen Versprechen über die zu erwartende Wirkung, dafür die Pflicht, die eigene Methode samt ihren Grenzen verständlich zu erklären.</p>
<p>Sie ist auch keine Massage, keine physiotherapeutische Anwendung und keine psychologische Beratung. Für all das gibt es eigene Berufe mit eigenen Ausbildungen, und dafür gibt es gute Gründe.</p>

<h3>Wie ein Termin abläuft</h3>
<p>Zuerst wird geredet. Was ist gerade los, was hat Sie hergeführt, seit wann geht das so.</p>
<p>Dann werden die Füße angesehen, im Sitzen und im Stehen, in Ruhe und in Bewegung. Was auffällt, wird benannt und zur Frage gemacht.</p>
<p>Am Ende steht kein Papier mit Befunden, sondern im besten Fall ein Satz, den Sie mitnehmen und der noch eine Woche später stimmt. Manchmal ist es auch ein Hinweis, dass Sie damit besser zu einer Ärztin gehen.</p>

<h3>Wann Sie nicht hierher gehören, sondern zum Arzt</h3>
<p>Das ist der wichtigste Absatz dieses Textes.</p>
<p>Gehen Sie ärztlich abklären, wenn Sie eine Wunde am Fuß haben, die nicht heilt. Wenn ein Fuß anschwillt, sich verfärbt, warm wird oder schmerzt, ohne dass Sie sich verletzt haben. Wenn Sie Taubheit oder Kribbeln spüren. Wenn Sie an Diabetes leiden, denn dann gehören Ihre Füße ohnehin regelmäßig in fachkundige Hände.</p>
<p>Solche Zeichen können auf Durchblutungsstörungen, Entzündungen oder Thrombosen hinweisen. Das sind keine Themen für eine Deutung, sondern für eine Untersuchung, und zwar zeitnah.</p>

<h3>Für wen es nichts ist</h3>
<p>Für Menschen, die eine schnelle Lösung suchen. Für Menschen, die ein Ergebnis auf Papier wollen. Und für Menschen, die auf keinen Fall hören möchten, dass ihre Erschöpfung mit ihren eigenen Entscheidungen zu tun haben könnte.</p>
<p>Für alle anderen ist es ein ungewöhnlich guter Einstieg in ein Gespräch, das sonst schwer beginnt.</p>
""",
 [("Ist eine Fußlesung eine medizinische Diagnose?",
   "Nein. Die Feststellung von Krankheiten ist Ärzten vorbehalten. Eine Fußlesung ist eine Beobachtung und ein Gespräch, keine Untersuchung und keine Heilbehandlung."),
  ("Ist das wissenschaftlich belegt?",
   "Teilweise. Dass Hornhaut durch wiederholte Belastung entsteht und den örtlichen Druck erhöht, ist gut untersucht. Die Deutung von Fußformen als Hinweis auf Persönlichkeit oder Lebensgeschichte ist dagegen Tradition und Erfahrung, nicht belegte Wissenschaft. Wir sagen das offen."),
  ("Was ist der Unterschied zur Fußreflexzonenmassage?",
   "Die Reflexzonenarbeit ist eine Behandlung mit den Händen. Bei einer Fußlesung wird geschaut und gesprochen. Massage und vergleichbare manuelle Anwendungen sind eigenen Berufen vorbehalten."),
  ("Muss ich meine Füße vorbereiten?",
   "Nein. Kommen Sie so, wie Sie sind. Lack, Hornhaut und alles andere gehören zum Bild. Hilfreich ist es, ein Paar länger getragene Schuhe mitzubringen."),
  ("Bekomme ich einen schriftlichen Befund?",
   "Nein, und das ist beabsichtigt. Ein Befund würde etwas behaupten, was hier nicht behauptet werden darf und auch nicht behauptet werden soll."),
  ("Wann sollte ich stattdessen zum Arzt?",
   "Bei nicht heilenden Wunden, Schwellung, Verfärbung, Überwärmung, plötzlichen Schmerzen ohne Verletzung, Taubheit oder Kribbeln, und generell bei bestehendem Diabetes. Solche Zeichen gehören zeitnah ärztlich abgeklärt."),
  ],
 [],
 [("Was der Körper über Druck erzählt", "wissen-koerper-druck.html"),
  ("Warum Symptome bekämpfen selten hilft", "wissen-koerper-symptome.html"),
  ("Der Körper liest mit", "wissen-koerper.html"),
  ("Konvaleszenz", "konvaleszenz.html")],
 "Was bei einer Fußlesung tatsächlich geschieht, was daran nachprüfbar ist, was Deutung bleibt und wann stattdessen eine ärztliche Abklärung nötig ist."
)


# ==================================================================== 2
artikel_k(
 "wissen-koerper-druck.html",
 "Was der Körper über Druck erzählt | Apollon",
 "Was der Körper über Druck erzählt",
 "Der Fuß ist ein Messgerät, das nie ausgeschaltet wird. Was er aufzeichnet, ist nachprüfbar. Was man daraus liest, ist eine andere Frage.",
 "Der Körper hält mechanische Belastung fest. Hornhaut bildet sich dort, wo wiederholt Druck wirkt, und erhöht diesen Druck zusätzlich: Nach dem Abtragen sanken die Spitzendrücke in einer Studie um sechsundzwanzig Prozent. Auch psychische Belastung ist im Körper messbar, etwa an erhöhter Muskelaktivität unter Stress, und psychosoziale Belastung am Arbeitsplatz gilt in Längsschnittstudien als Risikofaktor für Nacken- und Schulterbeschwerden. Vom sichtbaren Zeichen auf eine bestimmte Ursache zurückzuschließen, bleibt trotzdem Deutung.",
 """
<p>Es gibt zwei Arten von Druck, und die Sprache behandelt sie wie dasselbe. Der eine wirkt in Kilogramm pro Quadratzentimeter. Der andere kommt aus dem Terminkalender. Dieser Text handelt von beiden und davon, wo die Verbindung nachweisbar ist und wo sie eine Vermutung bleibt.</p>

<h3>Der Fuß zeichnet auf, ob Sie wollen oder nicht</h3>
<p>Der Fuß trägt das gesamte Körpergewicht, jeden Tag, jahrzehntelang. Er ist die einzige Stelle, an der ein Mensch dauerhaft mit dem Boden verhandelt.</p>
<p>Und er reagiert. Wo wiederholt Druck und Reibung wirken, verdickt sich die Haut. Das ist eine sinnvolle Schutzreaktion, und sie ist präzise: Hornhaut bildet sich nicht irgendwo, sondern genau dort, wo Last ankommt.</p>

<h3>Hornhaut ist ein Protokoll</h3>
<p>Hier wird es interessant, denn der Schutz hat einen Preis.</p>
<p>In einer Untersuchung an siebzehn diabetischen Patienten wurden dreiundvierzig Schwielen unter den Vorfußballen abgetragen. Die Spitzendrücke sanken danach um sechsundzwanzig Prozent, von durchschnittlich 14,2 auf 10,3 Kilogramm pro Quadratzentimeter. Bei jedem einzelnen Patienten war eine Reduktion messbar.</p>
<p>Die Schlussfolgerung der Autoren: Die Hornhaut wirkt selbst wie ein Fremdkörper und erhöht den Druck, den sie eigentlich abfangen soll.</p>
<p>Das ist mehr als eine Fußnote. Es ist ein Muster, das man in vielen Bereichen wiederfindet: Der Schutz, den ein System aufbaut, wird zum zusätzlichen Problem, wenn die Belastung nicht aufhört.</p>

<h3>Warum die Medizin das ernst nimmt</h3>
<p>In der Versorgung des diabetischen Fußes ist erhöhter plantarer Druck ein anerkannter Risikofaktor für Fußgeschwüre. Deshalb gehören Druckentlastung und die fachgerechte Entfernung von Hornhaut dort zu den Standardmaßnahmen.</p>
<p>Man kann daraus zwei Dinge lernen. Erstens: Was der Fuß aufzeichnet, ist keine Esoterik, sondern in bestimmten Zusammenhängen eine klinisch relevante Information. Zweitens: Es gibt Menschen, bei denen an den Füßen nicht gedeutet, sondern behandelt werden muss, und zwar von Fachleuten.</p>

<h3>Der andere Druck</h3>
<p>Dass psychische Belastung im Körper ankommt, spürt jeder, der schon einmal nach einem schwierigen Tag Schultern wie Beton hatte.</p>
<p>Messbar ist das auch. Untersuchungen der Muskelaktivität am Trapezmuskel zeigen unter mentaler Belastung ein verändertes Aktivitätsmuster gegenüber Ruhe und Entspannung. Die einzelnen Studien sind allerdings klein und finden unter Laborbedingungen statt, weshalb man daraus keine großen Schlüsse ziehen sollte.</p>
<p>Robuster ist der Befund auf der Ebene der Arbeitswelt. Systematische Übersichten longitudinaler Studien finden Zusammenhänge zwischen psychosozialen Bedingungen am Arbeitsplatz und dem Auftreten von Nacken- und Schulterbeschwerden. Es sind Zusammenhänge, keine einfachen Ursachenketten, aber sie sind über die Zeit hinweg nachweisbar.</p>
<p>Kurz gesagt: Belastung, die nicht körperlich beginnt, endet trotzdem oft körperlich.</p>

<h3>Was daraus folgt und was nicht</h3>
<p>Es folgt: Der Körper ist ein Aufzeichnungsgerät für Belastung, und zwar für beide Arten.</p>
<p>Es folgt nicht: dass man von einer Verhärtung an einer bestimmten Stelle auf ein bestimmtes Ereignis in einem bestimmten Lebensjahr schließen kann. Wer so etwas behauptet, hat die Grenze zwischen Beobachtung und Erfindung überschritten.</p>
<p>Die ehrliche Formulierung lautet: Hier ist Last angekommen. Woher sie kam, weiß nur der Mensch, der davor steht. Deshalb ist das Gespräch nicht die Beigabe zur Beobachtung, sondern der eigentliche Vorgang.</p>

<h3>Was Sie selbst sehen können</h3>
<p>Dafür brauchen Sie niemanden.</p>
<p>Nehmen Sie ein Paar Schuhe, die Sie mindestens ein halbes Jahr getragen haben, und drehen Sie sie um. Wo ist die Sohle abgelaufen? Außen, innen, vorne, an einer Seite mehr als an der anderen? Vergleichen Sie den linken mit dem rechten Schuh.</p>
<p>Dann sehen Sie sich die Fußsohlen an. Wo ist die Haut dicker? Ist es rechts und links gleich?</p>
<p>Das beantwortet keine Frage, aber es stellt eine gute: Warum eigentlich dort? Und seit wann?</p>

<h3>Warum uns das bei Apollon beschäftigt</h3>
<p>Weil die Menschen, mit denen wir arbeiten, meistens nicht kommen, weil ihnen der Fuß wehtut. Sie kommen, weil etwas nicht mehr geht, und sie haben dafür lange keine Sprache.</p>
<p>Unternehmer sind darin geübt, Belastung auszuhalten. Das ist über Jahre eine Stärke und irgendwann eine Falle, weil das Aushalten so gut funktioniert, dass die Rückmeldung ausbleibt. Wer sich selbst nicht mehr hört, hat noch einen Kanal übrig: den Körper.</p>
<p>Der Körper ist die letzte Instanz, die nicht verhandelt. Das ist unbequem und, wenn man es rechtzeitig ernst nimmt, ein enormer Vorteil.</p>
""",
 [("Kann man am Fuß erkennen, wie es einem Menschen geht?",
   "Man kann erkennen, wo Last angekommen ist, denn Hornhaut und Abnutzung folgen der Belastung. Welche Ursache dahinter steht, ergibt sich nicht aus dem Fuß, sondern aus dem Gespräch."),
  ("Ist Hornhaut schädlich?",
   "Sie ist zunächst ein Schutz. Sie kann aber den örtlichen Druck zusätzlich erhöhen. In einer Studie sanken die Spitzendrücke nach dem Abtragen um sechsundzwanzig Prozent. Bei Diabetes gehört das in fachkundige Hände, nicht in Eigenregie."),
  ("Macht Stress wirklich Muskelverspannung?",
   "Unter mentaler Belastung verändert sich messbar die Muskelaktivität, und psychosoziale Belastung am Arbeitsplatz gilt in Längsschnittstudien als Risikofaktor für Nacken- und Schulterbeschwerden. Es handelt sich um Zusammenhänge, nicht um eine einfache Ursachenkette."),
  ("Was sagen abgelaufene Schuhsohlen aus?",
   "Sie zeigen, wie sich Ihr Gewicht beim Gehen tatsächlich verteilt, über Monate gemittelt. Das ist eine gute Beobachtung und keine Diagnose."),
  ("Sollte ich Hornhaut selbst entfernen?",
   "Bei gesunden Füßen ist das Pflege. Bei Diabetes, Durchblutungsstörungen oder Gefühlsstörungen an den Füßen gehört das ausdrücklich in fachkundige Hände, weil dort schon kleine Verletzungen ernste Folgen haben können."),
  ],
 [],
 [("Was ist eine Fußlesung?", "wissen-koerper-fusslesung.html"),
  ("Warum Symptome bekämpfen selten hilft", "wissen-koerper-symptome.html"),
  ("Der Körper liest mit", "wissen-koerper.html"),
  ("Konvaleszenz", "konvaleszenz.html")],
 "Was der Körper über Belastung festhält: Hornhaut und plantarer Druck, Stress und Muskelaktivität, und wo die Grenze zwischen Beobachtung und Deutung verläuft."
)


# ==================================================================== 3
artikel_k(
 "wissen-koerper-symptome.html",
 "Warum Symptome bekämpfen selten hilft | Apollon",
 "Warum Symptome bekämpfen selten hilft",
 "Manchmal ist es genau richtig. Meistens ist es der teure Umweg. Der Rückenschmerz zeigt, warum.",
 "Bei Kreuzschmerzen lässt sich in etwa 85 bis 90 von 100 Fällen keine eindeutige körperliche Ursache feststellen. Die Leitlinien empfehlen deshalb ohne Warnhinweise zunächst keine Bildgebung, raten von Bettruhe ab und setzen auf Bewegung und Aufklärung. Die Versorgungsrealität sieht anders aus: unnötige Aufnahmen, Opioide, Operationen. Als Risikofaktoren für die Chronifizierung gelten Angst vor Schmerz, Schonverhalten, Stress, berufliche Unzufriedenheit und, bemerkenswerterweise, unnötige Untersuchungen selbst.",
 """
<p>Der Satz „Symptome bekämpfen hilft nicht“ steht auf tausend Websites und ist in dieser Form falsch. Fangen wir also damit an.</p>

<h3>Wann Symptombekämpfung richtig ist</h3>
<p>Bei akutem Schmerz gehört Schmerz gelindert. Bei hohem Fieber wird gesenkt. Bei einem gebrochenen Bein wird der Bruch versorgt und niemand fragt zuerst nach der Lebensgeschichte.</p>
<p>Es gibt Situationen, in denen das Symptom das Problem ist. Wer das leugnet, um eine Methode zu verkaufen, richtet Schaden an.</p>
<p>Interessant wird es bei dem, was danach kommt: wenn das Symptom bleibt, wiederkommt oder wandert.</p>

<h3>Der Rückenschmerz als Lehrstück</h3>
<p>Kaum ein Beschwerdebild ist besser untersucht, und keines zeigt das Problem so deutlich.</p>
<p>Bei etwa fünfundachtzig bis neunzig von hundert Betroffenen mit Kreuzschmerzen lässt sich keine eindeutige körperliche Ursache feststellen. Man nennt das nicht-spezifischen Kreuzschmerz. Der Schmerz ist echt, die Ursache aber nicht auf ein Bild zu bringen.</p>

<h3>Was die Leitlinien empfehlen</h3>
<p>Die Empfehlungen sind seit Jahren klar und lauten sinngemäß so:</p>
<p>Wenn Gespräch und körperliche Untersuchung keine Hinweise auf einen gefährlichen Verlauf ergeben, sollen zunächst keine weiteren Untersuchungen durchgeführt werden. Von Bettruhe soll abgeraten werden. Zu körperlicher Aktivität soll ermutigt werden.</p>
<p>Also: nicht sofort hineinschauen, nicht schonen, in Bewegung bleiben, verstehen, was los ist.</p>

<h3>Was tatsächlich passiert</h3>
<p>Eine große internationale Übersicht hat das nachgezählt, und die Zahlen sind unangenehm.</p>
<p>In Norwegen wurden neununddreißig Prozent der Betroffenen zur Bildgebung geschickt, in den USA vierundfünfzig, in Italien sechsundfünfzig, obwohl das nicht empfohlen war. In den USA erhielten rund sechzig Prozent der Rückenschmerzfälle in Notaufnahmen Opioide, deren Nutzen gering und deren Risiken erheblich sind. Versteifungsoperationen werden angeboten, obwohl sie gegenüber konservativer Behandlung keinen Vorteil zeigen, dafür mehr kosten und mehr Risiko tragen. Und auch die Physiotherapie greift zu Verfahren ohne Wirknachweis: In Schweden empfahlen achtunddreißig Prozent Elektrotherapie, in den USA fünfundsiebzig Prozent Traktion.</p>
<p>Der Befund der Autoren in einem Satz: Trotz enormer Ausgaben ist die rückenbedingte Beeinträchtigung nicht gesunken, sondern gestiegen.</p>

<h3>Warum es schiefgeht: das Bild findet immer etwas</h3>
<p>Der Kern des Problems ist nicht Bösartigkeit, sondern eine gut gemeinte Verwechslung.</p>
<p>Wenn man in einen Rücken hineinschaut, findet man etwas. Abnutzung, eine Vorwölbung, irgendeine Veränderung. Solche Befunde sind ab einem gewissen Alter weit verbreitet, auch bei Menschen ohne jede Beschwerde. Sobald ein Befund aber einen Namen hat, wird er zur Erklärung, und die Erklärung ruft die Behandlung.</p>
<p>So entsteht eine Kette, die logisch aussieht und am eigentlichen Geschehen vorbeiläuft. Und sie hat einen Preis, der über Geld hinausgeht: Wer eine Diagnose bekommt, die nach Schaden klingt, beginnt sich zu schonen.</p>

<h3>Die gelben Flaggen</h3>
<p>Genau dort setzt der zweite Teil der Leitlinien an. Als Risikofaktoren dafür, dass Schmerz chronisch wird, gelten unter anderem: starke Angst vor Schmerzen, Schon- und Vermeidungsverhalten, Stress, Mobbing, Depression, berufliche Unzufriedenheit.</p>
<p>Und, das ist der Satz, den man sich merken sollte: unnötige Untersuchungen selbst.</p>
<p>Die Suche nach der körperlichen Ursache kann also zu dem beitragen, was sie beheben soll. Nicht weil Untersuchen falsch wäre, sondern weil jede Untersuchung eine Botschaft mitschickt: Hier stimmt etwas mit deinem Rücken nicht.</p>

<h3>Was das über Symptome sagt</h3>
<p>Ein Symptom ist kein Feind. Es ist eine Meldung.</p>
<p>Wenn die Meldung wegfällt und die Lage bleibt, kommt die nächste Meldung. Auf einem anderen Kanal, oft lauter. Deshalb wandern Beschwerden bei Menschen, die über Jahre gegen sich arbeiten: Es ist nicht dieselbe Beschwerde, aber es ist dieselbe Lage.</p>
<p>Die brauchbare Frage lautet deshalb nicht „Wie bekomme ich das weg?“, sondern „Was meldet sich hier, und wovon?“</p>

<h3>Die roten Flaggen: wann sofort ärztlich</h3>
<p>Es gibt Situationen, in denen diese Überlegungen nicht gelten und Ursachensuche in einer Praxis stattfindet, und zwar sofort.</p>
<p>Die Leitlinien nennen als Warnzeichen unter anderem: schwere Verletzungen oder bekannte Osteoporose unter Langzeit-Kortisontherapie, Fieber und Schüttelfrost, in die Beine ausstrahlende Schmerzen mit Gefühlsstörungen oder Lähmungen, schleichender Beginn mit Morgensteifigkeit, Gewichtsverlust, Schmerzen nachts oder im Liegen.</p>
<p>Wenn eines davon zutrifft, lesen Sie hier bitte nicht weiter, sondern lassen Sie das abklären.</p>

<h3>Was Ursachen ansehen wirklich heißt</h3>
<p>Es heißt nicht, in der Kindheit zu graben, bis sich etwas findet. Es heißt, die Bedingungen anzusehen, unter denen jemand lebt und arbeitet, und dann eine davon zu ändern.</p>
<p>Wie viele Stunden. Wie viel Verantwortung ohne Entlastung. Wie lange schon ohne echte Pause. Was seit Jahren aufgeschoben wird, weil gerade keine Zeit ist. Wo jemand Ja sagt und Nein meint.</p>
<p>Das ist unspektakulär und deutlich wirksamer als es klingt. Die Leitlinien sagen dasselbe in ihrer Sprache: Aufklärung über die Natur der Beschwerden, Bewegung, aktiv bleiben, und bei anhaltenden Beschwerden psychologisch begleitete Verfahren.</p>

<h3>Der ehrliche Schluss</h3>
<p>Symptome bekämpfen hilft manchmal, und dann soll man es tun. Es hilft nur dann nicht, wenn die Bedingungen, die das Symptom erzeugen, unverändert weiterlaufen.</p>
<p>Der Unterschied ist einfach zu prüfen. Wenn dieselbe Beschwerde nach jeder Behandlung wiederkommt, oder wenn sie durch eine andere ersetzt wird, dann arbeiten Sie am Falschen. Nicht weil die Behandlung schlecht war, sondern weil sie eine Meldung abgestellt und die Lage gelassen hat.</p>
""",
 [("Sind Schmerzmittel bei Rückenschmerz falsch?",
   "Nicht grundsätzlich. Bei akuten Beschwerden kann Schmerzlinderung sinnvoll sein. Kritisch sehen die Leitlinien den breiten Einsatz starker Schmerzmittel, insbesondere von Opioiden, deren Nutzen bei Rückenschmerz gering ist und deren Risiken erheblich sind."),
  ("Warum soll ich kein Röntgen oder MRT machen lassen?",
   "Wenn Gespräch und Untersuchung keine Warnhinweise ergeben, empfehlen die Leitlinien zunächst keine Bildgebung. Bildbefunde wie Abnutzung sind ab einem gewissen Alter weit verbreitet, auch ohne Beschwerden, und werden leicht für die Ursache gehalten. Bei Warnzeichen gilt das Gegenteil, dann gehört abgeklärt."),
  ("Was sind rote Flaggen?",
   "Warnzeichen, die eine rasche ärztliche Abklärung erfordern: schwere Verletzung, Fieber und Schüttelfrost, ausstrahlende Schmerzen mit Gefühlsstörungen oder Lähmungen, Gewichtsverlust, nächtliche Schmerzen oder Schmerzen im Liegen, bekannte Osteoporose unter Langzeit-Kortisontherapie."),
  ("Heißt Ursachensuche, dass alles psychisch ist?",
   "Nein. Nicht-spezifisch bedeutet nicht eingebildet. Der Schmerz ist real, er lässt sich nur nicht auf eine einzelne körperliche Struktur zurückführen. Beteiligt sind körperliche, psychische und soziale Bedingungen zugleich."),
  ("Was hilft dann?",
   "Nach den Leitlinien: verstehen, worum es sich handelt, in Bewegung bleiben, Bettruhe vermeiden, körperlich aktiv sein und bei anhaltenden Beschwerden auch psychologisch begleitete Verfahren nutzen. Dazu kommt das Unbequeme: die Bedingungen ändern, unter denen die Beschwerden entstehen."),
  ("Woran erkenne ich, dass ich am Symptom arbeite statt an der Ursache?",
   "Daran, dass dieselbe Beschwerde nach jeder Behandlung wiederkommt oder durch eine andere abgelöst wird."),
  ],
 [],
 [("Was der Körper über Druck erzählt", "wissen-koerper-druck.html"),
  ("Was ist eine Fußlesung?", "wissen-koerper-fusslesung.html"),
  ("Der Körper liest mit", "wissen-koerper.html"),
  ("Konvaleszenz", "konvaleszenz.html")],
 "Warum das Bekämpfen von Symptomen manchmal richtig und häufig ein Umweg ist, was die Leitlinien zum Kreuzschmerz empfehlen, und woran sich erkennen lässt, dass am Falschen gearbeitet wird."
)
