---
titel: Xbloom Studio Rezepte für 16g Bohnen
datum: '2026-04-17'
quelle:
  typ: claude
  url: https://claude.ai/chat/c494fed6-a966-4205-bf49-b4497cd124e9
  hinweis: Xbloom Studio Rezepte für 16g Bohnen
importiert: true
---

Das zugrundeliegende System, mit dem die Rezepte in unserer Reihe entstanden sind. Gedacht als Referenz für zukünftige Bohnen.

---

## 0. Fixe Konstanten

Drei Parameter werden nie variiert – alle Anpassungen laufen über die anderen Variablen:

- **Bohnen-Dosis: immer 16 g** (Konzentrations- und Body-Anpassungen über Wassermenge, nie über die Dosis)
- **RPM: 60** (niedrige Fines-Produktion, saubere Partikelverteilung)
- **Flussrate: 3,0–3,5 ml/s** (Hardware-Bereich der Studio)

---

## 1. Bohnen-Diagnose (vor jedem Rezept)

Aus Tüte/Datenblatt werden fünf Dinge gelesen, plus ein eigener Messschritt:

1. **Verarbeitung** → bestimmt den primären Hebel (siehe Abschnitt 2)
2. **Varietät** → bestimmt Delikatesse/Agitations-Toleranz und Bohnengröße
3. **Höhenlage** → bestimmt Dichte (höher = dichter = mehr Substanz)
4. **Röstgrad** → hell = säurebetont/Top-Note-empfindlich; omni/medium = mehr Maillard-Toleranz
5. **Geschmacksnoten** → bestimmt, welche Verbindungsklassen anzusteuern sind

**Eigener Messschritt – Bohnen pro Gramm + visueller Eindruck:**

| Bohnen/g | visuell | Interpretation | Mahlgrad-Konsequenz |
|----------|---------|----------------|---------------------|
| 9–11 | normal | Standard-Heirloom/Bohne | Standard-Setting |
| 7–8 | groß | Selektion/Höhenlage, voluminös | gröber |
| 6 oder weniger | groß | Großbohnenvarietät (Pacamara, Sidra) | deutlich gröber, längerer Bloom |
| 7–8 | klein–normal | **hochdichte Höhenlagen-Bohne** | **feiner als Standard** |

Kernpunkt: Bohnenzahl allein ist mehrdeutig – erst die Kombination mit visueller Größe unterscheidet *groß* (träge Diffusion → gröber) von *dicht* (viel Substanz, kompakte Partikel → feiner).

---

## 2. Verarbeitung als primärer Hebel

Die entscheidende Weiche. Sie legt fest, welche Variable zuerst gedacht wird:

- **Washed** → **Mahlgrad ist primärer Hebel.** Aromen sind weniger schichtweise organisiert, flache Temperaturkurve, Säure-/Klarheits-Fokus.
- **Natural / Anaerobic** → **Temperatur ist primärer Hebel.** Aromen liegen in deutlichen Schichten in der Extraktionskurve; Temperatur ist das Selektionswerkzeug.

**Fermentationsdauer als primäre Temperatur-Variable (für Natural/Anaerobic):**

| Fermentation | Plateau-Maximum |
|--------------|-----------------|
| Washed (keine) | bis 96 °C |
| Natural ~12–18 h | ~96 °C |
| Natural Reposado ~36–48 h | ~95 °C |
| Anaerobic ~48–60 h | ~95 °C |
| Anaerobic ~72 h | ~95 °C |
| Anaerobic ~90 h | **max. 94 °C** |
| Anaerobic 120 h+ | max. 92 °C |

Je länger die Fermentation, desto kühler das Plateau – unabhängig vom Profilziel. Das Profilziel wird über Mahlgrad, Pour-Struktur und Drawdown-Dauer erreicht, nicht über das Anheben der Temperatur über diese Grenzen.

---

## 3. Die Stellschrauben und ihre Funktionen

| Variable | Funktion |
|----------|----------|
| **Mahlgrad** | Extraktionsoberfläche/-tiefe. Primärer Hebel bei Washed. |
| **Temperatur (pro Pour)** | Selektion der Verbindungsklasse. Primärer Hebel bei Natural/Anaerobic. |
| **Pour-Muster** | Extraktionsverteilung (siehe Abschnitt 5) |
| **Vibration** | Agitation + Entgasung (besonders wichtig bei dichten/großen Bohnen und Decaf) |
| **Bypass** | Entkopplung von Konzentration und Brühverhältnis (siehe Abschnitt 7) |
| **Pour-Anzahl** | Verteilung der Mid-Phase-Aktivität (mehr Pours = mehr verteilte Agitation) |

---

## 4. Verbindungsklassen-Modell (welche Aromen wann/wie extrahieren)

Das mentale Modell hinter der Temperaturarchitektur:

- **Florale & fruchtige Ester** (Jasmin, Zitruszeste, tropische Frucht): hoch flüchtig, brauchen Hitze, extrahieren früh
- **Säuren** (Apfel-, Zitronen-, Chinasäure): früh bis mittel
- **Maillard-Verbindungen** (Schokolade, Nuss, Karamell, Nougat, Cashew): Mid-Phase, optimal bei ~93 °C
- **Bitter-/Phenol-Spätphase**: spät, hitzegetrieben
- **Fermentations-Phenole** (medizinisch/Pflaster/gummi): spät + heiß – das zentrale Anaerobic-Risiko

---

## 5. Pour-Muster-Logik

- **Spiralförmig** (innen → außen): breite Flächenbenetzung = hohe Extraktionsverteilung = **Helligkeit/Klarheit**. Standard für Bloom großer/dichter Bohnen.
- **Zentriert**: konzentrierter Extraktionskern = **Body/Extraktionsmotor**. Hier passiert die Hauptarbeit.
- **Kreisförmig** (konstanter mittlerer Radius): ruhigste Bewegung, keine Wand-Agitation = **Aromenpräservation / sauberer Drawdown**.

Faustregel: Spiral verteilt, Zentriert konzentriert, Kreis bewahrt.

---

## 6. Temperatur-Architektur-Typen

| Typ | Verlauf | Wofür |
|-----|---------|-------|
| **Hohes Plateau + scharfer Endabfall** | 96/95/91 | delikate/florale Bohnen (Sidra, Pink Bourbon, Bookkisa) |
| **Niedriges flaches Plateau** | 93/93/92/90 | Maillard/Body-Fokus (Cashew, Brownie, Apfelkuchen) |
| **Steile Rampe** | 95/94/90 | Anaerobic-Kontrolle (kühler Schwanz schneidet Phenole) |
| **Gewölbte Kurve (Peak Pour 2)** | 94/95/93/90 | saftig/lebendig (Säure-Süße-Schichtung) |
| **Kurzes heißes Plateau + kurzer Drawdown** | 94/94/92, 2:30 | Funk/Tropical Forward (Anaerobic über Kürze geschützt) |

---

## 7. Bypass-Logik

Wasser am Kaffeebett vorbei direkt in die Tasse. Entkoppelt Konzentration vom Brühverhältnis:

- Über Puck konzentriert brühen (z. B. 1:12) → niedrigere Extraktionsausbeute (EY), die problematischen Spätphasen-Verbindungen bleiben im Puck
- Im Tasse auf Zielverhältnis (1:16) verdünnen → trinkbare Stärke ohne Spätphasen-Extraktion
- **Raumtemperatur-Bypass** dient zusätzlich der Temperaturkorrektur (bringt die Tasse in den Trinkkorridor und arretiert das Profil)

Besonders nützlich bei Anaerobics (Phenol-Vermeidung) und fruchtbetonten Verarbeitungen (Reposado, Honey, Carbonic). Skandinavisches "concentrate + dilute"-Paradigma.

---

## 8. Varietäts-/Bohnen-spezifische Anpassungen

- **Delikate elegante Varietäten** (Sidra, Pink Bourbon, Geisha): wenige Pours, niedrige Agitation, kreisförmige Muster, hohes Plateau + scharfer Endabfall. Reagieren binär auf zu feinen Mahlgrad mit Tannin-Adstringenz.
- **Große Bohnen** (Pacamara): gröber, längerer Bloom (50 s), höhere Temperatur (träge Diffusion)
- **Kleine dichte Höhenlagen-Bohnen** (Ethiopier ≥1.900 m): feiner als erwartet (viel Substanz, kompakte Partikel), kürzerer Bloom
- **SL-Linien (SL14/SL28) & JARC-Selektionen (74110/74112)**: empfindlich gegen Adstringenz bei zu feinem Mahlgrad
- **Decaf** (meist EA/Sugarcane): ~15–20 % schnellere Extraktion → gröber; Washed-Decaf hat Papier-Risiko in der Spätphase, Natural-Decaf maskiert es. Effekte von Decaf + Bohnengröße **nicht naiv addieren**, sondern moderieren (Standard +1,5 bis +2 Stufen statt +3 bis +4)

---

## 9. JIC (Japanese Iced Coffee) – Adaptation

- Eis im Server (80–100 g), Brühwasser über Puck reduziert, Gesamt = 1:16 nach Schmelze
- Über Puck effektiv ~1:10 konzentriert → **feinerer Mahlgrad** als bei Heißbrühung
- **Höhere Temperaturen gerechtfertigt**: kurze Kontaktzeit + Schock-Kühlung erreichen Spätphase nicht
- Flash-Cooling fixiert flüchtige Aromen (ideal für delikate/fruchtige Bohnen)
- Decaf-JIC ist besonders stark: vermeidet die Papier-Spätphase strukturell
- Große, dichte Eiswürfel (langsam gefroren); Glas vorkühlen; enges Trinkfenster

---

## 10. Diagnose-Framework (nach der ersten Tasse)

**Bei verschiedenen Temperaturen verkosten** – jede Phase verrät etwas:

- *Heiß (~75 °C)*: Top-Notes / Säurespitze
- *Mittel (~65 °C)*: Maillard / Body / Mid-Phase
- *Kalt (~40 °C)*: ehrlichste Phase – Spätphasen-Fehler (Bitterkeit, Phenole, Decaf-Papier) zeigen sich hier zuerst

**Mahlgrad vs. Temperatur als getrennte Hebel:**
- Adstringenz / Trockenheit → **Mahlgrad** (gröber), nie Temperatur
- Gedämpfte/fehlende Aromaklasse → **Temperatur** der entsprechenden Phase
- Unterextraktion (wässrig, bitter ohne Frucht) → **Mahlgrad feiner** + Mid-Phase-Energie
- Medizinisch/boozy (Anaerobic) → gröber + finaler Pour kühler, oder Bypass

---

## 11. Röster-Empfehlung übersetzen

- **Aeropress-Empfehlung** → Plateau **+1–2 °C** für xbloom Pour-over anheben (Aeropress hat mehr Agitation via Stirring, die thermische Energie ersetzt)
- **V60/Pour-over-Empfehlung** → direktere Übertragung (~+0,5 °C wegen RPM-60-Unterschieden)
- **Multi-Pour mit kurzen Pausen** (z. B. 5 Pours alle 30 s) → Signal für klein-dichte Höhenlagen-Bohne, Strategie B (Agitation statt feiner Mahlgrad)

---

## 12. Iterations-Prinzip

1. Hypothese aus Bohnen-Diagnose aufstellen
2. **Eine Variable** pro Versuch ändern (saubere Zuordnung)
3. Bohnenzahl + visueller Eindruck als Erst-Kalibrierung
4. Bei dichten/delikaten Bohnen ist der Sweet-Spot-Korridor enger – kleinere Schritte
