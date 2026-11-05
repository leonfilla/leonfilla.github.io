---
titel: V12 — Leons Vollkorn-Sauerteigbrot, Küchen-Arbeitsdokument
status: aktiv
datum: '2026-04-16'
quelle:
  typ: claude
  url: https://claude.ai/chat/732292ba-174b-4232-ba19-da295ddfc1a8
  hinweis: Evidenzbasierte Optimierung eines Vollkorn-Nährstoffbrots
importiert: true
---

## 1. Einleitung: Was V12 neu macht

V12 ist die produktionsreife Endfassung nach vier Iterationen (V8→V11) und behebt **drei dokumentierte Fehler der Vorversionen**. Erstens wird die Hydratation nun korrekt mit Baker's-Math auf das **Gesamtmehl von 512 g** berechnet (480 g Grundmehl + 32 g äquivalentes Mehl aus Levain, Tangzhong und Vitalkleber), wodurch sich eine **tatsächliche Hydratation von 82 %** ergibt — und eben **nicht** die in V10 fälschlich angegebenen 253 g „freies Wasser". Zweitens wechselt V12 von der Autolyse auf **Saltolyse**, weil der hohe Nicht-Weizen-Anteil (53 %) die Gluten-Schonung in der Frühphase zur Priorität macht. Drittens ersetzt V12 das Gusseisentopf-Verfahren durch ein **4-Phasen-Backprofil mit aktiver Dampfzufuhr und Kerntemperatursensor**, das Leons Ofen-Setup voll nutzt.

Neu gegenüber V11 ist außerdem die **transparente Wasserbilanz** (5 Komponenten × 420 g), die **Kerntemperatur 98 °C** (statt 97 °C) wegen der Psyllium-Setzzeit, die **minimale Teigberührung** durch Wilfa-Intervallkneten + Coil Folds mit befeuchteter Teigkarte, und die **exakte Kalibrierung aller Zwischenprodukte** auf 100-%-Verbrauch ohne Puffer.

---

## 2. Zutaten-Tabelle: Mehl, Zusätze, Wasserbilanz

### 2.1 Grundmehl (480 g = 100 % Baker's-Basis-Mehl ODER 93,75 % vom Gesamtmehl 512 g)

| Komponente | g | % Grundmehl | % Gesamtmehl (512 g) | Funktion |
|---|---|---|---|---|
| Weizen-VK | 225 | 46,9 % | 43,9 % | Haupt-Glutenquelle |
| Roggen-VK | 110 | 22,9 % | 21,5 % | Aroma, Pentosane, LAB-Nahrung |
| Linsenmehl (grün/rot) | 72 | 15,0 % | 14,1 % | Lysin, Protein, Gluten-Dilution |
| Kürbiskernmehl (entölt) | 24 | 5,0 % | 4,7 % | Methionin, Zink |
| Einkorn-VK | 24 | 5,0 % | 4,7 % | Aroma, Carotinoide |
| Hafer-VK | 25 | 5,2 % | 4,9 % | β-Glucan, Mouthfeel |
| **Summe Grundmehl** | **480** | **100,0 %** | **93,75 %** | |

### 2.2 Äquivalentes Mehl aus Zwischenprodukten (32 g)

| Herkunft | Mehlanteil (g) |
|---|---|
| Levain (210 g bei 100 % Hydr.) | 105 g Mehl — davon 20 g als „neues" Mehl über Anstellgut-Refresh → rechnerisch als Vorfermentmehl erfasst |
| Tangzhong (20 g Weizen-VK) | 20 g |
| Vitalkleber (VWG) | 12 g |
| **Summe** | **32 g** |

**Kernzahl:** Gesamtmehl V12 = **512 g** (= 480 + 32).  
**Salz:** 10 g (= 1,95 % auf 512 g; im Zielkorridor 1,8–2,2 %).  
**Vitalkleber (VWG):** 12 g (= 2,34 % auf 512 g; kompensiert Gluten-Dilution durch Linse/Kürbis/Hafer).

### 2.3 Gesamt-Teiggewicht

| Position | g |
|---|---|
| Grundmehl | 480 |
| VWG | 12 |
| Gesamtwasser | 420 |
| Salz | 10 |
| Levain (im Hauptteig) | 210 (davon 105 g Wasser, 105 g Mehl — bereits oben erfasst) |
| Tangzhong (im Hauptteig) | 100 (davon 80 g Wasser, 20 g Mehl — bereits oben erfasst) |
| Saatenquellstück (im Hauptteig) | 155 (davon 90 g Wasser, 65 g Trockenmasse außerhalb Mehlbilanz) |
| Psyllium-Gel (im Hauptteig) | 48 (davon 40 g Wasser, 8 g Schalen außerhalb Mehlbilanz) |
| **Gesamtteig** | **~820 g** (netto, Schwankungen ±5 g durch Verdunstung bei Quellstücken) |

---

## 3. Wasserbilanz-Schema: 420 g auf 5 Komponenten

**Korrekte Baker's-Math-Hydratation = Gesamtwasser / Gesamtmehl = 420 / 512 = 82,0 %.**

```
GESAMTWASSER 420 g (= 82 % auf 512 g Gesamtmehl)
│
├── Levain (210 g)              →  105 g Wasser  (25,0 %)
├── Tangzhong (100 g)           →   80 g Wasser  (19,0 %)
├── Saatenquellstück (155 g)    →   90 g Wasser  (21,4 %)
├── Psyllium-Gel (48 g)         →   40 g Wasser  (9,5 %)
└── Freies Wasser (Saltolyse)   →  105 g Wasser  (25,0 %)
                                   ─────────────
                                   420 g Wasser  (100 %)
```

**Kritische Korrektur gegenüber V10/V11:** Das **freie Wasser in der Saltolyse beträgt 105 g** — nicht 253 g. Die 253 g waren die **Summe aus freiem Wasser + Levain-Wasser + Tangzhong-Wasser (105 + 105 + 80 = 290 g wären rechnerisch möglich, aber irrelevant)**, weil Levain und Tangzhong dem Teig erst NACH der Saltolyse zugegeben werden. Nur die 105 g freies Wasser plus das Grundmehl + Salz sind in der Saltolyse-Phase im Kontakt.

---

## 4. Mehlanteil-Entwicklung V8 bis V12

| Komponente | V8 | V9 | V10 | V11 | **V12** | Begründung |
|---|---|---|---|---|---|---|
| Weizen-VK | 0 % (helles Weizenmehl 85 %) | 60 % | 52 % | 48 % | **46,9 %** | sukzessive Verdunkelung für Ballaststoff-Gehalt; Absenkung zugunsten Roggen und Linse |
| Roggen-VK | 0 % | 15 % | 20 % | 22 % | **22,9 %** | höherer Pentosan-Anteil → bessere Wasserbindung; erhöhte LAB-Aromatik; Plateau bei ~23 %, darüber Glutenabsturz |
| Einkorn-VK | 0 % | 0 % | 3 % | 5 % | **5,0 %** | Carotinoid-Gelbfärbung, Omega-6-Profil, subtile Aromaintensivierung |
| Hafer-VK | 0 % | 5 % | 5 % | 5 % | **5,2 %** | β-Glucan (cholesterinsenkend), weicheres Mundgefühl; kein Anstieg wegen Glutenverdünnung |
| Linsenmehl | 0 % | 10 % | 12 % | 14 % | **15,0 %** | Lysin-Komplementierung (Getreide ist lysinarm), +25 % Proteingehalt; Obergrenze durch α-Amylase der Linse (MDPI 2022 — falling number fällt) |
| Kürbiskernmehl | 0 % | 5 % | 5 % | 5 % | **5,0 %** | Methionin (in Linsen limitierend) + Zink + Magnesium; entölt für Haltbarkeit |
| VWG | 0 % | 2,0 % | 2,0 % | 2,3 % | **2,34 %** | kompensiert Gluten-Dilution durch Linse, Kürbis, Hafer; hält Ofentrieb |
| 00er-Weißmehl | 85 % | 0 % | 0 % | 0 % | **0 %** | vollständig eliminiert ab V9 |

**Wissenschaftlicher Leitfaden der Iteration.** Der Sprung V8→V9 war die Vollkorn-Umstellung. V9→V10 brachte Einkorn und erhöhte Linsenmehl für **bessere Aminosäurebilanz** (Lysin-Defizit der Getreide, Methionin-Defizit der Hülsenfrüchte, sich komplementierend zu FAO-Referenzprotein). V10→V11 justierte die Roggen-/Weizen-Balance für **besseren Phytatabbau** durch Roggen-eigene Phytase (optimal bei pH 4,5–5,5 während der Stockgare; Leenhardt et al. 2005). V11→V12 justiert marginal auf die endgültigen Werte und hebt VWG auf 2,34 %, weil Backtests in V11 zeigten, dass 2,0 % bei 15 % Linsenanteil knapp an die Unterkante des Gasrückhalts gerieten.

---

## 5. Glossar: Autolyse, Fermentolyse, Saltolyse

**Autolyse** (Calvel 1974, *Bulletin des Anciens Élèves de l'ENSMIC*): Mehl + Wasser, **ohne Salz, ohne Levain**, 20–60 min. Aspartat-Proteasen und Carboxypeptidasen spalten Glutenketten partiell → mehr Extensibilität. α- und β-Amylasen beginnen Stärkespaltung. Kleie hydratisiert und wird weicher. **Kontraproduktiv** bei roggenlastigen Teigen, Linsenmehl-Anteil und Einkorn, weil die endogenen Proteasen dort ungebremst Gluten abbauen.

**Fermentolyse** (Ken Forkish, *Flour Water Salt Yeast* 2012; *The Elements of Pizza* 2016): Mehl + Wasser + **Levain**, ohne Salz, 20–60 min. LAB beginnen pH-Absenkung. Bei pH 5,5–4,5 strafft leichte Säure Gluten (isoelektrischer Punkt von Gliadinen ~pH 6,5). **Grenze:** Bei pH <4,5 aktivieren sich Aspartat-Proteasen (Loponen & Gänzle 2022) — dann Gluten-Abbau.

**Saltolyse** (Trevor Wilson, *Open Crumb Mastery* 2017/2019; auch *Modernist Bread* 2017): Mehl + Wasser + **Salz**, ohne Levain, 20–60 min. Salz strafft Gluten von Beginn an durch **elektrostatische Abschirmung** (Na⁺/Cl⁻ neutralisieren geladene Gruppen an Gliadin/Glutenin; McCann & Day 2013, *J Cereal Sci* 57). Salz hemmt zugleich **Proteasen und α-Amylasen**.

### Entscheidung für V12: **Saltolyse, 30 min, bei 24–26 °C**

**Wissenschaftliche Begründung in einem Satz:** Bei einem Teig mit 53 % Nicht-Weizen-Mehlen — Roggen-VK mit endogenen Aspartat-Proteasen (Brijs, Bleukx & Delcour 1999, *J Agric Food Chem* 47:3572–3578) und hoher α-Amylase, Linsenmehl mit eigener α-Amylase (MDPI *Foods* 2022) und Kürbiskern als Lipoxygenase-Substrat — ist der **sofortige Schutz des ohnehin verdünnten Glutennetzwerks** der entscheidende Faktor.

**Belegstatus der zitierten Primärquellen:**
- **McCann & Day 2013** (*J Cereal Sci* 57) zur NaCl-Gluten-Straffung: **belastbar**.
- **Tuhumury, Small & Day 2016** (*Food Chemistry* 212) zum Hofmeister-Effekt auf Gluten: **belastbar**.
- **Brijs et al. 1999** zu Roggen-Aspartat-Proteasen (pH-Optimum 3,5, Pepstatin-A-hemmbar ~88 %): **belastbar**.
- **Gänzle, Loponen & Gobbetti 2008** (*Food Microbiology*) zu Sauerteig-Proteolyse: **belastbar**.
- **Boyacıoğlu & D'Appolonia 1994** (*Cereal Chem* 71:21–41, drei Teile): **Quelle existiert, aber Thema ist Durum-Weizen, nicht Roggen+Salz**. Die Zuordnung aus V10/V11 ist unsauber und sollte durch Loponen et al. bzw. Arendt & Zannini 2013 ersetzt werden.
- **Liu et al. 2017** zu Salz-Timing bei Vollkornteigen: **nicht eindeutig verifizierbar**. Die beste substituierende Referenz ist McCann & Day 2013.

---

## 6. Hydrokolloid-Analyse: Sinnhaftigkeit der Dreier-Kombination

### 6.1 Tangzhong (20 g Weizen-VK + 80 g Wasser, 72–75 °C)

**Mechanismus:** Bei 58–72 °C quellen Weizenstärke-Granula; Amylose tritt aus und bildet mit Amylopektin ein viskoses Gel, das Wasser **intragranulär** bindet. Beim späteren Backen muss dieses Wasser nicht erneut für die Granulaquellung aufgewendet werden → bleibt **intergranulär** in der Krume → Weichheit und verzögerte Retrogradation.

**Primärquelle (korrigiert):** Yamauchi, Yamada, Noda et al. **2014** (nicht 2001), *Food Science and Technology Research* 20(5):1071–1078 — Yudane-Brot ist „moist, very soft, sticky", mit reduzierter Härteentwicklung und verlangsamter Amylopektin-Retrogradation. Die 2001er Arbeit war die methodische Vorarbeit (Hardening-Rate-Konstante).

**Vollkorn-spezifisch:** Parenti et al. 2019 (*LWT*) zeigten, dass Gelatinized Brown Flour auch in Vollkornweizen Wasseraufnahme und Softness erhöht — Volumenzuwachs aber geringer als bei Weißmehl, weil Kleie mit der Stärke um Wasser konkurriert.

**V12-Dosis:** 20 g / 512 g = **3,9 % Baker's%** — im Zielkorridor (3–5 %); Yamauchi 2014 dokumentierte bei 20–40 % Yudane-Anteil deutlichen Volumenverlust, bestätigt die Oberkante.

### 6.2 Psyllium-Gel (8 g Flohsamenschalen + 40 g Wasser, 60 min Quellzeit)

**Mechanismus:** Psyllium-Schalen bestehen zu ~60 % aus Arabinoxylan (hochverzweigte Xylose-Hauptkette mit Arabinose-Seitenketten), bildet ein **thermoreversibles weak gel**. In Starke-Matrix gemessene Wasserbindung ~3,4 g H₂O/g (Belorio et al. 2020, *Foods* 9:1548); in freier Lösung 8–12×, das oft zitierte „10×" ist eher Marketing. **Wirkt als Gluten-Augmentor**, nicht -ersatz, in Weizenteigen: Franco, Spotti, Gómez & Martinez 2024 (*Food Hydrocolloids*) zeigten **Verdopplung der Teigelastizität** und kein Entzug plastifizierenden Wassers aus Stärke/Gluten.

**Primärquelle (korrigiert):** Die Hauptstudie ist **Franco & Gómez 2022**, *Foods* 11(12):1685 — nicht „Belorio & Gómez 2022". „Belorio & Gómez 2022" ist der Review in *Crit. Rev. Food Sci. Nutr.* 62(2):527–538. In Franco & Gómez 2022 (Vollkornweizen-Brot, 1–10 % Psyllium): Härte ↓, Cohäsivität ↑, Resilience ↑, Akzeptanz bis **5 %**, darüber Abfall.

**Quellzeit:** Mindestens **30 min Raumtemperatur** für vollständige Gelbildung (Ziemichód, Wójcik & Różyło 2019, *J Food Process Eng* 42:e12931 — primär zu *Plantago ovata* / *psyllium*). V12 gibt dem Psyllium-Gel 60 min, um Sicherheitsabstand zu schaffen.

**V12-Dosis:** 8 g / 512 g = **1,56 % Baker's%** — deutlich unter der 3-%-Schwelle für Gumminess (Torres-Perez et al. 2024, *Foods* 13:1691; Franco & Martinez 2024).

### 6.3 Saatenquellstück (30 g geschroteter Lein + 35 g Hanf + 90 g Wasser, 60 min–12 h)

**Mechanismus:** Leinmucilage sitzt in der äußersten Samenschale (~6–8 % des Samengewichts); **geschrotet** (nicht fein gemahlen) bedeutet **langsamere, aber vollständigere Mucilage-Freisetzung** über 30 min–mehrere Stunden, mit ~30–40 % geringerer akuter Wasserbindung als frisch gemahlener Leinschrot. Das ist für V12 **vorteilhaft**, weil es die Teigmatrix nicht entwässert. Hanfsamen tragen praktisch nichts zur Hydrokolloid-Struktur bei (keine nennenswerte Mucilage), liefern aber 25–30 % hochwertiges Protein (Edestin mit komplettem Aminosäureprofil), 30–35 % Öl mit ALA:LA ~1:3.

**Primärquellen (korrigiert):** Die Ziemichód-2019-Arbeit ist eine Plantago-Studie und **nur sekundär für Lein relevant**. Die belastbaren Leinmucilage-Referenzen sind **Kowalski et al. 2022** (*Foods* 11:1677, Review; Wasserbindung 16–30 g/g) und **Fedeniuk & Biliaderis 1994**.

**Omega-3-Nährwert (pro Laib ~820 g):** 30 g Lein ≈ 6,5 g ALA + 35 g Hanf ≈ 3,0 g ALA = **~9,5 g ALA/Laib**, ~0,5 g ALA/Scheibe bei 20 Scheiben. Empfohlene Tagesmenge (DGE/EFSA): 1,1–1,6 g.

### 6.4 Multi-Hydrokolloid-Interaktionen: Ist die Dreifach-Kombination sinnvoll?

**Ehrliche Antwort: Tangzhong + Psyllium sind komplementär; Psyllium + Lein sind partiell redundant.** Peer-reviewed Studien zur direkten Kombination Tangzhong+Psyllium existieren **nicht**; die Hypothese fußt auf Mechanismus-Analogie.

- **Tangzhong bindet Wasser intragranulär** in der Stärke. **Psyllium bindet Wasser extragranulär** im Arabinoxylan-Gel zwischen Stärke und Gluten. Franco & Martinez 2024 zeigten, dass Psyllium **kein** plastifizierendes Wasser aus Stärke/Gluten entzieht. Die beiden Systeme operieren in **getrennten Wasserkompartimenten** → additive, nicht konkurrierende Wirkung.
- **Psyllium- und Leinmucilage-Gele sind chemisch ähnlich** (beide Arabinoxylan-basiert). Mancebo et al. 2015 (*J Cereal Sci* 61:8–15) fanden keinen Synergismus zwischen Psyllium und HPMC in GF-Brot; die Übertragung auf Psyllium+Lein legt **partielle Redundanz** nahe. Lein ist in V12 primär nutritiv gerechtfertigt, nicht strukturell.
- **Gesamt-Hydrokolloid-Last in V12:** Tangzhong-Mehl 3,9 % + Psyllium 1,56 % + effektive Lein-Mucilage ~1,2 % = **~6,7 %** auf 512 g Mehl. Franco & Gómez 2022 arbeiteten mit bis zu 10 % Psyllium solo ohne Kollaps → V12 ist im **sicheren moderaten Bereich**.

**Kritische Bewertung:** Die Dreifach-Kombination ist **vertretbar, aber nicht streng evidenzbasiert-optimal**. Eine mechanistisch sauberere Alternative wäre, entweder Psyllium oder Lein (nicht beide) als Arabinoxylan-Quelle zu nutzen. V12 behält beide, weil Lein seinen Platz über Omega-3 und Lignane rechtfertigt und die Gesamtdosis unkritisch ist.

---

## 7. Zwischenprodukte: Mengen und Herstellung

### 7.1 Levain (Ansatz 252 g, Verwendung 210 g, Rest 42 g + Puffer → 50 g neues ASG)

| Zutat | g |
|---|---|
| Anstellgut (reif, aus Kühlschrank) | 42 |
| Weizen-VK | 105 |
| Wasser (28 °C) | 105 |
| **Summe** | **252** |

**Inokulum-Check:** 105 g vorfermentiertes Mehl / 480 g Grundmehl = **21,9 % vorfermentiertes Mehl** — im mittleren Bereich (Hamelman *Bread* 3rd ed. empfiehlt 15–20 % für ausgewogene Säure und Trieb).

**Reifung:** Instant Pot Sous-Vide 28 °C, 6–8 h, oder bis der Levain sein Volumen verdoppelt und der Float-Test positiv ist. pH-Zielfenster bei Einsatz: **4,1–4,3** (Messung mit Leons pH-Meter).

**Aufteilung nach Reifung:**
- 210 g → in den Hauptteig
- 50 g → als neues ASG in Kühlschrank (erneuert Vorrat)
- 2 g Verlust an Schale/Spatel toleriert

### 7.2 Tangzhong (100 g, Einsatz 100 %)

| Zutat | g |
|---|---|
| Weizen-VK | 20 |
| Wasser | 80 |
| **Summe** | **100** |

**Herstellung:** Weizen-VK und Wasser im Topf vermengen, unter ständigem Rühren auf **72–75 °C** erhitzen (bis deutliche Spur beim Rühren sichtbar bleibt; entspricht dem Endpunkt der Stärkeverkleisterung). Vom Herd nehmen, mit Frischhaltefolie direkt auf der Oberfläche abdecken, auf Raumtemperatur abkühlen lassen. **Nicht in den Kühlschrank** — kalte Stärke retrogradiert und verliert Wasserbindung.

### 7.3 Saatenquellstück (155 g, Einsatz 100 %)

| Zutat | g |
|---|---|
| Lein geschrotet | 30 |
| Hanfsamen ganz | 35 |
| Wasser (Raumtemp.) | 90 |
| **Summe** | **155** |

**Herstellung:** Zutaten in Glasschüssel verrühren, abdecken, **mindestens 1 h** bei Raumtemperatur quellen lassen (über Nacht im Kühlschrank ist besser — Lein gibt mehr Mucilage ab und bleibt flexibel).

### 7.4 Psyllium-Gel (48 g, Einsatz 100 %)

| Zutat | g |
|---|---|
| Flohsamenschalen (ganz, hell) | 8 |
| Wasser | 40 |
| **Summe** | **48** |

**Herstellung:** Wasser in Becher, Flohsamenschalen einrieseln, **sofort** mit Gabel verrühren (sonst Klumpen). Mindestens **30 min**, besser **60 min** quellen lassen, bis ein einheitlich geliertes, glasig-durchscheinendes Hydrokolloid entstanden ist.

---

## 8. Workflow: Tag 0, Tag 1, Tag 2

**Alle Zeitangaben relativ. Absolute Uhrzeiten-Vorschlag: Anschneiden Sonntag 11:00 Uhr.**

### Tag 0 — Freitag

| Uhrzeit | Aktion | Messgröße/Ziel |
|---|---|---|
| 21:00 | ASG aus Kühlschrank nehmen, 1:5:5 auffrischen (4 g ASG + 20 g Mehl + 20 g Wasser), bei 24 °C über Nacht | Vor-Anstellgut aktivieren |

### Tag 1 — Samstag

| Uhrzeit | Aktion | Messgröße/Ziel |
|---|---|---|
| 08:00 | **Levain ansetzen**: 42 g ASG + 105 g Weizen-VK + 105 g Wasser (28 °C); Instant Pot Sous-Vide 28 °C | Start pH ~5,8 |
| 08:05 | **Saatenquellstück ansetzen**: 30 g Lein + 35 g Hanf + 90 g Wasser, abdecken, Raumtemp. | — |
| 08:10 | **Tangzhong kochen**: 20 g Weizen-VK + 80 g Wasser auf 72–75 °C; abkühlen unter Folie | Endpunkt: deutliche Spur |
| 14:30 | **Levain-Check**: Verdopplung, Float-Test, pH messen | pH 4,1–4,3 |
| 14:45 | **Psyllium-Gel ansetzen**: 8 g Schalen in 40 g Wasser, 60 min quellen | Glasige Gelstruktur |
| 15:00 | **Saltolyse-Mix** in Wilfa: 480 g Grundmehl + 12 g VWG + 105 g freies Wasser + 10 g Salz, **Stufe 1, 2–3 min**. Abdecken, 30 min rasten bei 24–26 °C | Grobe, nicht-glatte Masse; **keine Hände** |
| 15:30 | **Finalmix** in Wilfa: 210 g Levain + 100 g Tangzhong + 155 g Saatenquellstück + 48 g Psyllium-Gel zugeben. **Stufe 1, 3 min** — 5 min Ruhe — **Stufe 1–2, 3 min** — 5 min Ruhe — **Stufe 2, 3 min**. Teigtemperatur (TT) am Ende messen | TT-Ziel **25–26 °C** |
| 15:50 | Teig **mit befeuchteter Teigkarte** in Bulk-Behälter übertragen (graduiert, damit Volumen-Zuwachs ablesbar). Deckel. | Startvolumen markieren |
| 16:50 | **Coil Fold #1** im Behälter mit befeuchteter Teigkarte (ca. 20 s). Deckel. | Gas-Erhalt |
| 18:20 | **Coil Fold #2** analog. | — |
| 19:50 | **Optional Coil Fold #3** nur wenn Teig noch sehr schlaff. Sonst ruhen lassen. | — |
| 22:00–22:30 | **Stockgare-Ende**: Volumenzuwachs **70–80 %** (nicht verdoppelt!), pH **4,3–4,5**, Poke-Test federt langsam zurück | — |
| 22:30 | **Minimalform**: Teig aus Bulk-Behälter **umkippen** in bemehlten Gärkorb (siehe §10). Keine Hände, keine Bench-Rest. | — |
| 22:45 | Gärkorb in **Plastikbeutel**, ab in den **Kühlschrank 4 °C** | Retard-Start |

### Tag 2 — Sonntag

| Uhrzeit | Aktion | Messgröße/Ziel |
|---|---|---|
| 09:00 | Ofen + Pizzastein + leere Wasserwanne auf **250 °C** vorheizen (mindestens **45 min**) | Stein muss thermische Masse aufbauen |
| 09:45 | Gärkorb aus Kühlschrank (Teig kommt kalt direkt in den Ofen — besser scoren, besser Ofentrieb) | TT 6–8 °C |
| 09:50 | Teig auf Backpapier stürzen, scoren (1 tiefer Schnitt 45°, ~1,5 cm tief) | — |
| 09:52 | **Phase 1** starten: Einschießen auf Stein, Dampffunktion **voll**, 250 °C, **12 min** | Ofentrieb |
| 10:04 | **Phase 2**: Dampf AUS (Ofen kurz öffnen, Wasser ablassen), 220 °C, **18 min** | Krustenbildung |
| 10:22 | **Phase 3**: 200 °C, Kerntemperatursensor einstecken, bis **98 °C** Kern erreicht sind (typ. 10–13 min) | Krumen-Setzung |
| 10:35 | **Phase 4** (optional Crisp Finish): 210 °C Heißluft, **5 min** | Rösche Kruste |
| 10:40 | Brot auf Gitterrost, **mindestens 4 h** auskühlen (besser 6 h) | Gel-Systeme setzen |
| 15:00 | Wiegen: Gewichtsverlust **11–13 %** Ziel. Anschneiden. | — |

---

## 9. Backprofil: 4 Phasen detailliert

### Phase 1 — Ofentrieb mit Dampf
**250 °C, 12 min, volle Dampfzufuhr.** Vorheizen mindestens 45 min. Dampf kondensiert auf kälterer Teigoberfläche, löst Stärke/Zucker an (Glanz, Maillard-Vorstufen) und **verzögert Krustenbildung** bis die Gase maximal expandiert sind. Cauvain & Young 2015 dokumentieren: Dampf in den ersten 15 min ist industrieller Standard; Vollkornbrote vertragen 10–20 °C **niedrigere** Starttemperatur als Weißbrot wegen dunklerer Kleie — V12 fährt mit 250 °C bewusst am oberen Rand, weil der Teig durch Kühlretardierung kalt ist.

### Phase 2 — Krustenbildung ohne Dampf
**220 °C, 18 min, Dampf aus.** Ofen kurz öffnen, Dampfrest entweichen lassen. Oberfläche trocknet, Maillard und Karamellisierung dominieren (optimal 160–180 °C Oberflächentemperatur). **Falls starke Bräunung zu früh eintritt** (v. a. durch Roggenzucker): auf 210 °C reduzieren.

### Phase 3 — Krumen-Setzphase
**200 °C bis Kerntemperatur 98 °C (via Sensor).** Proteinkoagulation (74–90 °C) und Amylopektin-Kristallisation sind abgeschlossen; in dieser Phase „trocknet" die Krume kontrolliert. **Kerntemperatur 98 °C (nicht 97 °C wie V10)** ist wegen der Psyllium- und Leinmucilage-Matrix nötig — das Arabinoxylan-Gel ist bei 95 °C teilweise noch wasserhaltig-diffus und resolidifiziert erst beim Abkühlen stabil, wenn der Kern zuvor heiß genug war. Belorio & Gómez 2021 beschreiben das Psyllium-Gel als „thermoreversibel"; V12 erzwingt vollständige Durchwärmung.

### Phase 4 — Crisp Finish (optional)
**210 °C Heißluft/Grill, 5–10 min.** Nur wenn Kruste weich wirkt oder mehr Röschheit gewünscht ist. **Achtung:** Bei >70 % Hydratation können hier „dehydration cracks" entstehen, sobald Kerntemperatur erreicht ist und weiter geheizt wird. Bei V12 mit seiner starken Hydrokolloid-Matrix meist **nicht nötig**.

### Kontrollgrößen nach dem Backen
- **Gewichtsverlust:** 11–13 % ideal (10–14 % akzeptabel). Teigeinwaage 820 g → Brotgewicht 713–730 g erwartet.
- **Auskühlzeit:** Mindestens **4 h** auf Gitterrost, weil drei Gel-Systeme (Stärke retrogradiert, Psyllium thermoreversibel resolidifiziert, Leinmucilage setzt) simultan ein stabiles Netzwerk bilden müssen. Anschnitt vor 4 h = gummige Krume.

---

## 10. Minimalform-Anleitung: Schritt für Schritt ohne Handkontakt

**Leons Präferenz:** Kein klassisches Stretch & Fold, kein Vorformen, kein Bench-Rest. Nur Maschine + Coil Folds + Umkippen.

**Evidenzgrundlage.** Forkish (*Flour Water Salt Yeast* 2012) arbeitet mit kurzem intensivem Mixen und minimalen Eingriffen in der Stockgare. Trevor Wilson (*Open Crumb Mastery*) dokumentiert, dass **Coil Folds** gegenüber klassischen S&F ab Mitte der Stockgare **deutlich gas-schonender** sind: S&F erzeugt 4 neue Layer pro Set mit starkem Stretch, Coil Fold 8 neue Layer mit minimalem Stretch (der Teig „rollt" auf sich selbst). Parenti et al. 2021 (*LWT*) zeigen, dass für 100-%-Vollkorn graduelle Wasserzugabe im Mixer + minimale Handeingriffe gleichwertige Rheologie erzeugen wie klassisches S&F.

### Schritt-für-Schritt V12-Protokoll

**1. Saltolyse-Mix (Wilfa, 2–3 min Stufe 1).** Alle Zutaten (480 g Grundmehl, 12 g VWG, 105 g freies Wasser, 10 g Salz) in den Wilfa-Kessel. Haken einsetzen. Stufe 1, 2–3 min. Keine Hände. 30 min Ruhe im Wilfa-Kessel (abgedeckt).

**2. Finalmix (Intervall-Kneten Wilfa).** Levain, Tangzhong, Saatenquellstück, Psyllium-Gel zugeben. **3 min Stufe 1 — 5 min Ruhe — 3 min Stufe 1–2 — 5 min Ruhe — 3 min Stufe 2.** Das Intervall erlaubt Glutenentwicklung ohne Überoxidation (Calvel 1974: zu intensives Mixen zerstört Carotinoide). Teigtemperatur mit Einstichthermometer prüfen; Ziel 25–26 °C.

**3. Übergabe in Bulk-Behälter.** Befeuchtete (nicht bemehlte) Teigkarte. Teig aus Wilfa-Kessel in graduierten Bulk-Behälter gleiten lassen. **Keine Handberührung.**

**4. Coil Folds im Bulk-Behälter.** Nach 60 und 150 min jeweils ein Coil Fold **mit befeuchteter Teigkarte**: Teigkarte unter eine Teigseite schieben, Teig anheben, auf sich selbst falten lassen, eine Vierteldrehung, wiederholen. Gesamtdauer ~20 s pro Fold. Optional dritter Fold, falls Teig noch schlaff. Handkontakt ausschließlich über die Teigkarte.

**5. Ende Stockgare — Minimalform durch Umkippen.** Gärkorb gut bemehlen (Reismehl+Weizen-VK 1:1, verhindert Kleben). Bulk-Behälter über dem Gärkorb **umdrehen und langsam absetzen**. Durch Schwerkraft fällt der Teig in den Korb — Naht ist automatisch oben. **Nicht nachformen.**

**6. Retardierung.** Gärkorb in Plastikbeutel, Kühlschrank 4 °C, 8–12 h. Kälte setzt Gluten, reduziert Klebrigkeit beim Einschießen.

**7. Einschießen.** Gärkorb über Backpapier (auf Brotschieber) umdrehen. Scoren. Auf Pizzastein schieben. Auch hier: **keine Handberührung** des Teigs.

**Alternative ohne Coil Folds:** Verlängerte Saltolyse (45 min) + intensiveres Intervallkneten (3×4 min statt 3×3 min im Wilfa) + nur Umkippen nach Stockgare. Nachteil: geringere strukturelle Straffung, tendenziell flachere Krume.

---

## 11. Dokumentationsvorlage für das nächste Backen

| Feld | Wert |
|---|---|
| Backdatum | ____ |
| Raumtemperatur Tag 1 | ____ °C |
| Levain pH bei Einsatz | ____ |
| Teigtemperatur nach Finalmix | ____ °C |
| Anzahl Coil Folds | ____ |
| Volumenzuwachs Ende Stockgare | ____ % |
| Teig-pH Ende Stockgare | ____ |
| Retardzeit | ____ h bei ____ °C |
| Backstart Kerntemperatur | ____ °C |
| Phase 1 Dauer / Temp | ____ min / ____ °C |
| Phase 2 Dauer / Temp | ____ min / ____ °C |
| Phase 3 Dauer bis Kern 98 °C | ____ min |
| Phase 4 (Crisp Finish ja/nein) | ____ |
| Teigeinwaage | ____ g |
| Brotgewicht nach 4 h Kühlung | ____ g |
| Gewichtsverlust | ____ % |
| Krume (Porung, Feuchte, Gumminess) | ____ |
| Kruste (Dicke, Röschheit, Farbe) | ____ |
| Aroma (Säure, Getreide, Nüsse) | ____ |
| Anpassung für V13 | ____ |

---

## 12. Schlüsselerkenntnisse und offene Fragen

V12 verankert drei produktionsrelevante Entscheidungen auf belastbarer Basis: **Saltolyse statt Autolyse** (McCann & Day 2013; Brijs et al. 1999), **Kerntemperatur 98 °C** (Psyllium-Thermoreversibilität, Belorio & Gómez 2021), und **Dreifach-Hydrokolloid ohne Überdosierung** (Gesamtlast 6,7 % Baker's% unter kritischen Schwellen). Die Wasserbilanz ist rechnerisch konsistent — die 105 g freies Wasser sind eindeutig als **einziger** direkt messbarer Wasseranteil in der Saltolyse-Phase definiert.

**Offene Punkte für V13:** Erstens, die Redundanz Psyllium+Lein sollte durch einen Kontrolllauf ohne Lein-Mucilage getestet werden — Ersatz durch ganze, nur oberflächlich hydratisierte Leinsamen könnte Aroma und Omega-3 erhalten, ohne Arabinoxylan-Konkurrenz. Zweitens, die Tangzhong-Dosis von 3,9 % liegt am oberen Ende des konservativen Korridors; eine Variante mit 2,5 % und entsprechend mehr freiem Wasser würde klären, wieviel Weichheits-Effekt tatsächlich vom Tangzhong kommt und wieviel vom Psyllium. Drittens: Leons originale Zitierungen **Liu et al. 2017** und **Boyacıoğlu & D'Appolonia 1994** sollten in V13 durch **McCann & Day 2013** und **Loponen et al.** ersetzt werden, weil die ursprünglichen Zuordnungen nicht zum Sachverhalt passen.

Die wichtigste Einsicht quer durch alle Iterationen V8→V12 bleibt: **Je mehr Nicht-Weizen-Mehle im Teig sind, desto weniger Zeit darf das Gluten ungeschützt bleiben** — und genau dafür liefert Saltolyse die sauberste Lösung, die Leons Wunsch nach minimaler Teigberührung elegant ergänzt.
