---
titel: pregym_smoothies.jsx
status: aktiv
datum: '2026-04-24'
quelle:
  typ: claude
  url: https://claude.ai/chat/e243ac2d-4628-41b9-ae87-39b4cf14f878
  hinweis: Protein-Smoothies für Frühstück und Muskelaufbau
importiert: true
---

<details><summary>Ursprüngliche Datei</summary><pre><code>import { useState } from &quot;react&quot;;

const breakfast = { kcal: 387, p: 17, f: 15, kh: 44 };
const target = { kcal: 2350, p: 117, f: 68, kh: 290 };
const rem = (k) =&gt; target[k] - breakfast[k];

const smoothies = [
  {
    id: 1,
    rank: &quot;Empfohlen&quot;,
    name: &quot;Mango Spinach Banana Hemp&quot;,
    badge: &quot;KH-Boost + Vit. K&quot;,
    badgeColor: &quot;#1a7a4a&quot;,
    rationale: &quot;Höchste KH für maximale Glykogen-Verfügbarkeit im Gym. Spinat deckt Vitamin K. Hanfsamen liefert vollständige Aminosäuren ohne Fettüberladung. Mango + Banane = cremig und süß.&quot;,
    pregym: &quot;KH für Energie · Spinat für Fokus (Folat) · leicht verdaulich&quot;,
    macros: { kcal: 646, p: 47, f: 21, kh: 75, bal: 10 },
    ingredients: [
      { name: &quot;Vollmilch 3,8 %&quot;, amt: &quot;220 ml&quot;, vol: 220, tag: null },
      { name: &quot;TK Mango&quot;, amt: &quot;150 g&quot;, vol: 142, tag: &quot;Vit. C · KH · Cremigkeit&quot; },
      { name: &quot;TK Banane&quot;, amt: &quot;80 g&quot;, vol: 76, tag: &quot;schnelle KH&quot; },
      { name: &quot;TK Blattspinat&quot;, amt: &quot;50 g&quot;, vol: 47, tag: &quot;Vit. K + Folat&quot; },
      { name: &quot;Hanfsamen, geschält&quot;, amt: &quot;15 g&quot;, vol: 17, tag: &quot;vollst. AS · Mg&quot; },
      { name: &quot;Haferflocken, fein&quot;, amt: &quot;30 g&quot;, vol: 48, tag: &quot;β-Glucan · langsame KH&quot; },
      { name: &quot;35 g Pulver + 5 g Kreatin&quot;, amt: &quot;fix&quot;, vol: 50, tag: null, fixed: true },
    ],
    totalVol: 600,
    color: &quot;#1a7a4a&quot;,
    note: &quot;Farbe: sattgrün · einfachste Zubereitung · Banane + Mango = natürlich cremig&quot;,
  },
  {
    id: 2,
    rank: &quot;Alternative A&quot;,
    name: &quot;Beet Blueberry Banana Spinach&quot;,
    badge: &quot;NO + Gymperformance&quot;,
    badgeColor: &quot;#8b1a4a&quot;,
    rationale: &quot;Rohe Rote Beete erhöht NO-Synthese → bessere Muskeldurchblutung und Kraft-Ausdauer im Gym. 60–90 Min. vor dem Training trinken für maximale Wirkung. Blaubeeren-Anthocyane zusätzlich anti-inflammatorisch.&quot;,
    pregym: &quot;Nitrat → NO → Muskeldurchblutung ↑ · Kraft-Ausdauer ↑&quot;,
    macros: { kcal: 597, p: 44, f: 17, kh: 70, bal: 12 },
    ingredients: [
      { name: &quot;Vollmilch 3,8 %&quot;, amt: &quot;215 ml&quot;, vol: 215, tag: null },
      { name: &quot;TK Blaubeeren&quot;, amt: &quot;125 g&quot;, vol: 119, tag: &quot;Anthocyane · Vit. K&quot; },
      { name: &quot;Rohe Rote Beete, gerieben&quot;, amt: &quot;60 g&quot;, vol: 57, tag: &quot;Nitrat roh ↑↑ · NO&quot; },
      { name: &quot;TK Banane&quot;, amt: &quot;80 g&quot;, vol: 76, tag: &quot;KH + Bindung&quot; },
      { name: &quot;TK Blattspinat&quot;, amt: &quot;55 g&quot;, vol: 52, tag: &quot;Vit. K&quot; },
      { name: &quot;Haferflocken, fein&quot;, amt: &quot;25 g&quot;, vol: 40, tag: null },
      { name: &quot;Chiasamen&quot;, amt: &quot;12 g&quot;, vol: 12, tag: &quot;Omega-3&quot; },
      { name: &quot;35 g Pulver + 5 g Kreatin&quot;, amt: &quot;fix&quot;, vol: 50, tag: null, fixed: true },
    ],
    totalVol: 621,
    color: &quot;#8b1a4a&quot;,
    note: &quot;Rote Beete zuletzt einfüllen · ~60–90 Min. vor Gym trinken für NO-Peak · niedrigstes Fett&quot;,
  },
  {
    id: 3,
    rank: &quot;Alternative B&quot;,
    name: &quot;Pineapple Broccoli Banana Flax&quot;,
    badge: &quot;Sulforaphan + Bromelain&quot;,
    badgeColor: &quot;#1a5a8a&quot;,
    rationale: &quot;Ananas überdeckt Brokkoli vollständig. Sulforaphan aktiviert Nrf2 (zellulären Stressschutz) — ideal vor intensivem Training. Bromelain wirkt anti-inflammatorisch. Höchste KH der drei.&quot;,
    pregym: &quot;Nrf2-Aktivierung vor Gym-Stress · Bromelain verhindert Muskelentzündung&quot;,
    macros: { kcal: 633, p: 47, f: 18, kh: 78, bal: 12 },
    ingredients: [
      { name: &quot;Vollmilch 3,8 %&quot;, amt: &quot;215 ml&quot;, vol: 215, tag: null },
      { name: &quot;TK Ananas&quot;, amt: &quot;140 g&quot;, vol: 133, tag: &quot;Bromelain · Vit. C&quot; },
      { name: &quot;TK Brokkoli&quot;, amt: &quot;80 g&quot;, vol: 76, tag: &quot;Sulforaphan · Nrf2↑&quot; },
      { name: &quot;TK Banane&quot;, amt: &quot;70 g&quot;, vol: 66, tag: &quot;schnelle KH&quot; },
      { name: &quot;Haferflocken, fein&quot;, amt: &quot;30 g&quot;, vol: 48, tag: &quot;β-Glucan&quot; },
      { name: &quot;Leinsamen, gemahlen&quot;, amt: &quot;12 g&quot;, vol: 12, tag: &quot;ALA Omega-3&quot; },
      { name: &quot;35 g Pulver + 5 g Kreatin&quot;, amt: &quot;fix&quot;, vol: 50, tag: null, fixed: true },
    ],
    totalVol: 600,
    color: &quot;#1a5a8a&quot;,
    note: &quot;Farbe: hellgelb-grün · höchste KH · Ananas-Menge nicht reduzieren — überdeckt Brokkoli vollständig&quot;,
  },
];

const mcols = [
  { key: &quot;kcal&quot;, label: &quot;kcal&quot;, color: &quot;#1a1a1a&quot;, unit: &quot;&quot; },
  { key: &quot;p&quot;, label: &quot;Protein&quot;, color: &quot;#7c3aed&quot;, unit: &quot;g&quot; },
  { key: &quot;f&quot;, label: &quot;Fett&quot;, color: &quot;#d4860a&quot;, unit: &quot;g&quot; },
  { key: &quot;kh&quot;, label: &quot;KH&quot;, color: &quot;#1a7a4a&quot;, unit: &quot;g&quot; },
  { key: &quot;bal&quot;, label: &quot;Ballaststoffe&quot;, color: &quot;#1a6b8a&quot;, unit: &quot;g&quot; },
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
          PRE-GYM MITTAGESSEN · 600 ML
        &lt;/p&gt;
        &lt;h1 style={{ fontSize: 19, fontWeight: 700, color: &quot;#1a1a1a&quot;, margin: &quot;0 0 3px&quot; }}&gt;
          3 Gym-Smoothies
        &lt;/h1&gt;
        &lt;p style={{ fontSize: 12, color: &quot;#999&quot;, margin: 0 }}&gt;
          Vollmilch · 35 g Pulver · 5 g Kreatin · TK Obst + Gemüse
        &lt;/p&gt;
      &lt;/div&gt;

      {/* Day status */}
      &lt;div style={{ background: &quot;#fff&quot;, borderRadius: 12, border: &quot;0.5px solid #e5e0d8&quot;, padding: &quot;10px 13px&quot;, marginBottom: 14 }}&gt;
        &lt;p style={{ fontSize: 9, fontFamily: &quot;monospace&quot;, fontWeight: 700, color: &quot;#bbb&quot;, letterSpacing: &quot;.1em&quot;, margin: &quot;0 0 7px&quot; }}&gt;
          FRÜHSTÜCK BEREITS · GYMTAG ZIELE
        &lt;/p&gt;
        &lt;div style={{ display: &quot;grid&quot;, gridTemplateColumns: &quot;repeat(4,1fr)&quot;, gap: 5, marginBottom: 7 }}&gt;
          {[
            { label: &quot;Gegessen&quot;, val: `${breakfast.kcal} kcal`, color: &quot;#aaa&quot; },
            { label: &quot;Protein&quot;, val: `${breakfast.p} g`, color: &quot;#7c3aed&quot; },
            { label: &quot;Fett&quot;, val: `${breakfast.f} g`, color: &quot;#d4860a&quot; },
            { label: &quot;KH&quot;, val: `${breakfast.kh} g`, color: &quot;#1a7a4a&quot; },
          ].map((d, i) =&gt; (
            &lt;div key={i} style={{ background: &quot;#f9f7f3&quot;, borderRadius: 7, padding: &quot;5px 3px&quot;, textAlign: &quot;center&quot; }}&gt;
              &lt;div style={{ fontSize: 9, color: &quot;#ccc&quot;, marginBottom: 1 }}&gt;{d.label}&lt;/div&gt;
              &lt;div style={{ fontSize: 11, fontWeight: 600, color: d.color }}&gt;{d.val}&lt;/div&gt;
            &lt;/div&gt;
          ))}
        &lt;/div&gt;
        &lt;div style={{ display: &quot;grid&quot;, gridTemplateColumns: &quot;repeat(4,1fr)&quot;, gap: 5 }}&gt;
          {[
            { label: &quot;kcal fehlen&quot;, val: `~${rem(&quot;kcal&quot;)}`, color: &quot;#555&quot; },
            { label: &quot;Protein&quot;, val: `~${rem(&quot;p&quot;)} g`, color: &quot;#7c3aed&quot; },
            { label: &quot;Fett&quot;, val: `~${rem(&quot;f&quot;)} g`, color: &quot;#d4860a&quot; },
            { label: &quot;KH&quot;, val: `~${rem(&quot;kh&quot;)} g`, color: &quot;#1a7a4a&quot; },
          ].map((d, i) =&gt; (
            &lt;div key={i} style={{ textAlign: &quot;center&quot; }}&gt;
              &lt;div style={{ fontSize: 8, color: &quot;#ddd&quot;, marginBottom: 1 }}&gt;noch offen&lt;/div&gt;
              &lt;div style={{ fontSize: 12, fontWeight: 700, color: d.color }}&gt;{d.val}&lt;/div&gt;
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
                &lt;p style={{ fontSize: 11, color: &quot;#888&quot;, margin: &quot;3px 0 4px&quot;, lineHeight: 1.5 }}&gt;{s.rationale}&lt;/p&gt;
                &lt;div style={{
                  display: &quot;inline-flex&quot;, alignItems: &quot;center&quot;, gap: 5,
                  background: s.color + &quot;0e&quot;, border: `0.5px solid ${s.color}25`,
                  borderRadius: 7, padding: &quot;3px 8px&quot;,
                }}&gt;
                  &lt;span style={{ fontSize: 10, color: s.color }}&gt;⚡ {s.pregym}&lt;/span&gt;
                &lt;/div&gt;
              &lt;/div&gt;
              &lt;span style={{ color: &quot;#ccc&quot;, fontSize: 13, marginTop: 2, flexShrink: 0 }}&gt;
                {open === s.id ? &quot;▲&quot; : &quot;▼&quot;}
              &lt;/span&gt;
            &lt;/div&gt;

            {/* Macros */}
            &lt;div style={{ display: &quot;grid&quot;, gridTemplateColumns: &quot;repeat(5,1fr)&quot;, gap: 5, marginTop: 9 }}&gt;
              {mcols.map((m) =&gt; (
                &lt;div key={m.key} style={{
                  background: &quot;#f9f7f3&quot;, borderRadius: 7, padding: &quot;5px 3px&quot;, textAlign: &quot;center&quot;,
                  border: m.key === &quot;kh&quot; ? `0.5px solid ${s.color}50` : &quot;0.5px solid transparent&quot;,
                }}&gt;
                  &lt;div style={{ fontSize: 9, color: &quot;#ccc&quot;, marginBottom: 1 }}&gt;{m.label}&lt;/div&gt;
                  &lt;div style={{ fontSize: 12, fontWeight: 700, color: m.key === &quot;kh&quot; ? s.color : m.color }}&gt;
                    {s.macros[m.key]}{m.unit}
                  &lt;/div&gt;
                &lt;/div&gt;
              ))}
            &lt;/div&gt;

            {/* After smoothie remaining */}
            &lt;div style={{
              display: &quot;grid&quot;, gridTemplateColumns: &quot;repeat(4,1fr)&quot;, gap: 4, marginTop: 6,
              background: &quot;#f9f7f3&quot;, borderRadius: 8, padding: &quot;5px 8px&quot;,
            }}&gt;
              {mcols.filter(m =&gt; m.key !== &quot;bal&quot;).map((m) =&gt; {
                const after = rem(m.key === &quot;p&quot; ? &quot;p&quot; : m.key === &quot;f&quot; ? &quot;f&quot; : m.key === &quot;kh&quot; ? &quot;kh&quot; : &quot;kcal&quot;) - s.macros[m.key === &quot;p&quot; ? &quot;p&quot; : m.key === &quot;f&quot; ? &quot;f&quot; : m.key === &quot;kh&quot; ? &quot;kh&quot; : &quot;kcal&quot;];
                return (
                  &lt;div key={m.key} style={{ textAlign: &quot;center&quot; }}&gt;
                    &lt;div style={{ fontSize: 8, color: &quot;#ddd&quot; }}&gt;nach Smoothie&lt;/div&gt;
                    &lt;div style={{ fontSize: 10, fontWeight: 700, color: after &lt; 0 ? &quot;#c0392b&quot; : m.color }}&gt;
                      {after &gt; 0 ? `~${Math.round(after)}${m.unit}` : &quot;gedeckt&quot;}
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
                &lt;p style={{ fontSize: 9, fontWeight: 700, color: &quot;#ccc&quot;, letterSpacing: &quot;.12em&quot;, margin: 0, fontFamily: &quot;monospace&quot; }}&gt;
                  ZUTATEN
                &lt;/p&gt;
                &lt;span style={{ fontSize: 10, color: s.color, fontWeight: 600 }}&gt;
                  ≈ {s.totalVol} ml vor dem Mixen
                &lt;/span&gt;
              &lt;/div&gt;

              {/* Volume bar */}
              &lt;div style={{ display: &quot;flex&quot;, gap: 1, marginBottom: 8, height: 8, borderRadius: 4, overflow: &quot;hidden&quot; }}&gt;
                {s.ingredients.map((ing, i) =&gt; {
                  const pct = (ing.vol / s.totalVol) * 100;
                  const colors = [&quot;#d4860a&quot;, &quot;#1a7a4a&quot;, &quot;#e67e22&quot;, &quot;#1a7a4a&quot;, &quot;#1a6b8a&quot;, &quot;#888&quot;, &quot;#7c3aed&quot;];
                  return (
                    &lt;div key={i} style={{
                      width: `${pct}%`, background: colors[i],
                      opacity: ing.fixed ? 0.4 : 0.6,
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

      &lt;div style={{
        background: &quot;#fff&quot;, borderRadius: 10, border: &quot;0.5px solid #e5e0d8&quot;,
        padding: &quot;9px 12px&quot;, marginTop: 4,
      }}&gt;
        &lt;p style={{ fontSize: 9, fontFamily: &quot;monospace&quot;, fontWeight: 700, color: &quot;#bbb&quot;, letterSpacing: &quot;.1em&quot;, margin: &quot;0 0 4px&quot; }}&gt;TIMING&lt;/p&gt;
        &lt;p style={{ fontSize: 12, color: &quot;#888&quot;, margin: 0, lineHeight: 1.5 }}&gt;
          60–90 Min. vor dem Gym trinken — besonders für Nr. 2 (Rote Beete) wichtig, da NO-Peak erst nach ~60 Min. einsetzt. Nr. 1 und 3 auch 30–45 Min. vorher möglich.
        &lt;/p&gt;
      &lt;/div&gt;
    &lt;/div&gt;
  );
}
</code></pre></details>
