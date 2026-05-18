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
})();
