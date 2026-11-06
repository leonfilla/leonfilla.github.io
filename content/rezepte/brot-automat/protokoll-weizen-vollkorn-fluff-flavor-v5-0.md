---
titel: Weizen-Vollkorn-Sauerteig Fluff & Flavor
status: aktiv
datum: '2026-02-02'
quelle: {typ: gemini, url: 'https://gemini.google.com/app/ff35960758945a73', hinweis: Bewerte die reine Knetfunktion von Sauerteigen des Panasonic SD-YR2540}
importiert: true
linie: protokoll-weizen-vollkorn-sauerteigbrot-high-hydra-4224d
version: V5.0
fokus: 'Weizenvollkorn-Sauerteig, der locker und trotzdem würzig wird: warmer Vorteig im Panasonic für maximale Hefeaktivität, Säure ausschließlich über 24 h Kaltgare.'
ergebnis: 1 Laib
zeit: {aktiv: 30, gesamt: 2020}
geraete: [panasonic-sd-yr2540, bosch-hng978]
tags: [Vollkorn, Sauerteig]
brot:
  programm: Menü 29 (Vorteig), Menü 31 (Mischen/Kneten)
  gare:
  - {phase: Vorteig im Panasonic, temp: 30, zeit: 3 h 15 min}
  - {phase: Autolyse, zeit: 30 min}
  - {phase: Stockgare, zeit: ca. 4 h}
  - {phase: Kaltgare, temp: 5, zeit: 24 h}
  backprofil:
  - {phase: Vorheizen (Stein), temp: 275, zeit: ≥ 45 min}
  - {phase: Dampfphase, temp: 250, dampf: Dampfstoß ein, zeit: 10 min}
  - {phase: Backphase, temp: 210, dampf: 'aus, Tür kurz öffnen', zeit: 30 min}
  - {phase: Crisp Finish, dampf: Crisp Finish, zeit: 10 min}
zutaten:
- {gruppe: Sauerteig, name: 'Anstellgut, kalt', menge: 40, einheit: g}
- {gruppe: Sauerteig, name: Weizenvollkornmehl, menge: 55, einheit: g, mehl: true}
- {gruppe: Sauerteig, name: 'Wasser, 35–40 °C', menge: 55, einheit: g, wasser: 1, hinweis: '50 g als Backup, 100 g in den Teig'}
- {gruppe: Kochstück, name: Weizenvollkornmehl, menge: 30, einheit: g, mehl: true}
- {gruppe: Kochstück, name: Wasser, menge: 150, einheit: g, wasser: 1}
- {gruppe: Hauptteig, name: 'Wasser, kalt', menge: 135, einheit: g, wasser: 1}
- {gruppe: Hauptteig, name: Zitronensaft, menge: 15, einheit: g}
- {gruppe: Hauptteig, name: Weizenvollkornmehl, menge: 340, einheit: g, mehl: true}
- {gruppe: Hauptteig, name: Weizenmehl Type 550, menge: 80, einheit: g, mehl: true}
- {gruppe: Hauptteig, name: Salz, menge: 12, einheit: g}
- {gruppe: Hauptteig, name: 'Wasser, kalt (Reserve)', menge: 20, einheit: g, wasser: 1, hinweis: nur bei Bedarf}
schritte:
- {titel: Vorteig ansetzen, text: '12:00: 40 g Anstellgut, 55 g Weizenvollkornmehl und 55 g Wasser (35–40 °C) im Panasonic-Behälter mischen, Menü 29 starten.', timer: 11700}
- {titel: Kochstück kochen, text: Parallel 30 g Vollkornmehl und 150 g Wasser aufkochen und in einer Schüssel mit Deckel abkühlen lassen.}
- {titel: Backup abnehmen, text: '15:15: Programm stoppen und 50 g Sauerteig als Backup in den Kühlschrank stellen.'}
- {titel: Autolyse mischen, text: 'Roggenhaken einsetzen. Kochstück, 135 g Wasser, 15 g Zitronensaft, 340 g Vollkornmehl und 80 g Type 550 zugeben und mit Menü 31 2 Minuten mischen.', timer: 120}
- {titel: Autolyse ruhen, text: 30 Minuten quellen lassen., timer: 1800}
- {titel: Kneten, text: '100 g Sauerteig und 12 g Salz zugeben und mit Menü 31 10 Minuten kneten. Bei Minute 8 prüfen: Teig muss sich lösen, Reservewasser nur bei Bedarf.', timer: 600}
- {titel: Stockgare, text: 'Teig in die Wanne geben und gehen lassen, bis +60–70 % Volumen (nicht verdoppeln).', timer: 14400}
- {titel: Coil Folds, text: Dreimal im Abstand von 45 Minuten sanft Coil Folds geben.}
- {titel: Formen, text: '20:00: Teig straff wirken und mit dem Schluss nach oben ins Gärkörbchen legen, Deckel drauf.'}
- {titel: Kaltgare, text: 24 Stunden bei 5 °C im Kühlschrank reifen lassen., timer: 86400}
- {titel: Vorheizen, text: 'Pizzastein auf Ebene 2, mindestens 45 Minuten auf 275 °C Ober-/Unterhitze.', timer: 2700}
- {titel: Einschießen, text: 'Teig auf den Stein stürzen und 1–1,5 cm tief im flachen Winkel einschneiden.'}
- {titel: Dampfphase, text: 'Auf 250 °C stellen und Dampfstoß einschalten, 10 Minuten.', timer: 600}
- {titel: Backphase, text: 'Dampfstoß aus, Tür kurz öffnen, auf 210 °C stellen und 30 Minuten backen.', timer: 1800}
- {titel: Crisp Finish, text: Crisp Finish einschalten und 10 Minuten bis zur tiefbraunen Kruste backen., timer: 600}
changelog:
- {version: V5.0, text: Vorteig 3 h 15 min warm im Panasonic statt bei Raumtemperatur}
- {version: V5.0, text: Kaltgare 12 → 24 h}
- {version: V5.0, text: Stockgare bei +60–70 % statt Verdopplung beenden}
---

## Warum so

Säure greift das Klebergerüst an, Lockerheit braucht ein starkes Gerüst – deshalb werden die Ziele getrennt. Die Wärme im Vorteig bevorzugt die Hefen und macht den Teig triebstark. Bei 5 °C arbeiten die Hefen kaum, Bakterien und Enzyme bilden aber weiter Säure und Aroma, ohne die Struktur abzubauen. Type 550 und Zitronensaft stützen das Gerüst gegen die Säure. Wer die Stockgare schon bei Verdopplung beendet, hat keinen Ofentrieb mehr übrig.

## Stellschrauben

- Teig hält das Gas nicht → länger kneten, bis er sich wirklich von der Wand löst
- Zu flach → Stockgare früher beenden, beim Wirken mehr Spannung aufbauen
