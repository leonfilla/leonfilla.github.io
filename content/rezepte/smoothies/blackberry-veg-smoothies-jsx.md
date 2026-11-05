---
titel: blackberry_veg_smoothies.jsx
status: aktiv
datum: '2026-04-24'
quelle:
  typ: claude
  url: https://claude.ai/chat/e243ac2d-4628-41b9-ae87-39b4cf14f878
  hinweis: Protein-Smoothies für Frühstück und Muskelaufbau
importiert: true
---

<details><summary>Ursprüngliche Datei</summary><pre><code>import { useState } from &quot;react&quot;;

const smoothies = [
  {
    id: 1,
    name: &quot;Blackberry Spinach Banana Walnut&quot;,
    badge: &quot;Anthocyane + Vit. K&quot;,
    badgeColor: &quot;#8b5cf6&quot;,
    desc: &quot;Brombeeren + Spinat = Vitamin-K-Synergie. Walnüsse für ALA Omega-3. Banane als schnelle KH post-run. Maximale Mikronährstoffdichte.&quot;,
    macros: { kcal: 762, protein: 50, fett: 31, kh: 72, bal: 16 },
    remaining: { kcal: &quot;~1045&quot;, protein: &quot;52 g&quot;, kh: &quot;168 g&quot;, fett: &quot;17 g&quot; },
    ingredients: [
      { name: &quot;TK Brombeeren&quot;, amount: &quot;150 g&quot;, tag: &quot;Anthocyane · Vit. K&quot;, tc: &quot;#8b5cf6&quot; },
      { name: &quot;TK Blattspinat&quot;, amount: &quot;65 g&quot;, tag: &quot;Vit. K + Folat&quot;, tc: &quot;#2a7a4f&quot; },
      { name: &quot;TK Banane&quot;, amount: &quot;90 g&quot;, tag: &quot;schnelle KH&quot;, tc: &quot;#2a7a4f&quot; },
      { name: &quot;Walnüsse, ganz&quot;, amount: &quot;20 g&quot;, tag: &quot;ALA Omega-3&quot;, tc: &quot;#d4860a&quot; },
      { name: &quot;Haferflocken, fein&quot;, amount: &quot;35 g&quot;, tag: null },
      { name: &quot;Leinsamen, gemahlen&quot;, amount: &quot;12 g&quot;, tag: &quot;ALA&quot;, tc: &quot;#d4860a&quot; },
    ],
    color: &quot;#8b5cf6&quot;,
    note: &quot;Farbe: tiefviolett · Brombeere + Spinat = fast schwarz · beerig dominant · einfachste Zubereitung&quot;,
  },
  {
    id: 2,
    name: &quot;Blackberry Beet Carrot Almond&quot;,
    badge: &quot;NO + DOMS · höchste KH&quot;,
    badgeColor: &quot;#dc2626&quot;,
    desc: &quot;Rohe Rote Beete + Brombeeren = maximaler NO-Boost plus Anthocyane. Karotte liefert Beta-Carotin. Höchste KH — optimales Glykogen-Replenishment.&quot;,
    macros: { kcal: 788, protein: 50, fett: 26, kh: 91, bal: 15 },
    remaining: { kcal: &quot;~1019&quot;, protein: &quot;52 g&quot;, kh: &quot;149 g&quot;, fett: &quot;22 g&quot; },
    ingredients: [
      { name: &quot;TK Brombeeren&quot;, amount: &quot;130 g&quot;, tag: &quot;Anthocyane&quot;, tc: &quot;#8b5cf6&quot; },
      { name: &quot;Rohe Rote Beete, gerieben&quot;, amount: &quot;70 g&quot;, tag: &quot;Nitrat roh ↑↑&quot;, tc: &quot;#dc2626&quot; },
      { name: &quot;TK Karotte, gegart&quot;, amount: &quot;100 g&quot;, tag: &quot;Beta-Carotin&quot;, tc: &quot;#e67e22&quot; },
      { name: &quot;TK Banane&quot;, amount: &quot;90 g&quot;, tag: &quot;KH + Bindung&quot;, tc: &quot;#2a7a4f&quot; },
      { name: &quot;Mandeln, ganz&quot;, amount: &quot;20 g&quot;, tag: null },
      { name: &quot;Haferflocken, fein&quot;, amount: &quot;30 g&quot;, tag: null },
      { name: &quot;Meersalz&quot;, amount: &quot;1 Prise&quot;, tag: &quot;Elektrolyte post-run&quot;, tc: &quot;#1a6b8a&quot; },
    ],
    color: &quot;#dc2626&quot;,
    note: &quot;Farbe: tief violett-rot · erdig-fruchtig · Rote Beete zuletzt in den Mixer&quot;,
  },
  {
    id: 3,
    name: &quot;Blackberry Broccoli Pea Mango&quot;,
    badge: &quot;Sulforaphan + Folat&quot;,
    badgeColor: &quot;#2a7a4f&quot;,
    desc: &quot;Drei Gemüse. Brombeeren + Mango überdecken Brokkoli und Erbsen vollständig. Höchstes Protein der Serie. Stärkste Mikronährstoffkombination.&quot;,
    macros: { kcal: 744, protein: 53, fett: 22, kh: 80, bal: 17 },
    remaining: { kcal: &quot;~1063&quot;, protein: &quot;49 g&quot;, kh: &quot;160 g&quot;, fett: &quot;26 g&quot; },
    ingredients: [
      { name: &quot;TK Brombeeren&quot;, amount: &quot;140 g&quot;, tag: &quot;Anthocyane · Vit. K&quot;, tc: &quot;#8b5cf6&quot; },
      { name: &quot;TK Brokkoli&quot;, amount: &quot;70 g&quot;, tag: &quot;Sulforaphan&quot;, tc: &quot;#2a7a4f&quot; },
      { name: &quot;TK Erbsen, aufgetaut&quot;, amount: &quot;80 g&quot;, tag: &quot;Folat&quot;, tc: &quot;#2a7a4f&quot; },
      { name: &quot;TK Mango&quot;, amount: &quot;140 g&quot;, tag: &quot;Gemüse überdecken&quot;, tc: &quot;#e67e22&quot; },
      { name: &quot;Hanfsamen, geschält&quot;, amount: &quot;20 g&quot;, tag: null },
      { name: &quot;Haferflocken, fein&quot;, amount: &quot;28 g&quot;, tag: null },
      { name: &quot;Limettensaft + Schale, Bio&quot;, amount: &quot;½ Limette&quot;, tag: &quot;Flavonoide&quot;, tc: &quot;#d4860a&quot; },
    ],
    color: &quot;#2a7a4f&quot;,
    note: &quot;Farbe: dunkelviolett · höchstes Protein (53 g) + Ballaststoffe (17 g) · Mango-Menge nicht reduzieren&quot;,
  },
];

const macroCols = [
  { key: &quot;kcal&quot;, label: &quot;kcal&quot;, color: &quot;#e8e4dc&quot; },
  { key: &quot;protein&quot;, label: &quot;Protein&quot;, color: &quot;#7c3aed&quot; },
  { key: &quot;fett&quot;, label: &quot;Fett&quot;, color: &quot;#d4860a&quot; },
  { key: &quot;kh&quot;, label: &quot;KH&quot;, color: &quot;#2a7a4f&quot; },
  { key: &quot;bal&quot;, label: &quot;Ballaststoffe&quot;, color: &quot;#1a6b8a&quot; },
];

export default function App() {
  const [open, setOpen] = useState(1);

  return (
    &lt;div style={{
      fontFamily: &quot;Georgia, serif&quot;,
      background: &quot;#0e1117&quot;,
      minHeight: &quot;100vh&quot;,
      padding: &quot;1.25rem 1rem 3rem&quot;,
      maxWidth: 520,
      margin: &quot;0 auto&quot;,
      color: &quot;#e8e4dc&quot;,
    }}&gt;

      {/* Header */}
      &lt;div style={{ marginBottom: &quot;1rem&quot; }}&gt;
        &lt;p style={{ fontSize: 10, letterSpacing: &quot;.15em&quot;, color: &quot;#444&quot;, margin: &quot;0 0 4px&quot;, fontFamily: &quot;monospace&quot; }}&gt;
          POST-RUN MITTAGESSEN · BROMBEERE + GEMÜSE
        &lt;/p&gt;
        &lt;h1 style={{ fontSize: 20, fontWeight: 700, margin: &quot;0 0 3px&quot; }}&gt;3 Lunch-Smoothies&lt;/h1&gt;
        &lt;p style={{ fontSize: 12, color: &quot;#555&quot;, margin: 0 }}&gt;
          300 ml Vollmilch · 35 g Proteinpulver · 5 g Kreatin · Brombeere in allen drei
        &lt;/p&gt;
      &lt;/div&gt;

      {/* Day status */}
      &lt;div style={{
        display: &quot;grid&quot;, gridTemplateColumns: &quot;repeat(4,1fr)&quot;, gap: 5, marginBottom: 14,
      }}&gt;
        {[
          { label: &quot;kcal übrig&quot;, val: &quot;1807&quot;, color: &quot;#e8e4dc&quot; },
          { label: &quot;Protein&quot;, val: &quot;102 g&quot;, color: &quot;#7c3aed&quot; },
          { label: &quot;KH&quot;, val: &quot;240 g&quot;, color: &quot;#2a7a4f&quot; },
          { label: &quot;Fett&quot;, val: &quot;48 g&quot;, color: &quot;#d4860a&quot; },
        ].map((d, i) =&gt; (
          &lt;div key={i} style={{
            background: &quot;#1a1e28&quot;, borderRadius: 8, padding: &quot;7px 8px&quot;,
            border: &quot;1px solid #2a2e3a&quot;, textAlign: &quot;center&quot;,
          }}&gt;
            &lt;div style={{ fontSize: 9, color: &quot;#444&quot;, marginBottom: 2, fontFamily: &quot;monospace&quot; }}&gt;{d.label}&lt;/div&gt;
            &lt;div style={{ fontSize: 13, fontWeight: 700, color: d.color }}&gt;{d.val}&lt;/div&gt;
          &lt;/div&gt;
        ))}
      &lt;/div&gt;

      {/* Smoothies */}
      {smoothies.map((s) =&gt; (
        &lt;div key={s.id} style={{
          background: &quot;#1a1e28&quot;,
          borderRadius: 14,
          marginBottom: 10,
          border: `1px solid ${open === s.id ? s.color + &quot;55&quot; : &quot;#2a2e3a&quot;}`,
          overflow: &quot;hidden&quot;,
        }}&gt;
          &lt;button
            onClick={() =&gt; setOpen(open === s.id ? null : s.id)}
            style={{ width: &quot;100%&quot;, background: &quot;none&quot;, border: &quot;none&quot;, padding: &quot;13px 14px 11px&quot;, textAlign: &quot;left&quot;, cursor: &quot;pointer&quot; }}
          &gt;
            {/* Badge + name */}
            &lt;div style={{ display: &quot;flex&quot;, alignItems: &quot;center&quot;, gap: 7, marginBottom: 4, flexWrap: &quot;wrap&quot; }}&gt;
              &lt;span style={{
                fontSize: 10, fontWeight: 700, padding: &quot;2px 9px&quot;,
                borderRadius: 20, background: s.color + &quot;22&quot;, color: s.color,
                letterSpacing: &quot;.04em&quot;, fontFamily: &quot;monospace&quot;,
              }}&gt;{s.badge}&lt;/span&gt;
              &lt;span style={{ fontSize: 15, fontWeight: 700, color: &quot;#e8e4dc&quot; }}&gt;{s.name}&lt;/span&gt;
              &lt;span style={{ marginLeft: &quot;auto&quot;, color: &quot;#444&quot;, fontSize: 13 }}&gt;{open === s.id ? &quot;▲&quot; : &quot;▼&quot;}&lt;/span&gt;
            &lt;/div&gt;
            &lt;p style={{ fontSize: 12, color: &quot;#666&quot;, margin: &quot;0 0 10px&quot;, lineHeight: 1.5 }}&gt;{s.desc}&lt;/p&gt;

            {/* Macros */}
            &lt;div style={{ display: &quot;grid&quot;, gridTemplateColumns: &quot;repeat(5,1fr)&quot;, gap: 5 }}&gt;
              {macroCols.map((c) =&gt; (
                &lt;div key={c.key} style={{
                  background: &quot;#12151e&quot;, borderRadius: 7, padding: &quot;6px 3px&quot;, textAlign: &quot;center&quot;,
                  border: c.key === &quot;kh&quot; ? `1px solid ${s.color}44` : &quot;1px solid transparent&quot;,
                }}&gt;
                  &lt;div style={{ fontSize: 9, color: &quot;#444&quot;, marginBottom: 1, fontFamily: &quot;monospace&quot; }}&gt;{c.label}&lt;/div&gt;
                  &lt;div style={{ fontSize: 12, fontWeight: 700, color: c.key === &quot;kh&quot; ? s.color : c.color }}&gt;
                    {c.key === &quot;kcal&quot; ? s.macros[c.key] : s.macros[c.key] + &quot; g&quot;}
                  &lt;/div&gt;
                &lt;/div&gt;
              ))}
            &lt;/div&gt;

            {/* Remaining */}
            &lt;div style={{
              display: &quot;grid&quot;, gridTemplateColumns: &quot;repeat(4,1fr)&quot;, gap: 4, marginTop: 6,
              background: &quot;#12151e&quot;, borderRadius: 8, padding: &quot;6px 8px&quot;,
            }}&gt;
              {[
                { label: &quot;kcal übrig&quot;, val: s.remaining.kcal, color: &quot;#555&quot; },
                { label: &quot;Protein&quot;, val: s.remaining.protein, color: &quot;#7c3aed&quot; },
                { label: &quot;KH&quot;, val: s.remaining.kh, color: &quot;#2a7a4f&quot; },
                { label: &quot;Fett&quot;, val: s.remaining.fett, color: &quot;#d4860a&quot; },
              ].map((r, i) =&gt; (
                &lt;div key={i} style={{ textAlign: &quot;center&quot; }}&gt;
                  &lt;div style={{ fontSize: 8, color: &quot;#333&quot;, fontFamily: &quot;monospace&quot;, marginBottom: 1 }}&gt;nach Smoothie&lt;/div&gt;
                  &lt;div style={{ fontSize: 9, color: &quot;#444&quot;, marginBottom: 1 }}&gt;{r.label}&lt;/div&gt;
                  &lt;div style={{ fontSize: 11, fontWeight: 700, color: r.color }}&gt;{r.val}&lt;/div&gt;
                &lt;/div&gt;
              ))}
            &lt;/div&gt;
          &lt;/button&gt;

          {/* Ingredients */}
          {open === s.id &amp;&amp; (
            &lt;div style={{ borderTop: &quot;1px solid #2a2e3a&quot;, padding: &quot;10px 14px 13px&quot; }}&gt;
              &lt;p style={{ fontSize: 9, fontWeight: 700, color: &quot;#333&quot;, letterSpacing: &quot;.12em&quot;, margin: &quot;0 0 7px&quot;, fontFamily: &quot;monospace&quot; }}&gt;
                ZUTATEN · 300 ml Milch + 35 g Pulver + 5 g Kreatin (Basis)
              &lt;/p&gt;
              {s.ingredients.map((ing, i) =&gt; (
                &lt;div key={i} style={{
                  display: &quot;flex&quot;, justifyContent: &quot;space-between&quot;, alignItems: &quot;flex-start&quot;,
                  padding: &quot;4px 0&quot;,
                  borderBottom: i &lt; s.ingredients.length - 1 ? &quot;1px solid #1e2230&quot; : &quot;none&quot;,
                }}&gt;
                  &lt;div&gt;
                    &lt;span style={{ fontSize: 13, color: &quot;#ddd&quot; }}&gt;{ing.name}&lt;/span&gt;
                    {ing.tag &amp;&amp; (
                      &lt;span style={{
                        fontSize: 10, marginLeft: 6, color: ing.tc || &quot;#888&quot;,
                        fontFamily: &quot;monospace&quot;,
                      }}&gt;· {ing.tag}&lt;/span&gt;
                    )}
                  &lt;/div&gt;
                  &lt;span style={{ fontSize: 12, fontWeight: 700, color: &quot;#666&quot;, whiteSpace: &quot;nowrap&quot;, marginLeft: 10 }}&gt;
                    {ing.amount}
                  &lt;/span&gt;
                &lt;/div&gt;
              ))}
              &lt;div style={{
                marginTop: 10, borderLeft: `3px solid ${s.color}`,
                paddingLeft: 9, fontSize: 11, color: &quot;#555&quot;, fontStyle: &quot;italic&quot;, lineHeight: 1.5,
              }}&gt;
                {s.note}
              &lt;/div&gt;
            &lt;/div&gt;
          )}
        &lt;/div&gt;
      ))}

      &lt;p style={{ fontSize: 10, color: &quot;#2a2e3a&quot;, textAlign: &quot;center&quot;, marginTop: 4, fontFamily: &quot;monospace&quot; }}&gt;
        TIPPE FÜR ZUTATEN · KH HIGHLIGHTED = POST-RUN PRIORITÄT
      &lt;/p&gt;
    &lt;/div&gt;
  );
}
</code></pre></details>
