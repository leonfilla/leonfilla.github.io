---
titel: Verbesserungsvorschläge
datum: '2025-07-12'
quelle:
  typ: gemini
  url: https://gemini.google.com/app/48aa8416945f14b0
  hinweis: Hinterfrage diesen Prompt anhand folgender Information und gib mir Verbesserungs…
importiert: true
---

> **Frage im Chat:** Hinterfrage diesen Prompt anhand folgender Information und gib mir Verbesserungsvorschläge: In der App ist die Temperatur in 1-Grad-Abschnitten bis 95 Grad einstellbar, der nächst höhere und auch letzte Punkt ist BP (wahrscheinlich Boiling Point)

Absolut. Als angehender Mediziner ist Ihnen die Präzision von Anweisungen und die Beachtung von Geräteparametern vertraut – ein Prinzip, das in der Rezeptentwicklung für Kaffee ebenso kritisch ist. Ihre Beobachtung bezüglich der Temperatureinstellung ist exzellent und deckt eine entscheidende Schwachstelle im vorliegenden Prompt auf.

Hier ist eine Analyse und die entsprechenden Verbesserungsvorschläge für den Prompt:

#### **Analyse des Problems**

Der Kern des Problems liegt in einer **Diskrepanz zwischen der im Prompt definierten Hardware-Spezifikation und der tatsächlichen Gerätefunktionalität**.

1. 

**Falsche Parameter-Definition:**

  - **Prompt-Angabe:** Der Prompt definiert den Temperaturbereich des Brühers als 40-98°C in 1°C-Schritten ().

  - **Ihre Information (Realität):** Die Maschine operiert von 40-95°C in 1°C-Schritten, gefolgt von einer finalen Stufe BP (Boiling Point).

2. 

**Fehlende Heuristik für "BP":**

  - Der Prompt enthält keine Regel, wie mit der BP-Einstellung umzugehen ist. Er zwingt das System, in einem numerischen Spektrum (bis 98°C) zu denken, das physisch nicht existiert. Dies kann zu Rezepten führen, die Temperaturen wie 96°C, 97°C oder 98°C fordern und somit in der Praxis nicht umsetzbar sind.

---

#### **Verbesserungsvorschläge**

Um den Prompt präziser, robuster und an die tatsächliche Hardware angepasst zu gestalten, schlage ich folgende Änderungen vor:

#### **1. Korrektur der Geräteparameter**

Der wichtigste Schritt ist die Berichtigung der Spezifikation unter dem Abschnitt "Geräteparameter und strategische Anwendung".

- 

**ALT:** Brüher: Kinematischer Ausguss mit einstellbarer Temperatur (40-98°C in 1°C-Schritten)... ()

- 

**NEU (Vorschlag):**
**Brüher**: Kinematischer Ausguss mit einstellbarer Temperatur (**40-95°C** in 1°C-Schritten sowie eine **'BP'** (Boiling Point) Stufe)...

  - **Begründung:** Diese Änderung sorgt für eine korrekte Abbildung der Hardware-Realität und ist die Grundlage für alle weiteren logischen Ableitungen.

#### **2. Einführung einer "Boiling Point"-Heuristik**

Der Prompt benötigt eine klare Regel, wann und warum die BP-Stufe eingesetzt werden soll. Diese Regel sollte in den Abschnitt "Expertenheuristik" oder "Anpassung an die Wasserchemie" integriert werden.

- **NEUE REGEL (Vorschlag):**
**4. Umgang mit der Boiling-Point-Einstellung (Priorität 4):**

  - 

**Regel:** Wenn eine Strategie (z.B. die Aggressive Strategie für dichte Bohnen) eine Temperatur von 96°C oder höher erfordert, um die Extraktion zu maximieren, **wird stattdessen die 'BP'-Einstellung verwendet**. Die BP-Einstellung repräsentiert die maximal verfügbare thermische Energie und wird typischerweise nur für den ersten oder die ersten beiden Aufgüsse genutzt, um eine Überextraktion von Bitterstoffen im späteren Brühverlauf zu vermeiden.

  - 

**Anwendungsbeispiel:** Eine Aggressive Strategie könnte für einen dichten, hell gerösteten Kaffee aus Kenia eine Starttemperatur von 96°C berechnen. Gemäß dieser neuen Regel würde das Rezept stattdessen BP als Temperatur für den Blooming-Guss festlegen.

  - 

**Begründung:** Ohne diese explizite Anweisung würde die KI entweder fälschlicherweise versuchen, eine nicht existierende Temperatur zu verwenden oder willkürlich auf 95°C kappen, was dem strategischen Ziel (maximale Extraktion) widersprechen könnte. Diese Regel schafft Klarheit und Reproduzierbarkeit.

Durch die Implementierung dieser beiden Vorschläge wird der Prompt von einer theoretischen Annahme zu einer präzisen, praxistauglichen Arbeitsanweisung aufgewertet.
