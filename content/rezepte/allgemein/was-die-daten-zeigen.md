---
titel: Was die Daten zeigen
status: aktiv
datum: '2026-10-05'
quelle:
  typ: claude
  url: https://claude.ai/chat/0319a6cb-7c50-4060-814c-26b974734a75
  hinweis: Kaffee-Programme für 8g Portionen anpassen
importiert: true
---

Die Logs korrigieren zwei Annahmen aus meiner letzten Antwort. Die Programme unten ersetzen die vorherigen.

**Was die Daten zeigen**

- **Die echten Pausen sind andere.** La Esperanza 2 läuft mit 30/25/25 s, nicht mit 35/30/30. Das Programm „El Eucalipto/La Cristalina“ läuft mit 40/30/30 s und durchgehend 3,0 ml/s.
- **Die halbe Eucalipto drainiert fast genauso schnell wie die vollen Programme.** Nach Pour 2–4 sind 90 % durchgelaufen nach 15–19 s. Bei der vollen Esperanza sind es 15–18 s, bei der vollen Cristalina 12–14 s. Dein feinerer Mahlgrad gleicht das flachere Bett also hydraulisch fast vollständig aus. Damit kann ich die Pausen der vollen Programme direkt übernehmen.
- **Die Esperanza hat das längste Nachlaufen.** Nach Pour 4 braucht sie 31 s bis 98 %, die Cristalina 17 s. Die Esperanza baut ihre Pours außerdem aufeinander auf: Bei Pour 3 tropft sie noch mit 0,86 g/s. Ausgerechnet der kühlste und bitterkeitsanfälligste Abschnitt hat bei ihr also die längste Kontaktzeit. Deshalb bekommt Pour 4 bei der halben Esperanza **kein** +1 °C.
- **Flow-Raten:** Die Profile der vollen Programme bleiben. Ob die 3,3–3,5 ml/s der halben Eucalipto eine bewusste Anpassung an die halbe Menge waren, lässt sich ohne das Log der alten vollen Eucalipto nicht trennen. Höherer Flow wühlt ein flaches Bett zudem stärker auf.

**Halbe La Esperanza** (Mahlgrad 58 = 63 − 5, RPM 60)

| Pour | ml | °C | ml/s | Muster | Pause |
|---|---|---|---|---|---|
| 1 | 24 | 92 | 3,0 | Zentrum + Vibration | 30 s |
| 2 | 36 | 92 | 3,2 | Spirale | 25 s |
| 3 | 36 | 90 | 3,3 | Spirale | 25 s |
| 4 | 32 | 87 | 3,3 | Kreis | – |

**Halbe La Cristalina** (Mahlgrad deines vollen Programms − 5, RPM 60)

| Pour | ml | °C | ml/s | Muster | Pause |
|---|---|---|---|---|---|
| 1 | 24 | 91 | 3,0 | Zentrum + Vibration | 40 s, ab ~8.10. 35 s |
| 2 | 36 | 91 | 3,0 | Spirale | 30 s |
| 3 | 36 | 89 | 3,0 | Spirale | 30 s |
| 4 | 32 | 86 | 3,0 | Kreis | – |

Der Mahlgrad steht nicht im Export. Weil das volle Programm für beide Bohnen gilt, setze ich ihn relativ an. Bei 64 wären es 59.

Den langen Bloom bei der Cristalina stützen die Daten: Ihr Bloom läuft deutlich langsamer ab als der der Esperanza (90 % nach 17,6 s gegenüber 6,8 s). Das spricht für noch vorhandenes CO₂. Die Verkürzung ab dem 8.10. würde ich erst vornehmen, wenn sich das im Log angleicht.

Noch eine Randnotiz: Die halbe Eucalipto hält relativ mehr Wasser zurück, 24 von 128 ml statt 38–41 von 256. Der Grund ist die Papierretention von schätzungsweise 8 g, die bei halber Menge gleich bleibt. Die Tasse wird dadurch minimal konzentrierter. Das reicht nicht, um die Ratio zu ändern, erklärt aber, falls dir die halben Versionen etwas kräftiger vorkommen.
