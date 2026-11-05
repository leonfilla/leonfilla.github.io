---
titel: smoothie_ingredient_macros.jsx
status: aktiv
datum: '2026-04-24'
quelle:
  typ: claude
  url: https://claude.ai/chat/e243ac2d-4628-41b9-ae87-39b4cf14f878
  hinweis: Protein-Smoothies für Frühstück und Muskelaufbau
importiert: true
---

<details><summary>Ursprüngliche Datei</summary><pre><code>const ingredients = [
  {
    name: &quot;Vollmilch 3,8 %&quot;,
    amount: &quot;300 ml&quot;,
    source: &quot;BLS&quot;,
    kcal: 195, protein: 10.2, fett: 11.4, kh: 14.1, bal: 0.0,
    note: &quot;Casein + Molke · Calcium · B12&quot;,
  },
  {
    name: &quot;Proteinpulver, vegan&quot;,
    amount: &quot;35 g&quot;,
    source: &quot;Label&quot;,
    fixed: true,
    kcal: 131, protein: 27.0, fett: 1.9, kh: 0.9, bal: 2.0,
    note: &quot;77 g P / 100 g · kein Zucker&quot;,
  },
  {
    name: &quot;Kreatin&quot;,
    amount: &quot;5 g&quot;,
    source: &quot;—&quot;,
    fixed: true,
    kcal: 0, protein: 0, fett: 0, kh: 0, bal: 0,
    note: &quot;Kalorienneutral · Aufnahme ↑ mit KH&quot;,
  },
  {
    name: &quot;TK Sauerkirschen&quot;,
    amount: &quot;150 g&quot;,
    source: &quot;BLS&quot;,
    kcal: 75, protein: 1.5, fett: 0.5, kh: 18.0, bal: 2.4,
    note: &quot;Anthocyane · COX-Hemmer · DOMS↓&quot;,
  },
  {
    name: &quot;TK Erdbeeren&quot;,
    amount: &quot;30 g&quot;,
    source: &quot;BLS&quot;,
    kcal: 10, protein: 0.2, fett: 0.1, kh: 2.3, bal: 0.6,
    note: &quot;Vit. C → Fe-Resorption ↑&quot;,
  },
  {
    name: &quot;Rohe Rote Beete, gerieben&quot;,
    amount: &quot;65 g&quot;,
    source: &quot;BLS&quot;,
    kcal: 28, protein: 1.0, fett: 0.1, kh: 6.5, bal: 1.8,
    note: &quot;Nitrat ~185 mg → NO · roh = Maximum&quot;,
  },
  {
    name: &quot;TK Blattspinat&quot;,
    amount: &quot;45 g&quot;,
    source: &quot;BLS&quot;,
    kcal: 10, protein: 1.3, fett: 0.2, kh: 1.6, bal: 1.0,
    note: &quot;Vit. K ~190 % AI · Folat&quot;,
  },
  {
    name: &quot;Medjool-Dattel, entkernt&quot;,
    amount: &quot;3 Stk. (~54 g)&quot;,
    source: &quot;USDA&quot;,
    kcal: 150, protein: 1.0, fett: 0.1, kh: 40.5, bal: 3.6,
    note: &quot;Bananenersatz · Bindung · GI ~42&quot;,
  },
  {
    name: &quot;Haferflocken, fein&quot;,
    amount: &quot;40 g&quot;,
    source: &quot;BLS&quot;,
    kcal: 149, protein: 5.2, fett: 2.8, kh: 24.0, bal: 4.0,
    note: &quot;β-Glucan · langsame KH · Sättigung&quot;,
  },
  {
    name: &quot;Rohkakao-Pulver, ungesüßt&quot;,
    amount: &quot;15 g&quot;,
    source: &quot;USDA&quot;,
    kcal: 34, protein: 3.0, fett: 2.1, kh: 3.6, bal: 5.0,
    note: &quot;Flavanole · Magnesium · Theobromin&quot;,
  },
  {
    name: &quot;Meersalz&quot;,
    amount: &quot;~0,5 g&quot;,
    source: &quot;—&quot;,
    kcal: 0, protein: 0, fett: 0, kh: 0, bal: 0,
    note: &quot;~195 mg Na · SGLT1-Aktivierung&quot;,
  },
];

const total = ingredients.reduce((acc, i) =&gt; ({
  kcal: acc.kcal + i.kcal,
  protein: acc.protein + i.protein,
  fett: acc.fett + i.fett,
  kh: acc.kh + i.kh,
  bal: acc.bal + i.bal,
}), { kcal: 0, protein: 0, fett: 0, kh: 0, bal: 0 });

const cols = [
  { key: &quot;kcal&quot;, label: &quot;kcal&quot;, color: &quot;#e8e4dc&quot; },
  { key: &quot;protein&quot;, label: &quot;P g&quot;, color: &quot;#7c3aed&quot; },
  { key: &quot;fett&quot;, label: &quot;F g&quot;, color: &quot;#d4860a&quot; },
  { key: &quot;kh&quot;, label: &quot;KH g&quot;, color: &quot;#2a7a4f&quot; },
  { key: &quot;bal&quot;, label: &quot;Bal g&quot;, color: &quot;#1a6b8a&quot; },
];

const fmt = (v) =&gt; v === 0 ? &quot;—&quot; : v % 1 === 0 ? v : v.toFixed(1);

export default function App() {
  return (
    &lt;div style={{
      fontFamily: &quot;&#x27;Georgia&#x27;, serif&quot;,
      background: &quot;#0e1117&quot;,
      minHeight: &quot;100vh&quot;,
      padding: &quot;1.25rem 1rem 3rem&quot;,
      maxWidth: 560,
      margin: &quot;0 auto&quot;,
      color: &quot;#e8e4dc&quot;,
    }}&gt;
      {/* Header */}
      &lt;div style={{ marginBottom: &quot;1.2rem&quot; }}&gt;
        &lt;p style={{ fontSize: 10, letterSpacing: &quot;.15em&quot;, color: &quot;#444&quot;, margin: &quot;0 0 4px&quot;, fontFamily: &quot;monospace&quot; }}&gt;
          TART CHERRY CACAO RECOVERY · MAKROS PRO ZUTAT
        &lt;/p&gt;
        &lt;h1 style={{ fontSize: 20, fontWeight: 700, margin: &quot;0 0 3px&quot;, lineHeight: 1.2 }}&gt;
          Zutatenliste mit Makros
        &lt;/h1&gt;
        &lt;p style={{ fontSize: 12, color: &quot;#555&quot;, margin: 0 }}&gt;
          Quellen: BLS 3.02 · USDA FoodData · Herstellerlabel
        &lt;/p&gt;
      &lt;/div&gt;

      {/* Column headers */}
      &lt;div style={{
        display: &quot;grid&quot;,
        gridTemplateColumns: &quot;1fr repeat(5, 52px)&quot;,
        gap: 4,
        padding: &quot;6px 10px&quot;,
        borderBottom: &quot;1px solid #2a2e3a&quot;,
        marginBottom: 4,
      }}&gt;
        &lt;div style={{ fontSize: 10, color: &quot;#444&quot;, fontFamily: &quot;monospace&quot; }}&gt;ZUTAT&lt;/div&gt;
        {cols.map(c =&gt; (
          &lt;div key={c.key} style={{
            fontSize: 10, color: c.color, fontFamily: &quot;monospace&quot;,
            textAlign: &quot;right&quot;, fontWeight: 700,
          }}&gt;{c.label}&lt;/div&gt;
        ))}
      &lt;/div&gt;

      {/* Ingredients */}
      {ingredients.map((ing, i) =&gt; (
        &lt;div key={i} style={{
          display: &quot;grid&quot;,
          gridTemplateColumns: &quot;1fr repeat(5, 52px)&quot;,
          gap: 4,
          padding: &quot;8px 10px&quot;,
          borderBottom: &quot;1px solid #15181f&quot;,
          background: ing.fixed ? &quot;#1a1530&quot; : i % 2 === 0 ? &quot;#12151e&quot; : &quot;#0e1117&quot;,
          borderRadius: 6,
          marginBottom: 2,
        }}&gt;
          &lt;div&gt;
            &lt;div style={{ display: &quot;flex&quot;, alignItems: &quot;center&quot;, gap: 5 }}&gt;
              {ing.fixed &amp;&amp; (
                &lt;span style={{
                  fontSize: 8, fontFamily: &quot;monospace&quot;, color: &quot;#7c3aed&quot;,
                  background: &quot;#7c3aed22&quot;, padding: &quot;1px 4px&quot;, borderRadius: 4, fontWeight: 700,
                }}&gt;FIX&lt;/span&gt;
              )}
              &lt;span style={{ fontSize: 13, color: ing.fixed ? &quot;#9d72ff&quot; : &quot;#ddd&quot;, fontWeight: ing.fixed ? 600 : 400 }}&gt;
                {ing.name}
              &lt;/span&gt;
            &lt;/div&gt;
            &lt;div style={{ fontSize: 10, color: &quot;#444&quot;, marginTop: 1 }}&gt;{ing.amount}&lt;/div&gt;
            &lt;div style={{ fontSize: 10, color: &quot;#333&quot;, marginTop: 1, fontStyle: &quot;italic&quot; }}&gt;{ing.note}&lt;/div&gt;
          &lt;/div&gt;
          {cols.map(c =&gt; (
            &lt;div key={c.key} style={{
              fontSize: 13, fontWeight: 500,
              color: ing[c.key] === 0 ? &quot;#2a2e3a&quot; : c.color,
              textAlign: &quot;right&quot;,
              alignSelf: &quot;center&quot;,
            }}&gt;
              {fmt(ing[c.key])}
            &lt;/div&gt;
          ))}
        &lt;/div&gt;
      ))}

      {/* Total */}
      &lt;div style={{
        display: &quot;grid&quot;,
        gridTemplateColumns: &quot;1fr repeat(5, 52px)&quot;,
        gap: 4,
        padding: &quot;10px 10px&quot;,
        background: &quot;#1e2230&quot;,
        borderRadius: 8,
        marginTop: 8,
        border: &quot;1px solid #2a2e3a&quot;,
      }}&gt;
        &lt;div&gt;
          &lt;div style={{ fontSize: 13, fontWeight: 700, color: &quot;#e8e4dc&quot; }}&gt;GESAMT&lt;/div&gt;
          &lt;div style={{ fontSize: 10, color: &quot;#555&quot;, fontFamily: &quot;monospace&quot; }}&gt;Smoothie komplett&lt;/div&gt;
        &lt;/div&gt;
        {cols.map(c =&gt; (
          &lt;div key={c.key} style={{
            fontSize: 14, fontWeight: 700, color: c.color,
            textAlign: &quot;right&quot;, alignSelf: &quot;center&quot;,
          }}&gt;
            {fmt(Math.round(total[c.key] * 10) / 10)}
          &lt;/div&gt;
        ))}
      &lt;/div&gt;

      {/* Macro distribution */}
      &lt;div style={{
        display: &quot;grid&quot;, gridTemplateColumns: &quot;repeat(3,1fr)&quot;, gap: 6, marginTop: 10,
      }}&gt;
        {[
          { label: &quot;% Protein&quot;, val: Math.round((total.protein * 4 / total.kcal) * 100), color: &quot;#7c3aed&quot; },
          { label: &quot;% Fett&quot;, val: Math.round((total.fett * 9 / total.kcal) * 100), color: &quot;#d4860a&quot; },
          { label: &quot;% KH&quot;, val: Math.round((total.kh * 4 / total.kcal) * 100), color: &quot;#2a7a4f&quot; },
        ].map((m, i) =&gt; (
          &lt;div key={i} style={{
            background: m.color + &quot;15&quot;, borderRadius: 8, padding: &quot;8px&quot;,
            border: `1px solid ${m.color}30`, textAlign: &quot;center&quot;,
          }}&gt;
            &lt;div style={{ fontSize: 22, fontWeight: 700, color: m.color }}&gt;{m.val} %&lt;/div&gt;
            &lt;div style={{ fontSize: 10, color: &quot;#555&quot;, fontFamily: &quot;monospace&quot; }}&gt;{m.label}&lt;/div&gt;
          &lt;/div&gt;
        ))}
      &lt;/div&gt;

      {/* Source note */}
      &lt;div style={{
        marginTop: 10, padding: &quot;7px 10px&quot;,
        background: &quot;#12151e&quot;, borderRadius: 8,
        fontSize: 11, color: &quot;#333&quot;, lineHeight: 1.5,
      }}&gt;
        Kreatin kalorienneutral · Meersalz kalorienneutral · Rohe Rote Beete: BLS-Wert für rohe Rote Rübe. Messunsicherheit ±5 % je nach Charge und Reifegrad.
      &lt;/div&gt;
    &lt;/div&gt;
  );
}
</code></pre></details>
