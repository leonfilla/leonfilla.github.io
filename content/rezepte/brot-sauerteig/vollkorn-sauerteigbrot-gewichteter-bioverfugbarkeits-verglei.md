---
titel: Vollkorn-Sauerteigbrot — Gewichteter Bioverfügbarkeits-Vergleich (V8/V9/V12) & Synthese V13
status: aktiv
datum: '2026-05-21'
quelle:
  typ: claude
  url: https://claude.ai/chat/1f1baaf8-2a5f-4084-89e7-3cc6e33c3012
  hinweis: Neues Brotrezept nach Anforderungen
importiert: true
---

*Bewertet nach der Zielhierarchie der Anforderungen: Nährwert (Mineral-Bioverfügbarkeit, GI, Präbiotika) > Sensorik (offene Krume, knusprige Kruste, mild, glatter Biss) > Reproduzierbarkeit > Arbeitsökonomie. Proteinqualität explizit irrelevant (Milchbeläge decken Lysin).*

---

## Teil 1 — Bewertungsrahmen

Die Frage lautet ausdrücklich: **Konzentration *bioverfügbarer*, evidenzbasiert gesundheitsförderlicher Stoffe.** „Bioverfügbar" ist der entscheidende Zusatz. Für Mineralstoffe gilt:

> **Netto-absorbierbarer Mineralstoff = Gehalt × Absorptionsanteil**, und der Absorptionsanteil wird durch das **Phytat:Mineral-Molverhältnis** gesteuert, nicht durch den Gehalt allein.

Schwellen (Hurrell & Egli 2010; Gibson & Ferguson 1998; Lönnerdal 2002; IZiNCG/Brown 2004):

| Verhältnis | gut | mittel | schlecht |
|---|---|---|---|
| Phytat : Eisen (molar) | < 1 (ideal 0,4) | 1–14 | > 14 |
| Phytat : Zink (molar) | < 5 (≈ 50 % Absorption) | 5–15 (≈ 30 %) | > 15 (≈ 15 %) |

Gewichtung der Nährwertkategorien (aus der Anforderungshierarchie abgeleitet):

| Kategorie | Gewicht | Begründung |
|---|---|---|
| Bioverfügbare Mineralien (Fe, Zn, Mg) | 35 % | oberste genannte Priorität, „bioverfügbar" betont |
| Glykämische Qualität (GI-Senkung) | 25 % | explizit genannt |
| Präbiotika / fermentierbare Faser | 20 % | explizit genannt |
| Polyphenole / weitere Mikronährstoffe | 10 % | evidenzbasiert gesundheitsförderlich |
| Omega-3 (ALA) | 5 % | gesundheitsförderlich, aber nicht priorisiert; schwache ALA→EPA/DHA-Konversion, Backoxidation |
| Proteinqualität / -menge | 0 % | laut Kontext irrelevant (Milchbelag) — nur zur Illustration der Fehlallokation gezeigt |

---

## Teil 2 — Gewichteter Vergleich V8 / V9 / V12

### 2.1 Phytatbilanz (Modell, kein Laborwert)

Annahmen Phytatgehalt (mg/g): Weizen-VK 7 · Roggen-VK 6 · Hafer-VK 7 · Einkorn 7 · Linsenmehl 10 · Kürbiskernmehl (entölt) 26 · Hanf 22 · Lein 28. Quellen: García-Estepa 1999 (Getreide); Phytic acid content of three legumes 1994 (Linse 0,86–1,5 % = 8,6–15 mg/g); El-Adawy/Taha & Mansour (entöltes Kürbismehl 23,7 / 30,1 mg/g); Galasso 2016 (Hanf ~22 mg/g); Oomah 1996 (Lein 23–33 mg/g).

| Rezept | Roh-Phytat (≈ mg/Laib) | geschätzter Abbau | Rest-Phytat (≈ mg) |
|---|---|---|---|
| **V8** | ~5.200 | ~68 % (10 % Roggen, Sauerteig, Kühlretard, **kein Warmschritt**) | **~1.560** |
| **V12** | ~6.400 (höchste Last) | ~72 % (23 % Roggen, Sauerteig pH 4,3–4,5; Saltolyse phytat-neutral, **kein Warmschritt**; Tangzhong-Fraktion phytasetot) | **~1.790** |
| **V9** | ~4.000 (niedrigste Last) | ~87 % (15 % Roggen + **45 °C salzfreier Phytase-Soak** + Sauerteig pH 4,6) | **~500** |

Kernpunkt: V12 hat die **höchste** Restphytatlast — mehr Roggenphytase, aber noch mehr Substrat (Linse/Kürbis/Lein/Hanf, deren Eigenphytase vernachlässigbar ist) und kein Warm-Aktivierungsschritt. V9 hat trotz weniger Roggen die **niedrigste** Restphytatlast, weil es Substrat minimiert *und* einen dedizierten Phytaseschritt fährt.

### 2.2 Mineralgehalt vs. Netto-absorbierbar (Modell)

| | Fe-Gehalt | Zn-Gehalt | Phytat:Fe | Phytat:Zn | Zn-Absorption | **absorb. Zn** |
|---|---|---|---|---|---|---|
| **V12** | ~30 mg | ~23 mg | ~5,1 | ~7,8 (mittel) | ~30 % | **~6,9 mg** |
| **V9** | ~19 mg | ~16 mg | ~2,2 | ~3,1 (hoch) | ~50 % | **~8,0 mg** |

**Das ist das zentrale, kontraintuitive Ergebnis:** V12 hat ~30 % mehr Zinkgehalt, liefert aber **weniger** absorbierbares Zink als V9, weil ein großer Teil seines Zinks phytatgebunden bleibt. Beim Eisen sind beide unter der Idealschwelle (PA:Fe < 1 nicht erreicht), aber V9 (~2,2) ist weniger als halb so gehemmt wie V12 (~5,1) — ein Vitamin-C-haltiger Belag (Enhancer) wirkt bei V9 entsprechend stärker. Die Zusatzmineralien aus Linse und Kürbiskern in V12 sind weitgehend „Gehalts-Theater": vorhanden, aber nicht resorbierbar.

> Alle Zahlen sind Modellschätzungen mit großen Fehlerbalken (Literatur-Phytat/Mineralwerte × geschätzter Abbau × Molverhältnis-Algorithmus). Die **Richtung** ist robust; die Absolutwerte sind nicht laborvaliert.

### 2.3 Übrige Kategorien

- **GI-Senkung:** V12 ≥ V9 > V8. Sauerteig ist bei allen der dominante Hebel (estimated GI ~53–55). V12 addiert Hafer-β-Glucan (EFSA-anerkannte postprandiale Glukosesenkung über Viskosität), Psyllium und Leinmucilage. **Wichtige Ehrlichkeit:** bei üblicher Scheibengröße erreicht kein Brot die EFSA-Wirkdosis (2–3 g β-Glucan pro 30 g verfügbare KH) — β-Glucan ist additiv, nicht der Haupthebel. V8 wird durch Melasse (freier Zucker) leicht abgewertet.
- **Präbiotika / fermentierbare Faser:** V12 > V9 ≈ V8. V12 bringt die meiste Arabinoxylan-/β-Glucan-Breite (23 % Roggen, Hafer, Psyllium, Lein, Kleie). V9 solide (15 % Roggen-AX, Kleie, resistente Stärke).
- **Polyphenole/Mikros:** V12 ≥ V8 > V9 (Kleie-Ferulasäure überall; Lein-Lignane V8/V12; Einkorn-Carotinoide V12). Geringes Gewicht.
- **Omega-3 ALA:** V12 (~9,5 g/Laib) >> V8 > V9 (~gering, nur Hanf). Geringes Gewicht; schlechte Konversion, Backoxidation.
- **Proteinqualität (Gewicht 0):** V12 >> V8 > V9 — zeigt, wohin V12 seine größten Strukturkompromisse investiert (15 % Linse → Glutenverdünnung), für einen hier wertlosen Nutzen.

### 2.4 Gewichtete Nährwert-Wertung (0–10 je Kategorie × Gewicht)

| Kategorie (Gewicht) | V8 | V9 | V12 |
|---|---|---|---|
| Bioverf. Mineralien (35 %) | 5 | **9** | 6 |
| GI (25 %) | 6 | 7 | **8** |
| Präbiotika (20 %) | 6 | 7 | **9** |
| Polyphenole (10 %) | 7 | 6 | **8** |
| Omega-3 (5 %) | 7 | 3 | **9** |
| **Gewichtet** | **5,50** | **7,05** | **7,15** |

**Verdikt:** Auf der reinen Nährwertachse liegen V9 und V12 praktisch gleichauf (7,05 vs. 7,15) — V12 minimal vorn durch Breite (Präbiotika, Omega-3), V9 vorn in der höchstgewichteten Einzelkategorie (bioverfügbare Mineralien). **V8 fällt klar ab** (Melasse, Hefeflocken, wenig Roggen, schwächste Phytatstrategie).

Sobald man die **gesamte** Hierarchie einbezieht, dreht es zugunsten der schlanken Linie: V12 erkauft seine Nährwertbreite mit Verstößen gegen Ziel #2 (Tangzhong + Psyllium + 53 % Nicht-Weizen → dichtere, weichere Krume, weniger knusprige Kruste — also gegen offene Krume *und* knusprige Kruste) und gegen Ziel #4 (mehrere Quellstücke, Tangzhong-Kochen → mehr Aktivzeit). V9 erfüllt Sensorik und Arbeitsökonomie deutlich besser.

**Die ideale Synthese (V13)** holt V12s *echte* Gewinne (Hafer-β-Glucan, Roggen-AX, die akribischen pH-/Temperatur-Endpunkte, die kontaktarme Wet-Scraper-Coil-Fold-Technik, das 4-Phasen-Dampfprofil) **ohne** seine Bioverfügbarkeits- und Sensorikfehler — und stellt V9s Phytase-Soak wieder her. Dazu ein *neuer* Bioverfügbarkeitshebel: gekeimtes Vollkornmehl.

---

## Teil 3 — Synthese-Rezept V13

**Basis = 500 g Getreidemehl (100 % Vollkorn). Bäcker-% auf Getreidemehl; VWG zählt als Zugabe, Hanf nicht in die Mehlbasis.**

### 3.1 Formel

| Komponente | Menge | Bäcker-% | Rolle (Ziel) |
|---|---|---|---|
| Weizen-VK, backstark, fein | 325 g | 65 % | Glutenrückgrat (Krume, Standfestigkeit) |
| **Gekeimtes Weizen-VK** *(neu)* | 50 g | 10 % | Phytat-Vorabbau + Phytase-Boost (Bioverfügbarkeit) |
| Roggen-VK, fein | 75 g | 15 % | höchste Getreidephytase + AX-Präbiotikum + Aroma |
| Hafer-VK, fein | 50 g | 10 % | β-Glucan (GI ↓, Präbiotikum, glatter Biss) |
| Vitalkleber (VWG) | 20 g | 4 % | kompensiert Roggen/Hafer/Keim-Verdünnung |
| Hanfsamen, geschält | 25 g | 5 % | Mg-dicht, texturneutral (Mineralien) |
| Wasser (gesamt) | 390 g | 78 % | Hydratation, Verkleisterung, Phytase-Mobilität |
| Salz | 10 g | 2,0 % | Geschmack, Glutenstraffung, Gärsteuerung |
| Ascorbinsäure *(optional, neu)* | ~0,05 g (~100 ppm) | — | Teigkonditionierer für offene Krume |
| Levain (reif) | 100 g | 20 % | Trieb, milde Säuerung, mikrobielle Phytase |
| **Teiggewicht ≈** | **~960 g** | | ein freigeschobener Laib |

**Levain (1:5:5):** 10 g Anstellgut (Kühlschrank) + 50 g Weizen-VK + 50 g Wasser (28 °C), +30 g Puffer ansetzen; bei 28 °C bis **pH 4,1–4,3** / Float-Test reifen. 100 g verwenden, Rest als neues ASG.

### 3.2 Ablauf (maschinell, kontaktarm, freigeschoben, pH-gesteuert)

**Phase A — 45–48 °C salzfreier Phytase-Soak (Bioverfügbarkeits-MVP).**
Weizen 325 g + Keimmehl 50 g + Roggen 75 g + Hafer 50 g + 300 g Wasser im Wilfa-Kessel (K-Haken, 90 s) homogenisieren. **Kein Salz, kein VWG, kein Levain, kein Hanf.** Im Instant Pot bei **45–48 °C, 35–40 min** halten. Bei nativem pH ~6 ist die Phytase (Optimum pH 5–5,5, 45–55 °C) maximal aktiv — und die Roggen-Aspartatproteasen (Optimum pH 3,5) bleiben dormant. *So bekommt man V9s Phytatabbau, ohne V12s Proteasefurcht zu triggern.*

**Phase B — Saltolyse-Kurzruhe.** Salz 10 g (+ Ascorbinsäure) + VWG 20 g + 30 g (kühles) Wasser zugeben, Stufe 1, 2 min. Abgedeckt 20 min bei Raumtemperatur. (Na⁺/Cl⁻-Abschirmung strafft Gluten von Beginn an — McCann & Day 2013.)

**Phase C — Finalmix, Intervallkneten.** Levain 100 g (kalt) + Hanf 25 g + restliche ~10 g Wasser zugeben. Spiralhaken: 3 min Stufe 1 — 5 min Ruhe — 3 min Stufe 1–2 — 5 min Ruhe — 3 min Stufe 2, bis Fenstertest. **Teigendtemperatur 27–28 °C** (über kühles Wasser/kalten Levain steuern).

**Phase D — Stockgare, pH-gesteuert.** 28 °C im Instant Pot. Coil Fold mit **befeuchteter Teigkarte** nach 60 und 150 min (je ~20 s, kein Handkontakt). Ende bei **pH 4,55–4,65** *und* +60–70 % Volumen (~3,5–4,5 h). Warm+feucht → milchsäurebetont = mild; Stopp bei 4,6 begrenzt Säure *und* hält die Säure über der Protease-Aktivierungsschwelle (pH < 4,5).

**Phase E — Minimalform + Kühlretard.** Bulk-Behälter über bemehltem Gärkorb umkippen (Naht oben, kein Nachformen). Im Beutel **12–16 h bei 4 °C**.

**Phase F — 4-Phasen-Dampfbacken (Bosch HNG978NB1).** Stein auf **250 °C** (≥ 45 min). Teig kalt stürzen, 1 Schnitt.
1. 250 °C, **Dampf Stufe 3**, 12–15 min (Ofentrieb).
2. 220 °C, **Dampf aus** (kurz lüften), 18 min (Kruste).
3. 200 °C bis **Kern 97 °C** (Krumensetzung).
4. *optional* Crisp Finish 210 °C Heißluft, 5 min.
**Auf Rost ≥ 3 h auskühlen** (Krume setzt; Keim-/Hafermatrix sonst gummig; resistente Stärke bildet sich).

---

## Teil 4 — Begründung jeder verwendeten Zutat

**Weizen-VK 65 %.** Glutenfundament für offene Krume + Standfestigkeit; Kleie liefert AX (Präbiotikum), Ferulasäure (Polyphenol) und Mineralien; fein vermahlen für glatten Biss (mittel-feines Korn ist das beste Evidenzband — weder grob noch ultrafein).

**Gekeimtes Weizen-VK 10 % *(neu)*.** Keimung baut Phytat vorab ab (~30–50 %) *und* hebt die Phytaseaktivität → verstärkt die Dephytinisierung der gesamten Charge im Soak. Direkt auf Ziel #1. Gedeckelt auf 10 %, weil Keim-Amylase/-Protease die Krume erweicht. Evidenz: Einweichen+Keimung+Fermentation lieferte die besten Phytat:Mineral-Verhältnisse (Mais-Studie, Frontiers 2024); Weizenphytase-Dephytinisierung erhöhte die Eisenabsorption in einer Humanstudie (Fonio-Studie, PMC3790800).

**Roggen-VK 15 %.** Höchste endogene Getreidephytase (~2,3× Weizen; Reale 2007) → MVP für Phytatabbau/Bioverfügbarkeit; Pentosane = Präbiotikum + Wasserbindung + mildes Aroma. Gedeckelt 15 % (Glutenplateau ~23 %; wir bleiben konservativ für offene Krume).

**Hafer-VK 10 %.** β-Glucan: EFSA-bestätigte Senkung des postprandialen Glukosepeaks (GI) + lösliche Faser (Präbiotikum) + weiches Mundgefühl (glatter Biss). Gedeckelt 10 % (Glutenverdünnung; Dosis additiv, nicht allein wirksam).

**Vitalkleber 4 %.** Kompensiert die Glutenverdünnung durch Roggen+Hafer+Keimmehl; ermöglicht freigeschobene offene Krume bei minimaler Handarbeit; 4 % = Festigkeits-Inflektionspunkt (Giannou & Tzia 2016). V12s 2,34 % war laut eigenen Backtests grenzwertig.

**Hanfsamen geschält 5 %.** Texturneutral (zugelassene Saat); Mg-dicht (echter Nutzen) plus etwas Zn/Fe/ALA/Protein; eigenes Phytat wird durch Soak/Sauerteig mit abgebaut. Einzige Saat, die Mg ohne Krumennachteil beiträgt.

**Salz 2,0 %.** Geschmacksbalance (mild braucht Salz), Glutenstraffung, Gärkontrolle. Erst nach dem Phytase-Soak zugegeben (Phytaseoptimum schützen; Salzhemmung der Getreidephytase ist allerdings gering — Sedaghati 2011).

**Ascorbinsäure ~100 ppm *(optional, neu)*.** Teigkonditionierer, stärkt Gluten für offene Krume/Standfestigkeit. **Ehrlicher Vorbehalt:** der Eisen-Absorptions-Bonus von Vitamin C wird beim Backen zerstört — diesen Effekt liefert nicht der Teig, sondern ein Vitamin-C-reicher Belag beim Essen (Paprika, Tomate, etwas Zitrone).

**Levain 20 %.** Trieb + milde Milchsäure (pH-4,6-Ziel) + mikrobielle Phytase; aus dem vorhandenen Kühlschrank-Anstellgut.

**Wasser 78 %.** Vollkornhydratation für Krume + Verkleisterung + Phytasemobilität; gedeckelt bei 78 % für Freistehen (kein Gusseisentopf). Bei zu festem Teig (Hafer/Keim binden) +10–15 g.

---

## Teil 5 — Begründung für Weglassen / Reduzieren (vs. V8 & V12)

| Zutat | War in | V13 | Begründung |
|---|---|---|---|
| **Linsenmehl** | V8 15 %, V12 15 % | **gestrichen** | Nutzen (Lysin/Protein) laut Kontext irrelevant; Kosten hoch: ~700–1.000 mg Phytat/Laib → senkt die Bioverfügbarkeit der Fe/Zn, um die es geht; 15–32 % Volumenverlust + härtere Krume (Marchini 2021) → gegen Ziel #2; α-Amylase → klebrig. Größter Verstoß gegen die gewichteten Ziele. |
| **Kürbiskernmehl (entölt)** | V8/V12 5 % | **gestrichen** | Nutzen (Methionin) irrelevant; entöltes Mehl konzentriert Phytat auf ~24–30 mg/g → ~600–720 mg/Laib für Zink, das phytatgebunden bleibt; Hanf liefert Mg/Zn bei geringerer Netto-Phytatlast; Glutenverdünnung. |
| **Lein (geschrotet)** | V8/V12 30 g | **gestrichen** | Einziger echter Nutzen ALA-Omega-3 (+ Lignane), aber höchstes Phytat pro Gramm (23–33 mg/g → ~840 mg/Laib) → größter Einzelsaboteur der Mineral-Bioverfügbarkeit; ALA-Konversion schlecht + Backoxidation. Falls gewünscht: separat essen oder ein paar ganze Körner auf die Kruste — nicht in ein mineralfokussiertes Brot einbacken. |
| **Psyllium** | V8 1 %, V12 1,56 % | **gestrichen** | In einem Weizen-Glutenteig mit 4 % VWG strukturell redundant (relevant erst > 5 % oder glutenfrei; Stankevičienė 2023; V12 räumt Psyllium/Lein-Teilredundanz selbst ein). Lösliche-Faser-Rolle besser durch Hafer-β-Glucan (mit EFSA-Glukoseclaim) gedeckt. Spart ein Gefäß (Ziel #4). |
| **Tangzhong** | V12 3,9 % | **gestrichen** | Weichbrot-Technik gegen knusprige Kruste + offene Krume im mageren Herdbrot; 72–75 °C-Schritt tötet Phytase in der kleiereichen Fraktion (gegen Ziel #1); Feuchterolle durch Hafer + 78 % Hydratation + Retard gedeckt. Streicht das arbeitsintensivste Teilrezept (Herd + Abkühlen). |
| **Einkorn-VK** | V12 5 % | **gestrichen** | Carotinoide marginal, keine gewichtete Priorität; schwaches Gluten gegen freigeschobene offene Krume. |
| **Melasse** | V8 10 g | **gestrichen** | Freier Zucker → erhöht glykämische Last (gegen GI-Ziel); Nicht-Häm-Eisen durch Restphytat in der Aufnahme unterdrückt (Christides & Sharp 2013) → Nutzen illusorisch. |
| **Hefeflocken** | V8 10 g | **gestrichen** | Glutamat-Aroma gegen „mild"; B-Vitamine durch omnivore + Milch-Ernährung gedeckt; Protein irrelevant. |
| **Roggen-VK** | V12 23 % | **reduziert auf 15 %** | 23 % steht am Glutenabsturz-Plateau und gefährdet die offene Krume; 15 % sichert den Großteil von Phytase + AX, Soak + Keimmehl decken den Rest. |
| **Hanf** | V8 5 %, V12 ~7 % | **5 %** | Beibehalten nur für Mg; gedeckelt, weil eigenes Phytat (~22 mg/g) sonst die Bilanz belastet. |
| **Vitalkleber** | V12 2,34 % | **erhöht auf 4 %** | V12s Backtests fanden 2 % grenzwertig für Gasrückhalt; 4 % = Evidenz-Inflektion → stützt offene Krume/Freistehen. |
| **Saltolyse (allein)** | V12 | **ersetzt durch Soak → Salzruhe** | V12s Glutenschutz-Einsicht bleibt (Kurz-Salzruhe + kontrollierter Bulk-pH gegen Roggenprotease), aber umgeordnet, damit Ziel #1 nicht geopfert wird; ermöglicht durch Linsen-Streichung (Nicht-Weizen 53 % → 25 %) und den pH-6-Soak (Proteasen dormant). |
| **Kerntemperatur** | V12 98 °C | **97 °C** | 98 °C war nötig, um Psyllium-/Leingele zu setzen; ohne diese setzt 97 °C die Hafer/Keim-Krume, ohne zu übertrocknen. |

---

## Teil 6 — Erwartete Kennzahlen V13

- **Phytatabbau ~88–92 %** (Soak + Keimmehl-Vorabbau + Roggenphytase + Sauerteig pH 4,6 + Retard) → klar > 80 %; Rest-Phytat ~400–500 mg/Laib.
- **Phytat:Zn ≈ 2,5–3,0** (hohes Absorptionsband), **Phytat:Fe ≈ 1,8–2,2** (gehemmt, aber nahe Schwelle — mit Vitamin-C-Belag deutlich verbessert). Netto-absorbierbares Zink **höher als V8 und V12**.
- **GI ~52–54** (Sauerteig + Roggen-AX + Hafer-β-Glucan + resistente Stärke).
- **Krume:** moderat offen (nicht weizenweiß-grobporig — das ginge nur ohne Vollkorn), gleichmäßige Porung.
- **Kruste:** rösch (Dampf-3 → Trockenphase → optional Crisp Finish).
- **Aroma:** mild milchsäurebetont, nussig vom Roggen, Hanf unmerklich.
- **Aktivzeit:** ~22–25 min/Laib (deutlich unter V12 wegen Wegfall von Tangzhong-Kochen + zwei Quellstücken).

---

## Teil 7 — Quellen & Unsicherheiten

**Schlüsselquellen (paraphrasiert):**
- Hurrell & Egli 2010; Gibson & Ferguson 1998; Lönnerdal 2002; IZiNCG/Brown 2004 — Phytat:Mineral-Molverhältnis-Schwellen (PA:Fe < 1, PA:Zn < 5/15).
- Castro-Alba et al. 2019 (*Food Sci Nutr* 7:2854) — Anwendung der Molverhältnisse auf reale Lebensmittel.
- Mais-Dephytinisierung (Frontiers Nutr 2024, PMC11646714) — Einweichen+Keimung+Fermentation: PA:Zn 40,8→7,8 (81 %), PA:Fe →6,2 (85 %).
- Fonio-Studie (PMC3790800) — Weizenphytase-Dephytinisierung erhöht Eisenabsorption beim Menschen; Kürbiskern bis 4,26 g/100 g Phytat.
- Reale et al. 2007 (*J Agric Food Chem* 55:2993) — Roggenphytase ~2,3× Weizen.
- Türk & Sandberg 1992; Leenhardt et al. 2005 — Warmschritt/Säuerung & Phytatabbau.
- EFSA 2026 (doi:10.2903/j.efsa.2026.9942) & EFSA 2025 (Art.-13(1)-Modifikation) — Hafer-β-Glucan & postprandiale Glukose.
- El-Adawy/Taha; Mansour et al. — entöltes Kürbiskernmehl 23,7/30,1 mg/g Phytat.
- Oomah 1996 — Lein 23–33 mg/g; Galasso 2016 — Hanf ~22 mg/g; Legumes 1994 — Linse 0,86–1,5 %.
- Marchini et al. 2021; Stankevičienė et al. 2023; Giannou & Tzia 2016; McCann & Day 2013; Brijs et al. 1999 — Rheologie/Struktur (Linse, Psyllium, VWG, Salz, Roggenproteasen).

**Unsicherheiten / Urteilsentscheidungen:**
1. Die Phytat-/Mineralzahlen sind **Modellschätzungen**, keine Laborwerte; Fehlerbalken groß. Nur die *Richtung* (Bioverfügbarkeit folgt dem Molverhältnis, nicht dem Gehalt) ist robust.
2. Abbaugrade (87–92 %) sind aus der Literatur **extrapoliert** für diese exakte Sequenz, nicht direkt gemessen. Ein Phytat-Assay (Auftragslabor) wäre die einzige echte Verifikation.
3. Gekeimtes Mehl variiert (Quelle/Keimgrad) und erhöht Amylase → Krumenrisiko; deshalb auf 10 % gedeckelt. Bei Nichtverfügbarkeit decken Soak + Roggen den Großteil ab.
4. Die β-Glucan-Dosis pro Scheibe liegt **unter** der EFSA-Wirkdosis — Hafer ist additiv, nicht der GI-Haupthebel (das ist der Sauerteig).
5. Hafer + Keimmehl + Roggen summieren sich auf 25 % Nicht-Voll-Gluten-Mehl; bei 4 % VWG und voller Maschinenentwicklung für Freistehen vertretbar, aber das ist die Grenze — höher würde die offene Krume kosten.
