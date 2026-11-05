---
titel: restday_smoothies.jsx
status: archiv
datum: '2026-04-24'
quelle:
  typ: claude
  url: https://claude.ai/chat/e243ac2d-4628-41b9-ae87-39b4cf14f878
  hinweis: Protein-Smoothies für Frühstück und Muskelaufbau
importiert: true
linie: smoothies-today-jsx-b74bc
---

<details><summary>Ursprüngliche Datei</summary><pre><code>import { useState } from &quot;react&quot;;

// From tracker: 2400 target shown, but REST DAY → use 1900 kcal
// Consumed: 2400-1718=682 kcal · Fett ~32g · KH ~33g · Protein ~21g
const eaten  = { kcal: 682, p: 21, f: 32, kh: 33 };
const trkApp = { kcal: 2400, p: 117, f: 68,  kh: 290 }; // app target (training day)
const tgtRest= { kcal: 1900, p: 117, f: 63,  kh: 214 }; // correct rest day target

const rem = (k) =&gt; Math.max(0, tgtRest[k] - eaten[k]);

const smoothies = [
  {
    id: 1,
    rank: &quot;Empfohlen&quot;,
    name: &quot;Mango Spinach Pea Chia&quot;,
    badge: &quot;Folat + Vit. K&quot;,
    badgeColor: &quot;#1a7a4a&quot;,
    rationale: &quot;Fettärmstes Rezept. Erbsen + Spinat decken Folat und Vit. K — beide heute noch offen. Mango für KH und Cremigkeit. Chia statt Nüssen: ALA ohne Fettüberlast am Ruhetag.&quot;,
    macros: { kcal: 593, p: 47, f: 17, kh: 66, bal: 12 },
    ingredients: [
      { name: &quot;Vollmilch 3,8 %&quot;,     amt: &quot;220 ml&quot;, vol: 220, tag: null },
      { name: &quot;TK Mango&quot;,            amt: &quot;160 g&quot;,  vol: 152, tag: &quot;Vit. C · KH · Cremigkeit&quot; },
      { name: &quot;TK Blattspinat&quot;,      amt: &quot;60 g&quot;,   vol: 57,  tag: &quot;Vit. K &gt;250 %&quot; },
      { name: &quot;TK Erbsen, aufgetaut&quot;,amt: &quot;70 g&quot;,   vol: 66,  tag: &quot;Folat ~60 % RDA&quot; },
      { name: &quot;Haferflocken, fein&quot;,  amt: &quot;28 g&quot;,   vol: 45,  tag: &quot;β-Glucan · langsame KH&quot; },
      { name: &quot;Chiasamen&quot;,           amt: &quot;10 g&quot;,   vol: 10,  tag: &quot;ALA · kein Nussanteil&quot; },
      { name: &quot;35 g Pulver + 5 g Kreatin&quot;, amt: &quot;fix&quot;, vol: 50, tag: null, fixed: true },
    ],
    totalVol: 600,
    note: &quot;Farbe: sattgrün · Mango überdeckt Spinat + Erbsen vollständig · niedrigstes Fett der drei&quot;,
    color: &quot;#1a7a4a&quot;,
  },
  {
    id: 2,
    rank: &quot;Alternative A&quot;,
    name: &quot;Cherry Blueberry Spinach Oat&quot;,
    badge: &quot;DOMS + Antioxidantien&quot;,
    badgeColor: &quot;#7c1a7a&quot;,
    rationale: &quot;Ruhetag = Regenerationstag. Sauerkirsche + Blaubeeren = doppelte Anthocyan-Dosis für Muskelregeneration nach vorherigen Trainingstagen. Spinat für Vit. K. Niedrigste kcal — gut für Ruhetag.&quot;,
    macros: { kcal: 555, p: 44, f: 18, kh: 57, bal: 13 },
    ingredients: [
      { name: &quot;Vollmilch 3,8 %&quot;,     amt: &quot;215 ml&quot;, vol: 215, tag: null },
      { name: &quot;TK Sauerkirschen&quot;,    amt: &quot;120 g&quot;,  vol: 114, tag: &quot;COX-Hemmer · DOMS↓&quot; },
      { name: &quot;TK Blaubeeren&quot;,       amt: &quot;110 g&quot;,  vol: 105, tag: &quot;Anthocyane · Vit. K&quot; },
      { name: &quot;TK Blattspinat&quot;,      amt: &quot;55 g&quot;,   vol: 52,  tag: &quot;Vit. K + Folat&quot; },
      { name: &quot;Haferflocken, fein&quot;,  amt: &quot;28 g&quot;,   vol: 45,  tag: null },
      { name: &quot;Chiasamen&quot;,           amt: &quot;12 g&quot;,   vol: 12,  tag: &quot;Omega-3&quot; },
      { name: &quot;35 g Pulver + 5 g Kreatin&quot;, amt: &quot;fix&quot;, vol: 50, tag: null, fixed: true },
    ],
    totalVol: 593,
    note: &quot;Farbe: dunkelviolett · niedrigste kcal der Serie → ideal Ruhetag · Kirsche + Beere = starke Regenerationskombi&quot;,
    color: &quot;#7c1a7a&quot;,
  },
  {
    id: 3,
    rank: &quot;Alternative B&quot;,
    name: &quot;Beet Peach Spinach Oat Chia&quot;,
    badge: &quot;NO-Boost + leicht&quot;,
    badgeColor: &quot;#8b1a4a&quot;,
    rationale: &quot;Rote Beete roh liefert Nitrat für vaskuläre Gesundheit — auch an Ruhetagen sinnvoll für Erholung. Pfirsich gibt Cremigkeit und Kalium. Kein Nussanteil, fettarm.&quot;,
    macros: { kcal: 571, p: 45, f: 18, kh: 59, bal: 11 },
    ingredients: [
      { name: &quot;Vollmilch 3,8 %&quot;,           amt: &quot;225 ml&quot;, vol: 225, tag: null },
      { name: &quot;TK Pfirsich&quot;,               amt: &quot;150 g&quot;,  vol: 142, tag: &quot;Kalium · mild-cremig&quot; },
      { name: &quot;Rohe Rote Beete, gerieben&quot;, amt: &quot;65 g&quot;,   vol: 62,  tag: &quot;Nitrat roh ↑↑&quot; },
      { name: &quot;TK Blattspinat&quot;,            amt: &quot;55 g&quot;,   vol: 52,  tag: &quot;Vit. K · Folat&quot; },
      { name: &quot;Haferflocken, fein&quot;,        amt: &quot;35 g&quot;,   vol: 56,  tag: &quot;β-Glucan&quot; },
      { name: &quot;Chiasamen&quot;,                 amt: &quot;12 g&quot;,   vol: 12,  tag: &quot;ALA&quot; },
      { name: &quot;35 g Pulver + 5 g Kreatin&quot;, amt: &quot;fix&quot;,    vol: 50,  tag: null, fixed: true },
    ],
    totalVol: 599,
    note: &quot;Farbe: lila-rosa · Rote Beete zuletzt einfüllen · Pfirsich + Beete = ungewöhnlich gut&quot;,
    color: &quot;#8b1a4a&quot;,
  },
];

const mcols = [
  { key: &quot;kcal&quot;, label: &quot;kcal&quot;,          color: &quot;#1a1a1a&quot;, unit: &quot;&quot; },
  { key: &quot;p&quot;,   label: &quot;Protein&quot;,        color: &quot;#7c3aed&quot;, unit: &quot;g&quot; },
  { key: &quot;f&quot;,   label: &quot;Fett&quot;,           color: &quot;#d4860a&quot;, unit: &quot;g&quot; },
  { key: &quot;kh&quot;,  label: &quot;KH&quot;,             color: &quot;#1a7a4a&quot;, unit: &quot;g&quot; },
  { key: &quot;bal&quot;, label: &quot;Ballaststoffe&quot;,  color: &quot;#1a6b8a&quot;, unit: &quot;g&quot; },
];

export default function App() {
  const [open, setOpen] = useState(1);

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
          RUHETAG · MITTAGESSEN · 600 ML
        &lt;/p&gt;
        &lt;h1 style={{ fontSize: 19, fontWeight: 700, color: &quot;#1a1a1a&quot;, margin: &quot;0 0 3px&quot; }}&gt;
          3 Ruhetag-Smoothies
        &lt;/h1&gt;
        &lt;p style={{ fontSize: 12, color: &quot;#999&quot;, margin: 0 }}&gt;
          Vollmilch · 35 g Pulver · 5 g Kreatin · Gemüse in allen drei
        &lt;/p&gt;
      &lt;/div&gt;

      {/* Tracker note */}
      &lt;div style={{
        background: &quot;#fff8e1&quot;, borderRadius: 10,
        border: &quot;0.5px solid #ffc10760&quot;, padding: &quot;8px 12px&quot;, marginBottom: 10,
      }}&gt;
        &lt;p style={{ fontSize: 11, color: &quot;#856404&quot;, margin: 0, lineHeight: 1.5 }}&gt;
          &lt;strong&gt;App zeigt 2,4k-Ziel&lt;/strong&gt; — das ist dein Trainingstag-Setting. Ruhetag-Ziel: &lt;strong&gt;~1.900 kcal · 214 g KH · 63 g Fett&lt;/strong&gt;. Smoothies unten sind auf Ruhetag kalibriert.
        &lt;/p&gt;
      &lt;/div&gt;

      {/* Day status */}
      &lt;div style={{
        background: &quot;#fff&quot;, borderRadius: 12, border: &quot;0.5px solid #e5e0d8&quot;,
        padding: &quot;10px 13px&quot;, marginBottom: 14,
      }}&gt;
        &lt;p style={{ fontSize: 9, fontFamily: &quot;monospace&quot;, fontWeight: 700, color: &quot;#bbb&quot;, letterSpacing: &quot;.1em&quot;, margin: &quot;0 0 7px&quot; }}&gt;
          FRÜHSTÜCK BEREITS · RUHETAG-ZIELE
        &lt;/p&gt;
        &lt;div style={{ display: &quot;grid&quot;, gridTemplateColumns: &quot;repeat(4,1fr)&quot;, gap: 5, marginBottom: 8 }}&gt;
          {[
            { label: &quot;Gegessen&quot;,  val: &quot;682 kcal&quot;, color: &quot;#888&quot; },
            { label: &quot;Protein&quot;,   val: &quot;21 g&quot;,     color: &quot;#7c3aed&quot; },
            { label: &quot;Fett&quot;,      val: &quot;32 g&quot;,     color: &quot;#d4860a&quot; },
            { label: &quot;KH&quot;,        val: &quot;33 g&quot;,     color: &quot;#1a7a4a&quot; },
          ].map((d, i) =&gt; (
            &lt;div key={i} style={{ background: &quot;#f9f7f3&quot;, borderRadius: 7, padding: &quot;5px 3px&quot;, textAlign: &quot;center&quot; }}&gt;
              &lt;div style={{ fontSize: 9, color: &quot;#ccc&quot;, marginBottom: 1 }}&gt;{d.label}&lt;/div&gt;
              &lt;div style={{ fontSize: 11, fontWeight: 600, color: d.color }}&gt;{d.val}&lt;/div&gt;
            &lt;/div&gt;
          ))}
        &lt;/div&gt;
        &lt;div style={{ display: &quot;grid&quot;, gridTemplateColumns: &quot;repeat(4,1fr)&quot;, gap: 5 }}&gt;
          {[
            { label: &quot;kcal offen&quot;,  val: `~${rem(&quot;kcal&quot;)}`,    color: &quot;#555&quot; },
            { label: &quot;Protein&quot;,     val: `~${rem(&quot;p&quot;)} g`,    color: &quot;#7c3aed&quot; },
            { label: &quot;Fett&quot;,        val: `~${rem(&quot;f&quot;)} g`,    color: &quot;#d4860a&quot; },
            { label: &quot;KH&quot;,          val: `~${rem(&quot;kh&quot;)} g`,   color: &quot;#1a7a4a&quot; },
          ].map((d, i) =&gt; (
            &lt;div key={i} style={{ textAlign: &quot;center&quot; }}&gt;
              &lt;div style={{ fontSize: 8, color: &quot;#ddd&quot;, marginBottom: 1 }}&gt;noch offen&lt;/div&gt;
              &lt;div style={{ fontSize: 12, fontWeight: 700, color: d.color }}&gt;{d.val}&lt;/div&gt;
            &lt;/div&gt;
          ))}
        &lt;/div&gt;
      &lt;/div&gt;

      {/* Cards */}
      {smoothies.map((s) =&gt; (
        &lt;div key={s.id} style={{
          background: &quot;#fff&quot;,
          borderRadius: 12,
          border: `0.5px solid ${open === s.id ? s.color + &quot;55&quot; : &quot;#e5e0d8&quot;}`,
          marginBottom: 10, overflow: &quot;hidden&quot;,
          transition: &quot;border-color .15s&quot;,
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
                    background: s.id === 1 ? &quot;#1a1a1a&quot; : &quot;#f0ece4&quot;,
                    color: s.id === 1 ? &quot;#fff&quot; : &quot;#888&quot;,
                    fontFamily: &quot;monospace&quot;, letterSpacing: &quot;.05em&quot;,
                  }}&gt;{s.rank}&lt;/span&gt;
                  &lt;span style={{
                    fontSize: 10, fontWeight: 700, padding: &quot;2px 7px&quot;, borderRadius: 20,
                    background: s.color + &quot;14&quot;, color: s.color, fontFamily: &quot;monospace&quot;,
                  }}&gt;{s.badge}&lt;/span&gt;
                &lt;/div&gt;
                &lt;div style={{ fontSize: 14, fontWeight: 700, color: &quot;#1a1a1a&quot; }}&gt;{s.name}&lt;/div&gt;
                &lt;p style={{ fontSize: 11, color: &quot;#888&quot;, margin: &quot;3px 0 0&quot;, lineHeight: 1.5 }}&gt;{s.rationale}&lt;/p&gt;
              &lt;/div&gt;
              &lt;span style={{ color: &quot;#ccc&quot;, fontSize: 13, flexShrink: 0, marginTop: 2 }}&gt;
                {open === s.id ? &quot;▲&quot; : &quot;▼&quot;}
              &lt;/span&gt;
            &lt;/div&gt;

            {/* Macros */}
            &lt;div style={{ display: &quot;grid&quot;, gridTemplateColumns: &quot;repeat(5,1fr)&quot;, gap: 5, marginTop: 9 }}&gt;
              {mcols.map((m) =&gt; (
                &lt;div key={m.key} style={{
                  background: &quot;#f9f7f3&quot;, borderRadius: 7, padding: &quot;5px 3px&quot;, textAlign: &quot;center&quot;,
                  border: m.key === &quot;kh&quot; ? `0.5px solid ${s.color}45` : &quot;0.5px solid transparent&quot;,
                }}&gt;
                  &lt;div style={{ fontSize: 9, color: &quot;#ccc&quot;, marginBottom: 1 }}&gt;{m.label}&lt;/div&gt;
                  &lt;div style={{ fontSize: 12, fontWeight: 700, color: m.key === &quot;kh&quot; ? s.color : m.color }}&gt;
                    {s.macros[m.key]}{m.unit}
                  &lt;/div&gt;
                &lt;/div&gt;
              ))}
            &lt;/div&gt;

            {/* After-smoothie remaining */}
            &lt;div style={{
              display: &quot;grid&quot;, gridTemplateColumns: &quot;repeat(4,1fr)&quot;, gap: 4, marginTop: 6,
              background: &quot;#f9f7f3&quot;, borderRadius: 8, padding: &quot;5px 8px&quot;,
            }}&gt;
              {[
                { key: &quot;kcal&quot;, label: &quot;kcal übrig&quot; },
                { key: &quot;p&quot;,    label: &quot;Protein&quot; },
                { key: &quot;f&quot;,    label: &quot;Fett&quot; },
                { key: &quot;kh&quot;,   label: &quot;KH&quot; },
              ].map((d) =&gt; {
                const after = rem(d.key) - s.macros[d.key];
                const c = d.key === &quot;p&quot; ? &quot;#7c3aed&quot; : d.key === &quot;f&quot; ? &quot;#d4860a&quot; : d.key === &quot;kh&quot; ? &quot;#1a7a4a&quot; : &quot;#555&quot;;
                const unit = d.key === &quot;kcal&quot; ? &quot;&quot; : &quot; g&quot;;
                return (
                  &lt;div key={d.key} style={{ textAlign: &quot;center&quot; }}&gt;
                    &lt;div style={{ fontSize: 8, color: &quot;#ddd&quot; }}&gt;{d.label} nach&lt;/div&gt;
                    &lt;div style={{ fontSize: 11, fontWeight: 700, color: after &lt; 0 ? &quot;#c0392b&quot; : c }}&gt;
                      {after &gt;= 0 ? `~${Math.round(after)}${unit}` : &quot;✓&quot;}
                    &lt;/div&gt;
                  &lt;/div&gt;
                );
              })}
            &lt;/div&gt;
          &lt;/button&gt;

          {/* Ingredients */}
          {open === s.id &amp;&amp; (
            &lt;div style={{ borderTop: &quot;0.5px solid #f0ece4&quot;, padding: &quot;8px 13px 12px&quot; }}&gt;
              &lt;div style={{ display: &quot;flex&quot;, justifyContent: &quot;space-between&quot;, alignItems: &quot;center&quot;, marginBottom: 7 }}&gt;
                &lt;p style={{ fontSize: 9, fontWeight: 700, color: &quot;#ccc&quot;, letterSpacing: &quot;.12em&quot;, margin: 0, fontFamily: &quot;monospace&quot; }}&gt;ZUTATEN&lt;/p&gt;
                &lt;span style={{ fontSize: 10, color: s.color, fontWeight: 600 }}&gt;≈ {s.totalVol} ml&lt;/span&gt;
              &lt;/div&gt;

              {/* Volume strip */}
              &lt;div style={{ display: &quot;flex&quot;, gap: 1, marginBottom: 8, height: 6, borderRadius: 3, overflow: &quot;hidden&quot; }}&gt;
                {s.ingredients.map((ing, i) =&gt; {
                  const cols = [&quot;#d4860a&quot;,&quot;#1a7a4a&quot;,&quot;#e67e22&quot;,&quot;#1a7a4a&quot;,&quot;#1a6b8a&quot;,&quot;#888&quot;,&quot;#7c3aed&quot;];
                  return (
                    &lt;div key={i} style={{
                      flexBasis: `${(ing.vol / s.totalVol) * 100}%`,
                      background: cols[i], opacity: ing.fixed ? 0.35 : 0.55,
                    }} /&gt;
                  );
                })}
              &lt;/div&gt;

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
                    {ing.tag &amp;&amp; &lt;span style={{ fontSize: 10, color: s.color, marginLeft: 5, fontFamily: &quot;monospace&quot; }}&gt;· {ing.tag}&lt;/span&gt;}
                  &lt;/div&gt;
                  &lt;div style={{ textAlign: &quot;right&quot;, marginLeft: 8, flexShrink: 0 }}&gt;
                    &lt;div style={{ fontSize: 11, fontWeight: 700, color: &quot;#bbb&quot; }}&gt;{ing.amt}&lt;/div&gt;
                    {!ing.fixed &amp;&amp; &lt;div style={{ fontSize: 9, color: &quot;#ddd&quot; }}&gt;≈ {ing.vol} ml&lt;/div&gt;}
                  &lt;/div&gt;
                &lt;/div&gt;
              ))}
              &lt;div style={{
                marginTop: 8, fontSize: 11, color: &quot;#999&quot;, fontStyle: &quot;italic&quot;,
                borderLeft: `3px solid ${s.color}35`, paddingLeft: 8, lineHeight: 1.5,
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
        padding: &quot;9px 12px&quot;, marginTop: 2,
      }}&gt;
        &lt;p style={{ fontSize: 9, fontFamily: &quot;monospace&quot;, fontWeight: 700, color: &quot;#bbb&quot;, letterSpacing: &quot;.1em&quot;, margin: &quot;0 0 4px&quot; }}&gt;
          NACH DEM SMOOTHIE · ABENDESSEN
        &lt;/p&gt;
        &lt;p style={{ fontSize: 12, color: &quot;#888&quot;, margin: 0, lineHeight: 1.5 }}&gt;
          Noch ~45–50 g Protein und ~115–125 g KH offen. Fett ist mit ~13 g knapp — Abendessen fettarm halten: Hülsenfrüchte im Instant Pot, Quark, oder Magerquark-Auflauf wären ideal.
        &lt;/p&gt;
      &lt;/div&gt;
    &lt;/div&gt;
  );
}
</code></pre></details>
