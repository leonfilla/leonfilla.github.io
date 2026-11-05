---
titel: Brotrezept-Vergleich und Optimierung
datum: '2026-10-12'
quelle:
  typ: claude
  url: https://claude.ai/chat/34bc62c3-614d-483a-aab8-bd4252524cb8
  hinweis: Brotrezept-Vergleich und Optimierung
importiert: true
---

Es gibt kein drittes Dokument: weder hier noch in deinem Drive-Ordner, dort liegen nur V18.1 und V19. Als dritten Vergleichspunkt nehme ich deshalb eine aus der Recherche abgeleitete **V20-Synthese**. Die Temperatur- und Enzymbilanzen habe ich nachgerechnet, statt sie aus den Dokumenten zu übernehmen.

## 1. Was sich tatsächlich unterscheidet

Die Formel ist in beiden Versionen identisch. Bei zwei Laiben sind es jeweils 550 g Weizen, 740 g Wasser im Hauptteig, 200 g Levain, VWG 40 g, Psyllium 10 g, Salz 20 g. V19 ist also eine reine Prozessänderung. Allerdings ändert V19 **fünf Prozessvariablen gleichzeitig**:
- Phytase-Phase
- Salzzeitpunkt
- Weizenaufteilung
- Wegfall der Saltolyse
- Levain-Trigger

Sieht V19 anders aus als V18.1, kannst du das Ergebnis keiner einzelnen Ursache zuordnen.

| Bereich | V18.1 | V19 | V20-Synthese |
|---|---|---|---|
| Phytase-Phase | 45 min bei 45 °C, pH ~6 | Quellstück 45 → 21 °C über Nacht, pH ~6 | wie V19, aber mit Milchsäure auf pH ~5,3–5,5 angesäuert |
| Steuerung | zwei gekoppelte Uhren (Gate + Δ-Vorhersage) | ein Trigger, das Quellstück puffert | wie V19, zusätzlich Quellstück-pH und -Alter protokollieren |
| Termingebundene Eingriffe morgens | 5 innerhalb von 1:45 h | 1 | 1 |
| Gluten-Schutz | alles im warmen Soak | 200 g Weizen + VWG frisch | wie V19 |
| Psyllium | Saltolyse (hydratisiert vor dem Kneten) | trocken in den Morgen-Mix | Testkandidat: ins Quellstück |
| Backprofil | Standard oder hell | nur hell | nur hell |

## 2. Prozessoptimierung

Der eigentliche Gewinn von V19 sind nicht die 6 eingesparten Minuten (42 → 36). V19 löst ein **Koordinationsproblem**. V18.1 ist eine Vorsteuerung: Du musst den Levain-Peak etwa 1,5–2 h im Voraus vorhersagen, und das Δ ist chargenabhängig. V19 macht das Quellstück zum wartetoleranten Puffer. Damit gibt es nur noch eine Führungsgröße, die Levain-Reife. Weniger gekoppelte Zeitpunkte bedeuten weniger Streuung, und das spricht klar für V19.

Der Preis ist eine **neue, unprotokollierte Störgröße**: das Alter des Quellstücks. Peakt der Levain um 08:30 statt um 10:30, ändert sich die Enzymdosis. Das Protokoll von V19 erfasst das nicht. Zwei Felder kosten fast nichts: Quellstück-Alter in Stunden und Quellstück-pH am Morgen. Der pH-Wert ist dabei der eigentliche Frühindikator für Spontangärung, informativer als der Geruch.

Die Temperaturrechnungen in V19 stimmen. Bei vorgewärmter Schüssel landet das Quellstück bei 45,6 °C, bei kalter Schüssel bei 42,4 °C. Für das Morgen-Wasser gilt bei 21 °C Küche und 27 °C Zielteig 60 °C. Die Empfindlichkeit beträgt 0,153 °C Teig pro °C Wasser, das bestätigt die Faustregel 1 : 6,5. Vor der Levain-Zugabe hat die Masse 28,3 °C. Die Annahme „Reibung ≈ Verluste“ ist auch mit den V18.1-Daten konsistent.

Drei Randfälle passen nicht ganz:
- **Einzelbrot mit kalter Schüssel:** Das Quellstück landet bei ca. 40 °C, nicht bei 42 °C. Die Stahlschüssel wiegt relativ zur kleineren Masse schwerer. Beim Einzelbrot ist Vorwärmen deshalb Pflicht.
- **Küche bei 19 °C:** Rechnerisch braucht es 71 °C Wasser. Das liegt über deiner eigenen 60-°C-Logik und führt zu lokaler Verkleisterung am Kontaktpunkt. Ich würde bei ca. 65 °C deckeln und lieber 26 °C Teigtemperatur akzeptieren.
- **Sommerregel:** Ein späterer Ansatz ist richtig, verschiebt aber das Quellstück-Alter (siehe oben).

## 3. Ergebnis: Nährwert (Phytat, deine Priorität 1)

Die Literatur bestätigt die Grundannahme. Optimal arbeitet die Phytase bei pH 5,0–5,5 und 50–55 °C.

Die Begründung in V19 ist aber an einer Stelle **überzogen**. Die Schwäche des V18.1-Soaks war nicht der pH, sondern die Dauer. Bei pH 6,5 behält Weizenphytase noch etwa 90 % (bei 55 °C) bzw. 80 % (bei 30 °C) ihrer Maximalaktivität. Bei pH ~6 ist sie also kaum gebremst.

Entscheidend ist die Temperatur. Bei 30 °C liegt die Aktivität zehnmal niedriger als bei 55 °C, während eine ältere Arbeit zwischen 15 und 50 °C einen annähernd gleichmäßigen Anstieg der Hydrolyserate fand. Mit beiden Modellen habe ich die Enzymstunden integriert, gemessen in Optimum-Äquivalent-Stunden. Für die Abkühlung des Quellstücks habe ich eine exponentielle Kurve mit τ = 1,5–4 h angenommen:

| | Q10-Modell (Leenhardt-Anker) | lineares Modell (Hill & Tyler) |
|---|---|---|
| V18.1 (Soak + Abkühlen + Saltolyse) | 0,37 | 0,79 |
| V19 (Quellstück, 13,5 h) | 0,76–1,16 | 2,5–3,7 |

Damit gewinnt V19 robust um etwa den Faktor 2–4, die Kernaussage hält. Im konservativen Modell fällt aber **knapp die Hälfte der V19-Enzymarbeit in die ersten 3 h**, solange das Quellstück noch warm ist. Der 45-°C-Start trägt also die Last: eine kalte Schüssel oder ein später Ansatz kosten überproportional.

Die zweite Behauptung, „die meiste Phytase-Arbeit leistet die Stockgare“, ist **modellabhängig**. Mit dem Leenhardt-Anker liefern 5 h bei ca. 24 °C nur etwa 0,3 Äquivalent-Stunden. Das entspricht dem alten Soak und ist nicht dominant.

Was die Säure tatsächlich bewirkt, zeigt Leenhardt 2005. Schon eine leichte Ansäuerung auf pH 5,5, durch Sauerteig oder durch Milchsäure, baute 70 % des Phytats ab, ohne Ansäuerung waren es 40 %. Das ist der stärkste verbleibende Nährwert-Hebel, und er passt genau in die V19-Architektur. Salz im Quellstück schadet der Phytase vermutlich nicht. In einer Arbeit zeigten salzreichere Teige sogar höhere Phytaseaktivität, das ist allerdings nur eine schwache Quelle (Abschlussarbeit). Dass Roggen im Quellstück bleibt, ist richtig: Roggen hatte fast die dreifache Phytaseaktivität von Weizen.

**Methodischer Punkt:** Phytat kannst du zu Hause nicht messen. Diesen Parameter solltest du deshalb nach Literatur entscheiden und dein Testbudget (ein Backtag pro Variable) für das ausgeben, was du am Laib beurteilen kannst.

## 4. Ergebnis: Gluten, Volumen, Krume

Hier zeigen die Effekte in **entgegengesetzte Richtungen**, das Vorzeichen für V19 ist offen.

**Für V19 spricht die Kleie-Vorhydratisierung.** Cai et al. (2015, *Cereal Chemistry*) fanden bei Vollkornweizen mit vorhydratisierter Kleie (60 % Feuchte) größere Laibvolumen und eine weichere Krume, auch nach 7 Tagen Lagerung. Dein „Fenster steht schon nach Block 2“ ist die direkte Folge davon.

**Gegen V19 spricht die Protease über Nacht.** Das Bild beim Keimweizen ist zweischneidig: Das Gluten wird schwächer, die Dehnbarkeit steigt aber, was zu Broten mit hohem spezifischem Volumen führen kann. Bei zu viel Protease kippt das jedoch. Hohe Proteaseaktivität ergab ein aufgetriebenes Volumen mit schlechter Krumenstruktur, zu viel α-Amylase klebrige Teige.

Zum „Gluten-Schutz“ von V19, quantifiziert: Morgens frisch dazu kommen etwa 28 g Protein aus 200 g Weizen und etwa 30 g aus 40 g VWG, zusammen ca. 58 g. Über Nacht im Quellstück liegen etwa 48 g aus 350 g Weizen plus das Keimmehl-Protein. Also ist ungefähr die Hälfte des funktionellen Glutens geschützt, und zwar die mit der besten Qualität (VWG). Das ist ein gut gewählter Kompromiss.

Ein Risiko sehe ich im Wasserhaushalt beim Kneten. Morgens brauchen 200 g Mehl, 40 g VWG und 10 g Psyllium grob 300+ g Wasser. Frei verfügbar sind aber nur 200 g plus 100 g aus dem Levain, weil Chia und Kleie im Quellstück ihr Wasser schon gebunden haben. Psyllium konkurriert dabei am schnellsten um freies Wasser, also genau mit dem VWG, das sich während des Knetens entwickeln soll. Das ist dasselbe Muster wie dein Tangzhong/Psyllium-Befund aus V11.

Meine Vorhersage: Der Teig fühlt sich beim Mix fester an und erschlafft während der Stockgare. **Die Hydratation solltest du deshalb erst nach dem ersten Coil Fold beurteilen**, nicht am Mischende. Als Hypothese für V20: Psyllium ins Quellstück verlegen, damit das VWG morgens das freie Wasser bekommt.

## 5. Kruste, Geschmack, Mikrobiologie

**Kruste:** Mehr Enzymstunden bedeuten mehr Maltose. Das gibt mehr Bräunung und Aroma und vermutlich eine schnellere Stockgare, weil mehr Gärsubstrat da ist. Dass V19 das helle Profil festschreibt, ist konsequent. Der Verlust der Wahlfreiheit ist hier kein echter Verlust.

**Mikrobiologie:** Das ist der unterbelichtete Punkt. Ein nasses, unangesäuertes Vollkorn-Quellstück mit pH ~6, das langsam von 45 °C abkühlt, ist ein gutes Inkubationsmilieu für die Spontanflora des Mehls. In der Praxis werden gesalzene Quellstücke bei Raumtemperatur lange geführt. Reinhart beschreibt, dass Salz die Enzymaktivität so weit dämpft, dass das Quellstück bei Raumtemperatur statt im Kühlschrank stehen kann. Allerdings starten diese Quellstücke kalt, nicht bei 45 °C.

Bacillus-Sporen überleben das Backen (Bakerpedia). Als Gegenmaßnahme gilt eine Krumen-pH von höchstens 5,4. Dein fertiger Teig liegt weit darunter, Fadenziehen im Brot ist also praktisch kein Thema. Das Risiko liegt im Quellstück selbst: Fehlaromen und mikrobielle Protease, ein zweiter möglicher Grund für „Teig schlaffer“. Die Ansäuerung auf pH ~5,5 löst Nährwert- und Sicherheitsfrage mit einem Eingriff.

## 6. Korrekturliste zu den Dokumenten

1. **„pH 6 weit weg vom Optimum“:** überzogen, die Aktivität liegt dort noch bei ca. 80–90 %. Der richtige Grund für das Quellstück sind die Enzymstunden.
2. **„Die meiste Phytase-Arbeit leistet die Stockgare“:** modellabhängig und mit dem Leenhardt-Anker nicht haltbar.
3. **Test 3 „mit Puffer-Levain ansäuern“ ist logisch nicht ausführbar.** Um 20:00 existiert der Puffer-Levain noch nicht, er entsteht erst morgens. Abends verfügbar sind nur die ca. 11 g ASG-Rest (35 − 24 g). Die sinnvolle Variante ist Milchsäure: deterministisch, ohne Mikroben, einmal mit dem Apera an einer Teilprobe titrieren.
4. **Einzelbrot mit kalter Schüssel:** ca. 40 °C statt 42 °C.
5. **Küche bei 19 °C:** 71 °C Wasser überschreitet die eigene Obergrenze.
6. **V19 ist kein Einvariablen-Test.** Das ist akzeptabel, aber beim Auswerten bewusst halten.

Ein Zielkonflikt fehlt in beiden Dokumenten: Die Gegenmaßnahme in V19 („Keimmehl in den Morgen-Mix“) kostet Phytase. Laut einer Arbeit stieg die Weizenphytase durch Keimung um das 5,4-Fache. Zugleich ist Keimmehl die Protease-Quelle. Ansäuerung und Keimmehl-Position solltest du deshalb nicht im selben Backen ändern.

## 7. Gesamturteil und V20 als Testreihenfolge

- **Prozess:** V19 dominiert V18.1 klar.
- **Nährwert:** V19 ist wahrscheinlich 2–4× besser in der Enzymphase, mit Ansäuerung deutlich mehr.
- **Volumen:** Das Vorzeichen ist offen (Kleie-Hydratation + gegen Protease −).
- **Kruste:** dunkler, wird über das helle Profil beherrscht.

V20 ist daher eher eine Reihenfolge als ein fertiges Rezept:
1. **V19 einmal unverändert backen.** Das ist die Baseline. Zusätzlich Quellstück-Alter und Quellstück-pH notieren, Hydratation erst nach dem ersten Fold beurteilen.
2. **Quellstück mit Milchsäure auf pH ~5,3–5,5 ansäuern** (vorher titrieren). Größter Nährwert-Hebel, zugleich Sicherheitsgewinn. Achtung: Der Start-pH im Teig sinkt, die Stockgare deshalb an diesem Tag nach Volumen beenden.
3. Erst wenn Schritt 2 den Teig schlaffer macht: **Keimmehl in den Morgen-Mix** oder auf 5 %.
4. **Psyllium ins Quellstück** als eigener Test. Dafür eignet sich der Fold-Split-Test aus V19 nicht, das braucht einen eigenen Backtag.

Soll ich daraus ein V20-Dokument im gewohnten Format bauen, mit Titrationsprotokoll für die Milchsäure und erweitertem Mitback-Protokoll?

Sources:
- [Fretzdorff & Brümmer 1992, Cereal Chemistry 69:266](https://www.cerealsgrains.org/publications/cc/backissues/1992/Documents/69_266.pdf)
- [Hill & Tyler 1954, J. Agric. Sci.](https://www.cambridge.org/core/journals/journal-of-agricultural-science/article/abs/influence-of-time-temperature-ph-and-calcium-carbonate-on-the-activity-of-the-phytase-of-certain-cereals/15C1024F04648294EB055E380FD65B5D)
- [BRENDA: Leenhardt et al. 2005, Enzymdaten](https://www.brenda-enzymes.org/literature.php?r=665280)
- [Leenhardt et al. 2005, HAL INRAE](https://hal.inrae.fr/hal-02681688)
- [Abdel-Gawad et al. 2008, Phytase und Keimung](https://www.aun.edu.eg/agriculture/characterization-phytases-cereal-grains-affected-soaking-and-germination-processes-and-some-1)
- [Phytase und Salz (Abschlussarbeit IUT)](https://library.iut.ac.ir/inventory/107/3028.htm)
- [Cardone et al., Keimweizen und Gluten](https://air.unimi.it/handle/2434/644300)
- [Lorenz et al. 1983, Cereal Chemistry 60:360](https://cerealsgrains.org/publications/cc/backissues/1983/Documents/CC1983a124.html)
- [Cai et al. 2015, Bran hydration, Cereal Chemistry 92(6)](https://pure.jbnu.ac.kr/en/publications/bran-hydration-and-physical-treatments-improve-the-bread-baking-q/)
- [The Fresh Loaf: Reinhart-Quellstück mit Salz](https://www.thefreshloaf.com/comment/441356)
- [Bakerpedia: Rope Spoilage](https://bakerpedia.com/?p=20489)
