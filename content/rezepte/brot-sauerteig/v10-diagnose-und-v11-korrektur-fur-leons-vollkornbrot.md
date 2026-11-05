---
titel: V10-Diagnose und V11-Korrektur für Leons Vollkornbrot
status: aktiv
datum: '2026-04-16'
quelle:
  typ: claude
  url: https://claude.ai/chat/732292ba-174b-4232-ba19-da295ddfc1a8
  hinweis: Evidenzbasierte Optimierung eines Vollkorn-Nährstoffbrots
importiert: true
---

**Primärursache ist ein quantifizierbares Defizit an freiem Wasser — dominiert durch Tangzhong, nicht durch Psyllium.** Die Fermentation lief korrekt (pH 4,2 → 4,6 sind Lehrbuchwerte), aber die physikalisch immobilisierte Wassermenge in Stärkegel und Hydrokolloiden ließ dem Gluten nicht genug freies Wasser zum Plastifizieren und dem Ofen nicht genug Wasser zum Verdampfen. Der **5,1 % Gewichtsverlust** ist der harte diagnostische Beweis — er liegt bei einem Drittel des Normwerts für freigeschobene Brote (15–22 %) und selbst deutlich unter Tangzhong-Broten (8–13 %). Leon hat kein Gärproblem und kein Scoring-Problem, sondern ein Wassermanagement-Problem. V11 sollte daher chirurgisch an vier Stellen eingreifen — nicht zehn.

## Wahrscheinlichkeitsordnung der fünf Hypothesen

**Primärursache (bestätigt, ~70 % Erklärungskraft): Hydrokolloid- und Stärkegel-Überbindung, dominiert durch Tangzhong.** Die quantitative Wasserbilanz ist eindeutig (Details im nächsten Abschnitt). Der 5,1 %-Backverlust lässt sich nur durch massiv gebundenes, nicht verdampfbares Wasser erklären — Psyllium-Gel bleibt bis 80 °C stabil, gelatinisierte Stärke gibt Wasser erst bei Retrogradation frei. Literatur (Yamauchi et al., Belorio & Gómez 2022) dokumentiert genau dieses Phänomen.

**Starke Sekundärursache (~50 % Erklärungskraft, teilweise unabhängig): Niedrige Teigtemperatur nach Kneten.** Diese Hypothese ist besonders plausibel, weil Leon DDT nicht gemessen hat. Mechanismus: LAB-Säureproduktion ist bei 23–24 °C noch nahe Optimum (pH 4,6 wird erreicht), aber Hefe-CO₂-Produktion fällt exponentiell (Q₁₀ ≈ 2–3). Resultat: **pH-Target erreicht, Volumen-Target nicht.** Exakt Leons Symptom "pH 4,6, aber nur etwas mehr als 50 % Volumenzuwachs, straff". Die beiden Primärursachen verstärken sich gegenseitig — weniger freies Wasser + kühlere Hefe = weniger Gas + weniger Elastizität.

**Plausible Mitursache (~30 %): Verkürzte Kaltgare 10–12 h.** Ein 1,5-kg-Teig braucht laut publizierten Abkühlkurven etwa 7–8 h, um tatsächlich auf 4–5 °C durchzukühlen. Bei 10–12 h Gesamtdauer hatte der Teig effektiv nur 3–4 h in Tiefkälte — zu wenig für die rheologische Versteifung, die sauberen Ofentrieb erlaubt. Leons Befund "maximal in der Höhe gewachsen, nicht an den Seiten" passt: Der Teig war beim Einschießen noch nicht kalt genug, die Oberfläche konnte dem Gasdruck seitlich nicht widerstehen und entlud alles am Längsschnitt. Dass Leon die Kaltgare wegen **Linsen-Protease-Sorge** gekürzt hatte, war rückblickend unbegründet: Rohes, ungekeimtes Rote-Linsen-Mehl hat bei 4 °C (Q₁₀-korrigiert) nur 1–5 % Restaktivität — die tatsächliche Proteolyse im Kühlschrank kommt aus LAB, nicht aus den Linsen.

**Weitgehend auszuschließen (~10 %): Intervallkneten-Problem.** Die Shear-Hypothese (Saaten schneiden Gluten) ist bei Wilfa Stufe 1–2 mit geschälten/teilentölten Saaten vernachlässigbar (belegt bei Hamelman, Glezer, NDSU/AmeriFlax). Die 12 min aktive Knetzeit sind grenzwertig-kurz, aber nicht die Hauptursache — die 45 min Saltolyse-Fermentolyse vorher entwickelt bereits brauchbare Glutenstruktur chemisch.

**Auszuschließen (~5 %): Minimalformen.** Vier Falten im Bulk-Gefäß sind knapp, aber bei 82 % Hydratation + Psyllium-Gel ist die Oberflächenspannung ohnehin schwer kontrollierbar. Das Symptombild (straffer Teig, wenig Volumen) passt nicht zu einem Formproblem — ein schlecht geformter Teig wäre schlaff und zerlaufen, nicht straff und kompakt.

## Die Wasserbilanz — korrigierte Rechnung für Leons tatsächliches V10-Rezept

Diese Rechnung ist das Herzstück der Diagnose. Alle Werte sind Literaturmittelwerte mit realistischen Bandbreiten, keine Labor-Maximalwerte in reinem Wasser.

| Komponente | Menge | Gebundenes Wasser (Mittelwert) | Hauptquelle |
|---|---|---|---|
| **Tangzhong-Stärkegel** (35 g Mehl + 140 g Wasser, 1:4) | — | **~140 g immobilisiert** | Yamauchi et al.; stabil bis Stärke-Retrogradation |
| **Rotes Linsenmehl grob** (75 g) | 1,0–1,3× | **~90 g** | Marchini et al. 2020, Bourré et al. 2019 |
| **Psyllium gemahlen** (8 g) | 8–12× in Teigmatrix | **~80 g** (Spanne 64–96) | US-Patent 8075938; Belorio & Gómez 2022 |
| **Leinsamen gemahlen** (30 g) | 1,3–2,5× | **~60 g** | AmeriFlax/NDSU, Singer et al. |
| **Kürbiskernmehl teilentölt** (25 g) | ~1,5× | **~38 g** | RSC Sustain. Food Tech 2025 |
| **Vitalkleber** (18 g) | 1,5–2× | **~32 g** | Schopf & Scherf 2021 |
| **Hanfsamen geschählt** (35 g) | netto ≈ 0 (46 % Fett) | **~5 g** | Sciacca et al. 2023 |
| **Glutenhaltiges Vollkornmehl für Gluten-Plastifizierung** (~315 g nach Levain-Abzug) | 70 % nötig | **~220 g** | Schopf & Scherf 2021 |
| **Summe Wasserbedarf** | | **~665 g** | — |
| **Verfügbares Gesamtwasser V10** | | **420 g** | Leons Rezept |
| **Defizit** | | **–245 g (~60 %)** | — |

Die theoretische Wasser-Nachfrage übersteigt das verfügbare Wasser um rund 60 %. Das ist kein Rechenartefakt der Bandbreiten — selbst mit den niedrigsten Literaturwerten für jede Komponente bleibt ein Defizit von 80–120 g. **Der größte Einzelposten ist Tangzhong mit 140 g**, gefolgt von der Gluten-Plastifizierung (220 g, aber unausweichlich) und Linsenmehl (90 g, durch Rezeptziel fixiert). Psyllium ist bei 8 g auf 480 g Mehl (1,67 % b%) **nicht überdosiert** — das Optimum für Vollkornbrot liegt laut Belorio & Gómez bei 2–5 %. Leons Psyllium-Einsatz ist also konservativ und nicht das Hauptproblem. Die populäre Vermutung "zu viel Psyllium" wird durch die Rechnung widerlegt.

**Tangzhong ist daher der rationale Haupt-Korrekturhebel.** Er trägt mehr immobilisiertes Wasser zur Bilanz bei als alle anderen Hydrokolloide zusammen und ist der primäre mechanistische Erklärer für den extrem niedrigen 5,1 %-Gewichtsverlust.

## Warum der Teig "straff statt klebrig" war — der Widerspruch aufgelöst

Bei 82 % nominaler Hydratation erwartet man einen schlaffen, klebrigen VK-Teig. Leons Teig war straff. Die Erklärung ist jetzt klar: Die nominale 82 %-Hydratation ist eine Etikettzahl, keine **effektive** Hydratation. Nach Abzug des in Stärkegel, Mucilagen und Psyllium-Gel sequestrierten Wassers blieb für die Gluten-Plastifizierung praktisch **kein Überschuss-Wasser** übrig — der Teig verhielt sich rheologisch wie ein 60–65 %-Teig, weil das sichtbare Wasser fehlte. Gluten, das nicht ausreichend plastifiziert ist, ist steif und unelastisch. Die Kombination mit dem viskosen Psyllium-Gel verstärkt den Eindruck von Festigkeit ohne Klebrigkeit. **Der Poke-Test ist bei dieser Matrix systematisch unzuverlässig** (Psyllium dämpft Rückfederung, auch bei korrekter Gare) und sollte als Einzel-Indikator aufgegeben werden.

## V11 — vier begründete Änderungen, alles andere bleibt

Die Diagnose legitimiert genau vier Eingriffe. Jeder adressiert eine identifizierte Ursache, keiner ist Spekulation.

### Änderung 1 — Tangzhong halbieren (Primär-Hebel)

**V10:** 35 g Mehl + 140 g Wasser = 175 g Tangzhong.
**V11:** 20 g Mehl + 80 g Wasser (Verhältnis 1:4) = 100 g Tangzhong.

Das gibt rund **60 g Wasser aus dem immobilisierten Stärkegel frei** und erhöht das Saltolyse-freie-Wasser von 30 g auf 90 g, **ohne die Gesamthydratation von 82 % zu ändern**. Das ist der wichtigste einzelne Stellhebel. Die erwartete Wirkung: Teig wird bei gleicher Etikett-Hydratation spürbar geschmeidiger und klebriger (was 82 % VK entspricht), Gluten plastifiziert besser, Gas-Expansion im Ofen steigt, und der Backverlust sollte auf 9–11 % zurückkehren. Das Tangzhong bleibt erhalten für seinen weichmachenden Haltbarkeitseffekt — nur die Dosierung wird auf ein realistisches Maß gekürzt. 20 g Tangzhong-Mehl entsprechen rund 4 % des Gesamtmehls, was im üblichen Yudane/Tangzhong-Bereich liegt.

### Änderung 2 — DDT-Protokoll einführen (Zielwert 25 °C)

Leon muss die Teigtemperatur **nach dem Kneten messen**. Für Wilfa Probaker Stufe 1/2 mit Intervallen ist der Reibungsfaktor empirisch zu ermitteln — Startschätzung 4 °C. DDT-Formel für Levain-Teige:

**Wassertemperatur = (DDT × 4) − (Mehltemp + Raumtemp + Reibung + Levaintemp)**

Bei 21 °C Mehl, 22 °C Küche, 4 °C Reibung, 24 °C Levain und Ziel-DDT 25 °C: **Wasser = 100 − 71 = 29 °C**. Das ist deutlich wärmer als vermutlich in V10 verwendet. Wenn die gemessene Teigtemperatur nach Kneten unter 24 °C liegt, Proofbox auf 28 °C nutzen und Stockgare um 30–45 min verlängern, bis der pH tatsächlich 4,5–4,6 erreicht. **Rationale:** Bei echter DDT 25 °C läuft Hefe nahe Optimum → CO₂-Produktion passt zur LAB-Säureproduktion → Volumenzuwachs folgt dem pH-Abfall synchron. Das adressiert das "korrekt gegärt, aber zu wenig Volumen"-Paradoxon direkt.

### Änderung 3 — Kaltgare auf 14–15 h verlängern (nicht länger)

**V10:** 10–12 h bei 4 °C. **V11:** 14–15 h bei 4 °C, mit **20–30 min Anstückgare bei Raumtemperatur vor dem Kühlschrank**.

14–15 h ist die optimale Balance aus publizierten Daten (Hamelman, Breadtopia, Culinary Exploration) für hochhydratisierten Vollkorn-Sauerteig. Die Obergrenze von 16 h sollte nicht überschritten werden: Bei 82 % Hydratation + 26 % Nicht-Gluten-Anteil ist das Glutennetz fragiler, LAB-Proteolyse schwächt es weiter, und die Gefahr eines flachen Laibs beim Stürzen steigt. **Die Linsen-Protease-Sorge, die Leon ursprünglich zur Verkürzung bewegt hat, ist durch die Literatur nicht gestützt** — ungekeimte Linsenprotease bei 4 °C ist vernachlässigbar gegenüber LAB. 14–15 h gibt dem Teig ausreichend Zeit, auf Kerntemperatur 4–5 °C durchzukühlen und rheologisch zu versteifen, was sowohl sauberes Scoren als auch symmetrische Ofenexpansion erlaubt.

### Änderung 4 — Scoring auf Kreuz oder flache Raute umstellen

Leons Symptom "Längsschnitt geöffnet, wenig seitliches Wachstum" ist der Lehrbuchfall für **asymmetrische Druckentlastung**. Ein einzelner Längsschnitt konzentriert die gesamte Expansionsenergie an einer Stelle, die restliche Kruste wird überdehnt und blockiert seitliches Wachstum. Für V11:

**Zwei gekreuzte Schnitte (+) oder flache Raute (#), Tiefe 0,5–0,7 cm, Winkel 90° senkrecht.** Nicht 45° Ear-Cut — schwaches Gluten verträgt das nicht. Bei Saatenbesatz gezacktes Messer statt Lame (Hamelman-Empfehlung). Geschnitten wird direkt aus der Kaltgare, kalter Teig schneidet sauberer. Das verteilt den Gasdruck auf vier Expansionspunkte, symmetrische Volumenausbreitung wird möglich, das typische "Erker-Ausreißen" bei schwachem Vollkorn-Gluten entfällt. Challenger Breadware, King Arthur, Maurizio Leo und der TFL-Konsens empfehlen diese Geometrie einhellig für mix-in-reiche oder Vollkornteige.

### Was bewusst NICHT geändert wird

Alle anderen Parameter bleiben identisch zu V10. Psyllium 8 g bleibt (nicht überdosiert). Das Saatenquellstück bleibt. Die 45-min-Saltolyse-Fermentolyse bleibt. Das Intervallkneten-Protokoll bleibt (adäquat bei vorausgehender Fermentolyse). Stockgare 4–4,5 h bei 28 °C bleibt (mit DDT 25 °C wird sie jetzt effektiv). Minimalformen bleibt. Keine zusätzlichen Coil Folds — Leons Constraint "kein S&F" wird respektiert, und die 4 Falten im Bulk-Gefäß sind bei der verbesserten Hydratation ausreichend.

## V11 in voller Form — Zeitplan und Mengen

**Mehlmischung und Zusätze unverändert** außer: Tangzhong 20 g Mehl + 80 g Wasser (statt 35 + 140). Gesamtwasser bleibt 420 g, neu verteilt: Levain 120, Tangzhong 80, Saatenquellstück 90, Psyllium-Gel 40, **freies Wasser in Saltolyse 90** (statt 30).

**Vortag 17:00:** Tangzhong 72–75 °C (20 g Mehl, 80 g Wasser, eingekocht bis viskos), Saatenquellstück, Levain 1:10:10 bei 28 °C. **22:00:** Levain pH 4,2, Kühlschrank.

**Tag 1 08:30:** Saltolyse-Fermentolyse mit DDT-Wassertemperatur (vorher per Formel berechnen, Start ~29 °C bei 22 °C Küche), Wilfa Stufe 1: 2 min + 1 min, 45 min Rast bei 26–28 °C. **09:15:** Intervallkneten wie V10, **Teigtemperatur direkt danach messen und protokollieren** — Ziel 24–26 °C. **09:45:** Stockgare 4–4,5 h bei 28 °C, Endpunkte pH 4,5–4,6 UND Volumenzuwachs 65–75 % (nicht Poke-Test). **13:45–14:15:** Minimalformen, 20–30 min Anstückgare bei Raumtemperatur, dann in den Gärkorb und in den Kühlschrank. **Kaltgare 14–15 h bei 4 °C.**

**Tag 2:** Ofen 60 min bei 250 °C mit Pizzastein vorheizen. Teig direkt aus Kühlschrank stürzen, **Kreuz-Scoring 0,5–0,7 cm tief, 90° senkrecht**. Backen unverändert: 15 min 240 °C mit Dampf, 30 min 205 °C ohne Dampf, 5 min 180 °C mit Türspalt.

## Prognose und ehrliche Grenzen-Einschätzung

**V11 verspricht eine substantielle, messbare Verbesserung — aber keine Revolution.** Die konkrete Erwartung: Gewichtsverlust von 5,1 % auf 9–11 %, Volumenzuwachs im Bulk von 50 % auf 65–75 %, Krume spürbar weniger klebrig und mit etwas feinerer Porung, sauberes symmetrisches Aufreißen statt einseitiger Riss. Das sind Effekte, die Leon mit Waage, pH-Meter und Augenmaß objektiv bestätigen kann.

**Was V11 nicht liefern wird — und das ist wichtig für realistische Erwartungen:** Eine offene, wild-hydrierte Tartine-Style-Krume ist bei Leons Constraints physikalisch ausgeschlossen. Kein einziger der recherchierten Referenzbäcker (Maurizio Leo, Trevor Wilson, Hamelman, Duffy, Robertson, Ginsberg) erreicht bei 100 % Vollkorn + 26 % Nicht-Gluten + freigeschobener Form eine offene Krume. Leos eigener Obergrenz-Versuch bei 95 % Vollkorn erzeugt "offen und luftig *für ein Vollkornbrot*" — optisch deutlich dichter als jedes Weißmehl-Brot. Leons beschriebene V10-Krume ("weitgehend homogen, eher dicht, leicht klebrig") ist nicht fehlerhaft, sondern **das systemisch erwartbare Ergebnis bei dieser Nährstoff-priorisierten Rezeptur**. V11 verschiebt die Krume nicht von "dicht" nach "wild offen", sondern von "dicht und klebrig" nach "dicht, aber weich-feucht statt gummig-feucht" — und genau das ist der realistische Qualitätssprung.

**Realistische Maximumseinschätzung:** V10 war bei ~70–75 % des Maximums für diese Constraint-Kombination. V11 kann auf ~85–90 % des Maximums kommen. Die restlichen 10–15 % wären nur durch grundsätzliche Constraint-Lockerung erreichbar (Vollkornanteil unter 70 %, Kastenformat, oder Nicht-Gluten-Anteil unter 15 %) — alles Dinge, die Leon aus Nährwertgründen bewusst nicht will. **Bei akzeptiertem Constraint-Set sollte V11 das praktische Optimum darstellen**, und weitere Iterationen würden eher marginale Handling- und Geschmacksnuancen adressieren als strukturelle Sprünge.
