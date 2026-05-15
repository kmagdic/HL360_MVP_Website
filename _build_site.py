#!/usr/bin/env python3
"""
Build script: reads FlexQ-Website-v3_8.html and outputs a proper multi-page site.
Produces: css/site.css  js/site.js  index.html  therapists.html
          enterprise.html  privacy.html  team.html
"""
import os, re

SRC = 'FlexQ-Website-v3_8.html'

with open(SRC, 'r', encoding='utf-8') as f:
    src = f.read()

os.makedirs('css', exist_ok=True)
os.makedirs('js', exist_ok=True)

# ─────────────────────────────────────────────────────────
# STEP 1 — Apply data-i18n attributes to a working copy
# ─────────────────────────────────────────────────────────
html = src

def r(old, new):
    """Replace first occurrence of old with new (warns if not found)."""
    global html
    if old not in html:
        print(f'  WARN: not found: {old[:60]!r}')
        return
    html = html.replace(old, new, 1)

def ra(old, new):
    """Replace ALL occurrences."""
    global html
    if old not in html:
        print(f'  WARN: not found (all): {old[:60]!r}')
        return
    html = html.replace(old, new)

# NAV
r('class="active" onclick="showPage(\'landing\')">Home</a>',
  'href="index.html" data-i18n="nav.home">Home</a>')
r('id="nav-therapists" onclick="showPage(\'therapists\')">For therapists</a>',
  'id="nav-therapists" href="therapists.html" data-i18n="nav.therapists">For therapists</a>')
r('id="nav-enterprise" onclick="showPage(\'enterprise\')">For enterprises</a>',
  'id="nav-enterprise" href="enterprise.html" data-i18n="nav.enterprise">For enterprises</a>')
r('onclick="openContact()" class="nav-cta">Contact us</a>',
  'onclick="openContact()" class="nav-cta" data-i18n="nav.contact">Contact us</a>')
r('<div class="logo" onclick="showPage(\'landing\')">',
  '<div class="logo" onclick="location.href=\'index.html\'" style="cursor:pointer">')

# LANDING — HERO
for old, new in [
    ('<div class="eyebrow">Hybrid Mental Health Platform</div>',
     '<div class="eyebrow" data-i18n="hero.eyebrow">Hybrid Mental Health Platform</div>'),
    ('<h1 class="hero-h1">Intervention<br><em>before</em><br>escalation.</h1>',
     '<h1 class="hero-h1" data-i18n-html="hero.h1">Intervention<br><em>before</em><br>escalation.</h1>'),
    ('<p class="hero-sub">FlexQ is the continuous layer between sessions',
     '<p class="hero-sub" data-i18n="hero.sub">FlexQ is the continuous layer between sessions'),
    ('<span>Therapist remains decision-maker</span>',
     '<span data-i18n="hero.trust">Therapist remains decision-maker</span>'),
]:
    if old in html: r(old, new)

# Hero CTAs
for old, new in [
    ('<button class="btn btn-dark" onclick="openContact()">Request a clinical demo</button>',
     '<button class="btn btn-dark" onclick="openContact()" data-i18n="cta.demo">Request a clinical demo</button>'),
    ('<button class="btn btn-ghost" onclick="showPage(\'therapists\')">See how it works →</button>',
     '<button class="btn btn-ghost" onclick="showPage(\'therapists\')" data-i18n="hero.cta2">See how it works →</button>'),
]:
    if old in html: r(old, new)

# PROBLEM SECTION
for old, new in [
    ('<div class="eyebrow" style="color:var(--accent)">The problem</div>',
     '<div class="eyebrow" style="color:var(--accent)" data-i18n="prob.eyebrow">The problem</div>'),
    ('<h2 class="serif" style="font-size:clamp(36px,4vw,54px);margin-bottom:56px">Therapy is episodic.<br><em>Mental strain isn\'t.</em></h2>',
     '<h2 class="serif" style="font-size:clamp(36px,4vw,54px);margin-bottom:56px" data-i18n-html="prob.h2">Therapy is episodic.<br><em>Mental strain isn\'t.</em></h2>'),
    ('>Weeks between sessions. The visibility window is empty',
     ' data-i18n="prob.stat1.desc">Weeks between sessions. The visibility window is empty'),
    ('>Of session time spent reconstructing what happened in between.',
     ' data-i18n="prob.stat2.desc">Of session time spent reconstructing what happened in between.'),
    ('<div class="why-num">Most</div>',
     '<div class="why-num" data-i18n="prob.stat3.num">Most</div>'),
    ('>Deterioration goes silent until a crisis forces it into view',
     ' data-i18n="prob.stat3.desc">Deterioration goes silent until a crisis forces it into view'),
    ('<p class="why-quote">',
     '<p class="why-quote" data-i18n-html="prob.quote">'),
    ('<p class="why-note">',
     '<p class="why-note" data-i18n="prob.note">'),
]:
    if old in html: r(old, new)

# SOLUTION
for old, new in [
    ('<div class="eyebrow">The solution</div>',
     '<div class="eyebrow" data-i18n="sol.eyebrow">The solution</div>'),
    ('<h2 class="serif" style="font-size:clamp(34px,3.8vw,52px);margin-bottom:14px">One product,<br><em>three honest promises.</em></h2>',
     '<h2 class="serif" style="font-size:clamp(34px,3.8vw,52px);margin-bottom:14px" data-i18n-html="sol.h2">One product,<br><em>three honest promises.</em></h2>'),
    ('>FlexQ shifts mental health care from episodic treatment to continuous presence.',
     ' data-i18n="sol.intro">FlexQ shifts mental health care from episodic treatment to continuous presence.'),
    ('<div class="p-tag">For patients</div>',
     '<div class="p-tag" data-i18n="sol.p1.tag">For patients</div>'),
    ('<h3>Your trend, your baseline, your choice.</h3>',
     '<h3 data-i18n="sol.p1.h3">Your trend, your baseline, your choice.</h3>'),
    ('<div class="p-tag">For therapists</div>',
     '<div class="p-tag" data-i18n="sol.p2.tag">For therapists</div>'),
    ('<h3>Walk into every session already oriented.</h3>',
     '<h3 data-i18n="sol.p2.h3">Walk into every session already oriented.</h3>'),
    ('>See the clinical view →</button>',
     ' data-i18n="sol.p2.cta">See the clinical view →</button>'),
    ('<div class="p-tag">For enterprises</div>',
     '<div class="p-tag" data-i18n="sol.p3.tag">For enterprises</div>'),
    ('<h3>A leading indicator, not a wellness app.</h3>',
     '<h3 data-i18n="sol.p3.h3">A leading indicator, not a wellness app.</h3>'),
    ('>See enterprise reporting →</button>',
     ' data-i18n="sol.p3.cta">See enterprise reporting →</button>'),
]:
    if old in html: r(old, new)

# HOW IT WORKS
for old, new in [
    ('<div class="eyebrow">How it works?</div>',
     '<div class="eyebrow" data-i18n="how.eyebrow">How it works?</div>'),
    ('<h2 class="serif" style="font-size:clamp(34px,3.8vw,52px);margin-bottom:14px">Grounded in recognised<br>therapeutic approaches.</h2>',
     '<h2 class="serif" style="font-size:clamp(34px,3.8vw,52px);margin-bottom:14px" data-i18n-html="how.h2">Grounded in recognised<br>therapeutic approaches.</h2>'),
    ('>Developed in collaboration with clinical experts.',
     ' data-i18n="how.intro">Developed in collaboration with clinical experts.'),
    ('<div class="step-n">01 · Capture</div><h3>Quick daily check-in</h3>',
     '<div class="step-n" data-i18n="how.s1.n">01 · Capture</div><h3 data-i18n="how.s1.h3">Quick daily check-in</h3>'),
    ('<div class="step-n">02 · Compare</div><h3>Baseline-relative</h3>',
     '<div class="step-n" data-i18n="how.s2.n">02 · Compare</div><h3 data-i18n="how.s2.h3">Baseline-relative</h3>'),
    ('<div class="step-n">03 · Surface</div><h3>Make patterns visible</h3>',
     '<div class="step-n" data-i18n="how.s3.n">03 · Surface</div><h3 data-i18n="how.s3.h3">Make patterns visible</h3>'),
    ('<div class="step-n">04 · Act</div><h3>Therapist-led action</h3>',
     '<div class="step-n" data-i18n="how.s4.n">04 · Act</div><h3 data-i18n="how.s4.h3">Therapist-led action</h3>'),
    ('>Acknowledge, adapt, or dismiss. No autonomous AI care. Full audit trail.</p>',
     ' data-i18n="how.s4.p">Acknowledge, adapt, or dismiss. No autonomous AI care. Full audit trail.</p>'),
]:
    if old in html: r(old, new)

# LANDING CTA BAND
r('<h2>Intervention before escalation.</h2>',
  '<h2 data-i18n="landing.cta.h2">Intervention before escalation.</h2>')
r('<p>Request a clinical demo and see what changed before the next session.</p>',
  '<p data-i18n="landing.cta.p">Request a clinical demo and see what changed before the next session.</p>')

# THERAPISTS HERO
for old, new in [
    ('<div class="eyebrow">For therapists</div>',
     '<div class="eyebrow" data-i18n="nav.therapists">For therapists</div>'),
    ('<h1>Walk into every session<br><em>already oriented.</em></h1>',
     '<h1 data-i18n-html="th.h1">Walk into every session<br><em>already oriented.</em></h1>'),
    ('>Stop reconstructing the last two weeks.',
     ' data-i18n="th.sub">Stop reconstructing the last two weeks.'),
]:
    if old in html: r(old, new)

# JOBS
for old, new in [
    ('<h2 class="serif" style="font-size:clamp(32px,3.5vw,48px);font-weight:300;margin-bottom:72px">Four jobs FlexQ does<br><em>for your caseload.</em></h2>',
     '<h2 class="serif" style="font-size:clamp(32px,3.5vw,48px);font-weight:300;margin-bottom:72px" data-i18n-html="jobs.h2">Four jobs FlexQ does<br><em>for your caseload.</em></h2>'),
    ('<div class="eyebrow">01 · Triage</div>',
     '<div class="eyebrow" data-i18n="jobs.j1.ey">01 · Triage</div>'),
    ('>Sort by change, not by score</h3>',
     ' data-i18n="jobs.j1.h3">Sort by change, not by score</h3>'),
    ('>Your caseload sorts by recent deviation',
     ' data-i18n="jobs.j1.p">Your caseload sorts by recent deviation'),
    ('<div class="eyebrow">02 · Brief</div>',
     '<div class="eyebrow" data-i18n="jobs.j2.ey">02 · Brief</div>'),
    ('>A 90-second pre-session view</h3>',
     ' data-i18n="jobs.j2.h3">A 90-second pre-session view</h3>'),
    ('>Trend, baseline band, deviation event, recent reflections.',
     ' data-i18n="jobs.j2.p">Trend, baseline band, deviation event, recent reflections.'),
    ('<div class="eyebrow">03 · Adapt</div>',
     '<div class="eyebrow" data-i18n="jobs.j3.ey">03 · Adapt</div>'),
    ('>Plan changes you review and control</h3>',
     ' data-i18n="jobs.j3.h3">Plan changes you review and control</h3>'),
    ('>When a signal persists, the Adaptive Care Engine',
     ' data-i18n="jobs.j3.p1">When a signal persists, the Adaptive Care Engine'),
    ('>No autonomous AI care.</p>',
     ' data-i18n="jobs.j3.p2">No autonomous AI care.</p>'),
    ('<div class="eyebrow">04 · Risk management</div>',
     '<div class="eyebrow" data-i18n="jobs.j4.ey">04 · Risk management</div>'),
    ('>Know who needs attention before it becomes a crisis.</h3>',
     ' data-i18n="jobs.j4.h3">Know who needs attention before it becomes a crisis.</h3>'),
    ('>FlexQ watches your entire caseload continuously.',
     ' data-i18n="jobs.j4.p1">FlexQ watches your entire caseload continuously.'),
    ('>Three clear decisions: acknowledge and adapt the plan',
     ' data-i18n="jobs.j4.p2">Three clear decisions: acknowledge and adapt the plan'),
]:
    if old in html: r(old, new)

# TRUST BAND
for old, new in [
    ('<h2>Inspectable. Conservative. Yours.</h2>',
     '<h2 data-i18n="trust.h2">Inspectable. Conservative. Yours.</h2>'),
    ('<h4>Every flag shows its rule</h4>',
     '<h4 data-i18n="trust.c1.h4">Every flag shows its rule</h4>'),
    ('>Persistence ≥5d above usual.',
     ' data-i18n="trust.c1.p">Persistence ≥5d above usual.'),
    ('<h4>Baseline is the patient\'s own</h4>',
     '<h4 data-i18n="trust.c2.h4">Baseline is the patient\'s own</h4>'),
    ('>Rolling 7-day window of self-reports.',
     ' data-i18n="trust.c2.p">Rolling 7-day window of self-reports.'),
    ('<h4>You remain the decision-maker</h4>',
     '<h4 data-i18n="trust.c3.h4">You remain the decision-maker</h4>'),
    ('>The system never autonomously contacts a patient',
     ' data-i18n="trust.c3.p">The system never autonomously contacts a patient'),
    ('<h4>Audit trail by default</h4>',
     '<h4 data-i18n="trust.c4.h4">Audit trail by default</h4>'),
    ('>Every acknowledgement, dismissal, and plan change logged',
     ' data-i18n="trust.c4.p">Every acknowledgement, dismissal, and plan change logged'),
]:
    if old in html: r(old, new)

# THERAPISTS CTA
for old, new in [
    ('<h2>Ready to try it?</h2>',
     '<h2 data-i18n="th.cta.h2">Ready to try it?</h2>'),
    ('<p>Walk into your next session already oriented.</p>',
     '<p data-i18n="th.cta.p">Walk into your next session already oriented.</p>'),
]:
    if old in html: r(old, new)

# ENTERPRISE
for old, new in [
    ('<div class="eyebrow">For enterprises</div>',
     '<div class="eyebrow" data-i18n="nav.enterprise">For enterprises</div>'),
    ('<h1>Mental health powers performance.<br><em>A leading indicator of workforce mental strain.</em></h1>',
     '<h1 data-i18n-html="ent.h1">Mental health powers performance.<br><em>A leading indicator of workforce mental strain.</em></h1>'),
    ('>Continuous mental health support that protects productivity',
     ' data-i18n="ent.sub">Continuous mental health support that protects productivity'),
    ('>Talk to our enterprise team</button>',
     ' data-i18n="ent.cta">Talk to our enterprise team</button>'),
    ('<div class="eyebrow">Value drivers</div>',
     '<div class="eyebrow" data-i18n="val.eyebrow">Value drivers</div>'),
    ('<h2 class="serif" style="font-size:clamp(32px,3.5vw,48px);margin-bottom:48px">Where the platform<br><em>earns its keep.</em></h2>',
     '<h2 class="serif" style="font-size:clamp(32px,3.5vw,48px);margin-bottom:48px" data-i18n-html="val.h2">Where the platform<br><em>earns its keep.</em></h2>'),
    ('<h3>High-value talent retention</h3>',
     '<h3 data-i18n="val.v1.h3">High-value talent retention</h3>'),
    ('>The most critical lever<',
     ' data-i18n="val.v1.tag">The most critical lever<'),
    ('>Detect sustained strain elevation',
     ' data-i18n="val.v1.p">Detect sustained strain elevation'),
    ('<h3>Sick-leave reduction</h3>',
     '<h3 data-i18n="val.v2.h3">Sick-leave reduction</h3>'),
    ('>A real, but secondary lever<',
     ' data-i18n="val.v2.tag">A real, but secondary lever<'),
    ('>Even reducing one sick day per employee',
     ' data-i18n="val.v2.p">Even reducing one sick day per employee'),
    ('<h3>Presenteeism stabilisation</h3>',
     '<h3 data-i18n="val.v3.h3">Presenteeism stabilisation</h3>'),
    ('>The largest hidden cost<',
     ' data-i18n="val.v3.tag">The largest hidden cost<'),
    ('>Employees under sustained mental strain remain at work',
     ' data-i18n="val.v3.p">Employees under sustained mental strain remain at work'),
    ('>For HR leaders who are tired of wellness theatre.</p>',
     ' data-i18n="ent.cta2.q">For HR leaders who are tired of wellness theatre.</p>'),
]:
    if old in html: r(old, new)

# FOOTERS
ra('onclick="showPage(\'privacy\')" style="cursor:pointer">Privacy · GDPR / HIPAA</a>',
   'href="privacy.html" data-i18n="footer.privacy">Privacy · GDPR / HIPAA</a>')
ra('onclick="showPage(\'team\')" style="cursor:pointer">The team</a>',
   'href="team.html" data-i18n="footer.team">The team</a>')
ra('onclick="showPage(\'landing\')" style="cursor:pointer">Home</a>',
   'href="index.html" data-i18n="nav.home">Home</a>')

# PRIVACY PAGE
for old, new in [
    ('<div class="eyebrow" style="color:var(--accent)">Legal · Data protection</div>',
     '<div class="eyebrow" style="color:var(--accent)" data-i18n="priv.eyebrow">Legal · Data protection</div>'),
    ('<h1 class="serif" style="font-size:clamp(44px,5.5vw,68px);color:var(--c);margin-bottom:20px">Privacy<br><em>policy.</em></h1>',
     '<h1 class="serif" style="font-size:clamp(44px,5.5vw,68px);color:var(--c);margin-bottom:20px" data-i18n-html="priv.h1">Privacy<br><em>policy.</em></h1>'),
    ('>This marketing site uses analytics tools and collects your email address only if you choose to share it.',
     ' data-i18n="priv.sub">This marketing site uses analytics tools and collects your email address only if you choose to share it.'),
    ('<h2 class="serif" style="font-size:28px;margin-bottom:16px">Who we are</h2>',
     '<h2 class="serif" style="font-size:28px;margin-bottom:16px" data-i18n="priv.s1.h2">Who we are</h2>'),
    ('<h2 class="serif" style="font-size:28px;margin-bottom:16px">What we collect</h2>',
     '<h2 class="serif" style="font-size:28px;margin-bottom:16px" data-i18n="priv.s2.h2">What we collect</h2>'),
    ('>We collect data in two ways only.</p>',
     ' data-i18n="priv.s2.p">We collect data in two ways only.</p>'),
    ('<h2 class="serif" style="font-size:28px;margin-bottom:16px">Legal basis &amp; your choices</h2>',
     '<h2 class="serif" style="font-size:28px;margin-bottom:16px" data-i18n="priv.s3.h2">Legal basis &amp; your choices</h2>'),
    ('>Managing cookies</h3>',
     ' data-i18n="priv.s3.h3">Managing cookies</h3>'),
    ('<h2 class="serif" style="font-size:28px;margin-bottom:16px">How long we keep your data</h2>',
     '<h2 class="serif" style="font-size:28px;margin-bottom:16px" data-i18n="priv.s4.h2">How long we keep your data</h2>'),
    ('<h2 class="serif" style="font-size:28px;margin-bottom:16px">Your rights</h2>',
     '<h2 class="serif" style="font-size:28px;margin-bottom:16px" data-i18n="priv.s5.h2">Your rights</h2>'),
    ('<h2 class="serif" style="font-size:28px;margin-bottom:16px">Contact</h2>',
     '<h2 class="serif" style="font-size:28px;margin-bottom:16px" data-i18n="nav.contact">Contact</h2>'),
    ('>For any question about this policy or a data subject request:</p>',
     ' data-i18n="priv.s6.p">For any question about this policy or a data subject request:</p>'),
    ('<h4 style="font-size:14.5px;font-weight:500;margin-bottom:6px">Access</h4>',
     '<h4 style="font-size:14.5px;font-weight:500;margin-bottom:6px" data-i18n="priv.r.access">Access</h4>'),
    ('<h4 style="font-size:14.5px;font-weight:500;margin-bottom:6px">Rectification</h4>',
     '<h4 style="font-size:14.5px;font-weight:500;margin-bottom:6px" data-i18n="priv.r.rect">Rectification</h4>'),
    ('<h4 style="font-size:14.5px;font-weight:500;margin-bottom:6px">Erasure</h4>',
     '<h4 style="font-size:14.5px;font-weight:500;margin-bottom:6px" data-i18n="priv.r.erase">Erasure</h4>'),
    ('<h4 style="font-size:14.5px;font-weight:500;margin-bottom:6px">Withdraw consent</h4>',
     '<h4 style="font-size:14.5px;font-weight:500;margin-bottom:6px" data-i18n="priv.r.withdraw">Withdraw consent</h4>'),
]:
    if old in html: r(old, new)

# COOKIE BANNER
for old, new in [
    ('<button class="cb-decline" onclick="cookieChoice(false)">Only essential</button>',
     '<button class="cb-decline" onclick="cookieChoice(false)" data-i18n="cookie.decline">Only essential</button>'),
    ('<button class="cb-accept" onclick="cookieChoice(true)">Accept analytics</button>',
     '<button class="cb-accept" onclick="cookieChoice(true)" data-i18n="cookie.accept">Accept analytics</button>'),
]:
    if old in html: r(old, new)

# TEAM
for old, new in [
    ('<div class="eyebrow" style="color:var(--accent)">Who builds FlexQ</div>',
     '<div class="eyebrow" style="color:var(--accent)" data-i18n="team.eyebrow">Who builds FlexQ</div>'),
    ('<h1 class="serif" style="font-size:clamp(44px,5.5vw,68px);color:var(--c);margin-bottom:20px">Built with clinicians,<br><em>not just for them.</em></h1>',
     '<h1 class="serif" style="font-size:clamp(44px,5.5vw,68px);color:var(--c);margin-bottom:20px" data-i18n-html="team.h1">Built with clinicians,<br><em>not just for them.</em></h1>'),
    ('<div class="eyebrow" style="margin-bottom:28px">Our teams</div>',
     '<div class="eyebrow" style="margin-bottom:28px" data-i18n="team.core">Our teams</div>'),
]:
    if old in html: r(old, new)

# Lang toggle hidden — single language (EN only)

print(f'data-i18n attrs in html: {html.count("data-i18n")}')

# ─────────────────────────────────────────────────────────
# STEP 2 — Extract CSS
# ─────────────────────────────────────────────────────────
css = re.search(r'<style>(.*?)</style>', html, re.DOTALL).group(1)

LANG_CSS = """
/* ── Language toggle ── */
.lang-toggle{display:flex;align-items:center;gap:4px;margin-left:12px}
.lang-sep{font-size:12px;color:var(--border);user-select:none}
.lang-btn{background:none;border:none;font-family:inherit;font-size:11.5px;font-weight:500;letter-spacing:.08em;cursor:pointer;color:var(--light);padding:4px 7px;border-radius:4px;transition:color .15s,background .15s;line-height:1}
.lang-btn:hover{color:var(--dark)}
.lang-btn.active{color:var(--dark);background:var(--border)}
"""

# Fix: nav <a href> links need explicit no-underline (original used onclick without href)
css = css.replace(
    ".nav-links a{font-size:14px;color:var(--mid);padding:6px 12px;border-radius:6px;cursor:pointer;border:none;background:none;font-family:'DM Sans',sans-serif;transition:all .18s}",
    ".nav-links a{font-size:14px;color:var(--mid);padding:6px 12px;border-radius:6px;cursor:pointer;border:none;background:none;font-family:'DM Sans',sans-serif;transition:all .18s;text-decoration:none}"
)

if '.lang-toggle' not in css:
    css = css.strip() + '\n' + LANG_CSS

with open('css/site.css', 'w', encoding='utf-8') as f:
    f.write(css.strip() + '\n')
print('✓ css/site.css')

# ─────────────────────────────────────────────────────────
# STEP 3 — Build js/site.js
# ─────────────────────────────────────────────────────────
SITE_JS = r"""
// ── Navigation ──
function showPage(name) {
  var map = {
    landing:'index.html', therapists:'therapists.html',
    enterprise:'enterprise.html', privacy:'privacy.html', team:'team.html'
  };
  location.href = map[name] || 'index.html';
}

function initNav() {
  var file = location.pathname.split('/').pop() || 'index.html';
  var map = {
    'index.html':'landing', '':'landing',
    'therapists.html':'therapists',
    'enterprise.html':'enterprise',
    'privacy.html':'privacy',
    'team.html':'team'
  };
  var page = map[file] || 'landing';
  var el = document.getElementById('nav-' + page);
  if (el) { el.removeAttribute('href'); el.classList.add('active'); }
}

// ── i18n ──
var T = {
  en: {
    'nav.home':'Home','nav.therapists':'For therapists','nav.enterprise':'For enterprises','nav.contact':'Contact us',
    'hero.eyebrow':'Hybrid Mental Health Platform',
    'hero.h1':'Intervention<br><em>before</em><br>escalation.',
    'hero.sub':'FlexQ is the continuous layer between sessions — turning small daily signals into early warning, so therapists can act before a crisis forces the issue.',
    'cta.demo':'Request a clinical demo',
    'hero.cta2':'See how it works →',
    'hero.trust':'Therapist remains decision-maker',
    'prob.eyebrow':'The problem',
    'prob.h2':'Therapy is episodic.<br><em>Mental strain isn\'t.</em>',
    'prob.stat1.desc':'Weeks between sessions. The visibility window is empty — a client can deteriorate in silence for most of it.',
    'prob.stat2.desc':'Of session time spent reconstructing what happened in between. Therapy time spent on administration.',
    'prob.stat3.num':'Most',
    'prob.stat3.desc':'Deterioration goes silent until a crisis forces it into view — when intervention is late and harder.',
    'prob.quote':'"The first 10–15 minutes of every session used to be <strong>reconstruction</strong>. Now it\'s therapy. That alone is worth it."',
    'prob.note':'A client may start sleeping worse, losing energy, or feeling overwhelmed days before the next appointment. FlexQ closes that gap — making the invisible visible before the next session.',
    'sol.eyebrow':'The solution',
    'sol.h2':'One product,<br><em>three honest promises.</em>',
    'sol.intro':'FlexQ shifts mental health care from episodic treatment to continuous presence. Not a mood tracker. Not a diagnostic tool. A clinical signal layer.',
    'sol.p1.tag':'For patients','sol.p1.h3':'Your trend, your baseline, your choice.',
    'sol.p1.p':'60-second daily check-in. Your therapist sees what you choose. Your employer never does. No streaks, no shaming.',
    'sol.p2.tag':'For therapists','sol.p2.h3':'Walk into every session already oriented.',
    'sol.p2.p':'Triage by change, not score. 90-second pre-session brief. Adapt plans with AI assistance you control and sign off on.',
    'sol.p2.cta':'See the clinical view →',
    'sol.p3.tag':'For enterprises','sol.p3.h3':'A leading indicator, not a wellness app.',
    'sol.p3.p':'Aggregated, anonymised workforce signal — useful to HR, defensible to regulators, invisible at the individual level.',
    'sol.p3.cta':'See enterprise reporting →',
    'how.eyebrow':'How it works?',
    'how.h2':'Grounded in recognised<br>therapeutic approaches.',
    'how.intro':'Developed in collaboration with clinical experts. Every flag shows its rule — no black boxes.',
    'how.s1.n':'01 · Capture','how.s1.h3':'Quick daily check-in',
    'how.s1.p':'60 seconds — mood, energy, stress, sleep, optional reflection. Skipping is safe.',
    'how.s2.n':'02 · Compare','how.s2.h3':'Baseline-relative',
    'how.s2.p':'Patient compared to themselves — not a population norm. Personal baseline, persistence detection.',
    'how.s3.n':'03 · Surface','how.s3.h3':'Make patterns visible',
    'how.s4.n':'04 · Act','how.s4.h3':'Therapist-led action',
    'how.s4.p':'Acknowledge, adapt, or dismiss. No autonomous AI care. Full audit trail.',
    'landing.cta.h2':'Intervention before escalation.',
    'landing.cta.p':'Request a clinical demo and see what changed before the next session.',
    'th.h1':'Walk into every session<br><em>already oriented.</em>',
    'th.sub':'Stop reconstructing the last two weeks. FlexQ shows you what changed, why it matters, and the rule that flagged it — in 90 seconds.',
    'jobs.h2':'Four jobs FlexQ does<br><em>for your caseload.</em>',
    'jobs.j1.ey':'01 · Triage','jobs.j1.h3':'Sort by change, not by score',
    'jobs.j1.p':'Your caseload sorts by recent deviation, so the patients who quietly slipped surface first. Stable patients stay stable, out of the way.',
    'jobs.j2.ey':'02 · Brief','jobs.j2.h3':'A 90-second pre-session view',
    'jobs.j2.p':'Trend, baseline band, deviation event, recent reflections. The talking points are suggestions — you decide which ones to use.',
    'jobs.j3.ey':'03 · Adapt','jobs.j3.h3':'Plan changes you review and control',
    'jobs.j3.p1':'When a signal persists, the Adaptive Care Engine (ACE) drafts a simpler plan as a review surface — the place where your clinical control is preserved. You accept, modify, or reject in fewer than three clicks. Audit-logged.',
    'jobs.j3.p2':'No autonomous AI care.',
    'jobs.j4.ey':'04 · Risk management','jobs.j4.h3':'Know who needs attention before it becomes a crisis.',
    'jobs.j4.p1':'FlexQ watches your entire caseload continuously. When a client crosses a risk threshold — sustained deterioration, missed check-ins, an emerging pattern — a named flag appears in your queue with the rule that raised it and the evidence behind it.',
    'jobs.j4.p2':'Three clear decisions: acknowledge and adapt the plan, acknowledge only, or dismiss. Every response is audit-logged. The system watches between sessions. You decide what happens next.',
    'trust.h2':'Inspectable. Conservative. Yours.',
    'trust.c1.h4':'Every flag shows its rule',
    'trust.c1.p':'Persistence ≥5d above usual. Sustained deviation >14d. Engagement drop + risk. No black boxes.',
    'trust.c2.h4':'Baseline is the patient\'s own',
    'trust.c2.p':'Rolling 7-day window of self-reports. Compared to themselves, never to a population norm.',
    'trust.c3.h4':'You remain the decision-maker',
    'trust.c3.p':'The system never autonomously contacts a patient about a clinical concern. ACE drafts; you sign off.',
    'trust.c4.h4':'Audit trail by default',
    'trust.c4.p':'Every acknowledgement, dismissal, and plan change logged with rule, timestamp, and rationale field.',
    'th.cta.h2':'Ready to try it?',
    'th.cta.p':'Walk into your next session already oriented.',
    'th.cta.btn':'Request a demo',
    'ent.h1':'A leading indicator of workforce mental strain —<br><em>not</em> a wellness app.',
    'ent.sub':'Continuous mental health support that protects productivity through proactive care. Aggregate signal, anonymised by design, defensible to regulators.',
    'ent.cta':'Talk to our enterprise team',
    'val.eyebrow':'Value drivers',
    'val.h2':'Where the platform<br><em>earns its keep.</em>',
    'val.v1.h3':'High-value talent retention','val.v1.tag':'The most critical lever',
    'val.v1.p':'Detect sustained strain elevation or early burnout signals early enough for leadership to intervene. Preventing even a handful of high-value exits annually can offset the entire platform investment.',
    'val.v2.h3':'Sick-leave reduction','val.v2.tag':'A real, but secondary lever',
    'val.v2.p':'Even reducing one sick day per employee annually generates meaningful savings at enterprise scale. Sick leave is a visible cost — presenteeism is the larger hidden one.',
    'val.v3.h3':'Presenteeism stabilisation','val.v3.tag':'The largest hidden cost',
    'val.v3.p':'Employees under sustained mental strain remain at work but operate below full cognitive capacity. Small productivity improvements across a large population yield significant returns.',
    'ent.cta2.q':'For HR leaders who are tired of wellness theatre.',
    'footer.privacy':'Privacy · GDPR / HIPAA','footer.science':'The science','footer.team':'The team',
    'priv.eyebrow':'Legal · Data protection',
    'priv.h1':'Privacy<br><em>policy.</em>',
    'priv.sub':'This marketing site uses analytics tools and collects your email address only if you choose to share it. That\'s it.',
    'priv.s1.h2':'Who we are','priv.s2.h2':'What we collect',
    'priv.s2.p':'We collect data in two ways only.',
    'priv.s3.h2':'Legal basis & your choices','priv.s3.h3':'Managing cookies',
    'priv.s4.h2':'How long we keep your data','priv.s5.h2':'Your rights',
    'priv.s6.p':'For any question about this policy or a data subject request:',
    'priv.r.access':'Access','priv.r.access.p':'Request a copy of all personal data we hold about you.',
    'priv.r.rect':'Rectification','priv.r.rect.p':'Ask us to correct inaccurate data we hold about you.',
    'priv.r.erase':'Erasure','priv.r.erase.p':'Ask us to delete your email address and any associated data at any time.',
    'priv.r.withdraw':'Withdraw consent','priv.r.withdraw.p':'Withdraw consent for analytics or newsletter at any time, with immediate effect.',
    'cookie.decline':'Only essential','cookie.accept':'Accept analytics',
    'team.eyebrow':'Who builds FlexQ',
    'team.h1':'Built with clinicians,<br><em>not just for them.</em>',
    'team.core':'Core team'
  },
  hr: {
    'nav.home':'Početna','nav.therapists':'Za terapeute','nav.enterprise':'Za tvrtke','nav.contact':'Kontakt',
    'hero.eyebrow':'Hibridna platforma za mentalno zdravlje',
    'hero.h1':'Intervencija<br><em>prije</em><br>eskalacije.',
    'hero.sub':'FlexQ je kontinuirani sloj između sesija — mali dnevni signali pretvaraju se u rano upozorenje, kako bi terapeuti mogli djelovati prije nego kriza postane neizbježna.',
    'cta.demo':'Zatražite klinički demo',
    'hero.cta2':'Kako funkcionira →',
    'hero.trust':'Terapeut ostaje nositelj odluka',
    'prob.eyebrow':'Problem',
    'prob.h2':'Terapija je epizodična.<br><em>Mentalni stres nije.</em>',
    'prob.stat1.desc':'Tjedna između sesija. Prozor vidljivosti je prazan — klijent može deteriorirati u tišini većinu tog vremena.',
    'prob.stat2.desc':'Vremena sesije troši se na rekonstrukciju prethodnog perioda. Terapijsko vrijeme troši se na administraciju.',
    'prob.stat3.num':'Većina',
    'prob.stat3.desc':'Deterioracija prolazi tiho dok je kriza ne iznudi na vidjelo — kad je intervencija kasna i teža.',
    'prob.quote':'"Prvih 10–15 minuta svake sesije bila je <strong>rekonstrukcija</strong>. Sada je terapija. To je samo po sebi vrijedno."',
    'prob.note':'Klijent može početi lošije spavati, gubiti energiju ili se osjećati preplavljenim danima prije sljedećeg termina. FlexQ zatvara tu prazninu — čineći nevidljivo vidljivim prije sljedeće sesije.',
    'sol.eyebrow':'Rješenje',
    'sol.h2':'Jedan produkt,<br><em>tri iskrena obećanja.</em>',
    'sol.intro':'FlexQ pomiče skrb o mentalnom zdravlju od epizodičnog tretmana prema kontinuiranoj prisutnosti. Nije praćenje raspoloženja. Nije dijagnostički alat. Klinički signalni sloj.',
    'sol.p1.tag':'Za pacijente','sol.p1.h3':'Vaš trend, vaša bazna linija, vaš izbor.',
    'sol.p1.p':'60-sekundni dnevni check-in. Vaš terapeut vidi ono što vi odlučite. Vaš poslodavac nikad. Bez streakova, bez srama.',
    'sol.p2.tag':'Za terapeute','sol.p2.h3':'Uđite u svaku sesiju već orijentirani.',
    'sol.p2.p':'Trijaza prema promjeni, ne prema rezultatu. 90-sekundni pregled pred sesiju. Prilagodba planova uz AI podršku — vi kontrolirate i potpisujete.',
    'sol.p2.cta':'Pogledajte klinički prikaz →',
    'sol.p3.tag':'Za tvrtke','sol.p3.h3':'Vodeći indikator, ne wellness aplikacija.',
    'sol.p3.p':'Agregirani, anonimizirani signal zaposlenika — koristan za HR, obranljiv pred regulatorima, nevidljiv na individualnoj razini.',
    'sol.p3.cta':'Pogledajte enterprise izvještavanje →',
    'how.eyebrow':'Kako funkcionira?',
    'how.h2':'Utemeljeno u priznatim<br>terapijskim pristupima.',
    'how.intro':'Razvijeno u suradnji s kliničkim stručnjacima. Svaka zastava prikazuje svoje pravilo — bez crnih kutija.',
    'how.s1.n':'01 · Snimanje','how.s1.h3':'Brzi dnevni check-in',
    'how.s1.p':'60 sekundi — raspoloženje, energija, stres, san, opcionalna refleksija. Preskakanje je sigurno.',
    'how.s2.n':'02 · Usporedba','how.s2.h3':'Prema baznoj liniji',
    'how.s2.p':'Pacijent se uspoređuje sa sobom — ne s populacijskom normom. Osobna bazna linija, detekcija perzistencije.',
    'how.s3.n':'03 · Površina','how.s3.h3':'Obrasci postaju vidljivi',
    'how.s4.n':'04 · Akcija','how.s4.h3':'Akcija pod vodstvom terapeuta',
    'how.s4.p':'Potvrdi, prilagodi ili odbaci. Bez autonomne AI njege. Potpuni revizijski trag.',
    'landing.cta.h2':'Intervencija prije eskalacije.',
    'landing.cta.p':'Zatražite klinički demo i vidite što se promijenilo prije sljedeće sesije.',
    'th.h1':'Uđite u svaku sesiju<br><em>već orijentirani.</em>',
    'th.sub':'Prestanite rekonstruirati posljednja dva tjedna. FlexQ vam pokazuje što se promijenilo, zašto je važno i koje pravilo je to označilo — za 90 sekundi.',
    'jobs.h2':'Četiri posla koja FlexQ radi<br><em>za vaš caseload.</em>',
    'jobs.j1.ey':'01 · Trijaza','jobs.j1.h3':'Sortiraj prema promjeni, ne prema rezultatu',
    'jobs.j1.p':'Vaš popis pacijenata sortira se prema nedavnoj devijaciji, pa oni koji su tiho klizili izlaze prvi. Stabilni pacijenti ostaju stabilni, izvan puta.',
    'jobs.j2.ey':'02 · Pregled','jobs.j2.h3':'90-sekundni pogled pred sesiju',
    'jobs.j2.p':'Trend, raspon bazne linije, devijacijski događaj, nedavne refleksije. Točke za razgovor su prijedlozi — vi odlučujete koje ćete koristiti.',
    'jobs.j3.ey':'03 · Prilagodba','jobs.j3.h3':'Promjene plana koje pregledavate i kontrolirate',
    'jobs.j3.p1':'Kad signal perzistira, Adaptive Care Engine (ACE) izrađuje jednostavniji plan kao površinu za pregled — mjesto na kojemu se čuva vaša klinička kontrola. Prihvaćate, mijenjate ili odbijate u manje od tri klika. Revizijski logirano.',
    'jobs.j3.p2':'Bez autonomne AI njege.',
    'jobs.j4.ey':'04 · Upravljanje rizikom','jobs.j4.h3':'Saznajte tko treba pozornost prije nego postane kriza.',
    'jobs.j4.p1':'FlexQ neprekidno prati vaš cjeloviti caseload. Kad klijent priđe pragu rizika — trajna deterioracija, propušteni check-ini, pojavljujući obrazac — imenovana zastava pojavljuje se u vašem redu s pravilom koje ju je podiglo i dokazima iza nje.',
    'jobs.j4.p2':'Tri jasne odluke: potvrdi i prilagodi plan, samo potvrdi ili odbaci. Svaki odgovor je revizijski logiran. Sustav prati između sesija. Vi odlučujete što se dogodi dalje.',
    'trust.h2':'Provjerljivo. Konzervativno. Vaše.',
    'trust.c1.h4':'Svaka zastava prikazuje svoje pravilo',
    'trust.c1.p':'Perzistencija ≥5d iznad uobičajenog. Trajna devijacija >14d. Pad angažmana + rizik. Bez crnih kutija.',
    'trust.c2.h4':'Bazna linija je vlastita pacijentova',
    'trust.c2.p':'Klizni 7-dnevni prozor samoprocjena. Uspoređuje se sa samim sobom, nikad s populacijskom normom.',
    'trust.c3.h4':'Vi ostajete nositelj odluka',
    'trust.c3.p':'Sustav nikada autonomno ne kontaktira pacijenta o kliničnoj zabrinutosti. ACE izrađuje nacrt; vi potpisujete.',
    'trust.c4.h4':'Revizijski trag prema zadanom',
    'trust.c4.p':'Svako potvrđivanje, odbijanje i promjena plana zapisani su s pravilom, vremenskom oznakom i poljem za obrazloženje.',
    'th.cta.h2':'Spremi za isprobavanje?',
    'th.cta.p':'Uđite u svoju sljedeću sesiju već orijentirani.',
    'th.cta.btn':'Zatražite demo',
    'ent.h1':'Vodeći indikator mentalnog stresa zaposlenika —<br><em>ne</em> wellness aplikacija.',
    'ent.sub':'Kontinuirana podrška mentalnom zdravlju koja štiti produktivnost proaktivnom skrbi. Agregirani signal, anonimiziran po dizajnu, obranljiv pred regulatorima.',
    'ent.cta':'Razgovarajte s našim enterprise timom',
    'val.eyebrow':'Pokretači vrijednosti',
    'val.h2':'Gdje platforma<br><em>zarađuje svoju cijenu.</em>',
    'val.v1.h3':'Zadržavanje visokovrijednih talenata','val.v1.tag':'Najkritičnija poluga',
    'val.v1.p':'Otkrijte trajno povišeni stres ili rane signale burnout-a dovoljno rano da vodstvo može intervenirati. Sprečavanje čak i nekolicine odlazaka visokovrijednih zaposlenika godišnje može pokriti cjelokupnu investiciju u platformu.',
    'val.v2.h3':'Smanjenje bolovanja','val.v2.tag':'Stvarna, ali sekundarna poluga',
    'val.v2.p':'Čak i smanjenje jednog dana bolovanja po zaposleniku godišnje generira značajne uštede u enterprise razmjeru. Bolovanje je vidljivi trošak — prezentizam je veći skriveni.',
    'val.v3.h3':'Stabilizacija prezentizma','val.v3.tag':'Najveći skriveni trošak',
    'val.v3.p':'Zaposlenici pod trajnim mentalnim stresom ostaju na poslu, ali rade ispod punog kognitivnog kapaciteta. Mala poboljšanja produktivnosti kroz veliku populaciju donose značajne povrate.',
    'ent.cta2.q':'Za HR lidere koji su umorni od wellness teatra.',
    'footer.privacy':'Privatnost · GDPR / HIPAA','footer.science':'Znanost','footer.team':'Tim',
    'priv.eyebrow':'Pravna zaštita · Zaštita podataka',
    'priv.h1':'Politika<br><em>privatnosti.</em>',
    'priv.sub':'Ova marketinška stranica koristi analitičke alate i prikuplja vašu e-mail adresu samo ako je odlučite podijeliti. To je to.',
    'priv.s1.h2':'Tko smo','priv.s2.h2':'Što prikupljamo',
    'priv.s2.p':'Prikupljamo podatke na dva načina.',
    'priv.s3.h2':'Pravna osnova i vaši izbori','priv.s3.h3':'Upravljanje kolačićima',
    'priv.s4.h2':'Koliko dugo čuvamo vaše podatke','priv.s5.h2':'Vaša prava',
    'priv.s6.p':'Za sva pitanja o ovoj politici ili zahtjev ispitanika:',
    'priv.r.access':'Pristup','priv.r.access.p':'Zatražite kopiju svih osobnih podataka koje čuvamo o vama.',
    'priv.r.rect':'Ispravak','priv.r.rect.p':'Zamolite nas da ispravimo netočne podatke koje čuvamo o vama.',
    'priv.r.erase':'Brisanje','priv.r.erase.p':'Zamolite nas da obrišemo vašu e-mail adresu i sve povezane podatke u bilo kojem trenutku.',
    'priv.r.withdraw':'Povlačenje suglasnosti','priv.r.withdraw.p':'Povucite suglasnost za analitiku ili newsletter u bilo kojem trenutku, s trenutnim učinkom.',
    'cookie.decline':'Samo nužni','cookie.accept':'Prihvati analitiku',
    'team.eyebrow':'Tko gradi FlexQ',
    'team.h1':'Izgrađeno s kliničarima,<br><em>ne samo za njih.</em>',
    'team.core':'Ključni tim'
  }
};

var currentLang = localStorage.getItem('flexq_lang') || 'en';

function setLang(lang) {
  currentLang = lang;
  localStorage.setItem('flexq_lang', lang);
  document.querySelectorAll('[data-i18n]').forEach(function(el) {
    var k = el.getAttribute('data-i18n');
    if (T[lang] && T[lang][k] !== undefined) el.textContent = T[lang][k];
  });
  document.querySelectorAll('[data-i18n-html]').forEach(function(el) {
    var k = el.getAttribute('data-i18n-html');
    if (T[lang] && T[lang][k] !== undefined) el.innerHTML = T[lang][k];
  });
  document.querySelectorAll('.lang-btn').forEach(function(b) {
    b.classList.toggle('active', b.dataset.lang === lang);
  });
  document.documentElement.lang = lang === 'hr' ? 'hr' : 'en';
}

// ── Contact ──
function openContact(){
  window.location.href='mailto:360healtlink@gmail.com?subject=FlexQ%20—%20demo%20request';
}

// ── Cookie consent ──
var GA_ID='G-XXXXXXXXXX';

function loadGA(){
  var s=document.createElement('script');
  s.async=true;
  s.src='https://www.googletagmanager.com/gtag/js?id='+GA_ID;
  document.head.appendChild(s);
  window.dataLayer=window.dataLayer||[];
  function gtag(){dataLayer.push(arguments);}
  window.gtag=gtag;
  gtag('js',new Date());
  gtag('config',GA_ID,{anonymize_ip:true});
}

function cookieChoice(accept){
  localStorage.setItem('flexq_cookies',accept?'yes':'no');
  document.getElementById('cookie-banner').style.display='none';
  if(accept) loadGA();
}

// ── Lightbox ──
function openLightboxImg(src,alt){
  var ov=document.getElementById('lb-overlay');
  var img=document.getElementById('lb-img');
  var wrap=document.getElementById('lb-screen-wrap');
  img.src=src; img.alt=alt||'';
  img.style.display='block';
  wrap.style.display='none'; wrap.innerHTML='';
  ov.classList.add('open');
  document.body.style.overflow='hidden';
}
function openLightboxScreen(el){
  var ov=document.getElementById('lb-overlay');
  var img=document.getElementById('lb-img');
  var wrap=document.getElementById('lb-screen-wrap');
  img.style.display='none'; img.src='';
  wrap.innerHTML=el.outerHTML;
  wrap.style.display='block';
  ov.classList.add('open');
  document.body.style.overflow='hidden';
}
function closeLightbox(){
  var ov=document.getElementById('lb-overlay');
  ov.classList.remove('open');
  document.body.style.overflow='';
  document.getElementById('lb-screen-wrap').innerHTML='';
}
document.addEventListener('keydown',function(e){if(e.key==='Escape') closeLightbox();});

// ── Ham menu ──
function toggleHam(){
  var ham=document.querySelector('.ham');
  var nl=document.querySelector('.nav-links');
  if(ham){ham.classList.toggle('open');nl.classList.toggle('open');}
}

// ── Init ──
(function(){
  var c=localStorage.getItem('flexq_cookies');
  var banner=document.getElementById('cookie-banner');
  if(banner){
    if(!c) banner.style.display='flex';
    else if(c==='yes') loadGA();
  }
  var lbOv=document.getElementById('lb-overlay');
  if(lbOv) lbOv.addEventListener('click',function(e){if(e.target===this) closeLightbox();});
  initNav();
  setLang(currentLang);
})();
"""

with open('js/site.js', 'w', encoding='utf-8') as f:
    f.write(SITE_JS.strip() + '\n')
print('✓ js/site.js')

# ─────────────────────────────────────────────────────────
# STEP 4 — Extract page content blocks
# ─────────────────────────────────────────────────────────
html_lines = html.split('\n')

def get_lines(start, end):
    return '\n'.join(html_lines[start-1:end])

def extract_page_content(html_block, page_id):
    """Strip outer wrapper div from page content."""
    # Remove opening div
    result = re.sub(rf'<div id="page-{page_id}" class="page[^"]*">\s*', '', html_block, count=1)
    # Remove last </div>
    idx = result.rfind('</div>')
    if idx != -1:
        result = result[:idx]
    return result.strip()

landing_raw    = get_lines(346, 476)
therapists_raw = get_lines(479, 569)
enterprise_raw = get_lines(572, 616)
privacy_raw    = get_lines(619, 800)
team_raw       = get_lines(803, 944)

landing_content    = extract_page_content(landing_raw,    'landing')
therapists_content = extract_page_content(therapists_raw, 'therapists')
enterprise_content = extract_page_content(enterprise_raw, 'enterprise')
privacy_content    = extract_page_content(privacy_raw,    'privacy')
team_content       = extract_page_content(team_raw,       'team')

# ─────────────────────────────────────────────────────────
# STEP 5 — Shared fragments
# ─────────────────────────────────────────────────────────
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300;1,6..72,400&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap" rel="stylesheet">'

# Extract nav from modified html
nav_raw = re.search(r'<nav>(.*?)</nav>', html, re.DOTALL).group(0)
# Fix ham button onclick
nav_raw = nav_raw.replace(
    'onclick="this.classList.toggle(\'open\');document.querySelector(\'.nav-links\').classList.toggle(\'open\')"',
    'onclick="toggleHam()"'
)
# Lang toggle hidden — single language (EN only)

COOKIE_BANNER = '''<!-- Cookie banner -->
<div id="cookie-banner" role="dialog" aria-label="Cookie consent">
  <p>We use analytics tools to understand how visitors use this site. No personal data is identified.
    <a href="privacy.html" data-i18n-void>Privacy policy</a>
  </p>
  <div class="cb-btns">
    <button class="cb-decline" onclick="cookieChoice(false)" data-i18n="cookie.decline">Only essential</button>
    <button class="cb-accept" onclick="cookieChoice(true)" data-i18n="cookie.accept">Accept analytics</button>
  </div>
</div>'''

LIGHTBOX = '''<!-- Lightbox -->
<div id="lb-overlay" role="dialog" aria-modal="true" aria-label="Enlarged image">
  <button id="lb-close" onclick="closeLightbox()" aria-label="Close">&#x2715;</button>
  <img id="lb-img" src="" alt=""/>
  <div id="lb-screen-wrap"></div>
</div>'''

# ─────────────────────────────────────────────────────────
# STEP 6 — HTML template
# ─────────────────────────────────────────────────────────
def build_html(title, desc, content):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
{FONTS}
<link rel="stylesheet" href="css/site.css">
</head>
<body>

{nav_raw}

{content}

{COOKIE_BANNER}

{LIGHTBOX}

<script src="js/site.js"></script>
</body>
</html>
"""

# ─────────────────────────────────────────────────────────
# STEP 7 — Write HTML files
# ─────────────────────────────────────────────────────────
pages = [
    ('index.html',       'FlexQ — Intervention before escalation',
     'Continuous mental health signal layer between therapy sessions.',
     landing_content),
    ('therapists.html',  'FlexQ — For therapists',
     'Walk into every session already oriented. 90-second pre-session brief.',
     therapists_content),
    ('enterprise.html',  'FlexQ — For enterprises',
     'A leading indicator of workforce mental strain. Aggregate signal, anonymised by design.',
     enterprise_content),
    ('privacy.html',     'FlexQ — Privacy policy',
     'FlexQ Health privacy policy. GDPR and AZOP compliant.',
     privacy_content),
    ('team.html',        'FlexQ — The team',
     'Built with clinicians, not just for them.',
     team_content),
]

for filename, title, desc, content in pages:
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(build_html(title, desc, content))
    size = os.path.getsize(filename) // 1024
    attrs = content.count('data-i18n')
    print(f'  {filename:20s}  {size:4d}KB   data-i18n attrs: {attrs}')

print('\nDone.')
