---
titel: V18.1 — Vollständiges Rezept & Workflow (Module A · C · D-Akazie)
status: aktiv
datum: '2026-07-09'
quelle:
  typ: claude
  url: https://claude.ai/chat/2acded25-5345-4b43-9ec8-82eace209a98
  hinweis: Vollkornbrot mit besserer Porung optimieren
importiert: true
linie: v17-vollstandiges-rezept-workflow-module-a-c-d-aka-cbb0b
---

**100 % Vollkorn · freigeschoben · maschinell · pH-gesteuert · so viel Raumtemperatur wie sinnvoll.**
**Fokus V18: Ofentrieb über das Gare-Schema statt über die Fasern.**
**Neu in V18.1: Doppelcharge (2 Laibe) · Krustenfarbe-Steuerung.**

Module: **A** gekeimtes Mehl · **C** Chia (ganz) · **D** Akazienfaser. — *Modul B (Hanf) entfällt seit V16.*

---

> ## Änderungen V18 → V18.1
>
> **Die Teigformel bleibt identisch zu V18** — bewusst, damit dein laufender Ofentrieb-Test (die vier V18-Hebel) sauber attribuierbar bleibt. Ergänzt wurden nur zwei Module:
>
> **A) Doppelcharge (2 Laibe)** — neuer Abschnitt 8. Kernlogik: **Teilung direkt nach dem Finalmix**, nicht nach der Stockgare. Skalierte Einwaagen, Wassertemperatur-Rechnung für den Instant Pot, sequenzielles Backen.
>
> **B) Krustenfarbe** — Backprofil Phase 2–4 überarbeitet (Phase 1 **unverändert**). Begründung s. Abschnitt 6.1: Trieb entsteht in Phase 1, Bräunung in Phase 2–4 — die beiden Ziele sind über die Phasentrennung entkoppelbar.
>
> > **Erwartungs-Kalibrierung:** V18 backt voraussichtlich **dunkler** als V16/V17 — der jüngere Teig hat mehr unvergorenen Restzucker (Maillard-Substrat) und weniger Säure (Säure hemmt Maillard). Krustenfarbe ist der klassische Gärgrad-Indikator: blass = übergar, dunkel = jünger. Eine dunklere Kruste nach V18 ist damit **Bestätigung, dass der Gare-Eingriff gegriffen hat** — nicht ein Fehler. Deshalb: Farbe **niemals über längere Gare** korrigieren, das ist der einzige Hebel, der den Trieb-Gewinn wieder kassiert.

> ## Änderungen V17 → V18 (unverändert gültig)
>
> **Ofentrieb-Paket — die vier kostengünstigen Hebel:**
> 1. **Stockgare deutlich jünger beenden:** pH 4,62–4,65 & +60–70 % → **pH ~4,7 & +30–50 %**. *Warum:* Der 16-h-Retard säuert weiter und lässt die Reife fertig werden. Ein Teig, der schon bei +60–70 % in den langen Retard ging, war beim Einschießen **über** dem Peak → flacher Laib, unabhängig von den Fasern. **Wahrscheinlich der größte Einzelhebel.**
> 2. **VWG 5 % → 4 %** (25 → 20 g), Pfad zu 3 %. *Warum:* Krücke fürs alte 11-g-Mehl; mit kleberstarkem Mehl teils redundant, macht das Netz zäh/weniger dehnbar.
> 3. **Psyllium 1,4 % → 1,0 %** (7 → 5 g), **Wasser gekoppelt −10 g** (Gesamt 86 → 84 %). *Warum:* hitzestabiles Gel friert das Volumen früh ein. **Mehl ↔ Psyllium ↔ Wasser als ein System** behandeln.
> 4. **Ascorbinsäure von „optional" auf Standard** (~0,05 g/500 g) — verbessert Gashaltung und Volumen.
>
> **Zusätzlich — Korrektur der Levain-Logik:** Der pH-4,1–4,3-Check stand fälschlich am *Soak-Start*, obwohl der Levain erst ~1,5–2 h später beim Finalmix in den Teig geht — so überreifte er genau um diese Spanne. Jetzt: **Soak-Start** gatet auf die *steigende* Kurve (pH ~4,4–4,6), **Reife-Check** sitzt am **Finalmix** (Float, pH ~4,3).
>
> **Bewusst *nicht* geändert:** Mehlsorte, Keimmehl 10 %, Roggen 15 %, Hafer 10 %, Chia 25 g ganz, Akazie 2 %, Salz 2 %, Temperaturführung, Spannungsform. Nächste Iterationsstufe s. Abschnitt 6.2.

---

## 1. Zutaten

### 1.1 Levain (Abend vor dem Backtag, Raumtemperatur)

| Zutat | 1 Laib | **2 Laibe** |
|---|---|---|
| Anstellgut (aus dem Kühlschrank) | 15 g | **24 g** |
| Weizenvollkornmehl, fein (kleberstark) | 75 g | **120 g** |
| Wasser, Raumtemp. | 75 g | **120 g** |
| **= reifer Levain** | **~165 g** | **~264 g** |

**Verbrauch (1 Laib):** 100 g Hauptteig · 35 g zurück in den Kühlschrank (neues ASG) · ~30 g Puffer.
**Verbrauch (2 Laibe):** 200 g Hauptteig · 35 g ASG · ~29 g Puffer.

> **Der Levain skaliert ×1,6, nicht ×2** — die 35-g-ASG-Rückstellung bleibt unverändert, nur der Teiganteil verdoppelt sich. Verhältnis **1:5:5 beibehalten**, damit Reifekurve und Δ identisch bleiben.

### 1.2 Hauptteig (Backtag) — genaue Einwaage

| Zutat | 1 Laib | **2 Laibe** | Bäcker-%¹ | Modul |
|---|---|---|---|---|
| Weizenvollkornmehl, fein, backstark (~13,8 g Eiweiß, extrafein) | 275 g | **550 g** | 55 % | Kern |
| Gekeimtes Weizen-/Dinkelvollkornmehl | 50 g | **100 g** | 10 % | A |
| Roggenvollkornmehl, fein | 75 g | **150 g** | 15 % | Kern |
| Hafervollkornmehl, fein | 50 g | **100 g** | 10 % | Kern |
| Vitalkleber (VWG) | 20 g | **40 g** | 4,0 % | Kern *(Pfad zu 3 %)* |
| Chia, ganz | 25 g | **50 g** | 5,0 % | C |
| Akazienfaser | 10 g | **20 g** | 2,0 % | D |
| Psylliumschalen, fein | 5 g | **10 g** | 1,0 % | Kern |
| Salz | 10 g | **20 g** | 2,0 % | Kern |
| Wasser (gesamt im Hauptteig) | 370 g | **740 g** | – | Kern |
| Reifer Levain | 100 g | **200 g** | 20 % | Kern |
| Ascorbinsäure (Standard) | ~0,05 g | **~0,1 g** | – | Teigkonditionierer |
| **Σ Teig** | **~990 g** | **~1980 g** | | |

> **VWG-Pfad:** 4 % ist die erste Stufe herunter von V17s 5 %. Hält der Laib Stand und Krume, ab dem übernächsten Backen **3 %** testen (15 g / 30 g). Weniger VWG = dehnbareres Netz = mehr Trieb.

¹ Bezug 500 g Getreidemehl gesamt (incl. ~50 g Weizenmehl, das im Levain steckt) — bei Doppelcharge 1000 g.

**Gesamthydratation ~84 %** (420 g Wasser inkl. Levain auf 500 g Getreidemehl). Die Senkung um 2 % ggü. V17 ist die **Kopplung an die Psyllium-Reduktion**, keine eigenständige Trockenlegung.

> **Hydratations-Fenster (84 → 86 %):** Die Kopplung ist ein Startwert, kein Dogma — Psyllium-Bindung streut nach Marke/Feinheit. Zu fest/trocken → in **+5-g-Schritten ins Soak** zurückgeben (85 % → 86 %); zu schlaff → bei 84 % bleiben. **Obergrenze für reines Wasser: 86 %** — darüber nur mit Binder (Psyllium zurück), sonst kippt es ins Breitlaufen. Wasser wirkt doppelt: mehr Dampf (Trieb ↑), aber schlafferer Teig (Breitlaufen ↑). **Erst V18 unverändert backen**, dann nachwässern — sonst holst du die Schlaffheit zurück, die gerade rausgenommen wurde.

**Wasseraufteilung:** Soak **320 g** (Doppel: **640 g**) · Saltolyse 50 g (**100 g**) · Levain bringt 50 g (**100 g**) mit.

> **Wenn du noch kein Keimmehl hast:** 50 g zusätzliches Weizenvollkornmehl (Weizen dann 325 g), Soak auf 50 min verlängern, Roggen optional auf 85 g (17 %). Bioverfügbarkeit bleibt nahezu gleich. *(Nebeneffekt: hellere Kruste, s. 6.1.)*

### 1.3 Geräte

Wilfa ProBaker (K-Haken + Spiralhaken; 7 l / max. 5 kg Teig — Doppelcharge nutzt ~40 % Kapazität) · Instant Pot (Sous-Vide 45 °C) · Apera-pH-Meter · Einstichthermometer · **2 Gärkörbe** (für Doppelcharge) · Bosch HNG978NB1 + Pizzastein · befeuchtete Teigkarte · ggf. Alufolie (Krustensteuerung).

---

## 2. Temperatur-Philosophie

So viel Raumtemperatur wie sinnvoll — mit zwei begründeten Ausnahmen:

- **45-°C-Phytase-Soak (warm, nötig):** Die Getreidephytase arbeitet bei 45–55 °C nahe ihrem Optimum und senkt das Phytat → bessere Zink-/Eisen-Bioverfügbarkeit. *(Zweitweg: die Säuerung über die lange Führung dephytiniert zusätzlich — der Soak ist der Boost obendrauf.)*
- **Kühlretardierung (kalt, nötig):** für Standfestigkeit, sauberes Einschneiden, Ofentrieb und einen praktikablen Zeitplan. *Mit ganzer Chia: der Retard ist das Fenster, in dem die Samen das eingewogene Wasser nachbinden.* **Ab V18:** Der Retard ist bewusst das Fenster, in dem die *Reife fertig wird* — deshalb endet die Stockgare jünger.

Alles dazwischen — Levain, Saltolyse, Stockgare — läuft bei Raumtemperatur und wird über **pH** gesteuert (Zeit ist nur Orientierung).

---

## TAG 0 — Abend (~20:00) · 3 min aktiv

1. Anstellgut aus dem Kühlschrank nehmen.
2. **Levain ansetzen** (Mengen s. 1.1, je nach 1 oder 2 Laiben) klümpchenfrei verrühren. Locker abdecken, bei Raumtemperatur stehen lassen. Füllstand markieren.
   - Bei ~21 °C reift er in ~10–14 h. Kühlere Küche (~19 °C) → früher ansetzen oder 1:4:4. Wärmere → später.
   - Falls das ASG nach 7 Tagen sehr träge ist: 2–3 h früher ansetzen; reicht der Trieb am Morgen nicht, 2–4 h länger geben.

---

## TAG 1 — Morgen

> **Wichtig (Logik seit V18):** Der Levain geht erst beim **Finalmix** in den Teig — ~1,5–2 h nach Soak-Start (Doppelcharge: ~2 h). Der Ziel-pH (~4,3) ist die Spezifikation **für den Zugabezeitpunkt**, nicht fürs Soak-Start-Gate.

### ~08:00 · Soak-Start-Gate + ASG zurückstellen (3 min aktiv)

3. **Soak-Start-Gate (steigende Kurve, nicht Zielwert):** Levain deutlich aufgegangen/gewölbt, **klar noch steigend**, pH **~4,4–4,6**, Peak in ~1,5–2 h vorhergesagt (Float ggf. noch nicht positiv — das ist korrekt). → Jetzt Soak starten.
   - *Feedforward-pH:* Miss einmal über deine exakte Vorlaufzeit (Soak-Start → Finalmix) den pH-Abfall Δ (nahe Peak ~0,1–0,3; wärmere Küche → größer). Gate dann bei **pH = Zugabeziel + Δ**. Steigkurve ist der primäre Trigger, der pH-Offset die Gegenprobe.
   - **Doppelcharge:** Vorlaufzeit wächst (~1:35 → ~2:00) → **Δ wird größer** → Gate früher/höher (~4,5–4,6). **Δ separat protokollieren** — es ist nicht dasselbe wie beim Einzelbrot.
   - *Im Zweifel früher:* Ein leicht *junger* Levain hilft dem Trieb; ein überreifer schadet doppelt (mehr Säure + ausgezehrte Hefe).
4. **35 g reifen Levain** in ein sauberes Glas → zurück in den Kühlschrank (ASG fürs nächste Brot; Menge bei Doppelcharge unverändert). Zeitlich unkritisch.
   - Backabstand > 10 Tage: dieses ASG vor dem Kühlen einmal füttern (10 g + 20 g Mehl + 20 g Wasser), 2 h anspringen lassen, dann kühlen.

### ~08:10 · Phytase-Soak (5 min aktiv, 45 min passiv)

5. In der Instant-Pot-Schüssel vermengen: Weizen-VK + Keimmehl + Roggen + Hafer + ganze Chia + Akazienfaser + **Soak-Wasser** (320 g / **640 g**). K-Haken/Löffel, bis homogen (kein trockenes Mehl). **Kein Salz, kein VWG, kein Psyllium, keine Ascorbinsäure, kein Levain.**
6. Abgedeckt in den Instant Pot, **Sous-Vide 45 °C, 45 min.**
   > **Wassertemperatur statt Aufheizen (gilt für beide Chargengrößen, für die Doppelcharge aber *notwendig*):** Die Mischtemperatur ist **mengenunabhängig** — nur das Verhältnis Trockenmasse : Wasser zählt. Bei diesem Rezept landet das Gemisch mit **~58–60 °C** Wasser direkt bei ~45 °C; der IP muss dann nur noch *halten*, nicht heizen. Konservativer: **~55 °C** Wasser → Gemisch ~42 °C, der IP schließt die letzten Grad schnell.
   > **Nicht über 60 °C** (beginnende Stärkeverkleisterung, Phytase-Denaturierung oberhalb ~60 °C). Der kalte Edelstahltopf zieht ein paar Grad ab — **einmal mit dem Einstichthermometer nachmessen und den Wert festschreiben.**
   > *Warum bei Doppelcharge Pflicht:* ~1,6 kg zähe Masse konvektiert nicht — die Aufheizzeit steigt überproportional und es entsteht ein Gefälle (unten 45 °C, Kern 35 °C): ungleiche Phytase-Arbeit bei gleichzeitig ungleicher Amylase-Exposition.
   > *Amylase-Deckel:* 45 °C liegt auch nahe dem Amylase-Optimum; das Keimmehl ist eine zusätzliche Enzymquelle. Soak **nicht** über 45 min ziehen.

### ~08:55 · Abkühlen lassen (passiv, ~15–20 min / Doppel ~25–30 min)

7. Schüssel aus dem Instant Pot, bei Raumtemperatur auf ~34 °C abkühlen lassen (Einstichthermometer).
   > **Doppelcharge:** Masse direkt nach dem Soak **in die Wilfa-Schüssel umfüllen** — breiter, mehr Oberfläche, kühlt deutlich schneller. Da die Wilfa durch die mitdrehende Schüssel mehr Reibungswärme einträgt als andere Maschinen, bei großer Charge eher auf **~32 °C** abkühlen, um die 26–27 °C Teigendtemperatur zu treffen.

### ~09:15 · Saltolyse (3 min aktiv, 25 min passiv, Raumtemperatur)

8. **Salz + VWG + Psyllium + Ascorbinsäure + Saltolyse-Wasser** (50 g / **100 g**) zugeben. K-Haken, Stufe 1, 2 min — gerade homogen.
   > **Klümpchen vermeiden:** VWG **vorher trocken mit dem Psyllium mischen**, dann einrühren — trockener Vitalkleber in nasse Masse gerührt bildet sonst gummige Nester.
9. Abgedeckt 25 min bei Raumtemperatur ruhen (kühlt weiter Richtung ~28 °C; Psyllium quillt, Salz strafft Gluten).

### ~09:45 · Finalmix + echter Reife-Check (10 min aktiv)

10. **Reife-Check jetzt (nicht am Soak-Start):** Float positiv, pH **~4,3**. Passt → **Levain zugeben** (100 g / **200 g**).
    - *Ist er schon deutlich unter 4,2 / Float längst über Peak:* Levain war zu alt → nächstes Mal Gate früher. Diesmal trotzdem verbacken, aber Stockgare am jüngeren Ende beenden.
11. Spiralhaken, Intervall: 3 min Stufe 1 — 5 min Ruhe — 3 min Stufe 1–2 — 5 min Ruhe — 3 min Stufe 2, bis dünnes Fenster.
    - *Kleberstarkes Mehl entwickelt schneller* — **eher am früheren Ende prüfen**, nicht überkneten. „Dünnes Fenster" bleibt bei 100 % VK relativ (Kleie schneidet den Film).
    - *Doppelcharge:* Knetzeit bleibt praktisch gleich; der Spiralhaken arbeitet mit mehr Masse eher sauberer. Teigendtemperatur genauer im Auge behalten.
12. Teigendtemperatur prüfen, Ziel ~26–27 °C.
13. **Doppelcharge — jetzt teilen:** mit befeuchteter Teigkarte in **zwei** graduierte Behälter zu je **~990 g** (auf der Waage tarieren). Startvolumen markieren, Deckel.
    > **Warum hier und nicht später:** Nach dem Mix ist die Masse homogen und strukturlos — Teilen kostet nichts. Nach der Stockgare müsstest du einen 84-%-Teig zerschneiden und nachformen: Gas raus, Struktur zerstört, genau gegen die Spannungsform-Logik. **Ab hier laufen beide Behälter exakt nach der Einzelbrot-Kalibrierung** — Stockgare, Form, Retard, Backen unverändert.
    - *Einzelbrot:* wie gehabt in **einen** Behälter.

### Stockgare · Raumtemperatur · pH-gesteuert (passiv, ~4–6 h)

14. Bei Raumtemperatur gehen lassen. Coil Fold mit befeuchteter Teigkarte nach ~60 und ~150 min (je ~20 s, kein Handkontakt). Dritter Fold, wenn noch sehr schlaff. *(Doppelcharge: beide Behälter gleich behandeln.)*
15. **Ende (V18-Kernänderung): pH ~4,7 und +30–50 % Volumen,** Poke-Test federt zügig zurück. **Deutlich jünger als V16/V17** — der 16-h-Retard macht die Reife fertig. (Bei ~21 °C grob ~4–6 h; **pH ist Master**.)
    > **Kalibrieren am Ergebnis:** Läuft er noch breit / flach → **jünger** beenden (pH ~4,75 / +30 %). Wird er dicht und platzt seitlich unkontrolliert auf → einen Tick **reifer** (pH ~4,65 / +50 %).
    > *pH bei Doppelcharge:* in **einem** Behälter messen (beide sind identisch), nicht doppelt stechen.

### Formen mit Oberflächenspannung (~2 min aktiv je Laib)

16. Gärkorb bemehlen — **reines Reismehl** (nicht mehr 1:1 mit Weizen-VK; Vollkorn-Staub verkohlt und schmeckt bitter, s. 6.1). **Spannungsform** (nicht reine Schwerkraft):
    1. Teig mit nasser Teigkarte auf leicht bemehlte/befeuchtete Fläche stürzen.
    2. Mit nasser Karte 3–4 Ränder locker zur Mitte einschlagen (lose Hülle) — **nicht** kräftig entgasen, nur Spannung aufbauen.
    3. Paket umdrehen (glatte Seite oben), mit der Karte 2–3× sanft „unterziehen"/spannen, bis die Oberfläche merklich strafft.
    4. **2–3 min setzen lassen**, damit die Haut fixiert, dann Naht **oben** in den Gärkorb.
    - *Jüngerer, festerer V18-Teig hält die Spannung besser.*
    - **Low-Effort-Fallback:** Schwerkraft, Naht oben, kein Nachformen. Nachteil: flacher/breiter.

### Kühlretardierung (kalt)

17. Gärkörbe in Plastikbeutel, **Kühlschrank 4 °C, ~16 h** (flexibel ~14–18 h). Da die Stockgare jetzt jünger endet, liegt die Reife am Ende des Retards **im Zielfenster** statt darüber.
    - **Doppelcharge:** Laib 2 bleibt im Kühlschrank, bis Laib 1 gebacken ist — er bekommt dadurch ~75–80 min mehr Retard und liegt damit weiterhin im 14–18-h-Fenster.
    - **RT-Alternative:** ~1,5–2,5 h bei Raumtemperatur bis Poke-Test, dann sofort backen. Nachteil: schwerer einzuschneiden, flacher, weniger Chia-Hydration.

---

## TAG 2 — Backtag

### Vorheizen (2 min aktiv, ≥ 50 min passiv)

18. Pizzastein mittlere Schiene, 250 °C Ober-/Unterhitze, **≥ 50 min** (Stein wirklich durchheizen — der Boden-Wärmestoß treibt den Sprung), Wassertank füllen.

### Backen (5 min aktiv) — 4 Phasen

19. Teig kalt aus dem Kühlschrank auf Backpapier stürzen, 1 tiefer Schnitt (~45°, ~1,5 cm). *Mit gespannter Haut + jüngerem Teig öffnet der Schnitt zuverlässiger — flacher Winkel, entschlossen ziehen.* Überschüssiges Bemehlungsmehl abklopfen.

**Standardprofil (V18):**

| Phase | Temp. | Dampf | Dauer |
|---|---|---|---|
| 1 Ofentrieb | 250 °C | voll (Stufe 3) | 12–15 min |
| 2 Krustenbildung | 220 °C | aus (kurz lüften) | 18 min |
| 3 Krumensetzung | 200 °C | aus | bis Kern 98 °C |
| 4 Crisp Finish (opt.) | 210 °C | Heißluft | 5 min |

**Hellere Kruste (V18.1) — Phase 1 identisch, nur die zweite Hälfte gezähmt:**

| Phase | Temp. | Dampf | Dauer |
|---|---|---|---|
| 1 Ofentrieb | **250 °C (unverändert)** | **voll, 3–5 min länger halten** | 15–18 min |
| 2 Krustenbildung | **205 °C** | aus (kurz lüften) | 18 min |
| 3 Krumensetzung | **185 °C** | aus, ggf. **Alu-Zelt** locker auflegen | bis Kern 98 °C |
| 4 Crisp Finish | **entfällt** | – | – |

> **Dampf-Timing:** Voller Dampf über die ganze Phase 1 hält die Kruste dehnbar, solange der Trieb läuft — erst zu Phase 2 ablassen. Die 3–5 min Verlängerung wirken doppelt (Trieb ↑, Bräunung ↓); nicht weiter ausdehnen, sonst ledrige Kruste.

> **Kern 98 °C (nicht 97) — nicht verhandelbar:** Chia-, Psyllium- und Akazie-/Hafergele müssen vollständig durchwärmt resolidifizieren, sonst gummige Krume. Das hellere Profil verlängert die Backzeit um ~5–10 min — die Kerntemperatur bleibt das Abbruchkriterium, nicht die Uhr.

**Doppelcharge — sequenziell backen, nicht gleichzeitig:**

> Zwei kalte ~990-g-Laibe auf einem Stein sind zwei Wärmesenken: die Steinoberfläche bricht ein, der Boden-Wärmestoß fehlt, sie beschatten sich gegenseitig und teilen sich den Dampf — genau der Ofentrieb, um den es in V18 geht.
> **Ablauf:** Laib 1 backen → Laib 2 bleibt im Kühlschrank → Stein **15–20 min bei 250 °C erholen** lassen → Wassertank auffüllen → Laib 2 backen. Ofenzeit gesamt ~2:15.

### Auskühlen

20. Auf Gitterrost ≥ 4 h (besser 6 h) — die Gele setzen, resistente Stärke bildet sich, der Biss wird glatt. Vorher anschneiden = gummig.
    - *Doppelcharge:* Laib 2 vollständig auskühlen lassen, dann **geschnitten einfrieren** — scheibenweise entnehmbar, kein Qualitätsverlust.

---

## 4. Zeitplan

**Einzelbrot (Anschnitt So. mittags):**

| Zeit | Schritt | aktiv |
|---|---|---|
| Fr. 20:00 | Levain ansetzen (RT) | 3 min |
| Sa. 08:00 | **Soak-Start-Gate** (Levain steigend, ~4,4–4,6) + 35 g ASG → Kühlschrank | 3 min |
| Sa. 08:10 | Phytase-Soak 45 °C (Wasser ~58–60 °C vorgewärmt) | 5 min |
| Sa. 09:15 | Saltolyse (RT) | 3 min |
| Sa. 09:45 | **Finalmix + Reife-Check** (Float, pH ~4,3) | 10 min |
| Sa. 10:00–~15:00 | Stockgare RT + 2 Coil Folds bis **pH ~4,7 / +30–50 %** | 1 min |
| Sa. ~15:00 | Spannungsform, in Kühlschrank | 2 min |
| So. ~07:00 | Vorheizen | 2 min |
| So. ~07:50 | Backen | 5 min |
| **Σ aktiv** | | **~34 min** |

**Doppelcharge — Abweichungen:** Gate ~15–20 min früher (größeres Δ) · Abkühlen +10 min · Teilen beim Finalmix (+2 min) · zweite Spannungsform (+2 min) · Backen sequenziell (Ofenzeit ~2:15 statt ~1 h).
**Σ aktiv ~42 min für zwei Laibe** statt ~68 min für zwei Einzelbackungen. Der Gewinn liegt in der Vorbereitung, nicht im Backen.

---

## 5. Anstellgut-Kreislauf

Kein separater Starter nötig — der Levain erneuert das Anstellgut bei jedem Backen.

```
Kühlschrank-ASG (15 g │ Doppel: 24 g)
└─ Abend, RT, über Nacht ──► reifer Levain (~165 g │ ~264 g)
   ├─  35 g ──► Kühlschrank = ASG fürs nächste Brot   (gezogen am Soak-Start-Gate)
   ├─ 100 g │ 200 g ──► Hauptteig                      (zugegeben am Finalmix, pH ~4,3)
   └─ ~30 g │ ~29 g  Puffer/Rest
```

---

## 6. Erwartete Krume, Kruste & Stellschrauben

**Krume:** gleichmäßig mittel-offen, feucht, weich — kein grobporiges Weißmehlbild (bei 100 % VK + Modul-Last physikalisch nicht erreichbar). Mit jüngerem Gare-Ende, weniger VWG/Psyllium, Ascorbinsäure und Spannungsform ist ein **spürbar höherer Laib** zu erwarten.

### 6.1 Krustenfarbe — warum sie dunkel wird und was hilft

**Phasentrennung als Grundprinzip:** Der Ofentrieb entsteht fast vollständig in **Phase 1** — unter vollem Dampf bleibt die Oberfläche nass bei ~100 °C, es bräunt kaum. Die Bräunung passiert überwiegend in **Phase 2–4** nach dem Ablassen. Beide Ziele sind damit **entkoppelbar**: Phase 1 aggressiv lassen, die zweite Hälfte zähmen.

**Strukturelle Bräunungstreiber in diesem Rezept:**
- **45-°C-Soak** = auch ein Amylase-Fenster → erzeugt Maltose (Maillard-Substrat).
- **Keimmehl 10 %** → zusätzliche Amylase *und* freie Zucker. Stärkster rezeptseitiger Treiber.
- **Roggen 15 %** → höhere Amylaseaktivität, mehr freie Zucker.
- **16 h Retard** → reichert reduzierende Zucker an der Oberfläche an.
- **Jüngerer V18-Teig** → mehr unvergorener Restzucker + weniger Säure (Säure hemmt Maillard).
- **Pizzastein, 50 min bei 250 °C** → sehr hohe gespeicherte Energie → dunkler Boden.

**Hebel, nach Kosten geordnet:**
1. **Phase 4 streichen.** Heißluft ist der aggressivste Bräuner (bewegte Luft, schnellerer Wärmeübergang). Kostet nur Knusprigkeit.
2. **Phase 2/3 senken** (220 → 205 °C, 200 → 185 °C). Bräunung skaliert überproportional mit der Oberflächentemperatur, die Backzeit nur linear → netto klar heller. Kostet ~5–10 min Backzeit.
3. **Alu-Zelt für Phase 3** — locker auflegen, schirmt Strahlungswärme ab und friert die Farbe ein, während der Kern hochzieht. Stärkster gezielter Hebel.
4. **Dampf 3–5 min länger** (in Phase 2 hinein) — Verdunstungskühlung hält die Oberfläche bei ~100 °C. Hilft zusätzlich dem Trieb.
5. **Nur der Boden dunkel?** Nach Phase 1 ein zweites Blech unterschieben oder den Laib vom Stein auf den Rost umsetzen.
6. **Bemehlung**: reines Reismehl statt 1:1 mit Weizen-VK — Vollkorn-Staub verkohlt und schmeckt bitter. Überschuss vor dem Einschießen abklopfen.
7. **Rezeptseitig:** Keimmehl 10 → 5 % senkt Amylase *und* Protease (doppelter Nutzen, s. 6.2). Roggen 15 → 12 % wirkt schwächer.

> **Nicht tun:** Farbe über **längere Gare** korrigieren (blasse Kruste = übergar). Das ist der einzige Hebel, der den V18-Trieb-Gewinn wieder kassiert. Ebenso: **kein diastatisches Backmalz** zugeben.

### 6.2 Nächste Iterationsstufe (falls noch luftiger gewünscht)

1. **VWG 4 % → 3 %.** Kostenlos, dehnbareres Netz.
2. **Teil des starken Weizens aus dem Soak** (75–100 g erst bei der Saltolyse). Schützt das Hauptgluten vor dem warmen Protease-/Amylase-Bad; Roggen + Kleie machen im Soak die Phytase-Arbeit, die Säuerung holt den Rest. Geringe Mineralkosten.
3. **Keimmehl 10 % → 5 %.** Weniger Protease → weniger Glutenabbau. *Zusätzlich: hellere Kruste.*
4. **Chia teilschroten** (15 g ganz + 10 g geschrotet). Weniger harte Störpartikel im Film. *Kostet Samen-Textur.*
5. **Roggen 15 % → 12 %.** Reiner Aroma-/Trieb-Trade.
6. **Gedeckt backen** (Cloche/Gusstopf, Phase 1). Physikalisch stärkster Einzelhebel — eigenes Dampfpolster. *Bricht „freigeschoben"; bei Doppelcharge ohnehin sequenziell.*

### 6.3 Fehlerbilder

**Teig läuft breit:** Stockgare jünger beenden (pH ~4,75), Hydratation −5 bis −10 g, Retard 16 h.
**Krume gummig:** Auskühlzeit ↑, Kern sicher 98 °C, Soak nicht über 45 min. *Bleiben Chiasamen hart → voller Retard oder teilschroten.*
**Zu sauer:** Stockgare noch jünger beenden, Levain jünger einsetzen (Δ kleiner), Retard ≤ 14 h.
**Zink-/Eisen-Maximierung am Tisch:** Brot mit Vitamin-C-Quelle essen (Paprika, Tomate, etwas Zitrone).

---

## 8. Doppelcharge — Kurzreferenz

| Punkt | Regel |
|---|---|
| **Teilungszeitpunkt** | Direkt nach dem Finalmix, 2 × ~990 g auf der Waage |
| **Levain** | ×1,6 (24 / 120 / 120 g) — ASG-Rückstellung bleibt 35 g |
| **Hauptteig** | ×2 (alle Positionen) |
| **Wilfa** | ~1,98 kg = ~40 % der 5-kg-Kapazität — unkritisch |
| **Instant Pot** | Wasser auf ~58–60 °C vorwärmen (Mischtemperatur ist mengenunabhängig) |
| **Abkühlen** | In die Wilfa-Schüssel umfüllen; Ziel ~32 °C statt 34 °C |
| **Δ (Levain)** | Größer als beim Einzelbrot → Gate früher, separat protokollieren |
| **Ab Stockgare** | Beide Behälter exakt nach Einzelbrot-Kalibrierung |
| **Backen** | Sequenziell, Stein 15–20 min erholen, Wassertank auffüllen |
| **Laib 2** | Bleibt im Kühlschrank (+75–80 min Retard, weiterhin im Fenster) |
| **Lagerung** | Ausgekühlt, geschnitten einfrieren |

---

## 7. Mitback-Protokoll (zum Eintragen)

| Feld | Wert |
|---|---|
| Datum / Raumtemp. | __ / __ °C |
| **Charge (1 / 2 Laibe)** | __ |
| Mehl / Eiweißgehalt | __ / __ g |
| VWG-Menge (4 % / 3 %) | __ g |
| Hydratation (84 / 85 / 86 %) | __ % |
| Levain-pH am **Soak-Start-Gate** | __ |
| Vorhergesagter Peak (in h) | __ |
| **Soak-Wassertemp. / erreichte Mischtemp.** | __ °C / __ °C |
| Levain-pH beim **Finalmix** (Ziel ~4,3) / Float | __ / __ |
| **Δ (Abfall Soak-Start → Finalmix)** | __ |
| Teigendtemp. nach Finalmix | __ °C |
| Coil Folds (Anzahl) | __ |
| **Stockgare-Ende: pH / Volumen** (Ziel ~4,7 / +30–50 %) | __ / __ % |
| Stockgare-Dauer | __ h |
| Form (Spannung / Schwerkraft) | __ |
| Retard: Dauer / Temp. | __ h / __ °C |
| **Backprofil (Standard / hell)** | __ |
| Phase 2 / Phase 3 Temp. | __ °C / __ °C |
| Alu-Zelt ab Minute | __ |
| Kern-Backtemp. erreicht / Gesamtbackzeit | __ °C / __ min |
| **Ofentrieb (Höhe / Öffnung)** | __ |
| **Krustenfarbe (1 hell – 5 sehr dunkel) / Boden separat** | __ / __ |
| Auskühlzeit | __ h |
| Krume (Porung/Feuchte/Biss) | __ |
| Anpassung nächstes Mal | __ |
