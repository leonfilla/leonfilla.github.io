---
titel: Temperatur pro Rezept auf der Oracle Jet – Was wirklich geht
status: aktiv
datum: '2026-04-19'
quelle:
  typ: claude
  url: https://claude.ai/chat/1f1ac57d-a7d5-433f-b42b-21074944bdb2
  hinweis: Alternativen zu Sage Oracle Jet mit Milchschaum
importiert: true
---

**Die Oracle Jet SES985 hat kein klassisches „Rezept speichern"-Menü mit Freitext-Namen.** Stattdessen überschreibt sie die Parameter jedes Werks-Drinks (Espresso, Flat White, Americano, Cold Brew …) direkt am Drink-Icon. Änderungen werden automatisch gespeichert, sobald du den Drink-Screen verlässt – ohne separaten Speicher-Dialog. Das heißt für deinen Anwendungsfall: Du kannst **nicht** drei Rezepte namens „Flat White hell", „Flat White mittel" und „Flat White Decaf" nebeneinander ablegen. Pragmatische Lösungen gibt es trotzdem – dazu unten mehr.

Die Brühtemperatur ist in **1 °C-Schritten** im Bereich von ca. 86–96 °C einstellbar, Werkseinstellung **93 °C**. Die offizielle Breville-Kommunikation beschreibt die Temperatur-Einstellung als **global** (wirkt auf alle Drinks), unabhängige Reviewer (Kaffeemacher, Coffeeness) berichten jedoch, dass die Temperatur im einzelnen Drink-Screen mitgespeichert wird. Vermutlich hat sich das per Firmware-Update geändert – prüfe deshalb an deinem Gerät, welches Verhalten die aktuelle Firmware zeigt.

## Wie Rezepte auf der Oracle Jet tatsächlich gespeichert werden

Jedes Werks-Drink-Icon (Espresso, Long Black/Americano, Flat White, Latte, Cappuccino, Babyccino, Hot Chocolate, Tea, Cold Brew, Cold Espresso; EU zusätzlich Café Shakerato, Milk Shakerato, Espresso Martini) ist ein eigener **Parameter-Slot**. Wenn du Dose, Ausgabe (ml oder Zeit), Pre-Infusion, Milchtemperatur und Milchtextur anpasst, bleiben diese Werte an diesem Icon haften, bis sie erneut geändert werden oder ein Factory Reset gefahren wird. **Händler wie Chris' Coffee sprechen von „bis zu 8 Custom Profilen"**, das offizielle Handbuch nennt keine konkrete Zahl; de facto hast du so viele personalisierte Rezepte wie Werks-Icons, die du anfasst.

**Pro Icon speicherbar sind:** Brühtemperatur (laut Reviewern), Brühausgabe (volumetrisch in g/ml oder zeitbasiert in s), Pre-Infusion-Zeit (je nach Drink-Modus), Milchtemperatur (45–75 °C in 1 °C-Schritten), Milchtextur (8 Schaum-Stufen), Milchtyp (Kuh/Soja/Mandel/Hafer) und das Drink-Icon selbst. **Nicht softwareseitig pro Rezept einstellbar ist die Dosis** – die Auto-Grind-Dose liefert standardmäßig ~22 g und wird mechanisch über das Tamping-Fan-Coupling (Inbusschlüssel) verändert. Das ist die wichtigste funktionale Einschränkung für deinen Anwendungsfall.

Die Namen der Drinks lassen sich nicht frei umbenennen, aber **die Icons können per Drag-and-Drop neu sortiert und per Long-Press ausgeblendet oder wiederhergestellt werden**. Komplett neue Drink-Typen erscheinen nur per OTA-Firmware-Update über WLAN, nicht durch Nutzer-Eingabe.

## So stellst du eine Temperatur pro Rezept ein – Schritt für Schritt

**Globale Temperatur ändern (wirkt auf alle Drinks):** Tippe auf dem Home-Screen das **Zahnrad-Icon (⚙) oben** an → **Drink Settings** → **Temperature settings** → Wert per Slider oder +/- in 1 °C-Schritten anpassen → zurück. Dieser Pfad ist im offiziellen Breville-Video „How to change the Brew Temperature on your Oracle Jet" dokumentiert.

**Drink-spezifisch einstellen und speichern (empfohlen für deinen Use Case):**
1. Home-Screen → das gewünschte Drink-Icon kurz **antippen** (z. B. Flat White).
2. Im Drink-Screen siehst du drei Phasen-Icons: **Grind/Tamp**, **Brew/Espresso** (Glas), **Milk/Steam** (Kännchen).
3. Tippe auf **Brew/Espresso** und passe Ausgabe (z. B. 36 g) sowie – falls sichtbar – Brühtemperatur und Pre-Infusion an.
4. Bei Milchdrinks: Milch-Icon antippen → Temperatur (z. B. 60 °C) und Foam-Level (1–8) setzen.
5. **Einfach zurück gehen**: Keine separate Speicher-Bestätigung – die Maschine verwendet diese Werte beim nächsten Tap auf das Icon automatisch.

**Wichtiger Workaround für dich:** Da du drei verschiedene Bohnen fährst, bietet sich dieses Mapping an:

| Deine Bohne | Werks-Drink als Slot nutzen | Temperatur | Rationale |
|---|---|---|---|
| Helle Röstung (Americano für dich) | **Americano / Long Black** | 95–96 °C | Längere Ratio passt zu Light Roast |
| Mittlere Röstung (Flat White für dich) | **Flat White** | 93–94 °C | Standard-Sweet-Spot für Milch |
| Decaf (Flat White Freundin) | **Latte** oder **Cappuccino** als Decaf-Slot belegen | 91–92 °C | Verfügbarer Milch-Drink-Slot, beschrifte ihn gedanklich als Decaf |

So hat jeder Slot automatisch die richtige Temperatur, Ratio und Milcheinstellung – ihr müsst nur jeweils das richtige Icon antippen. Für Light-Roast kannst du ungenutzte Icons wie **Cold Brew oder Hot Chocolate** per Long-Press ausblenden, damit dein Home-Screen aufgeräumter wirkt.

## Der entscheidende Haken: Dose und Temperaturaufbau

Zwei Limitationen solltest du vor dem Arrangement kennen. Erstens: **Die Dose ist nicht pro Rezept umschaltbar.** Wenn du für Light Roast 18 g und für Decaf 20 g willst, musst du mit einem Kompromiss-Dose arbeiten oder jedes Mal manuell die Schraube am Fan-Coupling verdrehen – unpraktisch. Meine Empfehlung: **eine feste Dose (z. B. 18–19 g) für alle drei Bohnen** und stattdessen Mahlgrad, Ratio und Temperatur als Stellschrauben nutzen.

Zweitens: **Die Oracle Jet hat einen „defensiven" Temperaturaufbau**, wie das Kaffeemacher-Labor nachgewiesen hat – die Zieltemperatur wird erst nach ca. 15–22 Sekunden Shot-Zeit erreicht. Für sehr helle Röstungen, die auf volle Hitze angewiesen sind, ist das ein bekannter Schwachpunkt. **Praxis-Tipp: Für Light Roast die Einstellung +1–2 °C über den Zielwert setzen** (also z. B. 95–96 °C, um real ~94 °C im Puck zu erreichen). Zusätzlich hilft ein 3–5 Sekunden Leer-Flush durch die Brühgruppe vor jedem Bezug, um die Gruppe zu temperieren.

## Temperatur-Empfehlungen nach Röstgrad

Die Temperatur ist das Feintuning, nicht der erste Hebel – Dose, Ratio und Mahlgrad zuerst. Für deine drei Bohnen auf der Oracle Jet gelten diese bewährten Bereiche, gestützt auf Kaffeemacher-Messungen, Barista Hustle, James Hoffmann und Scott Rao:

| Röstgrad | Display-Temp Oracle Jet | Ratio | Pre-Infusion | Mahlgrad relativ |
|---|---|---|---|---|
| **Helle Röstung** | **95–96 °C** (kompensiert Offset) | 1:2,5 bis 1:3 | lang (10–15 s) | feiner |
| **Mittlere Röstung** | **93–94 °C** | 1:2 bis 1:2,5 | mittel (6–10 s) | Standard |
| **Dunkle Röstung** | **91–92 °C** | 1:1,5 bis 1:2 | kurz (3–6 s) | gröber |
| **Decaf** (meist medium-dark) | **91–93 °C** | 1:2 | mittel (6–8 s) | deutlich feiner als caf |

**Decaf ist ein Sonderfall**: Die Entkoffeinierung öffnet die Bohnenstruktur, der Shot läuft bei gleichem Grind schneller, und hohe Temperaturen erzeugen schnell Bitterkeit. **Stelle Decaf deshalb typischerweise 1–2 °C niedriger als das coffeinhaltige Pendant** und mahle 5–7 Klicks feiner. Kaffeemacher und das Home-Barista-Forum sind sich hier einig. Für einen Flat White deiner Freundin mit Decaf ist **91 °C, 1:2, feiner Mahlgrad, 60 °C Milchtemperatur, Foam-Level 3–4** ein solider Startpunkt.

Für deinen Americano (hell) empfiehlt sich **95 °C, 1:2,5 bis 1:3 Espresso-Ratio, dann 90–120 ml Wasser bei 85–90 °C darauf**. Für deinen Flat White (mittel) **93 °C, 1:2, 18 g → 36 g in ca. 28 s, Milch 60–65 °C, Foam-Level 4**.

## App, Firmware und was du noch wissen solltest

Die Sage/Breville **Beanz-App** steuert primär Bohnen-Profile (Röstdatum, Empfehlungen), und WLAN liefert OTA-Firmware-Updates – neue Drinks wie Cold Brew und das Double-Tap-Purge-Feature kamen auf diesem Weg nach. **Eine echte Cloud-Synchronisation eigener Rezepte oder eine „Rezept-Bibliothek" in der App gibt es derzeit nicht.** Du kannst also nicht am Handy Rezepte komponieren und aufs Gerät schicken – alles läuft lokal am Touchscreen.

Zum Abschluss drei pragmatische Hinweise: Ein **Factory Reset löscht alle Anpassungen** (Menüpfad ⚙ → Machine Settings → Reset factory settings), also nur im Notfall. Die **Barista Guidance** auf dem Screen kann stören, wenn du abweichende Rezepte fährst – in Drink Settings abschaltbar. Und die **volumetrische Brewing-Steuerung** (Settings → Drink Settings → Brew control settings) ist reproduzierbarer als die zeitbasierte, weil sie direkt Gramm-Output misst – für deinen Dreibohnen-Workflow empfehlenswert.

## Fazit

Die Oracle Jet zwingt dich zu einem **Icon-als-Rezept-Workflow**: Belege jeden Werks-Drink mit genau einem deiner Anwendungsfälle und nutze Temperatur, Mahlgrad und Ratio als Unterscheidungsmerkmale. Drei Bohnen, drei Slots – das funktioniert. Die größte Einschränkung ist die nicht softwareseitig umschaltbare Dose; arbeite mit einer festen Dose von 18–19 g und passe die anderen Parameter an. Für Light Roasts kompensierst du den defensiven Temperaturaufbau mit +1–2 °C über dem rechnerischen Zielwert. Wenn du überwiegend Nordic-Light-Roasts auf Profi-Niveau extrahieren willst, stößt die Jet an ihre Grenzen – für deinen Mix aus Medium, Light-Medium und Decaf ist sie aber gut geeignet.
