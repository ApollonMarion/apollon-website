#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Letzte Runde Wissensartikel zum Verein.
from pages3 import artikel, Q_GV, Q_WKO

Q_VERG21 = ("§ 21 Vereinsgesetz 2002 im Rechtsinformationssystem des Bundes", "https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20001917&Paragraf=21")
Q_VERG29 = ("§ 29 Vereinsgesetz 2002 im Rechtsinformationssystem des Bundes", "https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20001917&Paragraf=29")
Q_GPLB = ("Gemeinsame Prüfung Lohnabgaben und Beiträge, WKO", "https://www.wko.at/sozialversicherung/pruefung-lohnabhaengiger-abgaben-beitraege-gplb")
Q_BAO45A = ("§ 45a Bundesabgabenordnung im Rechtsinformationssystem des Bundes", "https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10003940&Paragraf=45a")
Q_USP_KU = ("Kleinunternehmerregelung, Unternehmensserviceportal", "https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/weitere-informationen-zur-umsatzsteuer/weitere-steuertatbestaende-und-befreiungen/kleinunternehmen.html")

# ==================================================================== 11
artikel(
 "wissen-verein-pruefung.html",
 "Was passiert bei einer Vereinsprüfung? | Apollon",
 "Was passiert bei einer Vereinsprüfung?",
 "Es gibt drei verschiedene, und die meisten meinen die falsche.",
 "Es gibt drei Arten von Prüfung. Die interne durch die Rechnungsprüfer nach § 21 Vereinsgesetz, die abgabenrechtliche durch Finanzamt und Sozialversicherung, meist als gemeinsame Prüfung der Lohnabgaben alle drei bis fünf Jahre, und die vereinsbehördliche, die nur bei schweren Verstößen greift und bis zur Auflösung führen kann.",
 """
<p>Wenn jemand sagt „bei uns steht eine Prüfung an“, lohnt die Rückfrage, welche gemeint ist. Die drei haben unterschiedliche Prüfer, unterschiedliche Maßstäbe und sehr unterschiedliche Folgen.</p>

<h3>Erstens: die interne Prüfung durch die Rechnungsprüfer</h3>
<p>Sie ist die häufigste und die einzige, die jeder Verein jedes Jahr hat.</p>
<p>Nach § 21 Vereinsgesetz muss das Leitungsorgan ein angemessenes Rechnungswesen führen, sodass die Finanzlage rechtzeitig und hinreichend erkennbar ist. Innerhalb von fünf Monaten nach Jahresende sind eine Einnahmen- und Ausgabenrechnung sowie eine Vermögensübersicht zu erstellen.</p>
<p>Die Rechnungsprüfer prüfen dann innerhalb von vier Monaten zweierlei: die Ordnungsmäßigkeit der Rechnungslegung und die <em>statutengemäße Verwendung der Mittel</em>. Der zweite Teil wird regelmäßig unterschätzt. Es geht nicht nur darum, ob richtig gerechnet wurde, sondern ob das Geld für das ausgegeben wurde, wofür der Verein da ist.</p>
<p>Der Bericht geht an das Leitungsorgan. Er bestätigt entweder die Ordnungsmäßigkeit oder benennt festgestellte Mängel und Gefahren für den Bestand des Vereins. Besonderes Augenmerk gilt ungewöhnlichen Geschäften.</p>
<p>Und ein Detail, das kaum jemand kennt: Bei beharrlichen schweren Verstößen können die Rechnungsprüfer selbst eine Mitgliederversammlung einberufen. Sie sind also kein Feigenblatt, sondern ein Kontrollorgan mit Zähnen.</p>

<h3>Ab wann es aufwendiger wird</h3>
<p>Übersteigen die gewöhnlichen Einnahmen oder Ausgaben eine Million Euro in zwei aufeinanderfolgenden Jahren, verschärfen sich die Anforderungen an die Rechnungslegung. Ab drei Millionen Euro, oder ab einer Million Euro an Spenden, ist ein erweiterter Jahresabschluss mit einem qualifizierten Abschlussprüfer nötig.</p>

<h3>Zweitens: die abgabenrechtliche Prüfung</h3>
<p>Das ist die, vor der sich die meisten fürchten, und die einzige, bei der es unmittelbar um Geld geht.</p>
<p>Die häufigste Form ist die gemeinsame Prüfung der Lohnabgaben und Beiträge, kurz GPLB. Sie fasst mehrere Prüfungen in einem Vorgang zusammen: Lohnsteuer, Dienstgeberbeitrag samt Zuschlag, Kommunalsteuer und die Sozialversicherungsbeiträge.</p>
<p>Geprüft wird durch Prüfer des Finanzamts, des Prüfdienstes für lohnabhängige Abgaben und Beiträge oder der Gesundheitskasse. Angesehen werden Lohnaufzeichnungen, Zeitaufzeichnungen, Verträge, Reisekostenabrechnungen und Zahlungsbelege.</p>
<p>Der Rhythmus liegt bei drei bis maximal fünf Jahren. Kürzer wird es bei einem Verdacht oder einer Anzeige.</p>
<p>Für Vereine sind zwei Punkte typisch: Wurden Menschen als Selbstständige behandelt, die eigentlich Dienstnehmer waren? Und wurden Pauschalen wie die Freiwilligenpauschale oder die Reiseaufwandsentschädigung sauber aufgezeichnet? Wenn die Aufzeichnungen fehlen, wird im Zweifel Entgelt angenommen, und der Verein zahlt nach.</p>

<h3>Drittens: die vereinsbehördliche Prüfung</h3>
<p>Sie ist die seltenste und die einschneidendste.</p>
<p>Nach § 29 Vereinsgesetz kann die Vereinsbehörde einen Verein mit Bescheid auflösen, wenn er gegen Strafgesetze verstößt, wenn er seinen statutenmäßigen Wirkungskreis überschreitet, oder wenn er die Voraussetzungen seines rechtlichen Bestands nicht mehr erfüllt.</p>
<p>Der mittlere Punkt betrifft ganz normale Vereine: Wer dauerhaft etwas anderes tut, als in den Statuten steht, überschreitet seinen Wirkungskreis. Das ist der Grund, warum der Vereinszweck kein Formsatz ist.</p>

<h3>Was man vorbereiten kann, und zwar heute</h3>
<p>Alle drei Prüfungen fragen im Kern dasselbe: Stimmt das, was ihr tut, mit dem überein, was ihr aufgeschrieben habt?</p>
<p>Praktisch heißt das: aktuelle Statuten, Protokolle der Mitgliederversammlungen und Beschlüsse, eine nachvollziehbare Einnahmen- und Ausgabenrechnung, Belege zu jeder Zahlung, Aufzeichnungen über Pauschalen und Verträge mit allen, die für den Verein arbeiten.</p>
<p>Das ist kein großer Aufwand, wenn man es laufend macht. Es ist ein sehr großer, wenn man es nachträglich rekonstruieren muss.</p>
 """,
 [("Wer bestellt die Rechnungsprüfer?",
   "Sie werden nach den Regeln der Statuten bestellt, üblicherweise von der Mitgliederversammlung. Sie sollen unabhängig vom Leitungsorgan sein, sonst prüft der Verein sich selbst."),
  ("Wie oft kommt eine Prüfung des Finanzamts?",
   "Die gemeinsame Prüfung der Lohnabgaben und Beiträge findet in Abständen von drei bis maximal fünf Jahren statt. Bei Verdacht oder Anzeige kann sie früher kommen."),
  ("Was passiert, wenn Aufzeichnungen fehlen?",
   "Dann wird im Zweifel zu Lasten des Vereins geschätzt oder eine Zahlung als Entgelt gewertet. Nachforderungen bei Steuer und Sozialversicherung trägt der Verein."),
  ("Kann die Behörde einen Verein wirklich auflösen?",
   "Ja, nach § 29 Vereinsgesetz per Bescheid, etwa bei Verstößen gegen Strafgesetze oder bei dauerhafter Überschreitung des statutenmäßigen Wirkungskreises."),
  ],
 [Q_VERG21, Q_VERG29, Q_GPLB, Q_WKO],
 [("Wie zahlt ein Verein jemanden aus?", "wissen-verein-auszahlen.html"),
  ("Welche Organe braucht ein Verein wirklich?", "wissen-verein-organe.html"),
  ("Was gehört in Vereinsstatuten, und was besser nicht?", "wissen-verein-statuten.html"),
  ("Muss ein Verein gemeinnützig sein?", "wissen-verein-gemeinnuetzig.html")],
 "Interne Rechnungsprüfung, GPLB durch Finanzamt und Sozialversicherung, behördliche Prüfung nach § 29 VerG: die drei Vereinsprüfungen und was sie verlangen."
)

# ==================================================================== 12
artikel(
 "wissen-verein-tragender-betrieb.html",
 "Wie aus einem Verein ein wirtschaftlich tragender Betrieb wird | Apollon",
 "Wie aus einem Verein ein wirtschaftlich tragender Betrieb wird",
 "Nicht durch mehr Mitgliedsbeiträge. Durch Projekte, die sich selbst tragen.",
 "Ein Verein trägt sich wirtschaftlich, wenn seine Projekte Einnahmen erzeugen, die vom Vereinszweck gedeckt sind. Möglich macht das die Nebenzweckprivilegierung: Der Verein darf erwerbswirtschaftlich tätig sein, solange Überschüsse dem Zweck zufließen. Grenzen setzen die Gewerbeordnung, die Kleinunternehmergrenze von 55.000 Euro und bei Gemeinnützigkeit die 100.000-Euro-Schwelle des § 45a BAO.",
 """
<p>Die meisten Vereine leben von Beiträgen, Förderungen und dem guten Willen einiger weniger. Das trägt eine Weile und wird irgendwann müde. Der Weg heraus führt nicht über höhere Beiträge, sondern über Projekte, die sich selbst rechnen.</p>

<h3>Die Erlaubnis, die viele nicht kennen</h3>
<p>Ein Verein darf sich erwerbswirtschaftlich betätigen und dabei Gewinne erzielen. Die einzige Bedingung: Diese Gewinne dürfen nicht an die Mitglieder ausgeschüttet werden, sondern müssen dem ideellen Zweck zufließen.</p>
<p>Das ist das Nebenzweckprivileg. Es macht den Verein zu einem Rechtsträger, mit dem man tatsächlich arbeiten kann, und nicht nur zu einem Verwaltungsapparat für Mitgliedsbeiträge.</p>

<h3>Schritt eins: der Zweck muss es hergeben</h3>
<p>Bevor irgendetwas verkauft wird, muss der Vereinszweck die Tätigkeit abdecken, und die Statuten müssen die Mittel zur Zweckerreichung nennen. Das ist Pflichtinhalt.</p>
<p>Wer diesen Schritt überspringt, baut auf Sand. Er überschreitet seinen statutenmäßigen Wirkungskreis, und das ist einer der Gründe, aus denen die Behörde einen Verein auflösen kann.</p>

<h3>Schritt zwei: verstehen, welche Art von Betrieb entsteht</h3>
<p>Das Abgabenrecht kennt bei gemeinnützigen Vereinen drei Stufen, und der Unterschied ist erheblich.</p>
<p><strong>Der unentbehrliche Hilfsbetrieb</strong> ist ohne den Vereinszweck gar nicht denkbar. Ein Bildungsverein, der Kurse hält, ist das Musterbeispiel. Er ist von der Körperschaftsteuer befreit.</p>
<p><strong>Der entbehrliche Hilfsbetrieb</strong> dient dem Zweck, wäre aber auch ohne ihn möglich. Er ist steuerpflichtig, gefährdet die Begünstigung aber nicht.</p>
<p><strong>Der begünstigungsschädliche Betrieb</strong> geht darüber hinaus. Hier braucht es grundsätzlich eine Ausnahmegenehmigung. § 45a BAO nimmt dem die Schärfe: Übersteigen die Umsätze aus sämtlichen begünstigungsschädlichen Betrieben im Veranlagungszeitraum nicht 100.000 Euro, gilt die Genehmigung als erteilt. Diese Grenze gilt seit 1. Jänner 2024.</p>

<h3>Schritt drei: die drei Grenzen kennen</h3>
<p><strong>Die Gewerbeordnung.</strong> Wirtschaftliche Tätigkeit kann eine Gewerbeberechtigung erfordern, auch für einen Verein. Das wird gern übersehen, weil das Wort Verein nach Privatsache klingt.</p>
<p><strong>Die Umsatzsteuer.</strong> Die Kleinunternehmergrenze liegt seit 2025 bei 55.000 Euro, gemessen am gesamten vereinbarten Entgelt. Wer sie um mehr als zehn Prozent überschreitet, verliert die Befreiung ab dem Umsatz, mit dem sie gerissen wird.</p>
<p><strong>Die Gemeinnützigkeit.</strong> Wer sie hat und wirtschaftlich wächst, muss die 100.000-Euro-Schwelle im Blick behalten. Wer sie nicht hat, hat dieses Problem nicht, zahlt aber Steuern wie jeder andere.</p>

<h3>Schritt vier: rechnen lernen</h3>
<p>Hier scheitern die meisten Vereine, nicht am Recht.</p>
<p>Ein Projekt trägt sich, wenn der <strong>Preis</strong> die Kosten deckt, wenn der <strong>Wert</strong> für den Teilnehmer erkennbar über dem Preis liegt, und wenn ein <strong>Rückfluss</strong> übrig bleibt, der in den Verein zurückgeht.</p>
<p>Fehlt der Rückfluss, arbeitet der Verein für die Aufrechterhaltung seiner selbst. Das hält niemand lange durch. Fehlt der erkennbare Wert, muss man über den Preis verkaufen, und das endet immer gleich.</p>
<p>Der häufigste Fehler ist die Mischkalkulation im Kopf: Man weiß, dass insgesamt etwas übrig bleibt, aber nicht, welches Projekt trägt und welches zehrt. Wer das trennt, sieht innerhalb eines Jahres, wo die Kraft hingeht.</p>

<h3>Schritt fünf: die Menschen bezahlen können</h3>
<p>Ein Verein, der sich trägt, kann Menschen bezahlen. Das ist der Punkt, an dem aus Ehrenamt Verlässlichkeit wird.</p>
<p>Dafür gibt es geordnete Wege: echten Aufwandsersatz, die Freiwilligenpauschale, im Sport die Reiseaufwandsentschädigung, oder einen richtigen Vertrag. Was nicht funktioniert, ist die stille Barzahlung.</p>

<h3>Und der Satz, um den es eigentlich geht</h3>
<p>Ein Verein trägt sich nicht, weil er viele Mitglieder hat. Er trägt sich, weil das, was er tut, für jemanden so wertvoll ist, dass dafür bezahlt wird. Alles andere ist Verwaltung von Knappheit.</p>
 """,
 [("Darf ein gemeinnütziger Verein Gewinne machen?",
   "Ja, solange sie dem begünstigten Zweck zufließen und nicht an Mitglieder ausgeschüttet werden. Die Art des Betriebs entscheidet über die steuerliche Behandlung."),
  ("Braucht ein Verein eine Gewerbeberechtigung?",
   "Möglicherweise ja. Wer wirtschaftlich tätig wird, kann gewerberechtlich erfasst sein, auch als Verein. Das sollte vor dem Start geklärt werden."),
  ("Was passiert über 100.000 Euro Umsatz aus begünstigungsschädlichen Betrieben?",
   "Dann ist eine Ausnahmegenehmigung des Finanzamts erforderlich. Ohne sie steht die Gemeinnützigkeit auf dem Spiel."),
  ("Ist es besser, dafür eine GmbH zu gründen?",
   "Manchmal. Wenn der wirtschaftliche Teil dauerhaft überwiegt oder Anteile veräußerbar sein sollen, ist eine GmbH die passendere Form. Häufig ist auch eine Kombination sinnvoll."),
  ],
 [Q_WKO, Q_BAO45A, Q_USP_KU, Q_GV],
 [("Darf ein Verein Rechnungen schreiben?", "wissen-verein-rechnungen.html"),
  ("Muss ein Verein gemeinnützig sein?", "wissen-verein-gemeinnuetzig.html"),
  ("Wie zahlt ein Verein jemanden aus?", "wissen-verein-auszahlen.html"),
  ("Verein oder GmbH: der ehrliche Vergleich", "wissen-verein-oder-gmbh.html")],
 "Nebenzweckprivileg, Hilfsbetriebe, Gewerbeberechtigung und die Grenzen bei 55.000 und 100.000 Euro: wie ein Verein wirtschaftlich tragfähig wird."
)

print("Die letzten zwei Artikel gebaut.")
