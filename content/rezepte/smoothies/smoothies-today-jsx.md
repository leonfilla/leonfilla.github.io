---
titel: smoothies_today.jsx
status: aktiv
datum: '2026-04-24'
quelle:
  typ: claude
  url: https://claude.ai/chat/e243ac2d-4628-41b9-ae87-39b4cf14f878
  hinweis: Protein-Smoothies für Frühstück und Muskelaufbau
importiert: true
---

<details><summary>Ursprüngliche Datei</summary><pre><code>import { useState } from &quot;react&quot;;

const today = [
  { icon: &quot;🥔&quot;, item: &quot;Kartoffelbrötchen&quot;, covers: null },
  { icon: &quot;🧀&quot;, item: &quot;Halloumi-Käse&quot;, covers: &quot;Calcium, Protein, Fett&quot; },
  { icon: &quot;🫒&quot;, item: &quot;Bio Olivenöl nativ extra&quot;, covers: &quot;MUFA, Polyphenole&quot; },
  { icon: &quot;🍅&quot;, item: &quot;Kirschtomaten&quot;, covers: &quot;Lycopin, Vit. C&quot; },
  { icon: &quot;🫘&quot;, item: &quot;Hummus&quot;, covers: &quot;Eisen, Folat (teilw.)&quot; },
  { icon: &quot;🫑&quot;, item: &quot;Rote Paprika roh&quot;, covers: &quot;Vit. C ~200%&quot; },
  { icon: &quot;☕&quot;, item: &quot;Schwarzer Kaffee&quot;, covers: null },
  { icon: &quot;🍵&quot;, item: &quot;Chia-Hanf-Pudding&quot;, covers: &quot;Omega-3, Ballaststoffe&quot; },
];

const gaps = [
  { label: &quot;Protein ~55–60 g fehlen noch&quot;, color: &quot;#e05555&quot; },
  { label: &quot;Vitamin K (kein Blattgemüse)&quot;, color: &quot;#e05555&quot; },
  { label: &quot;Folat (nur Hummus-Anteil)&quot;, color: &quot;#e05555&quot; },
  { label: &quot;Kalium (kein Obst bisher)&quot;, color: &quot;#e05555&quot; },
  { label: &quot;Ballaststoffe (wenig)&quot;, color: &quot;#e05555&quot; },
  { label: &quot;Kreatin (0 g bisher)&quot;, color: &quot;#e05555&quot; },
];

const smoothies = [
  {
    id: 1,
    name: &quot;Mango Spinach Flax&quot;,
    badge: &quot;Vit. K + Folat&quot;,
    badgeColor: &quot;#2a9d6e&quot;,
    desc: &quot;Schließt die zwei größten Lücken: Vitamin K (Spinat) und Folat. Leichtestes Fettprofil als Gegenpart zu Halloumi + Olivenöl.&quot;,
    macros: { kcal: 668, protein: 47, fett: 22, kh: 68, ballaststoffe: 13 },
    dayTotal: { kcal: &quot;~1400&quot;, protein: &quot;~90 g&quot;, highlight: &quot;Vit. K &gt;250%&quot; },
    ingredients: [
      { name: &quot;TK Banane&quot;, amount: &quot;90 g&quot;, tag: null },
      { name: &quot;TK Mango&quot;, amount: &quot;130 g&quot;, tag: &quot;Kalium + Vit. C&quot; },
      { name: &quot;TK Blattspinat&quot;, amount: &quot;65 g&quot;, tag: &quot;Vit. K + Folat&quot; },
      { name: &quot;Haferflocken, fein&quot;, amount: &quot;30 g&quot;, tag: null },
      { name: &quot;Leinsamen, gemahlen&quot;, amount: &quot;12 g&quot;, tag: &quot;ALA&quot; },
    ],
    color: &quot;#2a9d6e&quot;,
    note: &quot;Farbe: sattgrün · niedrigstes Fett der Serie · kein Nussanteil&quot;,
  },
  {
    id: 2,
    name: &quot;Beet Blueberry Banana&quot;,
    badge: &quot;Antioxidantien&quot;,
    badgeColor: &quot;#c0392b&quot;,
    desc: &quot;Rote Beete NO-Booster, Blaubeeren Anthocyane, kein Nussanteil. Maximale Polyphenoldichte als Tagesabschluss.&quot;,
    macros: { kcal: 672, protein: 46, fett: 19, kh: 79, ballaststoffe: 12 },
    dayTotal: { kcal: &quot;~1400&quot;, protein: &quot;~89 g&quot;, highlight: &quot;Nitrat ↑↑&quot; },
    ingredients: [
      { name: &quot;TK Rote Beete, gegart&quot;, amount: &quot;100 g&quot;, tag: &quot;Nitrat → NO&quot; },
      { name: &quot;TK Blaubeeren&quot;, amount: &quot;130 g&quot;, tag: &quot;Anthocyane&quot; },
      { name: &quot;TK Banane&quot;, amount: &quot;90 g&quot;, tag: null },
      { name: &quot;Chiasamen&quot;, amount: &quot;15 g&quot;, tag: null },
      { name: &quot;Haferflocken, fein&quot;, amount: &quot;25 g&quot;, tag: null },
      { name: &quot;Zitronensaft, frisch&quot;, amount: &quot;½ Zitrone&quot;, tag: null },
    ],
    color: &quot;#8e24aa&quot;,
    note: &quot;Farbe: tief violett · niedrigstes Fett der Serie · Zitrone gleicht Erdigkeit aus&quot;,
  },
  {
    id: 3,
    name: &quot;Banana Pea Raspberry Flax&quot;,
    badge: &quot;Folat + Eisen&quot;,
    badgeColor: &quot;#d4860a&quot;,
    desc: &quot;TK Erbsen: höchste Folatquelle unter Gemüse. Himbeere Vit. C steigert Eisenresorption. Höchstes Protein + Ballaststoffe.&quot;,
    macros: { kcal: 683, protein: 51, fett: 22, kh: 72, ballaststoffe: 16 },
    dayTotal: { kcal: &quot;~1410&quot;, protein: &quot;~94 g&quot;, highlight: &quot;Folat ~85 %&quot; },
    ingredients: [
      { name: &quot;TK Banane&quot;, amount: &quot;90 g&quot;, tag: null },
      { name: &quot;TK Erbsen, aufgetaut&quot;, amount: &quot;90 g&quot;, tag: &quot;Folat&quot; },
      { name: &quot;TK Himbeeren&quot;, amount: &quot;120 g&quot;, tag: &quot;Vit. C → Fe↑&quot; },
      { name: &quot;Haferflocken, fein&quot;, amount: &quot;30 g&quot;, tag: null },
      { name: &quot;Leinsamen, gemahlen&quot;, amount: &quot;12 g&quot;, tag: &quot;ALA&quot; },
      { name: &quot;Chiasamen&quot;, amount: &quot;10 g&quot;, tag: null },
    ],
    color: &quot;#c0392b&quot;,
    note: &quot;Farbe: dunkelviolett · höchste Ballaststoffe + Protein · Erbsen hinter Himbeere unsichtbar&quot;,
  },
  {
    id: 4,
    name: &quot;Carrot Peach Ginger Hemp&quot;,
    badge: &quot;Beta-Carotin&quot;,
    badgeColor: &quot;#d4860a&quot;,
    desc: &quot;Karotte + Pfirsich decken Vitamin-A-Tagesbedarf vollständig. Ingwer + Kurkuma antiinflammatorisch. Kein Nussanteil.&quot;,
    macros: { kcal: 677, protein: 49, fett: 25, kh: 65, ballaststoffe: 11 },
    dayTotal: { kcal: &quot;~1405&quot;, protein: &quot;~92 g&quot;, highlight: &quot;Vit. A &gt;100 %&quot; },
    ingredients: [
      { name: &quot;TK Banane&quot;, amount: &quot;80 g&quot;, tag: null },
      { name: &quot;TK Karotte, gegart&quot;, amount: &quot;110 g&quot;, tag: &quot;Beta-Carotin&quot; },
      { name: &quot;TK Pfirsich&quot;, amount: &quot;120 g&quot;, tag: null },
      { name: &quot;Hanfsamen, geschält&quot;, amount: &quot;20 g&quot;, tag: null },
      { name: &quot;Haferflocken, fein&quot;, amount: &quot;28 g&quot;, tag: null },
      { name: &quot;Ingwer + Kurkuma + Pfeffer&quot;, amount: &quot;1,5 TL / ½ TL / 1 Msp.&quot;, tag: &quot;Curcumin&quot; },
    ],
    color: &quot;#e67e22&quot;,
    note: &quot;Farbe: leuchtendes Orange · kein Gemüsegeschmack · gut am Nachmittag&quot;,
  },
  {
    id: 5,
    name: &quot;Triple Green Mango&quot;,
    badge: &quot;Maximale Mikros&quot;,
    badgeColor: &quot;#1a6b8a&quot;,
    desc: &quot;Drei Gemüse kombiniert. Schließt alle Lücken in einem Rezept. Mikronährstoffdichtester Smoothie der gesamten Sammlung.&quot;,
    macros: { kcal: 670, protein: 50, fett: 22, kh: 69, ballaststoffe: 14 },
    dayTotal: { kcal: &quot;~1398&quot;, protein: &quot;~93 g&quot;, highlight: &quot;Vit. K &gt;300 %&quot; },
    ingredients: [
      { name: &quot;TK Banane&quot;, amount: &quot;80 g&quot;, tag: null },
      { name: &quot;TK Mango&quot;, amount: &quot;150 g&quot;, tag: &quot;Gemüse überdeckt&quot; },
      { name: &quot;TK Blattspinat&quot;, amount: &quot;55 g&quot;, tag: &quot;Vit. K&quot; },
      { name: &quot;TK Brokkoli&quot;, amount: &quot;60 g&quot;, tag: &quot;Sulforaphan&quot; },
      { name: &quot;TK Erbsen&quot;, amount: &quot;60 g&quot;, tag: &quot;Folat&quot; },
      { name: &quot;Hanfsamen, geschält&quot;, amount: &quot;18 g&quot;, tag: null },
      { name: &quot;Leinsamen, gemahlen&quot;, amount: &quot;10 g&quot;, tag: null },
      { name: &quot;Limettensaft, frisch&quot;, amount: &quot;½ Limette&quot;, tag: null },
    ],
    color: &quot;#1a6b8a&quot;,
    note: &quot;Farbe: tiefgrün · Mango-Menge unverzichtbar — überdeckt alle drei Gemüse vollständig&quot;,
  },
];

export default function App() {
  const [open, setOpen] = useState(null);

  return (
    &lt;div style={{
      fontFamily: &quot;&#x27;Georgia&#x27;, serif&quot;,
      background: &quot;#f7f5f0&quot;,
      minHeight: &quot;100vh&quot;,
      padding: &quot;1.25rem 1rem 3rem&quot;,
      maxWidth: 520,
      margin: &quot;0 auto&quot;,
    }}&gt;
      {/* Header */}
      &lt;div style={{ marginBottom: &quot;1.5rem&quot; }}&gt;
        &lt;p style={{ fontSize: 11, letterSpacing: &quot;.1em&quot;, color: &quot;#999&quot;, margin: &quot;0 0 4px&quot;, fontFamily: &quot;monospace&quot; }}&gt;
          HEUTE · 28.04.2026 · RUHETAG
        &lt;/p&gt;
        &lt;h1 style={{ fontSize: 22, fontWeight: 700, margin: &quot;0 0 6px&quot;, color: &quot;#1a1a1a&quot;, lineHeight: 1.2 }}&gt;
          5 passende Smoothies
        &lt;/h1&gt;
        &lt;p style={{ fontSize: 13, color: &quot;#666&quot;, margin: 0 }}&gt;
          Basis: 250 ml Vollmilch 3,8 % · 35 g Proteinpulver · 5 g Kreatin
        &lt;/p&gt;
      &lt;/div&gt;

      {/* Today&#x27;s food */}
      &lt;div style={{ background: &quot;#fff&quot;, borderRadius: 12, padding: &quot;12px 14px&quot;, marginBottom: 16, border: &quot;1px solid #e8e4dc&quot; }}&gt;
        &lt;p style={{ fontSize: 11, fontWeight: 600, color: &quot;#999&quot;, letterSpacing: &quot;.08em&quot;, margin: &quot;0 0 8px&quot;, fontFamily: &quot;monospace&quot; }}&gt;BEREITS GEGESSEN&lt;/p&gt;
        &lt;div style={{ display: &quot;grid&quot;, gridTemplateColumns: &quot;1fr 1fr&quot;, gap: &quot;3px 12px&quot; }}&gt;
          {today.map((t, i) =&gt; (
            &lt;div key={i} style={{ display: &quot;flex&quot;, alignItems: &quot;center&quot;, gap: 6, fontSize: 12, padding: &quot;2px 0&quot; }}&gt;
              &lt;span&gt;{t.icon}&lt;/span&gt;
              &lt;span style={{ color: t.covers ? &quot;#1a1a1a&quot; : &quot;#aaa&quot; }}&gt;{t.item}&lt;/span&gt;
            &lt;/div&gt;
          ))}
        &lt;/div&gt;
        &lt;div style={{ marginTop: 10, paddingTop: 8, borderTop: &quot;1px dashed #e8e4dc&quot; }}&gt;
          &lt;p style={{ fontSize: 11, fontWeight: 600, color: &quot;#e05555&quot;, letterSpacing: &quot;.08em&quot;, margin: &quot;0 0 5px&quot;, fontFamily: &quot;monospace&quot; }}&gt;SMOOTHIE FÜLLT&lt;/p&gt;
          &lt;div style={{ display: &quot;grid&quot;, gridTemplateColumns: &quot;1fr 1fr&quot;, gap: &quot;2px 10px&quot; }}&gt;
            {gaps.map((g, i) =&gt; (
              &lt;div key={i} style={{ fontSize: 11, color: &quot;#888&quot;, display: &quot;flex&quot;, gap: 5, alignItems: &quot;center&quot; }}&gt;
                &lt;span style={{ width: 5, height: 5, borderRadius: &quot;50%&quot;, background: &quot;#e05555&quot;, flexShrink: 0 }}&gt;&lt;/span&gt;
                {g.label}
              &lt;/div&gt;
            ))}
          &lt;/div&gt;
        &lt;/div&gt;
      &lt;/div&gt;

      {/* Smoothies */}
      {smoothies.map((s) =&gt; (
        &lt;div
          key={s.id}
          style={{
            background: &quot;#fff&quot;,
            borderRadius: 12,
            marginBottom: 10,
            border: &quot;1px solid #e8e4dc&quot;,
            overflow: &quot;hidden&quot;,
            transition: &quot;box-shadow .2s&quot;,
          }}
        &gt;
          {/* Card header - always visible */}
          &lt;button
            onClick={() =&gt; setOpen(open === s.id ? null : s.id)}
            style={{
              width: &quot;100%&quot;,
              background: &quot;none&quot;,
              border: &quot;none&quot;,
              padding: &quot;12px 14px&quot;,
              textAlign: &quot;left&quot;,
              cursor: &quot;pointer&quot;,
              display: &quot;block&quot;,
            }}
          &gt;
            &lt;div style={{ display: &quot;flex&quot;, alignItems: &quot;flex-start&quot;, justifyContent: &quot;space-between&quot;, gap: 8 }}&gt;
              &lt;div style={{ flex: 1 }}&gt;
                &lt;div style={{ display: &quot;flex&quot;, alignItems: &quot;center&quot;, gap: 7, marginBottom: 4, flexWrap: &quot;wrap&quot; }}&gt;
                  &lt;span style={{
                    fontSize: 10, fontWeight: 600, padding: &quot;2px 8px&quot;,
                    borderRadius: 20, background: s.color + &quot;18&quot;, color: s.color,
                    letterSpacing: &quot;.04em&quot;, fontFamily: &quot;monospace&quot;,
                  }}&gt;
                    {s.badge}
                  &lt;/span&gt;
                  &lt;span style={{ fontSize: 15, fontWeight: 700, color: &quot;#1a1a1a&quot; }}&gt;{s.name}&lt;/span&gt;
                &lt;/div&gt;
                &lt;p style={{ fontSize: 12, color: &quot;#777&quot;, margin: 0, lineHeight: 1.4 }}&gt;{s.desc}&lt;/p&gt;
              &lt;/div&gt;
              &lt;span style={{ fontSize: 16, color: &quot;#bbb&quot;, flexShrink: 0, marginTop: 2 }}&gt;
                {open === s.id ? &quot;↑&quot; : &quot;↓&quot;}
              &lt;/span&gt;
            &lt;/div&gt;

            {/* Macros always visible */}
            &lt;div style={{ display: &quot;grid&quot;, gridTemplateColumns: &quot;repeat(5,1fr)&quot;, gap: 5, marginTop: 10 }}&gt;
              {[
                { label: &quot;kcal&quot;, val: s.macros.kcal },
                { label: &quot;Protein&quot;, val: s.macros.protein + &quot; g&quot; },
                { label: &quot;Fett&quot;, val: s.macros.fett + &quot; g&quot; },
                { label: &quot;KH&quot;, val: s.macros.kh + &quot; g&quot; },
                { label: &quot;Ballaststoffe&quot;, val: s.macros.ballaststoffe + &quot; g&quot; },
              ].map((m, i) =&gt; (
                &lt;div key={i} style={{ background: &quot;#f7f5f0&quot;, borderRadius: 8, padding: &quot;6px 4px&quot;, textAlign: &quot;center&quot; }}&gt;
                  &lt;div style={{ fontSize: 9, color: &quot;#999&quot;, marginBottom: 2 }}&gt;{m.label}&lt;/div&gt;
                  &lt;div style={{ fontSize: 13, fontWeight: 600, color: &quot;#1a1a1a&quot; }}&gt;{m.val}&lt;/div&gt;
                &lt;/div&gt;
              ))}
            &lt;/div&gt;

            {/* Day total pill */}
            &lt;div style={{
              display: &quot;inline-flex&quot;, alignItems: &quot;center&quot;, gap: 8,
              background: &quot;#f0faf5&quot;, borderRadius: 8, padding: &quot;4px 10px&quot;, marginTop: 7,
              fontSize: 11, color: &quot;#2a9d6e&quot;,
            }}&gt;
              &lt;span&gt;Tag gesamt: {s.dayTotal.kcal} kcal · {s.dayTotal.protein}&lt;/span&gt;
              &lt;span style={{ background: &quot;#2a9d6e&quot;, color: &quot;#fff&quot;, borderRadius: 6, padding: &quot;1px 6px&quot;, fontWeight: 600 }}&gt;
                {s.dayTotal.highlight}
              &lt;/span&gt;
            &lt;/div&gt;
          &lt;/button&gt;

          {/* Expandable ingredients */}
          {open === s.id &amp;&amp; (
            &lt;div style={{ borderTop: &quot;1px solid #f0ece4&quot;, padding: &quot;10px 14px 12px&quot; }}&gt;
              &lt;p style={{ fontSize: 10, fontWeight: 600, color: &quot;#bbb&quot;, letterSpacing: &quot;.1em&quot;, margin: &quot;0 0 6px&quot;, fontFamily: &quot;monospace&quot; }}&gt;
                ZUTATEN
              &lt;/p&gt;
              {s.ingredients.map((ing, i) =&gt; (
                &lt;div key={i} style={{
                  display: &quot;flex&quot;, justifyContent: &quot;space-between&quot;, alignItems: &quot;center&quot;,
                  fontSize: 13, padding: &quot;4px 0&quot;,
                  borderBottom: i &lt; s.ingredients.length - 1 ? &quot;1px solid #f0ece4&quot; : &quot;none&quot;,
                }}&gt;
                  &lt;div style={{ display: &quot;flex&quot;, alignItems: &quot;center&quot;, gap: 6 }}&gt;
                    &lt;span style={{ color: &quot;#333&quot; }}&gt;{ing.name}&lt;/span&gt;
                    {ing.tag &amp;&amp; (
                      &lt;span style={{
                        fontSize: 10, padding: &quot;1px 6px&quot;, borderRadius: 6,
                        background: s.color + &quot;15&quot;, color: s.color, fontWeight: 600,
                      }}&gt;
                        {ing.tag}
                      &lt;/span&gt;
                    )}
                  &lt;/div&gt;
                  &lt;span style={{ fontWeight: 600, color: &quot;#555&quot;, fontSize: 12, whiteSpace: &quot;nowrap&quot;, marginLeft: 8 }}&gt;
                    {ing.amount}
                  &lt;/span&gt;
                &lt;/div&gt;
              ))}
              &lt;p style={{
                fontSize: 11, color: &quot;#aaa&quot;, fontStyle: &quot;italic&quot;,
                margin: &quot;10px 0 0&quot;, paddingTop: 8, borderTop: &quot;1px dashed #e8e4dc&quot;,
                lineHeight: 1.5,
              }}&gt;
                {s.note}
              &lt;/p&gt;
            &lt;/div&gt;
          )}
        &lt;/div&gt;
      ))}

      &lt;p style={{ fontSize: 11, color: &quot;#bbb&quot;, textAlign: &quot;center&quot;, marginTop: 8, fontFamily: &quot;monospace&quot; }}&gt;
        Tippe auf einen Smoothie für die Zutaten
      &lt;/p&gt;
    &lt;/div&gt;
  );
}
</code></pre></details>
