---
titel: A. Levain und Soak entkoppeln
datum: '2026-10-12'
quelle:
  typ: claude
  url: https://claude.ai/chat/5f29d3a1-2693-4201-8c36-2700c641b383
  hinweis: Brotherstellung Prozessoptimierung
importiert: true
---

Die Abstimmung zwischen Levain und Soak ist aufwendig, weil zwei zeitkritische Abläufe aneinander gekoppelt sind: Der Levain muss genau 1,5–2 h nach Soak-Start auf dem Peak sein. Das Soak-Start-Gate, die Δ-Messung, der Feedforward-pH und das separate Δ bei der Doppelcharge gibt es nur wegen dieser Kopplung. Die ergiebigsten Fragen zielen deshalb darauf, einen der beiden Abläufe zeitlich unkritisch zu machen.

## A. Levain und Soak entkoppeln

**1. „Kann der Soak am Vorabend als gesalzenes Quellstück laufen?"**
Der Ablauf wäre: abends 45 min bei 45 °C, dann das Salz zugeben und über Nacht bei Raumtemperatur stehen lassen. Morgens würden VWG, Psyllium, Ascorbinsäure und Levain zugegeben, sobald der Levain auf dem Peak ist. Damit entfallen das Gate, die Δ-Messung, das Abkühlen und vermutlich die Saltolyse. Claude sollte drei Punkte klären:
- **Mikrobiologische Sicherheit:** Hemmen 2 % Salz bezogen auf das Gesamtmehl, im Quellstück also höher konzentriert, die Spontangärung ausreichend?
- **Enzymaktivität über Nacht:** Wie viel zusätzliche Amylase- und Proteaseaktivität entsteht bei Raumtemperatur? Das bedeutet mehr Bräunung und Glutenabbau, vor allem durch das Keimmehl.
- **Phytase:** Arbeitet sie über Nacht messbar weiter und bringt damit einen Zusatznutzen?

Diese Variante passt gut zu Hebel 2 aus 6.2: Der starke Weizen bleibt aus dem Quellstück heraus und kommt erst morgens dazu. Das Gluten wäre dann besser geschützt als heute.

**2. Falls der Soak morgens bleibt: „Wie verbreitere ich das Reifefenster des Levains auf über 1 h?"**
Infrage kommen ein festerer Levain mit 50–60 % Hydratation, ein anderes Verhältnis oder ein Levain, der nach dem Peak 1–3 h bei 4 °C gehalten wird. Damit entfiele nicht der Soak, sondern das Gate. Abzuwägen ist das Aroma: Feste Levains verschieben das Säurespektrum Richtung Essigsäure.

**3. „Kann der ~30-g-Puffer-Levain den Soak ansäuern?"**
Das schließt an die Phytase-Frage von vorhin an: Der Soak läuft heute bei pH ~6, das Phytase-Optimum liegt bei ~5–5,5. Die Mikroben im Puffer sterben bei 45 °C ab, die Säure bleibt aber wirksam. Der Puffer wäre damit kein Abfall mehr. Zu klären ist, wie viel Säure man für pH ~5,5 braucht und ob das die Amylase bremst, was die Bräunung verringern würde.

## B. Schritte zusammenlegen

**4. „Kann ich das Abkühlen durch Eis ersetzen?"**
Ein grober Überschlag (Mehl ~1,7 kJ/kg·K, ohne Topfverluste): Gibst du die 50 g Saltolysewasser als Eis zu, landet die Masse rechnerisch direkt bei ~34 °C. Das spart 15–20 min, bei der Doppelcharge 25–30 min, und den Wechsel der Schüssel. Claude sollte das sauber nachrechnen und prüfen, ob Eis die Verteilung von VWG und Psyllium stört. Crushed Ice wäre wahrscheinlich besser als Würfel.

**5. „Welche Funktion der Saltolyse übernehmen nicht ohnehin die Ruhepausen beim Intervallkneten?"**
Die Saltolyse leistet drei Dinge: Das Salz strafft das Gluten, das Psyllium quillt, und die Masse kühlt ab. Das Intervallkneten enthält bereits 2 × 5 min Ruhe. Möglicherweise reicht es, Salz, VWG und Psyllium direkt beim Finalmix zuzugeben.

**6. „Brauche ich den Instant Pot überhaupt?"**
Wenn das Wasser auf ~60 °C vorgewärmt ist und die Wilfa-Schüssel isoliert wird, etwa im Ofen bei Gärstufe oder mit Handtuch, fällt die Temperatur in 45 min vielleicht auf ~40 °C. Dort arbeitet die Phytase noch. Das spart ein Gefäß und das Umfüllen.

**7. „Lässt sich das Intervallkneten kürzen, wenn das Mehl schon lange hydratisiert ist?"**
Das gilt besonders in Kombination mit Frage 1: Nach einem Quellstück über Nacht entwickelt sich der Teig schneller.

**8. „Reicht ein Coil Fold?"**
Kleberstarkes Mehl, VWG und Spannungsform übernehmen bereits einen Teil der Strukturarbeit.

## C. Messaufwand

**9. „Welche Messungen werden redundant, sobald der Prozess stabil ist?"**
Mit Entkopplung entfallen Gate-pH und Δ ganz. Liegt der Levain-pH beim Finalmix über mehrere Backtage stabil bei 4,3 ± 0,05, reichen Float und Höhe. Als harte Messung bliebe dann nur das Ende der Stockgare. Das ist im Kern die Logik einer statistischen Prozesskontrolle: Gemessen wird nur noch, was tatsächlich schwankt.

## D. Doppelcharge

**10. „Wie lange braucht der Stein wirklich, um sich zu erholen?"**
Mit einem IR-Thermometer lässt sich das nach Laib 1 messen. Wenn 8–10 min reichen statt 15–20, verkürzt sich die Ofenzeit.

## Zur Qualitätssicherung

Änderungen nach dem Finalmix (Folds, Retard, Backen) kannst du sauber mit der Doppelcharge testen, als A/B-Vergleich aus einer homogenen Masse. Änderungen davor, also Quellstück, Eis und Saltolyse, betreffen die ganze Masse und brauchen aufeinanderfolgende Backtage mit sonst unveränderten Parametern.

Wenn du willst, rechne ich Frage 4 sauber durch und skizziere einen möglichen V19-Ablauf auf Basis von Frage 1, mit Zeitplan und den offenen Risiken.
