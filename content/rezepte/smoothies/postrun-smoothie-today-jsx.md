---
titel: postrun_smoothie_today.jsx
status: aktiv
datum: '2026-04-24'
quelle:
  typ: claude
  url: https://claude.ai/chat/e243ac2d-4628-41b9-ae87-39b4cf14f878
  hinweis: Protein-Smoothies für Frühstück und Muskelaufbau
importiert: true
---

<details><summary>Ursprüngliche Datei</summary><pre><code>import { useState } from &quot;react&quot;;

const dayAnalysis = {
  consumed: { kcal: 1385, p: 53, f: 74, kh: 122 },
  target: { kcal: 2350, p: 117, f: 68, kh: 290 },
  note: &quot;Fett bereits bei ~74g — Tagesziel (~68g) überschritten durch Avocado, Bacon, Cheddar, Mayo, Eier&quot;,
};

const smoothies = [
  {
    id: 1,
    rank: &quot;Empfohlen&quot;,
    name: &quot;Mango Spinach Pea Chia&quot;,
    badge: &quot;Folat + Vit. K + KH&quot;,
    badgeColor: &quot;#1a7a4a&quot;,
    rationale: &quot;Fettärmstes Rezept der drei. Spinat + Erbsen decken Folat und Vit. K — heute kein Blattgemüse gegessen. Mango gibt KH und Cremigkeit. Kein Nussanteil da Fett heute bereits überschritten.&quot;,
    macros: { kcal: 641, p: 50, f: 16, kh: 81, bal: 15 },
    afterSmootie: { kcal: &quot;~324&quot;, p: &quot;~14 g&quot;, f: &quot;Achtung ↑&quot;, kh: &quot;~87 g&quot; },
    milch: &quot;210 ml&quot;,
    ingredients: [
      { name: &quot;Vollmilch 3,8 %&quot;, amt: &quot;210 ml&quot;, tag: null, vol: 210 },
      { name: &quot;TK Mango&quot;, amt: &quot;170 g&quot;, tag: &quot;Vit. C · KH · Cremigkeit&quot;, vol: 161 },
      { name: &quot;TK Blattspinat&quot;, amt: &quot;65 g&quot;, tag: &quot;Vit. K &gt;250 %&quot;, vol: 62 },
      { name: &quot;TK Erbsen, aufgetaut&quot;, amt: &quot;70 g&quot;, tag: &quot;Folat ~60 %&quot;, vol: 66 },
      { name: &quot;Haferflocken, fein&quot;, amt: &quot;30 g&quot;, tag: &quot;β-Glucan&quot;, vol: 48 },
      { name: &quot;Chiasamen&quot;, amt: &quot;12 g&quot;, tag: &quot;Omega-3 · kein Nussanteil&quot;, vol: 12 },
      { name: &quot;35 g Pulver + 5 g Kreatin&quot;, amt: &quot;fix&quot;, tag: null, vol: 41, fixed: true },
    ],
    totalVol: 600,
    color: &quot;#1a7a4a&quot;,
    note: &quot;Farbe: sattgrün · Mango überdeckt Spinat + Erbsen vollständig · kein Nussanteil bewusst&quot;,
  },
  {
    id: 2,
    rank: &quot;Alternative A&quot;,
    name: &quot;Beet Blueberry Spinach Flax&quot;,
    badge: &quot;NO-Boost + Anthocyane&quot;,
    badgeColor: &quot;#8b1a4a&quot;,
    rationale: &quot;Rohe Rote Beete post-run für Durchblutung und NO-Synthese. Blaubeeren-Anthocyane ergänzen anti-inflammatorisch. Leinsamen statt Nüssen für ALA. Fettarm.&quot;,
    macros: { kcal: 624, p: 47, f: 17, kh: 76, bal: 14 },
    afterSmootie: { kcal: &quot;~341&quot;, p: &quot;~17 g&quot;, f: &quot;Achtung ↑&quot;, kh: &quot;~92 g&quot; },
    milch: &quot;210 ml&quot;,
    ingredients: [
      { name: &quot;Vollmilch 3,8 %&quot;, amt: &quot;210 ml&quot;, tag: null, vol: 210 },
      { name: &quot;TK Blaubeeren&quot;, amt: &quot;140 g&quot;, tag: &quot;Anthocyane&quot;, vol: 133 },
      { name: &quot;Rohe Rote Beete, gerieben&quot;, amt: &quot;70 g&quot;, tag: &quot;Nitrat roh ↑↑&quot;, vol: 66 },
      { name: &quot;TK Banane&quot;, amt: &quot;80 g&quot;, tag: &quot;KH + Bindung&quot;, vol: 76 },
      { name: &quot;TK Blattspinat&quot;, amt: &quot;55 g&quot;, tag: &quot;Vit. K&quot;, vol: 52 },
      { name: &quot;Leinsamen, gemahlen&quot;, amt: &quot;12 g&quot;, tag: &quot;ALA · kein Nussanteil&quot;, vol: 12 },
      { name: &quot;Haferflocken, fein&quot;, amt: &quot;20 g&quot;, tag: null, vol: 32 },
      { name: &quot;35 g Pulver + 5 g Kreatin&quot;, amt: &quot;fix&quot;, tag: null, vol: 41, fixed: true },
    ],
    totalVol: 622,
    color: &quot;#8b1a4a&quot;,
    note: &quot;Farbe: tief violett · Rote Beete zuletzt einfüllen · Volumen leicht über 600 ml — Hafer auf 15g reduzieren wenn exakt gewünscht&quot;,
  },
  {
    id: 3,
    rank: &quot;Alternative B&quot;,
    name: &quot;Cherry Broccoli Mango Chia&quot;,
    badge: &quot;DOMS + Sulforaphan&quot;,
    badgeColor: &quot;#1a5a8a&quot;,
    rationale: &quot;Sauerkirsche reduziert DOMS nach Zone 2. Brokkoli aktiviert Nrf2. Mango überdeckt Brokkoli vollständig. Kein Nussanteil. Höchste Protein- und Ballaststoffdichte der drei.&quot;,
    macros: { kcal: 648, p: 51, f: 17, kh: 79, bal: 16 },
    afterSmootie: { kcal: &quot;~317&quot;, p: &quot;~13 g&quot;, f: &quot;Achtung ↑&quot;, kh: &quot;~89 g&quot; },
    milch: &quot;215 ml&quot;,
    ingredients: [
      { name: &quot;Vollmilch 3,8 %&quot;, amt: &quot;215 ml&quot;, tag: null, vol: 215 },
      { name: &quot;TK Sauerkirschen&quot;, amt: &quot;130 g&quot;, tag: &quot;COX · DOMS↓&quot;, vol: 123 },
      { name: &quot;TK Mango&quot;, amt: &quot;140 g&quot;, tag: &quot;Brokkoli überdecken&quot;, vol: 133 },
      { name: &quot;TK Brokkoli&quot;, amt: &quot;75 g&quot;, tag: &quot;Sulforaphan · Nrf2↑&quot;, vol: 71 },
      { name: &quot;Chiasamen&quot;, amt: &quot;14 g&quot;, tag: &quot;Omega-3&quot;, vol: 14 },
      { name: &quot;Haferflocken, fein&quot;, amt: &quot;25 g&quot;, tag: null, vol: 40 },
      { name: &quot;35 g Pulver + 5 g Kreatin&quot;, amt: &quot;fix&quot;, tag: null, vol: 41, fixed: true },
    ],
    totalVol: 637,
    color: &quot;#1a5a8a&quot;,
    note: &quot;Farbe: dunkelviolett-grün · kein Blattgemüse aber Brokkoli deckt ähnliche Mikros · Mango-Menge unverzichtbar&quot;,
  },
];

const macroLabels = [
  { key: &quot;kcal&quot;, label: &quot;kcal&quot;, color: &quot;#1a1a1a&quot;, unit: &quot;&quot; },
  { key: &quot;p&quot;, label: &quot;Protein&quot;, color: &quot;#7c3aed&quot;, unit: &quot;g&quot; },
  { key: &quot;f&quot;, label: &quot;Fett&quot;, color: &quot;#d4860a&quot;, unit: &quot;g&quot; },
  { key: &quot;kh&quot;, label: &quot;KH&quot;, color: &quot;#1a7a4a&quot;, unit: &quot;g&quot; },
  { key: &quot;bal&quot;, label: &quot;Ballaststoffe&quot;, color: &quot;#1a6b8a&quot;, unit: &quot;g&quot; },
];

export default function App() {
  const [open, setOpen] = useState(1);
  const rem = (key) =&gt; Math.max(0, dayAnalysis.target[key] - dayAnalysis.consumed[key]);

  return (
    &lt;div style={{
      fontFamily: &quot;Georgia, serif&quot;,
      background: &quot;#f9f7f3&quot;,
      minHeight: &quot;100vh&quot;,
      padding: &quot;1rem 1rem 3rem&quot;,
      maxWidth: 480,
      margin: &quot;0 auto&quot;,
    }}&gt;
      {/* Header */}
      &lt;div style={{ marginBottom: &quot;1rem&quot; }}&gt;
        &lt;p style={{ fontSize: 10, color: &quot;#bbb&quot;, letterSpacing: &quot;.12em&quot;, margin: &quot;0 0 3px&quot;, fontFamily: &quot;monospace&quot; }}&gt;
          POST ZONE 2 · 55 MIN · 600 ML
        &lt;/p&gt;
        &lt;h1 style={{ fontSize: 19, fontWeight: 700, color: &quot;#1a1a1a&quot;, margin: &quot;0 0 3px&quot; }}&gt;
          Smoothie-Empfehlung
        &lt;/h1&gt;
        &lt;p style={{ fontSize: 12, color: &quot;#999&quot;, margin: 0 }}&gt;
          basierend auf heutigem Frühstück + Mittagessen
        &lt;/p&gt;
      &lt;/div&gt;

      {/* Day analysis */}
      &lt;div style={{
        background: &quot;#fff&quot;, borderRadius: 12, border: &quot;0.5px solid #e5e0d8&quot;,
        padding: &quot;10px 13px&quot;, marginBottom: 14,
      }}&gt;
        &lt;p style={{ fontSize: 9, fontFamily: &quot;monospace&quot;, fontWeight: 700, color: &quot;#bbb&quot;, letterSpacing: &quot;.1em&quot;, margin: &quot;0 0 7px&quot; }}&gt;
          HEUTIGER STAND VOR SMOOTHIE
        &lt;/p&gt;
        &lt;div style={{ display: &quot;grid&quot;, gridTemplateColumns: &quot;repeat(4,1fr)&quot;, gap: 6, marginBottom: 8 }}&gt;
          {[
            { label: &quot;Gegessen&quot;, val: &quot;1385 kcal&quot;, color: &quot;#1a1a1a&quot; },
            { label: &quot;Protein&quot;, val: &quot;53 g&quot;, color: &quot;#7c3aed&quot; },
            { label: &quot;Fett ⚠&quot;, val: &quot;74 g&quot;, color: &quot;#c0392b&quot; },
            { label: &quot;KH&quot;, val: &quot;122 g&quot;, color: &quot;#1a7a4a&quot; },
          ].map((d, i) =&gt; (
            &lt;div key={i} style={{ background: &quot;#f9f7f3&quot;, borderRadius: 7, padding: &quot;6px 4px&quot;, textAlign: &quot;center&quot; }}&gt;
              &lt;div style={{ fontSize: 9, color: &quot;#bbb&quot;, marginBottom: 1 }}&gt;{d.label}&lt;/div&gt;
              &lt;div style={{ fontSize: 12, fontWeight: 700, color: d.color }}&gt;{d.val}&lt;/div&gt;
            &lt;/div&gt;
          ))}
        &lt;/div&gt;
        {/* Fat warning */}
        &lt;div style={{
          background: &quot;#fff3cd&quot;, borderRadius: 8, padding: &quot;6px 10px&quot;,
          border: &quot;0.5px solid #ffc10750&quot;, marginBottom: 7,
        }}&gt;
          &lt;p style={{ fontSize: 11, color: &quot;#856404&quot;, margin: 0, lineHeight: 1.5 }}&gt;
            &lt;strong&gt;Fett bereits bei 74 g&lt;/strong&gt; — Tagesziel 68 g überschritten durch Avocado, Bacon, Cheddar, Mayo + Eier im Mittagessen. Kein Nussanteil im Smoothie.
          &lt;/p&gt;
        &lt;/div&gt;
        &lt;div style={{ display: &quot;grid&quot;, gridTemplateColumns: &quot;repeat(4,1fr)&quot;, gap: 6 }}&gt;
          {[
            { label: &quot;kcal fehlen&quot;, val: `~${rem(&quot;kcal&quot;)}`, color: &quot;#1a1a1a&quot; },
            { label: &quot;Protein&quot;, val: `~${rem(&quot;p&quot;)} g`, color: &quot;#7c3aed&quot; },
            { label: &quot;Fett&quot;, val: &quot;gedeckt&quot;, color: &quot;#c0392b&quot; },
            { label: &quot;KH&quot;, val: `~${rem(&quot;kh&quot;)} g`, color: &quot;#1a7a4a&quot; },
          ].map((d, i) =&gt; (
            &lt;div key={i} style={{ textAlign: &quot;center&quot; }}&gt;
              &lt;div style={{ fontSize: 9, color: &quot;#ccc&quot;, marginBottom: 1 }}&gt;{d.label}&lt;/div&gt;
              &lt;div style={{ fontSize: 11, fontWeight: 700, color: d.color }}&gt;{d.val}&lt;/div&gt;
            &lt;/div&gt;
          ))}
        &lt;/div&gt;
      &lt;/div&gt;

      {/* Smoothies */}
      {smoothies.map((s) =&gt; (
        &lt;div key={s.id} style={{
          background: &quot;#fff&quot;,
          borderRadius: 12,
          border: `0.5px solid ${open === s.id ? s.color + &quot;55&quot; : &quot;#e5e0d8&quot;}`,
          marginBottom: 10,
          overflow: &quot;hidden&quot;,
        }}&gt;
          &lt;button
            onClick={() =&gt; setOpen(open === s.id ? null : s.id)}
            style={{ width: &quot;100%&quot;, background: &quot;none&quot;, border: &quot;none&quot;, padding: &quot;12px 13px 10px&quot;, textAlign: &quot;left&quot;, cursor: &quot;pointer&quot; }}
          &gt;
            &lt;div style={{ display: &quot;flex&quot;, alignItems: &quot;flex-start&quot;, gap: 8 }}&gt;
              &lt;div style={{ flex: 1 }}&gt;
                &lt;div style={{ display: &quot;flex&quot;, alignItems: &quot;center&quot;, gap: 6, flexWrap: &quot;wrap&quot;, marginBottom: 3 }}&gt;
                  &lt;span style={{
                    fontSize: 9, fontWeight: 700, padding: &quot;2px 7px&quot;, borderRadius: 20,
                    background: s.id === 1 ? &quot;#1a1a1a&quot; : &quot;#f9f7f3&quot;,
                    color: s.id === 1 ? &quot;#fff&quot; : &quot;#888&quot;,
                    fontFamily: &quot;monospace&quot;, letterSpacing: &quot;.06em&quot;,
                  }}&gt;{s.rank}&lt;/span&gt;
                  &lt;span style={{
                    fontSize: 10, fontWeight: 700, padding: &quot;2px 7px&quot;, borderRadius: 20,
                    background: s.color + &quot;15&quot;, color: s.color,
                    fontFamily: &quot;monospace&quot;,
                  }}&gt;{s.badge}&lt;/span&gt;
                &lt;/div&gt;
                &lt;div style={{ fontSize: 14, fontWeight: 700, color: &quot;#1a1a1a&quot; }}&gt;{s.name}&lt;/div&gt;
                &lt;p style={{ fontSize: 11, color: &quot;#888&quot;, margin: &quot;3px 0 0&quot;, lineHeight: 1.5 }}&gt;{s.rationale}&lt;/p&gt;
              &lt;/div&gt;
              &lt;span style={{ color: &quot;#ccc&quot;, fontSize: 13, marginTop: 2, flexShrink: 0 }}&gt;
                {open === s.id ? &quot;▲&quot; : &quot;▼&quot;}
              &lt;/span&gt;
            &lt;/div&gt;

            {/* Macros */}
            &lt;div style={{ display: &quot;grid&quot;, gridTemplateColumns: &quot;repeat(5,1fr)&quot;, gap: 5, marginTop: 9 }}&gt;
              {macroLabels.map((m) =&gt; (
                &lt;div key={m.key} style={{
                  background: &quot;#f9f7f3&quot;, borderRadius: 7, padding: &quot;5px 3px&quot;, textAlign: &quot;center&quot;,
                  border: m.key === &quot;f&quot;
                    ? &quot;0.5px solid #ffc10770&quot;
                    : m.key === &quot;kh&quot;
                    ? `0.5px solid ${s.color}40`
                    : &quot;0.5px solid transparent&quot;,
                }}&gt;
                  &lt;div style={{ fontSize: 9, color: &quot;#bbb&quot;, marginBottom: 1 }}&gt;{m.label}&lt;/div&gt;
                  &lt;div style={{ fontSize: 12, fontWeight: 700, color: m.key === &quot;f&quot; ? &quot;#c0392b&quot; : m.key === &quot;kh&quot; ? s.color : m.color }}&gt;
                    {s.macros[m.key]}{m.unit}
                  &lt;/div&gt;
                &lt;/div&gt;
              ))}
            &lt;/div&gt;

            {/* Volume */}
            &lt;div style={{
              marginTop: 7, fontSize: 11, color: &quot;#aaa&quot;,
              display: &quot;flex&quot;, gap: 10, alignItems: &quot;center&quot;,
            }}&gt;
              &lt;span&gt;Volumen vor Mixen: &lt;strong style={{ color: &quot;#555&quot; }}&gt;{s.totalVol} ml&lt;/strong&gt;&lt;/span&gt;
              &lt;span&gt;Milch: &lt;strong style={{ color: &quot;#555&quot; }}&gt;{s.milch}&lt;/strong&gt;&lt;/span&gt;
              &lt;span style={{ color: &quot;#ddd&quot; }}&gt;kein Nussanteil&lt;/span&gt;
            &lt;/div&gt;
          &lt;/button&gt;

          {/* Ingredients */}
          {open === s.id &amp;&amp; (
            &lt;div style={{ borderTop: &quot;0.5px solid #f0ece4&quot;, padding: &quot;8px 13px 12px&quot; }}&gt;
              &lt;p style={{ fontSize: 9, fontWeight: 700, color: &quot;#ccc&quot;, letterSpacing: &quot;.12em&quot;, margin: &quot;0 0 6px&quot;, fontFamily: &quot;monospace&quot; }}&gt;
                ZUTATEN · GESAMTVOLUMEN {s.totalVol} ML
              &lt;/p&gt;
              {s.ingredients.map((ing, i) =&gt; (
                &lt;div key={i} style={{
                  display: &quot;flex&quot;, justifyContent: &quot;space-between&quot;, alignItems: &quot;flex-start&quot;,
                  padding: &quot;4px 0&quot;,
                  borderBottom: i &lt; s.ingredients.length - 1 ? &quot;0.5px solid #f5f2ee&quot; : &quot;none&quot;,
                  background: ing.fixed ? &quot;#f5f3ff&quot; : &quot;transparent&quot;,
                  borderRadius: ing.fixed ? 4 : 0,
                  paddingLeft: ing.fixed ? 4 : 0,
                }}&gt;
                  &lt;div&gt;
                    &lt;span style={{ fontSize: 13, color: ing.fixed ? &quot;#7c3aed&quot; : &quot;#333&quot; }}&gt;{ing.name}&lt;/span&gt;
                    {ing.tag &amp;&amp; (
                      &lt;span style={{ fontSize: 10, color: s.color, marginLeft: 5, fontFamily: &quot;monospace&quot; }}&gt;
                        · {ing.tag}
                      &lt;/span&gt;
                    )}
                  &lt;/div&gt;
                  &lt;div style={{ textAlign: &quot;right&quot;, marginLeft: 8, flexShrink: 0 }}&gt;
                    &lt;div style={{ fontSize: 11, fontWeight: 700, color: &quot;#bbb&quot; }}&gt;{ing.amt}&lt;/div&gt;
                    {!ing.fixed &amp;&amp; &lt;div style={{ fontSize: 9, color: &quot;#ddd&quot; }}&gt;≈ {ing.vol} ml&lt;/div&gt;}
                  &lt;/div&gt;
                &lt;/div&gt;
              ))}
              &lt;div style={{
                marginTop: 8, fontSize: 11, color: &quot;#999&quot;, fontStyle: &quot;italic&quot;,
                borderLeft: `3px solid ${s.color}40`,
                paddingLeft: 8, lineHeight: 1.5,
              }}&gt;
                {s.note}
              &lt;/div&gt;
            &lt;/div&gt;
          )}
        &lt;/div&gt;
      ))}

      {/* Abend note */}
      &lt;div style={{
        background: &quot;#fff&quot;, borderRadius: 10, border: &quot;0.5px solid #e5e0d8&quot;,
        padding: &quot;9px 12px&quot;, marginTop: 4,
      }}&gt;
        &lt;p style={{ fontSize: 10, fontFamily: &quot;monospace&quot;, fontWeight: 700, color: &quot;#bbb&quot;, letterSpacing: &quot;.1em&quot;, margin: &quot;0 0 5px&quot; }}&gt;
          ABENDESSEN · EMPFEHLUNG
        &lt;/p&gt;
        &lt;p style={{ fontSize: 12, color: &quot;#888&quot;, margin: 0, lineHeight: 1.5 }}&gt;
          Nach dem Smoothie fehlen noch ~14–17 g Protein und ~87–92 g KH. Fett ist heute gedeckt — Abendessen fettarm halten: z.B. Linsen, Kichererbsen, Hülsenfrüchte im Instant Pot, oder Quark mit Früchten.
        &lt;/p&gt;
      &lt;/div&gt;
    &lt;/div&gt;
  );
}
</code></pre></details>
