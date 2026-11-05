---
titel: Mobiles Setup
datum: '2026-08-20'
quelle:
  typ: claude
  url: https://claude.ai/chat/331f9ff3-3111-4e71-828f-76b987fff885
  hinweis: Mobiles Setup
importiert: true
---

Der Ständer ändert mehr als die Standfläche: Er ändert, was die Waage überhaupt messen kann. Steht der Pulsar direkt auf dem Carter, sind Brewer, Slurry und Gefäß eine gemeinsame Masse — die Waage sieht nur, was du eingießt, und der Durchtritt durchs Bett ist massenneutral, also unsichtbar. Auf einem Ständer trägt dieser die Brühkammer, und nur das Auffanggefäß steht auf der Aku Pro. Damit liest du in Echtzeit ausschließlich das, was das Bett passiert hat. Die Aku Pro zeigt die Flussrate in allen Modi und lässt sie in den Settings separat zuschalten; AKU Flow (Mode F) ist der passende Modus. Das macht aus „Ventil 2/3" — einer geräteindividuellen, driftenden Angabe — eine echte Regelgröße.

Zweiter Gewinn: Du kannst jetzt Filter spülen und vorheizen, ohne das Spülwasser in den Carter zu kippen. Spül den Papierfilter mit ~100 g kochendem Wasser, fang es im Carter auf, kipp es weg — Filtergeschmack raus, Brewer und Serviergefäß in einem Zug vorgeheizt. Das hebt die Slurry-Temperatur um 2–3 °C und bringt dich näher an den Startpunkt deines xbloom-Profils.

## Vollständiger Parametersatz — Variante A

**Bohne & Mahlen**
| Parameter | Wert |
|---|---|
| Dosis | 20,0 g |
| Post roast | 7–21 Tage (Anaerobe unter 7 Tagen lassen das Bett nach dem Bloom kollabieren) |
| Mahlgrad | Klick 74 ab Nullpunkt (≈925 µm nominell) |
| RDT | 1 Sprüher Wasser auf die Bohnen vor dem Mahlen |
| Bett | nach Einfüllen plan klopfen, nicht verdichten |

**Wasser**
| Parameter | Wert |
|---|---|
| Brühwasser gesamt | 320 g (1:16) |
| Calcium (Etikett) | 25–40 mg/L |
| Hydrogencarbonat | 40–60 mg/L |
| Natrium / Sulfat | so niedrig wie verfügbar |
| Kessel | einmal aufkochen, ~400 g füllen, **nicht nachkochen** |
| Rast vor Bloom | 45 s bei vorgeheiztem Brewer (sonst 30 s) |
| Temperaturverlauf | ≈95 / 92 / 90 / 88 / 86 / 85 °C |
| Rampensteuerung | Deckel zu = langsamer, Deckel auf = schneller |

**Ablauf mit Fluss- und Waagenzielen**

| Zeit | Guss | Ventil | Fluss | Waage (Ausbeute) |
|---|---|---|---|---|
| 0:00 | 60 g Bloom, WWDT-Swirl | **zu** | 0 | 0 g |
| 0:45 | 52 g | 2/3 auf | **1,2–1,4 g/s** | 0 g |
| 1:15 | 52 g | 2/3 | 1,2–1,4 | ~35 g |
| 1:45 | 52 g | 2/3 | 1,2–1,4 | ~75 g |
| 2:15 | 52 g | 2/3 | 1,2–1,4 | ~112 g |
| 2:45 | 52 g | 2/3 | 1,2–1,4 | ~150 g |
| 3:15 | — | **ganz auf** | 3 → 1 g/s | ~190 g |
| 4:00–4:15 | Ende, trockenes Bett | | | **~278 g** |

Jeder Guss über ~10 s eintragen, nicht schneller — nach dem Bloom keine Agitation mehr.

**Wassersäule, indirekt gemessen:** stehende Flüssigkeit = eingegossen − 42 g Retention − Waagenanzeige. Bei 2:45 also ~128 g, bei 3:15 ~88 g. Halte den Spitzenwert direkt nach einem Guss unter ~150 g; darüber beginnt die Fines-Migration, die dir das Papier zugesetzt hat.

**Zielwerte:** Ausbeute ~278 ml, TDS ~1,55 %, EY 21–22 %. Ohne Refraktometer sind das Referenz-, keine Messgrößen — die Ausbeute auf der Waage ist dein bester Proxy: liegt sie deutlich unter 270 g, hat das Bett zu viel gehalten oder du hast zu früh abgebrochen.

**Servieren:** Carter vor dem Eingießen schwenken. Der No-Bypass-Auslauf ist stratifiziert, die ersten 90 g haben rund die doppelte TDS der letzten.

## Regelhierarchie

Erste Stellgröße ist die Flussrate am Ventil, zweite die Bloom-Dauer, dritte der Mahlgrad — in dieser Reihenfolge, weil nur die ersten beiden die Partikelverteilung unangetastet lassen. Dünn und sauer bei sauberem Durchlauf: Fluss auf 1,0 g/s drosseln. Bitter oder adstringent bei langer Gesamtzeit: auf 1,6 g/s öffnen. Erst wenn du am Ventil an den Anschlag kommst, in 3-Klick-Schritten am Mahlgrad. Läuft es unter 3:30 durch, ist das bei 20 g noch kein Alarmsignal — Rao's 3:30-Untergrenze bezieht sich auf 25-g-Dosen mit entsprechend tieferem Bett.

Prüf vor dem ersten Lauf die Durchgangshöhe: Der Carter ist ein hoher Becher, und improvisierte Ständer sind oft für flache Tassen gebaut. Passt er nicht darunter, nimm ein flaches Gefäß und gieß um — der Wärmeverlust beim Umfüllen ist kleiner als der Genauigkeitsverlust, wenn du wieder blind am Ventil drehst.
