---
titel: smoothies_620ml.jsx
status: aktiv
datum: '2026-04-24'
quelle:
  typ: claude
  url: https://claude.ai/chat/e243ac2d-4628-41b9-ae87-39b4cf14f878
  hinweis: Protein-Smoothies für Frühstück und Muskelaufbau
importiert: true
linie: smoothies-today-jsx-b74bc
---

<details><summary>Ursprüngliche Datei</summary><pre><code>import { useState } from &quot;react&quot;;

// Volume estimation: frozen ingredients ~0.85ml/g when blended, milk 1ml/g
// Target: 620ml total blended volume
// Base: 35g powder (~20ml), 5g creatine (0ml)
// Milk + frozen ingredients must reach ~600ml blended
// ~250ml milk + ~400g frozen = ~250 + 340 = 590 → +30ml water or adjust
// Each recipe calibrated individually

const smoothies = [
  {
    id: 1,
    num: &quot;01&quot;,
    name: &quot;Rote Kraft&quot;,
    subtitle: &quot;Beet · Cherry · Spinach&quot;,
    tagline: &quot;NO-Synthese + DOMS-Prävention&quot;,
    color: &quot;#b91c1c&quot;,
    light: &quot;#fef2f2&quot;,
    focus: [&quot;Nitrat → NO&quot;, &quot;Anthocyane&quot;, &quot;Vit. K + Folat&quot;, &quot;Eisen&quot;],
    macros: { kcal: 698, protein: 47, fett: 21, kh: 81, bal: 14 },
    volume: {
      milk: 240,
      frozen: [
        { name: &quot;TK Sauerkirschen&quot;, g: 130, ml: 111 },
        { name: &quot;Rohe Rote Beete, gerieben&quot;, g: 70, ml: 60 },
        { name: &quot;TK Blattspinat&quot;, g: 55, ml: 47 },
        { name: &quot;TK Banane&quot;, g: 85, ml: 72 },
      ],
      extras: [
        { name: &quot;Haferflocken, fein&quot;, g: 35, ml: 30 },
        { name: &quot;Chiasamen&quot;, g: 12, ml: 10 },
        { name: &quot;Zitronensaft, frisch&quot;, g: 20, ml: 20 },
      ],
      totalFrozenMl: 320,
      totalMl: 620,
    },
    ingredients: [
      { name: &quot;Vollmilch 3,8 %&quot;, amount: &quot;240 ml&quot;, role: &quot;Basis&quot; },
      { name: &quot;TK Sauerkirschen&quot;, amount: &quot;130 g&quot;, role: &quot;Anthocyane · DOMS↓&quot; },
      { name: &quot;Rohe Rote Beete, gerieben&quot;, amount: &quot;70 g&quot;, role: &quot;Nitrat roh → NO&quot; },
      { name: &quot;TK Blattspinat&quot;, amount: &quot;55 g&quot;, role: &quot;Vit. K + Folat + Eisen&quot; },
      { name: &quot;TK Banane&quot;, amount: &quot;85 g&quot;, role: &quot;KH + Bindung&quot; },
      { name: &quot;Haferflocken, fein&quot;, amount: &quot;35 g&quot;, role: &quot;β-Glucan · langsame KH&quot; },
      { name: &quot;Chiasamen&quot;, amount: &quot;12 g&quot;, role: &quot;ALA Omega-3&quot; },
      { name: &quot;Zitronensaft, frisch&quot;, amount: &quot;20 ml&quot;, role: &quot;Vit. C → Fe-Resorption ↑&quot; },
      { name: &quot;35 g Proteinpulver + 5 g Kreatin&quot;, amount: &quot;fix&quot;, role: null, fixed: true },
    ],
    note: &quot;Rote Beete zuletzt einmixen · Farbe: tief violett-schwarz · kein Gemüsegeschmack&quot;,
  },
  {
    id: 2,
    num: &quot;02&quot;,
    name: &quot;Grüne Tiefe&quot;,
    subtitle: &quot;Broccoli · Pea · Mango · Pineapple&quot;,
    tagline: &quot;Sulforaphan + Folat + Bromelain&quot;,
    color: &quot;#166534&quot;,
    light: &quot;#f0fdf4&quot;,
    focus: [&quot;Sulforaphan&quot;, &quot;Folat ~80%&quot;, &quot;Vit. C &gt;100%&quot;, &quot;Bromelain&quot;],
    macros: { kcal: 712, protein: 51, fett: 20, kh: 88, bal: 15 },
    volume: {
      milk: 230,
      frozen: [
        { name: &quot;TK Mango&quot;, g: 120, ml: 102 },
        { name: &quot;TK Ananas&quot;, g: 100, ml: 85 },
        { name: &quot;TK Brokkoli&quot;, g: 75, ml: 64 },
        { name: &quot;TK Erbsen&quot;, g: 75, ml: 64 },
      ],
      extras: [
        { name: &quot;Hanfsamen, geschält&quot;, g: 20, ml: 17 },
        { name: &quot;Haferflocken, fein&quot;, g: 28, ml: 24 },
        { name: &quot;Limette mit Schale, Bio&quot;, g: 30, ml: 25 },
      ],
      totalFrozenMl: 381,
      totalMl: 620,
    },
    ingredients: [
      { name: &quot;Vollmilch 3,8 %&quot;, amount: &quot;230 ml&quot;, role: &quot;Basis&quot; },
      { name: &quot;TK Mango&quot;, amount: &quot;120 g&quot;, role: &quot;Gemüse überdecken · Vit. C&quot; },
      { name: &quot;TK Ananas&quot;, amount: &quot;100 g&quot;, role: &quot;Bromelain · Süße&quot; },
      { name: &quot;TK Brokkoli&quot;, amount: &quot;75 g&quot;, role: &quot;Sulforaphan · direkt aus TK&quot; },
      { name: &quot;TK Erbsen, aufgetaut&quot;, amount: &quot;75 g&quot;, role: &quot;Folat · Protein&quot; },
      { name: &quot;Hanfsamen, geschält&quot;, amount: &quot;20 g&quot;, role: &quot;vollst. Aminosäuren · Mg&quot; },
      { name: &quot;Haferflocken, fein&quot;, amount: &quot;28 g&quot;, role: &quot;Ballaststoffe&quot; },
      { name: &quot;½ Bio-Limette mit Schale&quot;, amount: &quot;30 g&quot;, role: &quot;Flavonoide · D-Limonen&quot; },
      { name: &quot;35 g Proteinpulver + 5 g Kreatin&quot;, amount: &quot;fix&quot;, role: null, fixed: true },
    ],
    note: &quot;Brokkoli nicht auftauen — TK direkt · Mango + Ananas überdecken alles · Farbe: hellgrün-gelb&quot;,
  },
  {
    id: 3,
    num: &quot;03&quot;,
    name: &quot;Orangene Wärme&quot;,
    subtitle: &quot;Carrot · Peach · Turmeric · Walnut&quot;,
    tagline: &quot;Beta-Carotin + Curcumin + ALA&quot;,
    color: &quot;#c2410c&quot;,
    light: &quot;#fff7ed&quot;,
    focus: [&quot;Vit. A &gt;100%&quot;, &quot;Curcumin + Piperin&quot;, &quot;ALA ~4 g&quot;, &quot;Kalium ↑&quot;],
    macros: { kcal: 731, protein: 49, fett: 30, kh: 72, bal: 13 },
    volume: {
      milk: 245,
      frozen: [
        { name: &quot;TK Karotte, gegart&quot;, g: 120, ml: 102 },
        { name: &quot;TK Pfirsich&quot;, g: 140, ml: 119 },
        { name: &quot;TK Banane&quot;, g: 70, ml: 60 },
      ],
      extras: [
        { name: &quot;Walnüsse, ganz&quot;, g: 20, ml: 17 },
        { name: &quot;Leinsamen, gemahlen&quot;, g: 12, ml: 10 },
        { name: &quot;Haferflocken, fein&quot;, g: 30, ml: 26 },
        { name: &quot;Ingwer + Kurkuma + Pfeffer&quot;, g: 8, ml: 7 },
      ],
      totalFrozenMl: 342,
      totalMl: 620,
    },
    ingredients: [
      { name: &quot;Vollmilch 3,8 %&quot;, amount: &quot;245 ml&quot;, role: &quot;Basis&quot; },
      { name: &quot;TK Karotte, gegart&quot;, amount: &quot;120 g&quot;, role: &quot;Beta-Carotin · Kalium&quot; },
      { name: &quot;TK Pfirsich&quot;, amount: &quot;140 g&quot;, role: &quot;Kalium · mild-süß&quot; },
      { name: &quot;TK Banane&quot;, amount: &quot;70 g&quot;, role: &quot;Bindung + KH&quot; },
      { name: &quot;Walnüsse, ganz&quot;, amount: &quot;20 g&quot;, role: &quot;ALA Omega-3 · Polyphenole&quot; },
      { name: &quot;Leinsamen, gemahlen&quot;, amount: &quot;12 g&quot;, role: &quot;ALA · Ballaststoffe&quot; },
      { name: &quot;Haferflocken, fein&quot;, amount: &quot;30 g&quot;, role: &quot;langsame KH&quot; },
      { name: &quot;Ingwer 1,5 TL + Kurkuma ½ TL + Pfeffer 1 Msp.&quot;, amount: &quot;~8 g&quot;, role: &quot;Curcumin + Piperin → Resorption ↑&quot; },
      { name: &quot;35 g Proteinpulver + 5 g Kreatin&quot;, amount: &quot;fix&quot;, role: null, fixed: true },
    ],
    note: &quot;Farbe: leuchtendes Orange · kein Gemüsegeschmack · Walnüsse 10 Sek. trocken vorschroten&quot;,
  },
  {
    id: 4,
    num: &quot;04&quot;,
    name: &quot;Dunkle Beere&quot;,
    subtitle: &quot;Blackberry · Blueberry · Zucchini · Hemp&quot;,
    tagline: &quot;Polyphenol-Maximum + niedrigstes Fett&quot;,
    color: &quot;#4c1d95&quot;,
    light: &quot;#f5f3ff&quot;,
    focus: [&quot;Anthocyane ↑↑&quot;, &quot;Resveratrol&quot;, &quot;Vit. K&quot;, &quot;niedrigstes Fett&quot;],
    macros: { kcal: 672, protein: 50, fett: 18, kh: 76, bal: 16 },
    volume: {
      milk: 250,
      frozen: [
        { name: &quot;TK Brombeeren&quot;, g: 120, ml: 102 },
        { name: &quot;TK Blaubeeren&quot;, g: 100, ml: 85 },
        { name: &quot;TK Zucchini, roh&quot;, g: 100, ml: 85 },
        { name: &quot;TK Banane&quot;, g: 65, ml: 55 },
      ],
      extras: [
        { name: &quot;Hanfsamen, geschält&quot;, g: 22, ml: 19 },
        { name: &quot;Haferflocken, fein&quot;, g: 28, ml: 24 },
      ],
      totalFrozenMl: 370,
      totalMl: 620,
    },
    ingredients: [
      { name: &quot;Vollmilch 3,8 %&quot;, amount: &quot;250 ml&quot;, role: &quot;Basis&quot; },
      { name: &quot;TK Brombeeren&quot;, amount: &quot;120 g&quot;, role: &quot;Anthocyane · Vit. K&quot; },
      { name: &quot;TK Blaubeeren&quot;, amount: &quot;100 g&quot;, role: &quot;Anthocyane · Resveratrol&quot; },
      { name: &quot;TK Zucchini, roh gewürfelt&quot;, amount: &quot;100 g&quot;, role: &quot;Volumen ohne KH · kein Eigengeschmack&quot; },
      { name: &quot;TK Banane&quot;, amount: &quot;65 g&quot;, role: &quot;Cremigkeit + Süße&quot; },
      { name: &quot;Hanfsamen, geschält&quot;, amount: &quot;22 g&quot;, role: &quot;vollst. Aminosäuren · Mg&quot; },
      { name: &quot;Haferflocken, fein&quot;, amount: &quot;28 g&quot;, role: &quot;β-Glucan · Sättigung&quot; },
      { name: &quot;35 g Proteinpulver + 5 g Kreatin&quot;, amount: &quot;fix&quot;, role: null, fixed: true },
    ],
    note: &quot;Farbe: tief violett-schwarz · Zucchini unsichtbar · niedrigstes Fett der Serie (18 g)&quot;,
  },
];

const Vol = ({ recipe }) =&gt; {
  const total = recipe.volume.totalMl;
  const milkPct = (recipe.volume.milk / total) * 100;
  const frozenPct = (recipe.volume.totalFrozenMl / total) * 100;
  const extraPct = 100 - milkPct - frozenPct;

  return (
    &lt;div style={{ marginTop: 8 }}&gt;
      &lt;div style={{ display: &quot;flex&quot;, justifyContent: &quot;space-between&quot;, marginBottom: 3 }}&gt;
        &lt;span style={{ fontSize: 9, color: &quot;#555&quot;, fontFamily: &quot;monospace&quot; }}&gt;VOLUMEN · {total} ML GESAMT&lt;/span&gt;
      &lt;/div&gt;
      &lt;div style={{ height: 6, borderRadius: 3, overflow: &quot;hidden&quot;, display: &quot;flex&quot;, gap: 1 }}&gt;
        &lt;div style={{ width: `${milkPct}%`, background: &quot;#e8e4dc55&quot;, borderRadius: &quot;3px 0 0 3px&quot; }} /&gt;
        &lt;div style={{ width: `${frozenPct}%`, background: &quot;#ffffff22&quot; }} /&gt;
        &lt;div style={{ width: `${Math.max(extraPct, 0)}%`, background: &quot;#ffffff11&quot;, borderRadius: &quot;0 3px 3px 0&quot; }} /&gt;
      &lt;/div&gt;
      &lt;div style={{ display: &quot;flex&quot;, gap: 10, marginTop: 3 }}&gt;
        &lt;span style={{ fontSize: 9, color: &quot;#555&quot; }}&gt;Milch {recipe.volume.milk} ml&lt;/span&gt;
        &lt;span style={{ fontSize: 9, color: &quot;#555&quot; }}&gt;TK-Zutaten ~{recipe.volume.totalFrozenMl} ml&lt;/span&gt;
      &lt;/div&gt;
    &lt;/div&gt;
  );
};

export default function App() {
  const [open, setOpen] = useState(null);

  return (
    &lt;div style={{
      fontFamily: &quot;&#x27;Palatino Linotype&#x27;, &#x27;Book Antiqua&#x27;, Palatino, Georgia, serif&quot;,
      background: &quot;#080a0e&quot;,
      minHeight: &quot;100vh&quot;,
      padding: &quot;1.5rem 1rem 3rem&quot;,
      maxWidth: 540,
      margin: &quot;0 auto&quot;,
    }}&gt;

      {/* Header */}
      &lt;div style={{ marginBottom: &quot;1.5rem&quot;, borderBottom: &quot;1px solid #1a1e28&quot;, paddingBottom: &quot;1rem&quot; }}&gt;
        &lt;p style={{
          fontSize: 9, letterSpacing: &quot;.25em&quot;, color: &quot;#333&quot;,
          margin: &quot;0 0 6px&quot;, fontFamily: &quot;&#x27;Courier New&#x27;, monospace&quot;, textTransform: &quot;uppercase&quot;,
        }}&gt;
          35 g Proteinpulver · 5 g Kreatin · TK Obst &amp; Gemüse · Vollmilch
        &lt;/p&gt;
        &lt;h1 style={{
          fontSize: 26, fontWeight: 400, margin: &quot;0 0 4px&quot;,
          color: &quot;#e8e4dc&quot;, letterSpacing: &quot;-.02em&quot;, lineHeight: 1.15,
          fontStyle: &quot;italic&quot;,
        }}&gt;
          Vier Smoothies
        &lt;/h1&gt;
        &lt;p style={{ fontSize: 12, color: &quot;#444&quot;, margin: 0, letterSpacing: &quot;.05em&quot; }}&gt;
          620 ml · Vollmilch-Basis · evidenzbasierte Nährstoffverteilung
        &lt;/p&gt;
      &lt;/div&gt;

      {/* Recipe cards */}
      {smoothies.map((s, idx) =&gt; (
        &lt;div
          key={s.id}
          style={{
            marginBottom: 10,
            borderRadius: 3,
            overflow: &quot;hidden&quot;,
            border: `1px solid ${open === s.id ? s.color + &quot;80&quot; : &quot;#1a1e28&quot;}`,
            transition: &quot;border-color .25s&quot;,
            animation: `fadeIn .4s ease ${idx * 0.08}s both`,
          }}
        &gt;
          &lt;style&gt;{`
            @keyframes fadeIn { from { opacity:0; transform:translateY(8px); } to { opacity:1; transform:translateY(0); } }
          `}&lt;/style&gt;

          &lt;button
            onClick={() =&gt; setOpen(open === s.id ? null : s.id)}
            style={{
              width: &quot;100%&quot;, background: open === s.id ? &quot;#0d1018&quot; : &quot;#0d0f14&quot;,
              border: &quot;none&quot;, padding: &quot;14px 14px 12px&quot;, textAlign: &quot;left&quot;, cursor: &quot;pointer&quot;,
              transition: &quot;background .2s&quot;,
            }}
          &gt;
            {/* Number + name row */}
            &lt;div style={{ display: &quot;flex&quot;, alignItems: &quot;flex-start&quot;, gap: 12 }}&gt;
              &lt;span style={{
                fontSize: 36, fontWeight: 300, color: s.color + &quot;30&quot;,
                lineHeight: 1, fontStyle: &quot;italic&quot;, flexShrink: 0, marginTop: -4,
                fontFamily: &quot;Palatino, Georgia, serif&quot;,
              }}&gt;{s.num}&lt;/span&gt;
              &lt;div style={{ flex: 1 }}&gt;
                &lt;div style={{ display: &quot;flex&quot;, justifyContent: &quot;space-between&quot;, alignItems: &quot;flex-start&quot; }}&gt;
                  &lt;div&gt;
                    &lt;div style={{
                      fontSize: 17, fontWeight: 400, color: &quot;#e8e4dc&quot;,
                      letterSpacing: &quot;-.01em&quot;, fontStyle: &quot;italic&quot;,
                    }}&gt;{s.name}&lt;/div&gt;
                    &lt;div style={{ fontSize: 11, color: &quot;#444&quot;, marginTop: 1, letterSpacing: &quot;.08em&quot; }}&gt;
                      {s.subtitle}
                    &lt;/div&gt;
                  &lt;/div&gt;
                  &lt;span style={{
                    fontSize: 10, color: open === s.id ? s.color : &quot;#2a2e3a&quot;,
                    fontFamily: &quot;monospace&quot;, marginTop: 3, transition: &quot;color .2s&quot;,
                  }}&gt;
                    {open === s.id ? &quot;▲&quot; : &quot;▼&quot;}
                  &lt;/span&gt;
                &lt;/div&gt;

                {/* Tagline */}
                &lt;div style={{
                  display: &quot;inline-block&quot;, marginTop: 5,
                  fontSize: 10, color: s.color, letterSpacing: &quot;.06em&quot;,
                  borderBottom: `1px solid ${s.color}44`, paddingBottom: 1,
                  fontFamily: &quot;monospace&quot;,
                }}&gt;{s.tagline}&lt;/div&gt;

                {/* Focus tags */}
                &lt;div style={{ display: &quot;flex&quot;, gap: 4, flexWrap: &quot;wrap&quot;, marginTop: 6 }}&gt;
                  {s.focus.map((f, i) =&gt; (
                    &lt;span key={i} style={{
                      fontSize: 9, padding: &quot;2px 7px&quot;, borderRadius: 2,
                      background: s.color + &quot;15&quot;, color: s.color + &quot;cc&quot;,
                      fontFamily: &quot;monospace&quot;, letterSpacing: &quot;.04em&quot;,
                    }}&gt;{f}&lt;/span&gt;
                  ))}
                &lt;/div&gt;
              &lt;/div&gt;
            &lt;/div&gt;

            {/* Macro row */}
            &lt;div style={{
              display: &quot;grid&quot;, gridTemplateColumns: &quot;repeat(5,1fr)&quot;,
              gap: 4, marginTop: 10,
            }}&gt;
              {[
                { label: &quot;kcal&quot;, val: s.macros.kcal, key: &quot;kcal&quot; },
                { label: &quot;P&quot;, val: s.macros.protein + &quot;g&quot;, key: &quot;p&quot; },
                { label: &quot;F&quot;, val: s.macros.fett + &quot;g&quot;, key: &quot;f&quot; },
                { label: &quot;KH&quot;, val: s.macros.kh + &quot;g&quot;, key: &quot;kh&quot; },
                { label: &quot;Bal&quot;, val: s.macros.bal + &quot;g&quot;, key: &quot;b&quot; },
              ].map((m) =&gt; (
                &lt;div key={m.key} style={{
                  background: &quot;#0a0c10&quot;,
                  borderRadius: 2, padding: &quot;5px 3px&quot;, textAlign: &quot;center&quot;,
                  borderTop: m.key === &quot;kh&quot; ? `2px solid ${s.color}` : &quot;2px solid transparent&quot;,
                }}&gt;
                  &lt;div style={{ fontSize: 8, color: &quot;#333&quot;, fontFamily: &quot;monospace&quot;, marginBottom: 1 }}&gt;{m.label}&lt;/div&gt;
                  &lt;div style={{
                    fontSize: 12, fontWeight: 500,
                    color: m.key === &quot;kh&quot; ? s.color : m.key === &quot;p&quot; ? &quot;#8b8bcc&quot; : &quot;#555&quot;,
                  }}&gt;{m.val}&lt;/div&gt;
                &lt;/div&gt;
              ))}
            &lt;/div&gt;

            {/* Volume bar */}
            &lt;Vol recipe={s} /&gt;
          &lt;/button&gt;

          {/* Expandable ingredients */}
          {open === s.id &amp;&amp; (
            &lt;div style={{
              background: &quot;#080a0e&quot;,
              borderTop: `1px solid ${s.color}30`,
              padding: &quot;12px 14px 14px&quot;,
            }}&gt;
              &lt;p style={{
                fontSize: 9, color: &quot;#333&quot;, letterSpacing: &quot;.18em&quot;,
                margin: &quot;0 0 10px&quot;, fontFamily: &quot;monospace&quot;, textTransform: &quot;uppercase&quot;,
              }}&gt;Zutaten&lt;/p&gt;

              {s.ingredients.map((ing, i) =&gt; (
                &lt;div key={i} style={{
                  display: &quot;flex&quot;, justifyContent: &quot;space-between&quot;,
                  alignItems: &quot;flex-start&quot;,
                  padding: &quot;5px 0&quot;,
                  borderBottom: `1px solid #0e1018`,
                }}&gt;
                  &lt;div style={{ flex: 1 }}&gt;
                    &lt;span style={{
                      fontSize: 13, color: ing.fixed ? s.color + &quot;99&quot; : &quot;#ccc&quot;,
                      fontStyle: ing.fixed ? &quot;italic&quot; : &quot;normal&quot;,
                    }}&gt;{ing.name}&lt;/span&gt;
                    {ing.role &amp;&amp; (
                      &lt;div style={{
                        fontSize: 10, color: &quot;#333&quot;, marginTop: 1,
                        fontFamily: &quot;monospace&quot;,
                      }}&gt;{ing.role}&lt;/div&gt;
                    )}
                  &lt;/div&gt;
                  &lt;span style={{
                    fontSize: 12, color: ing.fixed ? s.color + &quot;66&quot; : &quot;#3a3e4a&quot;,
                    whiteSpace: &quot;nowrap&quot;, marginLeft: 12, paddingTop: 1,
                    fontFamily: &quot;monospace&quot;,
                  }}&gt;{ing.amount}&lt;/span&gt;
                &lt;/div&gt;
              ))}

              {/* Note */}
              &lt;div style={{
                marginTop: 12, padding: &quot;8px 10px&quot;,
                background: s.color + &quot;08&quot;,
                borderLeft: `2px solid ${s.color}40`,
                fontSize: 11, color: &quot;#444&quot;, fontStyle: &quot;italic&quot;, lineHeight: 1.6,
              }}&gt;
                {s.note}
              &lt;/div&gt;
            &lt;/div&gt;
          )}
        &lt;/div&gt;
      ))}

      &lt;p style={{
        fontSize: 9, color: &quot;#1a1e28&quot;, textAlign: &quot;center&quot;,
        marginTop: 12, fontFamily: &quot;monospace&quot;, letterSpacing: &quot;.15em&quot;,
      }}&gt;
        TIPPE FÜR ZUTATEN · KH MARKIERT · 620 ML GESAMT
      &lt;/p&gt;
    &lt;/div&gt;
  );
}
</code></pre></details>
