# HL360 MVP Website — FlexQ

## Što je ovaj projekt

MVP marketing website za **FlexQ** (FlexQ Health) — hibridnu platformu za mentalno zdravlje. Jedina svrha stranice je: pitchat tri publike i generirati demo leadove.

Tagline: *"Intervention before escalation."*

Produkt u jednoj rečenici: kontinuirani signal-layer između terapijskih sesija — 60-sekundni dnevni check-in za pacijenta, dashboard za terapeuta, anonimiziran aggregate za HR.

---

## Tech stack

| Što | Kako |
|-----|------|
| Build alat | Webpack 5 (webpack-merge, odvojeni dev/prod configovi) |
| JS | Vanilla — nula frameworka, nula dependencija u runtimeu |
| CSS | Jedan fajl (`css/style.css`), BEM-style klase |
| Fontovi | Newsreader (serif, headinzi/italic) + DM Sans (body) — Google Fonts |
| Dev server | `npm start` → webpack-dev-server |
| Produkcija | `npm run build` → `dist/` |

**Trenutno stanje `index.html`**: još uvijek HTML5 Boilerplate placeholder. Sav stvarni sadržaj živi u `FlexQ-Website-v3_8.html` (667 KB, dizajn referenca / mockup).

---

## Struktura stranice

Stranica je SPA — jedan HTML, tri "page" diva, JS `showPage(name)` funkcija prebacuje koji je aktivan.

### Navigacija
```
Logo (FlexQ)   |   Home   For therapists   For enterprises   [Talk to us]
```

### Tri stranice (page divovi)

#### `#page-landing` (Home)
- **Hero** — "Intervention before escalation." + signal card demo (SVG chart, animirani pulse)
- **Why / The Problem** — "Therapy is episodic. Mental strain isn't." + 3 statistike (2–4 tjedna između sesija, 30–40% session time na rekonstrukciju, tiha deterioracija)
- **What / The Solution** — "One product, three honest promises." — 3 promise kartice: za pacijente, terapeute, enterprise
- **How / The Approach** — 4 koraka: Capture → Compare → Surface → Act
- **CTA band** + footer

#### `#page-therapists` (For therapists)
- **Hero** — "Walk into every session already oriented."
- **Three jobs** — 01 Triage (sort by change), 02 Brief (90-sec pre-session view), 03 Adapt (ACE plan drafts, ti sign off)
- **Trust band** — "Inspectable. Conservative. Yours." — 4 garancije
- **CTA band** + footer

#### `#page-enterprise` (For enterprises)
- **Hero** — "A leading indicator of workforce mental strain — not a wellness app."
- **Privacy by design** — "What HR sees. What HR never sees." — aggregate ≥50, nikada individualni podaci
- **Value drivers** — 3 karte: talent retention, sick-leave reduction, presenteeism stabilisation
- **Rollout timeline** — pilot u 6 tjedana, aggregate insight za 90 dana
- **CTA band** + footer

---

## Design system

### Boje (CSS varijable)
```css
--c:        #fbf9f4  /* cream pozadina */
--dark:     #2e2c28  /* gotovo crna — tekst, nav, dark sekcije */
--mid:      #6b6860  /* body tekst, opisi */
--light:    #a09d98  /* metadata, eyebrow sekundarni */
--border:   #e8e4db  /* borderovi, grid razmaci */
--accent:   #a85522  /* rust/terakota — CTAi, em tagovi */
--accent-l: #f0e0d0  /* blagi accent za pozadine */
--amber:    #cc7722  /* risk indikatori */
--green:    #2d6a4f
--red:      #b03020
```

### Tipografija
- **Newsreader** — serif, light (300), italic — koristi se za sve h1/h2/h3 i tagline tekst
- **DM Sans** — sans-serif, 300/400/500 — body, navigacija, buttoni

### Grid logika
- `.g2`, `.g3`, `.g4` — CSS grid s `gap:2px` i `background:var(--border)` → daje efekt "cell borderade"
- `.cell` — bijela ili cream pozadina, `padding:32px`
- Sekcije koriste `.pad` (88px gornji/donji) ili inline padding

### Komponente
- `.btn-dark`, `.btn-ghost`, `.btn-accent` — tri varijante buttona
- `.eyebrow` — mali uppercase label iznad headinga
- `.serif` — utility klasa za Newsreader font
- `.sig-card` — signal card demo (hero sekcija, SVG trend chart + risk pill)
- `.cta-band` — dark pozadina CTA sekcija

---

## Ključni product pojmovi (za copywriting)

| Pojam | Značenje |
|-------|----------|
| **Signal card** | UI prikaz pacijentovog trenda vs. osobnog baselinea |
| **ACE** (Adaptive Care Engine) | AI koji drafta promjene plana njege — terapeut prihvaća/odbija/mijenja |
| **Baseline** | Rolling 7-day prosjek pacijentovih self-reportova — usporedba sa sobom, ne populacijom |
| **Persistence flag** | ≥5 dana iznad uobičajenog raspona → flag |
| **Sustained deviation** | ≥14 dana devijacije → jači flag |
| **n ≥ 50** | Minimalna veličina grupe za bilo koji enterprise aggregate prikaz |

### Tone of voice
- Izbjegava: "wellness app", "mood tracker", "diagnostic tool"
- Naglašava: "clinical signal layer", "leading indicator", "inspectable", "no black boxes"
- Terapeut ostaje decision-maker — ACE nikada autonomno ne kontaktira pacijenta

---

## Compliance claims
- GDPR i HIPAA compliant "by design, not by policy"
- Employer nikada ne vidi individualne podatke, refleksije, ni subgrupe <50
- Svaki flag pokazuje svoje pravilo (transparentnost)
- Audit trail za sve akcije terapeuta

---

## Datoteke

```
/
├── index.html                  ← trenutno Boilerplate placeholder (prazan)
├── FlexQ-Website-v3_8.html     ← PRAVA stranica / dizajn referenca (667KB)
├── css/style.css               ← H5BP base + custom stilovi (proširiti ovdje)
├── js/app.js                   ← prazan (vendor JS ide u js/vendor/)
├── webpack.common.js           ← entry: js/app.js → dist/
├── webpack.config.dev.js       ← dev server config
├── webpack.config.prod.js      ← produkcija config
├── package.json
└── img/                        ← .gitkeep, slike idu ovdje
```

---

## Kako pokrenuti

```bash
npm install
npm start        # dev server na localhost
npm run build    # produkcija → dist/
```
