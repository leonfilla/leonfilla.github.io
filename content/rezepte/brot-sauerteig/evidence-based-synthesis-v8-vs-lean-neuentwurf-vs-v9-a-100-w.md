---
titel: Vollkorn-Sauerteigbrot V9
status: aktiv
datum: '2026-05-21'
quelle:
  typ: claude
  url: https://claude.ai/chat/1f1baaf8-2a5f-4084-89e7-3cc6e33c3012
  hinweis: Neues Brotrezept nach Anforderungen
importiert: true
linie: vollkorn-sauerteig
version: V9
fokus: "100 % Vollkorn (85 % Weizen, 15 % Roggen) mit 4 % Vitalkleber, frei geschoben – das Gerüst des schlanken Neuentwurfs plus ein salzfreies Phytase-Soak bei 45 °C vor der Levain-Zugabe. Ziel: über 80 % Phytatabbau bei mildem, milchsaurem Geschmack und offener Krume."
ergebnis: 1 Laib
zeit: {aktiv: 25, gesamt: 1680}
geraete: [wilfa-probaker, instant-pot-pro-max, bosch-hng978, apera-ph60f, kernthermometer]
tags: [Sauerteig, Vollkorn]
changelog:
  - {version: "V9", text: "Gerüst vom schlanken Neuentwurf: Roggen als Phytasequelle, milde Milchsäuregärung, volles Maschinenkneten, 4 % Vitalkleber"}
  - {version: "V9", text: "Neu: salzfreies Phytase-Soak der Vollkornmehle, 45 min bei 45 °C"}
  - {version: "V9", text: "Gegenüber V8 gestrichen: Tangzhong, Psyllium, Nährhefe, Melasse, Linsenmehl, Kürbiskernmehl, Leinsamen"}
  - {version: "V9", text: "Kein Dehnen und Falten, nur einmal formen; Hydration 78 %"}
brot:
  kerntemperatur: 97
  gare:
    - {phase: "Levain", temp: "26–28", zeit: "8–10 h", ph: 4.2}
    - {phase: "Phytase-Soak (salzfrei, Instant Pot Sous Vide)", temp: 45, zeit: "45 min", ph: "5.8–6.2"}
    - {phase: "Stockgare ohne Falten", temp: 28, zeit: "3,5–4,5 h, +60–70 %", ph: "4.55–4.65"}
    - {phase: "Kaltgare im Gärkorb", temp: 4, zeit: "14–18 h"}
  backprofil:
    - {phase: "Vorheizen mit Pizzastein, mittlere Schiene", temp: 250, zeit: "mind. 45 min nach Signal"}
    - {phase: "Ofentrieb", temp: 250, dampf: "Stufe 3", zeit: "0–15 min"}
    - {phase: "Ohne Dampf", temp: 220, dampf: "aus, ggf. lüften", zeit: "15–22 min"}
    - {phase: "Crisp Finish", temp: 210, dampf: "Entfeuchtung", zeit: "ab 22 min bis 97 °C Kern, gesamt 38–45 min"}
zutaten:
  - {gruppe: "Levain", name: "Anstellgut, Weizenvollkorn", menge: 10, einheit: "g"}
  - {gruppe: "Levain", name: "Weizenvollkornmehl", menge: 50, einheit: "g", mehl: true}
  - {gruppe: "Levain", name: "Wasser, 28 °C", menge: 50, einheit: "g", wasser: 1}
  - {gruppe: "Phytase-Soak", name: "Weizenvollkornmehl, backstark, fein", menge: 425, einheit: "g", mehl: true}
  - {gruppe: "Phytase-Soak", name: "Roggenvollkornmehl, fein", menge: 75, einheit: "g", mehl: true}
  - {gruppe: "Phytase-Soak", name: "Wasser", menge: 380, einheit: "g", wasser: 1}
  - {gruppe: "Hauptteig", name: "Levain", menge: 100, einheit: "g", hinweis: "reif, pH ca. 4,2"}
  - {gruppe: "Hauptteig", name: "Salz, fein", menge: 11, einheit: "g"}
  - {gruppe: "Hauptteig", name: "Vitalkleber", menge: 20, einheit: "g", mehl: true}
  - {gruppe: "Hauptteig", name: "Wasser", menge: 10, einheit: "g", wasser: 1}
  - {gruppe: "Einlage", name: "Geschälte Hanfsamen", menge: 20, einheit: "g"}
schritte:
  - {titel: "Levain ansetzen", text: "Am Vorabend 10 g Anstellgut, 50 g Weizenvollkornmehl und 50 g Wasser (28 °C) verrühren und bei 26–28 °C reifen lassen, bis pH ca. 4,2 und die Oberfläche durchgehend blasig ist.", timer: 32400}
  - {titel: "Soak mischen", text: "425 g Weizenvollkorn, 75 g Roggen und 380 g Wasser mit dem K-Haken auf niedriger Stufe 90 Sekunden mischen – ohne Salz, Vitalkleber, Levain und Hanf."}
  - {titel: "Phytase-Soak", text: "Abgedeckt im Instant Pot (Sous Vide, Schüssel im Wasserbad) bei einer Teigtemperatur von 45 ± 2 °C halten.", timer: 2700}
  - {titel: "Hauptteig zugeben", text: "Schüssel herausnehmen, 100 g Levain, 11 g Salz, 20 g Vitalkleber, 20 g Hanfsamen und 10 g Wasser zugeben. Ziel-Teigtemperatur 27–28 °C."}
  - {titel: "Einarbeiten", text: "Mit dem Spiralhaken 4 Minuten auf Stufe 1 einarbeiten.", timer: 240}
  - {titel: "Auskneten", text: "Auf Stufe 2 5–7 Minuten bis zum vollen Fenstertest kneten.", timer: 360}
  - {titel: "Stockgare", text: "In ein Gefäß mit geraden Wänden geben, Startvolumen markieren und bei 28 °C ohne Falten gehen lassen, bis +60–70 % Volumen und pH 4,55–4,65 (1 cm tief gemessen).", timer: 14400}
  - {titel: "Formen", text: "Auf leicht bemehlte Fläche stürzen, einmal sanft mit der Teigkarte rundschleifen und sofort mit der Naht nach oben in den bemehlten Gärkorb legen; mit Duschhaube abdecken."}
  - {titel: "Kaltgare", text: "Bei 4 °C 14–18 Stunden kühlen, nicht über 24 Stunden.", timer: 57600}
  - {titel: "Vorheizen", text: "Pizzastein auf mittlerer Schiene, 250 °C Ober-/Unterhitze; nach dem Signal noch mindestens 45 Minuten.", timer: 2700}
  - {titel: "Einschneiden", text: "Direkt aus dem Kühlschrank auf Backpapier stürzen, mit einem entschlossenen Schnitt (Klinge ca. 30°) einschneiden und auf den Stein ziehen."}
  - {titel: "Ofentrieb", text: "15 Minuten bei 250 °C mit Dampf Stufe 3.", timer: 900}
  - {titel: "Ohne Dampf", text: "Auf 220 °C ohne Dampf senken, wenn möglich lüften.", timer: 420}
  - {titel: "Crisp Finish", text: "Auf Crisp Finish bei 210 °C wechseln und bis 97 °C Kerntemperatur backen."}
  - {titel: "Auskühlen", text: "Mindestens 90 Minuten auf dem Gitter auskühlen lassen.", timer: 5400}
---

## Warum so

Getreidephytase arbeitet am besten bei pH 5,0–6,0 und 45–55 °C: Das salzfreie Soak bei 45 °C und dem natürlichen Mehl-pH baut voraussichtlich schon 40–60 % des Phytats ab, bevor der Levain dazukommt; Roggen liefert gut doppelt so viel Phytase wie Weizen. Die Stockgare läuft danach bei 28 °C für eine milde, milchsaure Note und endet bei pH 4,6 statt 4,2, damit die Gesamtsäure begrenzt bleibt. Tangzhong (65 °C zerstört Phytase), Psyllium, Lein, Linsen- und Kürbiskernmehl stören jeweils Ofentrieb oder Krume. 78 % Hydration halten den Laib ohne Topf auf dem Stein. Erwartet: ca. 85–92 % Phytatabbau, GI um 54.

## Stellschrauben

- Krume zu dicht → Hydration 80 % und Stockgare-Endpunkt pH 4,55
- Laib läuft breit → Hydration 76 % und Kaltgare 18 h
- Zu sauer → Stockgare bei pH 4,7 beenden, Teig nie über 30 °C
- Schwacher Ofentrieb → Levain-pH beim Einsatz prüfen (4,2 ± 0,1), sonst länger führen
- Erst zweimal unverändert backen, dann pro Backtag nur eine Variable ändern

## Varianten

- **Mehr Phytatabbau:** Soak auf 60 Minuten verlängern und 5 g frisch gemahlenen Roggen zugeben.
- **Im Topf gebacken:** Hydration bis 82 % möglich.
