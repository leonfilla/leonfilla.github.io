---
titel: post_zone2_smoothies.jsx
status: archiv
datum: '2026-04-24'
quelle:
  typ: claude
  url: https://claude.ai/chat/e243ac2d-4628-41b9-ae87-39b4cf14f878
  hinweis: Protein-Smoothies für Frühstück und Muskelaufbau
importiert: true
---

<details><summary>Ursprüngliche Datei</summary><pre><code>import { useState } from &quot;react&quot;;

const context = [
  { icon: &quot;🏃&quot;, label: &quot;Zone 2 Laufen&quot;, val: &quot;6,1 km · 8:30 Pace · ~52 Min.&quot; },
  { icon: &quot;🔥&quot;, label: &quot;Mehrverbrauch&quot;, val: &quot;~410 kcal&quot; },
  { icon: &quot;📈&quot;, label: &quot;TDEE heute&quot;, val: &quot;~2.300 kcal&quot; },
  { icon: &quot;🎯&quot;, label: &quot;KH-Ziel post-run&quot;, val: &quot;~290 g/Tag · Fenster 30–45 Min.&quot; },
];

const priorities = [
  { label: &quot;Schnelle + langsame KH&quot;, sub: &quot;Glykogen-Replenishment&quot;, color: &quot;#2a7a4f&quot; },
  { label: &quot;Elektrolyte Na + K + Mg&quot;, sub: &quot;~600 ml Schweißverlust&quot;, color: &quot;#1a6b8a&quot; },
  { label: &quot;Protein ≥45 g&quot;, sub: &quot;MPS-Fenster post-workout&quot;, color: &quot;#7c3aed&quot; },
  { label: &quot;Anti-inflammatorisch&quot;, sub: &quot;DOMS-Prävention&quot;, color: &quot;#c0392b&quot; },
];

const smoothies = [
  {
    id: 1,
    num: &quot;01&quot;,
    name: &quot;Tart Cherry Cacao Recovery&quot;,
    badge: &quot;DOMS-Prävention&quot;,
    badgeColor: &quot;#c0392b&quot;,
    rationale: &quot;Sauerkirsche (Anthocyane, COX-Hemmer) + Kakao-Flavanole = stärkste anti-inflammatorische Kombination direkt post-workout. Banane + Datteln liefern schnelle + mittlere KH für sofortiges Glykogen-Replenishment.&quot;,
    base: &quot;300 ml Vollmilch 3,8 %&quot;,
    baseReason: &quot;Casein + Molke für sustained MPS, Calcium, B12&quot;,
    macros: { kcal: 791, protein: 50, fett: 24, kh: 96, ballaststoffe: 11 },
    electrolytes: { na: &quot;~290 mg&quot;, k: &quot;~920 mg&quot;, mg: &quot;~78 mg&quot; },
    timing: &quot;Innerhalb 20 Min. post-run · KH:Protein ~1,9:1 optimal für Glykogen + MPS&quot;,
    ingredients: [
      { name: &quot;TK Sauerkirschen&quot;, amount: &quot;180 g&quot;, tag: &quot;COX-Hemmer · DOMS↓&quot;, color: &quot;#c0392b&quot; },
      { name: &quot;TK Banane&quot;, amount: &quot;100 g&quot;, tag: &quot;Kalium + schnelle KH&quot;, color: &quot;#2a7a4f&quot; },
      { name: &quot;Medjool-Dattel, entkernt&quot;, amount: &quot;2 Stk. (~36 g)&quot;, tag: &quot;mittlere KH · Bindung&quot;, color: &quot;#d4860a&quot; },
      { name: &quot;Rohkakao-Pulver, ungesüßt&quot;, amount: &quot;15 g&quot;, tag: &quot;Flavanole · Mg&quot;, color: &quot;#6b4226&quot; },
      { name: &quot;Haferflocken, fein&quot;, amount: &quot;35 g&quot;, tag: &quot;β-Glucan · langsame KH&quot;, color: &quot;#888&quot; },
      { name: &quot;Meersalz&quot;, amount: &quot;1 Prise (~0,5 g)&quot;, tag: &quot;Elektrolyt · Rehydrierung&quot;, color: &quot;#1a6b8a&quot; },
      { name: &quot;35 g Proteinpulver&quot;, amount: &quot;fix&quot;, tag: null, color: &quot;#7c3aed&quot;, fixed: true },
      { name: &quot;5 g Kreatin&quot;, amount: &quot;fix&quot;, tag: null, color: &quot;#7c3aed&quot;, fixed: true },
    ],
    color: &quot;#c0392b&quot;,
    note: &quot;Farbe: dunkelbraun-rot · dessertartig · Dattel nicht auslassen — gleicht Kirschsäure aus und erhöht KH gezielt&quot;,
    strength: &quot;Stärkste DOMS-Reduktion der drei&quot;,
  },
  {
    id: 2,
    num: &quot;02&quot;,
    name: &quot;Coconut Mango Spinach Elektrolyt&quot;,
    badge: &quot;Elektrolyte + Vit. K&quot;,
    badgeColor: &quot;#1a6b8a&quot;,
    rationale: &quot;Kokoswasser als Basis: natürliche Elektrolytmatrix (K, Mg, Na) die Sportgetränke physiologisch überlegen ist. Mango + Banane für KH, Spinat schließt Vitamin-K-Lücke des Tages. Höchstes Kalium aller drei.&quot;,
    base: &quot;200 ml Kokoswasser + 100 ml Vollmilch&quot;,
    baseReason: &quot;Kokoswasser: 600 mg K/100ml · Milch: Protein + Ca&quot;,
    macros: { kcal: 754, protein: 48, fett: 20, kh: 92, ballaststoffe: 10 },
    electrolytes: { na: &quot;~260 mg&quot;, k: &quot;~1.180 mg&quot;, mg: &quot;~92 mg&quot; },
    timing: &quot;Innerhalb 30 Min. post-run · Kokoswasser-Kalium wirkt rehydrierend innerhalb 15–20 Min.&quot;,
    ingredients: [
      { name: &quot;Kokoswasser, pur&quot;, amount: &quot;200 ml&quot;, tag: &quot;K 1200 mg · Mg · isotonisch&quot;, color: &quot;#1a6b8a&quot; },
      { name: &quot;Vollmilch 3,8 %&quot;, amount: &quot;100 ml&quot;, tag: &quot;Protein + Calcium&quot;, color: &quot;#555&quot; },
      { name: &quot;TK Mango&quot;, amount: &quot;180 g&quot;, tag: &quot;Vit. C + KH + Cremigkeit&quot;, color: &quot;#e67e22&quot; },
      { name: &quot;TK Banane&quot;, amount: &quot;90 g&quot;, tag: &quot;Kalium + schnelle KH&quot;, color: &quot;#2a7a4f&quot; },
      { name: &quot;TK Blattspinat&quot;, amount: &quot;60 g&quot;, tag: &quot;Vit. K &gt;200% · Folat&quot;, color: &quot;#2a7a4f&quot; },
      { name: &quot;Hanfsamen, geschält&quot;, amount: &quot;20 g&quot;, tag: &quot;Mg · vollst. Aminosäuren&quot;, color: &quot;#888&quot; },
      { name: &quot;Leinsamen, gemahlen&quot;, amount: &quot;10 g&quot;, tag: &quot;ALA Omega-3&quot;, color: &quot;#888&quot; },
      { name: &quot;Meersalz&quot;, amount: &quot;1 Prise (~0,5 g)&quot;, tag: &quot;Na-Ausgleich&quot;, color: &quot;#1a6b8a&quot; },
      { name: &quot;35 g Proteinpulver&quot;, amount: &quot;fix&quot;, tag: null, color: &quot;#7c3aed&quot;, fixed: true },
      { name: &quot;5 g Kreatin&quot;, amount: &quot;fix&quot;, tag: null, color: &quot;#7c3aed&quot;, fixed: true },
    ],
    color: &quot;#1a6b8a&quot;,
    note: &quot;Farbe: hellgrün-gelb · frischeste Variante · Kokoswasser gibt leichte Süße ohne Zusatzzucker&quot;,
    strength: &quot;Höchstes Kalium · beste Rehydrierung · Vit. K-Tagesbedarf gedeckt&quot;,
  },
  {
    id: 3,
    num: &quot;03&quot;,
    name: &quot;Triple KH Beet Banana Oat&quot;,
    badge: &quot;Maximale KH&quot;,
    badgeColor: &quot;#2a7a4f&quot;,
    rationale: &quot;Drei KH-Quellen unterschiedlicher Geschwindigkeit: Banane (GI ~51, schnell), Haferflocken (GI ~55, mittel), Rote Beete (GI ~64, mittel-schnell). Gleichzeitig NO-Boost durch Roh-Beete: verbessert post-workout Muskeldurchblutung und damit Nährstofflieferung.&quot;,
    base: &quot;300 ml Vollmilch 3,8 %&quot;,
    baseReason: &quot;Casein-Anteil → sustained MPS über 3–4 Stunden&quot;,
    macros: { kcal: 803, protein: 52, fett: 21, kh: 103, ballaststoffe: 12 },
    electrolytes: { na: &quot;~320 mg&quot;, k: &quot;~1.050 mg&quot;, mg: &quot;~85 mg&quot; },
    timing: &quot;Bis 45 Min. post-run · höchste KH der Serie → maximales Glykogen-Replenishment&quot;,
    ingredients: [
      { name: &quot;TK Banane&quot;, amount: &quot;110 g&quot;, tag: &quot;GI ~51 · schnelle KH · K&quot;, color: &quot;#2a7a4f&quot; },
      { name: &quot;TK Rote Beete, gegart&quot;, amount: &quot;100 g&quot;, tag: &quot;Nitrat → NO · Durchblutung↑&quot;, color: &quot;#c0392b&quot; },
      { name: &quot;TK Blaubeeren&quot;, amount: &quot;120 g&quot;, tag: &quot;Anthocyane · Antioxidantien&quot;, color: &quot;#7c3aed&quot; },
      { name: &quot;Haferflocken, fein&quot;, amount: &quot;50 g&quot;, tag: &quot;GI ~55 · β-Glucan · sustained KH&quot;, color: &quot;#888&quot; },
      { name: &quot;Chiasamen&quot;, amount: &quot;15 g&quot;, tag: &quot;Omega-3 · Ballaststoffe&quot;, color: &quot;#888&quot; },
      { name: &quot;Meersalz&quot;, amount: &quot;1 Prise (~0,5 g)&quot;, tag: &quot;Na-Elektrolyt&quot;, color: &quot;#1a6b8a&quot; },
      { name: &quot;Zitronensaft, frisch&quot;, amount: &quot;½ Zitrone&quot;, tag: &quot;Vit. C · Antioxidation&quot;, color: &quot;#e6a817&quot; },
      { name: &quot;35 g Proteinpulver&quot;, amount: &quot;fix&quot;, tag: null, color: &quot;#7c3aed&quot;, fixed: true },
      { name: &quot;5 g Kreatin&quot;, amount: &quot;fix&quot;, tag: null, color: &quot;#7c3aed&quot;, fixed: true },
    ],
    color: &quot;#2a7a4f&quot;,
    note: &quot;Farbe: violett-dunkelrot · höchste KH (103 g) + höchstes Protein (52 g) der Serie · Haferflocken vorab in Milch 2 Min. quellen lassen&quot;,
    strength: &quot;Maximales Glykogen-Replenishment · höchstes Protein&quot;,
  },
];

export default function App() {
  const [open, setOpen] = useState(1);

  return (
    &lt;div style={{
      fontFamily: &quot;&#x27;Georgia&#x27;, serif&quot;,
      background: &quot;#0e1117&quot;,
      minHeight: &quot;100vh&quot;,
      padding: &quot;1.25rem 1rem 3rem&quot;,
      maxWidth: 520,
      margin: &quot;0 auto&quot;,
      color: &quot;#e8e4dc&quot;,
    }}&gt;

      {/* Header */}
      &lt;div style={{ marginBottom: &quot;1.5rem&quot; }}&gt;
        &lt;p style={{ fontSize: 10, letterSpacing: &quot;.15em&quot;, color: &quot;#555&quot;, margin: &quot;0 0 5px&quot;, fontFamily: &quot;monospace&quot; }}&gt;
          POST ZONE 2 · 28.04.2026
        &lt;/p&gt;
        &lt;h1 style={{ fontSize: 22, fontWeight: 700, margin: &quot;0 0 4px&quot;, color: &quot;#e8e4dc&quot;, lineHeight: 1.2 }}&gt;
          3 Post-Run Smoothies
        &lt;/h1&gt;
        &lt;p style={{ fontSize: 12, color: &quot;#666&quot;, margin: 0 }}&gt;
          Fix: 35 g Proteinpulver · 5 g Kreatin · Rest optimiert für Zone 2
        &lt;/p&gt;
      &lt;/div&gt;

      {/* Context */}
      &lt;div style={{
        display: &quot;grid&quot;, gridTemplateColumns: &quot;1fr 1fr&quot;, gap: 6, marginBottom: 14,
      }}&gt;
        {context.map((c, i) =&gt; (
          &lt;div key={i} style={{
            background: &quot;#1a1e28&quot;, borderRadius: 10, padding: &quot;8px 10px&quot;,
            border: &quot;1px solid #2a2e3a&quot;,
          }}&gt;
            &lt;div style={{ fontSize: 16, marginBottom: 2 }}&gt;{c.icon}&lt;/div&gt;
            &lt;div style={{ fontSize: 10, color: &quot;#555&quot;, marginBottom: 1, fontFamily: &quot;monospace&quot; }}&gt;{c.label}&lt;/div&gt;
            &lt;div style={{ fontSize: 12, fontWeight: 600, color: &quot;#e8e4dc&quot; }}&gt;{c.val}&lt;/div&gt;
          &lt;/div&gt;
        ))}
      &lt;/div&gt;

      {/* Priorities */}
      &lt;div style={{ display: &quot;flex&quot;, gap: 5, flexWrap: &quot;wrap&quot;, marginBottom: 16 }}&gt;
        {priorities.map((p, i) =&gt; (
          &lt;div key={i} style={{
            background: p.color + &quot;18&quot;, border: `1px solid ${p.color}40`,
            borderRadius: 8, padding: &quot;4px 9px&quot;,
          }}&gt;
            &lt;div style={{ fontSize: 11, fontWeight: 600, color: p.color }}&gt;{p.label}&lt;/div&gt;
            &lt;div style={{ fontSize: 10, color: &quot;#666&quot; }}&gt;{p.sub}&lt;/div&gt;
          &lt;/div&gt;
        ))}
      &lt;/div&gt;

      {/* Smoothies */}
      {smoothies.map((s) =&gt; (
        &lt;div key={s.id} style={{
          background: &quot;#1a1e28&quot;,
          borderRadius: 14,
          marginBottom: 12,
          border: `1px solid ${open === s.id ? s.color + &quot;60&quot; : &quot;#2a2e3a&quot;}`,
          overflow: &quot;hidden&quot;,
          transition: &quot;border-color .2s&quot;,
        }}&gt;
          &lt;button
            onClick={() =&gt; setOpen(open === s.id ? null : s.id)}
            style={{
              width: &quot;100%&quot;, background: &quot;none&quot;, border: &quot;none&quot;,
              padding: &quot;14px 14px 12px&quot;, textAlign: &quot;left&quot;, cursor: &quot;pointer&quot;,
            }}
          &gt;
            {/* Number + name */}
            &lt;div style={{ display: &quot;flex&quot;, alignItems: &quot;flex-start&quot;, gap: 10 }}&gt;
              &lt;span style={{
                fontSize: 28, fontWeight: 800, color: s.color + &quot;40&quot;,
                lineHeight: 1, fontFamily: &quot;monospace&quot;, flexShrink: 0,
              }}&gt;{s.num}&lt;/span&gt;
              &lt;div style={{ flex: 1 }}&gt;
                &lt;div style={{ display: &quot;flex&quot;, alignItems: &quot;center&quot;, gap: 7, flexWrap: &quot;wrap&quot;, marginBottom: 3 }}&gt;
                  &lt;span style={{
                    fontSize: 10, fontWeight: 700, padding: &quot;2px 8px&quot;,
                    borderRadius: 20, background: s.color + &quot;25&quot;, color: s.color,
                    letterSpacing: &quot;.05em&quot;, fontFamily: &quot;monospace&quot;,
                  }}&gt;{s.badge}&lt;/span&gt;
                &lt;/div&gt;
                &lt;div style={{ fontSize: 15, fontWeight: 700, color: &quot;#e8e4dc&quot;, lineHeight: 1.3 }}&gt;{s.name}&lt;/div&gt;
              &lt;/div&gt;
              &lt;span style={{ color: &quot;#444&quot;, fontSize: 14, marginTop: 4 }}&gt;{open === s.id ? &quot;▲&quot; : &quot;▼&quot;}&lt;/span&gt;
            &lt;/div&gt;

            {/* Rationale */}
            &lt;p style={{ fontSize: 12, color: &quot;#777&quot;, margin: &quot;8px 0 10px&quot;, lineHeight: 1.5 }}&gt;{s.rationale}&lt;/p&gt;

            {/* Base */}
            &lt;div style={{
              background: &quot;#12151e&quot;, borderRadius: 8, padding: &quot;6px 10px&quot;, marginBottom: 10,
              display: &quot;flex&quot;, justifyContent: &quot;space-between&quot;, alignItems: &quot;center&quot;,
            }}&gt;
              &lt;div&gt;
                &lt;span style={{ fontSize: 10, color: &quot;#555&quot;, fontFamily: &quot;monospace&quot; }}&gt;BASIS · &lt;/span&gt;
                &lt;span style={{ fontSize: 12, color: &quot;#aaa&quot; }}&gt;{s.base}&lt;/span&gt;
              &lt;/div&gt;
            &lt;/div&gt;

            {/* Macros */}
            &lt;div style={{ display: &quot;grid&quot;, gridTemplateColumns: &quot;repeat(5,1fr)&quot;, gap: 5 }}&gt;
              {[
                { label: &quot;kcal&quot;, val: s.macros.kcal },
                { label: &quot;Protein&quot;, val: s.macros.protein + &quot; g&quot; },
                { label: &quot;Fett&quot;, val: s.macros.fett + &quot; g&quot; },
                { label: &quot;KH&quot;, val: s.macros.kh + &quot; g&quot; },
                { label: &quot;Balaststoffe&quot;, val: s.macros.ballaststoffe + &quot; g&quot; },
              ].map((m, i) =&gt; (
                &lt;div key={i} style={{
                  background: &quot;#12151e&quot;, borderRadius: 8, padding: &quot;6px 4px&quot;, textAlign: &quot;center&quot;,
                  border: i === 3 ? `1px solid ${s.color}50` : &quot;1px solid transparent&quot;,
                }}&gt;
                  &lt;div style={{ fontSize: 9, color: &quot;#444&quot;, marginBottom: 2, fontFamily: &quot;monospace&quot; }}&gt;{m.label}&lt;/div&gt;
                  &lt;div style={{ fontSize: i === 3 ? 13 : 12, fontWeight: 700, color: i === 3 ? s.color : &quot;#ccc&quot; }}&gt;{m.val}&lt;/div&gt;
                &lt;/div&gt;
              ))}
            &lt;/div&gt;

            {/* Electrolytes */}
            &lt;div style={{ display: &quot;flex&quot;, gap: 6, marginTop: 8, flexWrap: &quot;wrap&quot; }}&gt;
              {Object.entries(s.electrolytes).map(([k, v]) =&gt; (
                &lt;div key={k} style={{
                  background: &quot;#1a3a4a&quot;, borderRadius: 6, padding: &quot;3px 8px&quot;,
                  fontSize: 11, color: &quot;#4a9eba&quot;,
                }}&gt;
                  &lt;span style={{ fontFamily: &quot;monospace&quot;, fontWeight: 700 }}&gt;{k.toUpperCase()} &lt;/span&gt;{v}
                &lt;/div&gt;
              ))}
            &lt;/div&gt;

            {/* Timing */}
            &lt;div style={{
              marginTop: 8, background: s.color + &quot;15&quot;, borderRadius: 8,
              padding: &quot;5px 10px&quot;, fontSize: 11, color: s.color, lineHeight: 1.4,
            }}&gt;
              ⏱ {s.timing}
            &lt;/div&gt;
          &lt;/button&gt;

          {/* Expandable */}
          {open === s.id &amp;&amp; (
            &lt;div style={{ borderTop: `1px solid #2a2e3a`, padding: &quot;10px 14px 14px&quot; }}&gt;
              &lt;p style={{ fontSize: 10, fontWeight: 700, color: &quot;#444&quot;, letterSpacing: &quot;.1em&quot;, margin: &quot;0 0 8px&quot;, fontFamily: &quot;monospace&quot; }}&gt;
                ZUTATEN
              &lt;/p&gt;
              {s.ingredients.map((ing, i) =&gt; (
                &lt;div key={i} style={{
                  display: &quot;flex&quot;, justifyContent: &quot;space-between&quot;, alignItems: &quot;flex-start&quot;,
                  padding: &quot;5px 0&quot;,
                  borderBottom: i &lt; s.ingredients.length - 1 ? &quot;1px solid #1e2230&quot; : &quot;none&quot;,
                }}&gt;
                  &lt;div style={{ display: &quot;flex&quot;, alignItems: &quot;flex-start&quot;, gap: 7, flex: 1 }}&gt;
                    {ing.fixed &amp;&amp; (
                      &lt;span style={{ fontSize: 9, color: &quot;#7c3aed&quot;, fontFamily: &quot;monospace&quot;, paddingTop: 2 }}&gt;FIX&lt;/span&gt;
                    )}
                    &lt;div&gt;
                      &lt;div style={{ fontSize: 13, color: ing.fixed ? &quot;#7c3aed&quot; : &quot;#ddd&quot; }}&gt;{ing.name}&lt;/div&gt;
                      {ing.tag &amp;&amp; (
                        &lt;div style={{
                          fontSize: 10, color: ing.color, marginTop: 1,
                          fontFamily: &quot;monospace&quot;,
                        }}&gt;{ing.tag}&lt;/div&gt;
                      )}
                    &lt;/div&gt;
                  &lt;/div&gt;
                  &lt;span style={{
                    fontSize: 12, fontWeight: 700,
                    color: ing.fixed ? &quot;#7c3aed&quot; : &quot;#888&quot;,
                    whiteSpace: &quot;nowrap&quot;, marginLeft: 10,
                  }}&gt;{ing.amount}&lt;/span&gt;
                &lt;/div&gt;
              ))}

              {/* Strength + note */}
              &lt;div style={{
                marginTop: 10, background: s.color + &quot;12&quot;,
                borderRadius: 8, padding: &quot;7px 10px&quot;,
                borderLeft: `3px solid ${s.color}`,
              }}&gt;
                &lt;div style={{ fontSize: 11, fontWeight: 700, color: s.color, marginBottom: 3 }}&gt;
                  {s.strength}
                &lt;/div&gt;
                &lt;div style={{ fontSize: 11, color: &quot;#666&quot;, fontStyle: &quot;italic&quot;, lineHeight: 1.5 }}&gt;
                  {s.note}
                &lt;/div&gt;
              &lt;/div&gt;
            &lt;/div&gt;
          )}
        &lt;/div&gt;
      ))}

      &lt;div style={{ textAlign: &quot;center&quot;, marginTop: 8 }}&gt;
        &lt;p style={{ fontSize: 10, color: &quot;#333&quot;, fontFamily: &quot;monospace&quot; }}&gt;
          TIPPE FÜR ZUTATEN · KREATIN IMMER MIT KH NEHMEN → INSULIN ↑ → AUFNAHME ↑
        &lt;/p&gt;
      &lt;/div&gt;
    &lt;/div&gt;
  );
}
</code></pre></details>
