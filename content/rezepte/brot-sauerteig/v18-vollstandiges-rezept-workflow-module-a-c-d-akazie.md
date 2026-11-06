---
titel: Vollkorn-Sauerteigbrot V18 (Module A, C, D)
status: archiv
datum: '2026-07-09'
quelle: {typ: claude, url: 'https://claude.ai/chat/2acded25-5345-4b43-9ec8-82eace209a98', hinweis: Vollkornbrot mit besserer Porung optimieren}
importiert: true
linie: vollkorn-sauerteig
version: V18
fokus: 100 % Vollkorn mit Keimmehl, ganzer Chia und Akazienfaser, so viel wie möglich bei Raumtemperatur. V18 holt den Ofentrieb über eine deutlich jüngere Stockgare und korrigiert, wann der Levain geprüft wird.
ergebnis: 1 freigeschobener Laib
zeit: {aktiv: 34, gesamt: 2440}
geraete: [wilfa-probaker, instant-pot-pro-max, apera-ph60f, kernthermometer, bosch-hng978]
tags: [Vollkorn, Sauerteig]
brot:
  kerntemperatur: 98
  gare:
  - {phase: Levain, temp: Raumtemperatur (~21), zeit: 10–14 h, ph: '4,4–4,6 beim Soak-Start, 4,3 beim Finalmix'}
  - {phase: Phytase-Soak, temp: 45, zeit: 45 min}
  - {phase: Abkühlen, temp: auf 34, zeit: 15–20 min}
  - {phase: Saltolyse, temp: Raumtemperatur, zeit: 25 min}
  - {phase: Stockgare, temp: Raumtemperatur, zeit: 4–6 h, ph: 4.7}
  - {phase: Retard, temp: 4, zeit: ca. 16 h}
  backprofil:
  - {phase: Vorheizen (Stein), temp: 250, zeit: ≥ 50 min}
  - {phase: Ofentrieb, temp: 250, dampf: voll (Stufe 3), zeit: 12–15 min}
  - {phase: Krustenbildung, temp: 220, dampf: 'aus, kurz lüften', zeit: 18 min}
  - {phase: Krumensetzung, temp: 200, dampf: aus, zeit: bis Kern 98 °C}
  - {phase: Crisp Finish (optional), temp: 210, dampf: Heißluft, zeit: 5 min}
zutaten:
- {gruppe: Levain, name: Anstellgut, menge: 15, einheit: g, hinweis: aus dem Kühlschrank}
- {gruppe: Levain, name: 'Weizenvollkornmehl, fein', menge: 75, einheit: g, mehl: true}
- {gruppe: Levain, name: 'Wasser, Raumtemperatur', menge: 75, einheit: g, wasser: 1, hinweis: '100 g in den Teig, 35 g als neues Anstellgut'}
- {gruppe: Phytase-Soak, name: 'Weizenvollkornmehl, fein, backstark', menge: 275, einheit: g, mehl: true}
- {gruppe: Phytase-Soak, name: Gekeimtes Weizen- oder Dinkelvollkornmehl, menge: 50, einheit: g, mehl: true, hinweis: Modul A}
- {gruppe: Phytase-Soak, name: 'Roggenvollkornmehl, fein', menge: 75, einheit: g, mehl: true}
- {gruppe: Phytase-Soak, name: 'Hafervollkornmehl, fein', menge: 50, einheit: g, mehl: true}
- {gruppe: Phytase-Soak, name: 'Chiasamen, ganz', menge: 25, einheit: g, hinweis: Modul C}
- {gruppe: Phytase-Soak, name: Akazienfaser, menge: 10, einheit: g, hinweis: Modul D}
- {gruppe: Phytase-Soak, name: Wasser, menge: 320, einheit: g, wasser: 1, hinweis: auf 45–50 °C vorgeheizt}
- {gruppe: Saltolyse, name: Salz, menge: 10, einheit: g}
- {gruppe: Saltolyse, name: Vitalkleber, menge: 20, einheit: g}
- {gruppe: Saltolyse, name: 'Psylliumschalen, fein', menge: 5, einheit: g}
- {gruppe: Saltolyse, name: Ascorbinsäure, menge: 0.05, einheit: g}
- {gruppe: Saltolyse, name: Wasser, menge: 50, einheit: g, wasser: 1}
- {gruppe: Finalmix, name: 'Levain, reif', menge: 100, einheit: g}
schritte:
- {titel: Levain ansetzen, text: 'Abends (ca. 20:00) 15 g Anstellgut, 75 g Weizenvollkornmehl und 75 g Wasser klümpchenfrei verrühren, locker abdecken, Füllstand markieren und bei Raumtemperatur stehen lassen.'}
- {titel: Soak-Start prüfen, text: 'Morgens (ca. 08:00) starten, wenn der Levain deutlich gewölbt ist, noch steigt und pH 4,4–4,6 zeigt.'}
- {titel: Anstellgut zurückstellen, text: 35 g reifen Levain in ein sauberes Glas füllen und in den Kühlschrank stellen.}
- {titel: Soak mischen, text: '275 g Weizenvollkornmehl, 50 g Keimmehl, 75 g Roggen-, 50 g Hafervollkornmehl, 25 g Chia, 10 g Akazienfaser und 320 g auf 45–50 °C vorgeheiztes Wasser homogen mischen. Kein Salz, kein Vitalkleber, kein Psyllium, kein Levain.'}
- {titel: Phytase-Soak, text: 'Abgedeckt im Instant Pot 45 Minuten bei 45 °C (Sous Vide) halten, nicht länger.', timer: 2700}
- {titel: Abkühlen, text: Bei Raumtemperatur auf ca. 34 °C abkühlen lassen., timer: 1080}
- {titel: Saltolyse einarbeiten, text: '20 g Vitalkleber trocken mit 5 g Psyllium mischen. Mit 10 g Salz, 0,05 g Ascorbinsäure und 50 g Wasser zugeben und 2 Minuten mit dem K-Haken auf Stufe 1 homogen mischen.', timer: 120}
- {titel: Saltolyse ruhen, text: Abgedeckt 25 Minuten bei Raumtemperatur ruhen lassen., timer: 1500}
- {titel: Reife-Check, text: 'Levain prüfen: schwimmt und pH ca. 4,3. Dann 100 g Levain zugeben.'}
- {titel: Intervallkneten, text: 'Mit dem Spiralhaken 3 Minuten Stufe 1, 5 Minuten Ruhe, 3 Minuten Stufe 1–2, 5 Minuten Ruhe, 3 Minuten Stufe 2 – bis dünnes Fenster, eher früh prüfen.', timer: 1140}
- {titel: Umfüllen, text: 'Teigendtemperatur prüfen (Ziel 26–27 °C), Teig mit befeuchteter Teigkarte in einen graduierten Behälter füllen, Volumen markieren, Deckel auflegen.'}
- {titel: Stockgare, text: 'Bei Raumtemperatur gehen lassen; nach ca. 60 und 150 Minuten je einen Coil Fold mit befeuchteter Teigkarte, bei sehr schlaffem Teig einen dritten.', timer: 16200}
- {titel: Stockgare beenden, text: 'Bei pH ca. 4,7 und +30–50 % Volumen beenden; die Delle federt zügig zurück.'}
- {titel: Spannung formen, text: 'Gärkorb mit Reismehl und Weizenvollkorn 1:1 bemehlen. Teig mit nasser Karte auf die Fläche stürzen, 3–4 Ränder locker zur Mitte schlagen, umdrehen und 2–3 Mal unterziehen, bis die Oberfläche strafft.'}
- {titel: Haut setzen lassen, text: '2–3 Minuten ruhen lassen, dann mit der Naht nach oben in den Gärkorb legen.', timer: 150}
- {titel: Retard, text: Gärkorb in einem Beutel ca. 16 Stunden bei 4 °C kühlen., timer: 57600}
- {titel: Ofen vorheizen, text: 'Pizzastein mittlere Schiene, 250 °C Ober-/Unterhitze, mindestens 50 Minuten, Wassertank füllen.', timer: 3000}
- {titel: Einschneiden, text: 'Teig kalt auf Backpapier stürzen und einmal tief (ca. 45°, 1,5 cm) einschneiden.'}
- {titel: Ofentrieb, text: 12–15 Minuten bei 250 °C mit vollem Dampf backen., timer: 840}
- {titel: Krustenbildung, text: Kurz lüften und 18 Minuten bei 220 °C ohne Dampf backen., timer: 1080}
- {titel: Krumensetzung, text: Bei 200 °C ohne Dampf bis 98 °C Kerntemperatur backen.}
- {titel: Crisp Finish, text: Optional 5 Minuten bei 210 °C Heißluft., timer: 300}
- {titel: Auskühlen, text: 'Mindestens 4 Stunden, besser 6, auf dem Gitterrost auskühlen lassen.', timer: 14400}
changelog:
- {version: V18, text: 'Stockgare-Ende pH ca. 4,7 und +30–50 % statt pH 4,62–4,65 und +60–70 %'}
- {version: V18, text: Vitalkleber 25 → 20 g}
- {version: V18, text: 'Psyllium 7 → 5 g, Soak-Wasser 330 → 320 g (86 → 84 %)'}
- {version: V18, text: Ascorbinsäure von optional zu Standard}
- {version: V18, text: 'Levain-Gate: Soak-Start auf steigender Kurve, Reife-Check erst beim Finalmix'}
---

## Warum so

Der 16-h-Retard säuert weiter und vollendet die Reife; wer schon bei +60–70 % einlagert, schießt über den Peak ein und bekommt einen flachen Laib – deshalb jünger beenden. Mit kleberstarkem Extrafein-Mehl ist weniger Vitalkleber nötig, ein dehnbareres Netz treibt besser. Weniger Psyllium friert das Volumen später ein; Mehl, Psyllium und Wasser werden als ein System verschoben. Der Levain geht erst 1,5–2 h nach Soak-Start in den Teig, deshalb startet der Soak bei steigender Kurve und die eigentliche Reifeprüfung sitzt beim Finalmix.

## Stellschrauben

- Läuft breit → Stockgare jünger beenden (pH ca. 4,75, +30 %), Wasser −5 bis −10 g
- Platzt seitlich, dicht → einen Tick reifer (pH ca. 4,65, +50 %)
- Teig zu fest → bis 86 % zurück (+10 g in den Soak)
- Krume gummig → Kern sicher 98 °C, länger auskühlen, Soak nicht über 45 min
- Zu sauer → Stockgare jünger beenden, Levain jünger, Retard ≤ 14 h
- Levain beim Finalmix unter pH 4,2 → nächstes Mal Soak früher starten
- Kein Keimmehl → 50 g mehr Weizenvollkorn, Soak 50 Minuten, Roggen optional 85 g

## Varianten

- Nächste Stufen für mehr Lockerheit: Vitalkleber 15 g, 75–100 g Weizen erst zur Saltolyse, Keimmehl 5 %, Chia teilschroten, Roggen 12 %
- Raumtemperatur statt Retard: 1,5–2,5 h bis Fingertest, dann sofort backen
- Seltener als alle 10 Tage backen: zurückgestelltes Anstellgut vor dem Kühlen einmal füttern (10 g + 20 g Mehl + 20 g Wasser)
