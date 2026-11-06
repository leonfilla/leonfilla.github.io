---
titel: Vollkorn-Sauerteigbrot V18.1
status: aktiv
datum: '2026-07-09'
quelle:
  typ: claude
  url: https://claude.ai/chat/2acded25-5345-4b43-9ec8-82eace209a98
  hinweis: Vollkornbrot mit besserer Porung optimieren
importiert: true
linie: vollkorn-sauerteig
version: V18.1
variante: Module A · C · D-Akazie
fokus: "100 % Vollkorn, frei geschoben, maschinell und pH-gesteuert – Ofentrieb über ein jüngeres Gare-Ende statt über weniger Fasern. Mit 45-°C-Phytase-Soak, Keimmehl, ganzer Chia und Akazienfaser; V18.1 ergänzt Doppelcharge und ein helleres Backprofil."
ergebnis: 1 Laib, ca. 990 g Teig
zeit: {aktiv: 34, gesamt: 2160}
geraete: [instant-pot-pro-max, wilfa-probaker, bosch-hng978, apera-ph60f, kernthermometer]
tags: [Sauerteig, Vollkorn, Meal Prep]
changelog:
  - {version: "V18", text: "Stockgare jünger beenden: pH ca. 4,7 und +30–50 % statt pH 4,62–4,65 und +60–70 %"}
  - {version: "V18", text: "Vitalkleber 25 → 20 g (Pfad zu 3 %), Psyllium 7 → 5 g, Wasser −10 g (86 → 84 %)"}
  - {version: "V18", text: "Ascorbinsäure als Standard; Levain-Check vom Soak-Start an den Finalmix verlegt"}
  - {version: "V18.1", text: "Teigformel unverändert; neu: Doppelcharge mit Teilung direkt nach dem Finalmix"}
  - {version: "V18.1", text: "Helleres Backprofil für Phase 2–4, Phase 1 unverändert; Gärkorb nur mit Reismehl"}
brot:
  teiggewicht: 990
  kerntemperatur: 98
  gare:
    - {phase: "Levain", temp: "ca. 21", zeit: "10–14 h", ph: "4.4–4.6 am Soak-Start"}
    - {phase: "Phytase-Soak (Instant Pot, Sous Vide)", temp: 45, zeit: "45 min"}
    - {phase: "Abkühlen", temp: "auf ca. 34", zeit: "15–20 min"}
    - {phase: "Saltolyse", temp: "Raumtemperatur", zeit: "25 min"}
    - {phase: "Levain beim Finalmix", ph: 4.3}
    - {phase: "Stockgare mit 2 Coil Folds", temp: "Raumtemperatur", zeit: "ca. 4–6 h, +30–50 %", ph: 4.7}
    - {phase: "Kaltgare im Gärkorb", temp: 4, zeit: "ca. 16 h (14–18 h)"}
  backprofil:
    - {phase: "Vorheizen mit Pizzastein, mittlere Schiene", temp: 250, zeit: "mind. 50 min"}
    - {phase: "1 Ofentrieb", temp: 250, dampf: "voll (Stufe 3)", zeit: "12–15 min"}
    - {phase: "2 Krustenbildung", temp: 220, dampf: "aus, kurz lüften", zeit: "18 min"}
    - {phase: "3 Krumensetzung", temp: 200, dampf: "aus", zeit: "bis 98 °C Kern"}
    - {phase: "4 Crisp Finish (optional)", temp: 210, dampf: "Heißluft", zeit: "5 min"}
zutaten:
  - {gruppe: "Levain", name: "Anstellgut", menge: 15, einheit: "g"}
  - {gruppe: "Levain", name: "Weizenvollkornmehl, fein, kleberstark", menge: 75, einheit: "g", mehl: true}
  - {gruppe: "Levain", name: "Wasser, Raumtemperatur", menge: 75, einheit: "g", wasser: 1}
  - {gruppe: "Phytase-Soak", name: "Weizenvollkornmehl, fein, backstark", menge: 275, einheit: "g", mehl: true, hinweis: "ca. 13,8 % Eiweiß"}
  - {gruppe: "Phytase-Soak", name: "Gekeimtes Weizen- oder Dinkelvollkornmehl", menge: 50, einheit: "g", mehl: true, hinweis: "Modul A"}
  - {gruppe: "Phytase-Soak", name: "Roggenvollkornmehl, fein", menge: 75, einheit: "g", mehl: true}
  - {gruppe: "Phytase-Soak", name: "Hafervollkornmehl, fein", menge: 50, einheit: "g", mehl: true}
  - {gruppe: "Phytase-Soak", name: "Chia, ganz", menge: 25, einheit: "g", hinweis: "Modul C"}
  - {gruppe: "Phytase-Soak", name: "Akazienfaser", menge: 10, einheit: "g", hinweis: "Modul D"}
  - {gruppe: "Phytase-Soak", name: "Wasser, 55–60 °C", menge: 320, einheit: "g", wasser: 1}
  - {gruppe: "Saltolyse", name: "Salz", menge: 10, einheit: "g"}
  - {gruppe: "Saltolyse", name: "Vitalkleber", menge: 20, einheit: "g", hinweis: "vorher trocken mit dem Psyllium mischen"}
  - {gruppe: "Saltolyse", name: "Psylliumschalen, fein", menge: 5, einheit: "g"}
  - {gruppe: "Saltolyse", name: "Ascorbinsäure", menge: 0.05, einheit: "g"}
  - {gruppe: "Saltolyse", name: "Wasser", menge: 50, einheit: "g", wasser: 1}
  - {gruppe: "Finalmix", name: "Levain, reif", menge: 100, einheit: "g", hinweis: "35 g als neues Anstellgut zurückstellen, Rest Puffer"}
schritte:
  - {titel: "Fr 20:00 – Levain ansetzen", text: "15 g Anstellgut, 75 g Weizenvollkornmehl und 75 g Wasser klümpchenfrei verrühren, locker abdecken, Füllstand markieren und bei Raumtemperatur reifen lassen.", timer: 43200}
  - {titel: "Sa 08:00 – Soak-Start prüfen", text: "Levain deutlich gewölbt und noch steigend, pH ca. 4,4–4,6. 35 g als neues Anstellgut in den Kühlschrank."}
  - {titel: "Soak mischen", text: "275 g Weizenvollkorn, 50 g Keimmehl, 75 g Roggen, 50 g Hafer, 25 g Chia, 10 g Akazienfaser und 320 g Wasser (55–60 °C) homogen verrühren – ohne Salz, Vitalkleber, Psyllium, Ascorbinsäure und Levain."}
  - {titel: "Phytase-Soak", text: "Abgedeckt im Instant Pot bei Sous Vide 45 °C halten, nicht länger.", timer: 2700}
  - {titel: "Abkühlen", text: "Bei Raumtemperatur auf ca. 34 °C abkühlen lassen.", timer: 1080}
  - {titel: "Saltolyse", text: "10 g Salz, die trocken vermischten 20 g Vitalkleber und 5 g Psyllium, 0,05 g Ascorbinsäure und 50 g Wasser zugeben, mit dem K-Haken 2 Minuten auf Stufe 1 gerade homogen mischen."}
  - {titel: "Saltolyse ruhen lassen", text: "Abgedeckt bei Raumtemperatur ruhen lassen.", timer: 1500}
  - {titel: "09:45 – Levain prüfen", text: "Float positiv, pH ca. 4,3. Liegt er deutlich unter 4,2, trotzdem verwenden und die Stockgare am jüngeren Ende beenden."}
  - {titel: "Finalmix 1", text: "100 g Levain zugeben, mit dem Spiralhaken 3 Minuten Stufe 1, dann ruhen.", timer: 480}
  - {titel: "Finalmix 2", text: "3 Minuten Stufe 1–2, dann ruhen.", timer: 480}
  - {titel: "Finalmix 3", text: "3 Minuten Stufe 2 bis zum dünnen Fenster, eher früher prüfen. Teigendtemperatur ca. 26–27 °C.", timer: 180}
  - {titel: "Umfüllen", text: "Mit befeuchteter Teigkarte in einen graduierten Behälter geben, Startvolumen markieren."}
  - {titel: "Coil Fold 1", text: "Nach ca. 60 Minuten Coil Fold mit befeuchteter Teigkarte (ca. 20 Sekunden).", timer: 3600}
  - {titel: "Coil Fold 2", text: "Nach ca. 150 Minuten zweiter Coil Fold; einen dritten nur, wenn der Teig sehr schlaff ist.", timer: 5400}
  - {titel: "Stockgare beenden", text: "Bei pH ca. 4,7 und +30–50 % Volumen, Fingertest federt zügig zurück – pH ist maßgeblich."}
  - {titel: "Formen", text: "Gärkorb mit reinem Reismehl bemehlen. Teig mit nasser Karte stürzen, 3–4 Ränder locker einschlagen, umdrehen und 2–3-mal mit der Karte unterziehen, bis die Oberfläche strafft."}
  - {titel: "Haut setzen lassen", text: "2–3 Minuten liegen lassen, dann mit der Naht nach oben in den Gärkorb.", timer: 150}
  - {titel: "Kaltgare", text: "Im Beutel bei 4 °C ca. 16 Stunden kühlen.", timer: 57600}
  - {titel: "So 07:00 – Vorheizen", text: "Pizzastein auf mittlerer Schiene, mindestens 50 Minuten bei 250 °C Ober-/Unterhitze, Wassertank füllen.", timer: 3000}
  - {titel: "Einschneiden", text: "Kalt auf Backpapier stürzen, überschüssiges Mehl abklopfen und einmal ca. 1,5 cm tief im 45°-Winkel entschlossen einschneiden."}
  - {titel: "Ofentrieb", text: "250 °C mit vollem Dampf (Stufe 3).", timer: 780}
  - {titel: "Krustenbildung", text: "Dampf aus, kurz lüften, 18 Minuten bei 220 °C.", timer: 1080}
  - {titel: "Krumensetzung", text: "Bei 200 °C bis 98 °C Kerntemperatur backen; optional 5 Minuten Crisp Finish bei 210 °C Heißluft."}
  - {titel: "Auskühlen", text: "Mindestens 4, besser 6 Stunden auf dem Gitter auskühlen lassen.", timer: 14400}
---

## Warum so

Der lange Kaltretard säuert weiter und vollendet die Reife – endet die Stockgare schon bei +60–70 %, ist der Teig beim Einschießen über dem Peak und läuft flach; deshalb endet sie jung bei pH 4,7. Weniger Vitalkleber macht das Netz dehnbarer, weniger Psyllium friert das Volumen nicht so früh ein, Ascorbinsäure verbessert die Gashaltung. Der Soak bei 45 °C liegt nahe dem Phytase-Optimum (bessere Zink- und Eisenverfügbarkeit); 55–60 °C warmes Wasser bringt die Mischung direkt auf ca. 45 °C, über 60 °C beginnen Verkleisterung und Phytase-Schaden. Chia-, Psyllium- und Hafergele brauchen 98 °C Kern, um beim Abkühlen fest zu werden. Ein jüngerer Teig backt dunkler – das bestätigt, dass die Gare-Änderung greift.

## Stellschrauben

- Läuft breit → jünger beenden (pH ca. 4,75, +30 %), 5–10 g weniger Wasser, Retard 16 h
- Dicht und platzt seitlich → etwas reifer (pH ca. 4,65, +50 %)
- Zu fest → in 5-g-Schritten bis 86 % Wasser ins Soak; darüber nur mit mehr Psyllium
- Krume gummig → länger auskühlen, sicher 98 °C, Soak nicht über 45 Minuten; harte Chia → voller Retard oder teilschroten
- Zu sauer → Stockgare jünger, Levain jünger einsetzen, Retard höchstens 14 h
- Kruste zu dunkel → Crisp Finish streichen, Phase 2 auf 205 °C, Phase 3 auf 185 °C mit Alu-Zelt, Dampf 3–5 Minuten länger; nie über längere Gare korrigieren, kein Backmalz
- Nur der Boden dunkel → nach Phase 1 ein Blech unterschieben oder vom Stein auf den Rost

## Varianten

- **Helles Profil:** Phase 1 250 °C, voller Dampf 15–18 Minuten · Phase 2 205 °C 18 Minuten · Phase 3 185 °C mit Alu-Zelt bis 98 °C · kein Crisp Finish.
- **Doppelcharge:** Levain 24 g ASG + 120 g Mehl + 120 g Wasser, Hauptteig ×2, Soak-Gate 15–20 Minuten früher, nach dem Soak in die Wilfa-Schüssel umfüllen und auf ca. 32 °C kühlen, direkt nach dem Finalmix in 2 × ca. 990 g teilen, nacheinander backen (Stein 15–20 Minuten erholen lassen).
- **Ohne Keimmehl:** 325 g Weizenvollkorn, Soak 50 Minuten, Roggen optional 85 g.
- **Nächste Stufe für mehr Lockerheit:** Vitalkleber 3 %, 75–100 g Weizen erst zur Saltolyse, Keimmehl 5 %, Chia teilweise schroten, Roggen 12 %.
