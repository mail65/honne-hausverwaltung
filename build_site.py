#!/usr/bin/env python3
"""Build script for Honne Hausverwaltung website."""

import os

base = "/Users/felix/.openclaw/workspace/honne-hausverwaltung"

# ── Logo SVG (nav/footer version – inverted for dark bg) ──────────────────────
LOGO_NAV = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <rect width="400" height="400" fill="transparent"/>
  <rect x="130" y="120" width="140" height="90" fill="#ffffff"/>
  <polygon points="120,120 200,70 280,120" fill="#ffffff"/>
  <circle cx="200" cy="105" r="10" fill="#1B2A4A"/>
  <rect x="145" y="130" width="22" height="30" rx="11" fill="#1B2A4A"/>
  <rect x="189" y="130" width="22" height="30" rx="11" fill="#1B2A4A"/>
  <rect x="233" y="130" width="22" height="30" rx="11" fill="#1B2A4A"/>
  <rect x="183" y="168" width="34" height="42" rx="17" fill="#1B2A4A"/>
  <rect x="95" y="145" width="38" height="65" fill="#ffffff"/>
  <polygon points="88,145 114,125 140,145" fill="#ffffff"/>
  <rect x="102" y="153" width="12" height="18" rx="6" fill="#1B2A4A"/>
  <rect x="118" y="153" width="12" height="18" rx="6" fill="#1B2A4A"/>
  <rect x="267" y="145" width="38" height="65" fill="#ffffff"/>
  <polygon points="260,145 286,125 312,145" fill="#ffffff"/>
  <rect x="270" y="153" width="12" height="18" rx="6" fill="#1B2A4A"/>
  <rect x="286" y="153" width="12" height="18" rx="6" fill="#1B2A4A"/>
  <circle cx="200" cy="188" r="7" fill="none" stroke="#C19A4B" stroke-width="2.5"/>
  <line x1="200" y1="195" x2="200" y2="218" stroke="#C19A4B" stroke-width="2.5"/>
  <line x1="188" y1="202" x2="212" y2="202" stroke="#C19A4B" stroke-width="2.5"/>
  <path d="M200,218 Q188,224 185,220" fill="none" stroke="#C19A4B" stroke-width="2.5" stroke-linecap="round"/>
  <path d="M200,218 Q212,224 215,220" fill="none" stroke="#C19A4B" stroke-width="2.5" stroke-linecap="round"/>
</svg>"""

# ── CSS ───────────────────────────────────────────────────────────────────────
CSS = """
    *,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
    :root{
      --navy:#1B2A4A;--navyd:#111D30;--gold:#C19A4B;--goldl:#D4AD62;
      --white:#FFFFFF;--off:#F8F6F2;--text:#2C2C2C;--muted:#5C5C5C;
      --border:#E0D9CE;--sp:clamp(64px,8vw,112px)
    }
    html{scroll-behavior:smooth}
    body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI','Helvetica Neue',Arial,sans-serif;color:var(--text);background:var(--white);line-height:1.7;-webkit-font-smoothing:antialiased}
    h1,h2,h3,h4{font-family:Georgia,'Times New Roman',serif;line-height:1.25;color:var(--navy)}
    p{color:var(--muted)}
    img{display:block;max-width:100%}
    a{text-decoration:none;color:inherit}
    .wrap{width:100%;max-width:1140px;margin:0 auto;padding:0 clamp(20px,5vw,60px)}
    .lbl{display:inline-block;font-size:11px;font-weight:600;letter-spacing:3px;text-transform:uppercase;color:var(--gold);margin-bottom:14px}
    .ttl{font-size:clamp(28px,4vw,42px);font-weight:normal;margin-bottom:18px}
    .sub{font-size:17px;color:var(--muted);max-width:560px;line-height:1.75}
    .bar{width:48px;height:2px;background:var(--gold);margin:18px 0 32px}
    #nav{position:fixed;top:0;left:0;right:0;z-index:1000;transition:background .35s,box-shadow .35s}
    #nav.scrolled{background:rgba(27,42,74,.97);backdrop-filter:blur(8px);box-shadow:0 2px 24px rgba(0,0,0,.18)}
    .navin{display:flex;align-items:center;justify-content:space-between;height:80px}
    .nlogo{display:flex;align-items:center;gap:10px}
    .nlogo svg{width:44px;height:44px}
    .nlt{display:flex;flex-direction:column;line-height:1.1}
    .nlt .b{font-family:Georgia,serif;font-size:17px;font-weight:bold;letter-spacing:3px;color:#fff}
    .nlt .s{font-size:9px;letter-spacing:2.5px;text-transform:uppercase;color:var(--gold);margin-top:2px}
    .nlinks{display:flex;align-items:center;gap:32px;list-style:none}
    .nlinks a{font-size:12px;letter-spacing:1.5px;text-transform:uppercase;color:rgba(255,255,255,.8);font-weight:500;transition:color .2s;position:relative}
    .nlinks a::after{content:'';position:absolute;bottom:-4px;left:0;right:0;height:1px;background:var(--gold);transform:scaleX(0);transition:transform .25s}
    .nlinks a:hover{color:#fff}
    .nlinks a:hover::after{transform:scaleX(1)}
    .ncta{background:var(--gold)!important;color:var(--navy)!important;padding:10px 20px!important;font-weight:700!important}
    .ncta::after{display:none!important}
    .ncta:hover{background:var(--goldl)!important}
    .hbtn{display:none;flex-direction:column;gap:5px;cursor:pointer;padding:8px;background:none;border:none}
    .hbtn span{display:block;width:24px;height:2px;background:#fff;transition:all .3s}
    .hbtn.open span:nth-child(1){transform:translateY(7px) rotate(45deg)}
    .hbtn.open span:nth-child(2){opacity:0}
    .hbtn.open span:nth-child(3){transform:translateY(-7px) rotate(-45deg)}
    .mobm{display:none;position:fixed;top:80px;left:0;right:0;background:rgba(27,42,74,.98);padding:20px 0;z-index:999}
    .mobm.open{display:block}
    .mobm a{display:block;padding:14px 32px;font-size:13px;letter-spacing:1.5px;text-transform:uppercase;color:rgba(255,255,255,.8);border-bottom:1px solid rgba(255,255,255,.06);transition:color .2s,background .2s}
    .mobm a:hover{color:var(--gold);background:rgba(255,255,255,.04)}
    #hero{position:relative;min-height:100svh;display:flex;align-items:center;background:var(--navy);overflow:hidden}
    .hbg{position:absolute;inset:0;background-image:url('https://images.unsplash.com/photo-1570129477492-45c003dc44a4?w=1800&q=80&auto=format&fit=crop');background-size:cover;background-position:center 35%;opacity:.26}
    .hov{position:absolute;inset:0;background:linear-gradient(135deg,rgba(27,42,74,.96) 0%,rgba(27,42,74,.75) 50%,rgba(27,42,74,.55) 100%)}
    .hcon{position:relative;z-index:2;padding:140px 0 80px}
    .hbdg{display:inline-flex;align-items:center;gap:10px;background:rgba(193,154,75,.12);border:1px solid rgba(193,154,75,.28);padding:8px 18px;margin-bottom:32px}
    .hbdg span{font-size:11px;letter-spacing:2.5px;text-transform:uppercase;color:var(--gold);font-weight:600}
    .dot{width:5px;height:5px;background:var(--gold);border-radius:50%;display:inline-block}
    .htit{font-size:clamp(38px,5.8vw,72px);font-weight:normal;color:#fff;max-width:760px;line-height:1.1;margin-bottom:22px}
    .htit em{font-style:italic;color:var(--gold)}
    .hsub{font-size:clamp(16px,2vw,19px);color:rgba(255,255,255,.75);max-width:520px;margin-bottom:44px;line-height:1.8}
    .hact{display:flex;align-items:center;gap:22px;flex-wrap:wrap}
    .btn1{display:inline-flex;align-items:center;gap:8px;background:var(--gold);color:var(--navy);padding:15px 34px;font-size:12px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;transition:all .25s}
    .btn1:hover{background:var(--goldl);transform:translateY(-2px);box-shadow:0 8px 24px rgba(193,154,75,.35)}
    .btn2{display:inline-flex;align-items:center;gap:6px;color:rgba(255,255,255,.75);font-size:12px;letter-spacing:1px;text-transform:uppercase;font-weight:500;border-bottom:1px solid rgba(255,255,255,.28);padding-bottom:2px;transition:all .2s}
    .btn2:hover{color:#fff;border-color:var(--gold)}
    .hstats{position:relative;z-index:2;display:flex;gap:clamp(28px,5vw,64px);margin-top:72px;padding-top:36px;border-top:1px solid rgba(255,255,255,.1);flex-wrap:wrap}
    .hsn{font-family:Georgia,serif;font-size:clamp(30px,4vw,46px);color:#fff;line-height:1}
    .hsn .g{color:var(--gold)}
    .hsl{font-size:11px;letter-spacing:1.5px;text-transform:uppercase;color:rgba(255,255,255,.45);margin-top:6px}
    #ueber{padding:var(--sp) 0;background:var(--white)}
    .ug{display:grid;grid-template-columns:1fr 1fr;gap:clamp(40px,6vw,80px);align-items:center}
    .uiw{position:relative}
    .uimg{width:100%;aspect-ratio:4/5;object-fit:cover;display:block}
    .uacc{position:absolute;bottom:-20px;right:-20px;width:135px;height:135px;background:var(--navy);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px;border:3px solid var(--gold)}
    .uacc .un{font-family:Georgia,serif;font-size:36px;color:#fff;line-height:1}
    .uacc .ul{font-size:9px;letter-spacing:1.5px;text-transform:uppercase;color:var(--gold);text-align:center;padding:0 10px}
    .ucont{padding-left:clamp(0px,2vw,16px)}
    .utxt{font-size:16px;color:var(--muted);line-height:1.85;margin-bottom:18px}
    .uqt{font-size:18px;font-family:Georgia,serif;color:var(--navy);font-style:italic;border-left:3px solid var(--gold);padding-left:20px;margin:30px 0;line-height:1.6}
    .ufacts{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:36px}
    .ufact{background:var(--off);padding:18px 20px;border-left:3px solid var(--gold);transition:transform .2s}
    .ufact:hover{transform:translateX(4px)}
    .ufact strong{display:block;font-family:Georgia,serif;font-size:22px;color:var(--navy);margin-bottom:3px}
    .ufact span{font-size:11px;letter-spacing:1px;text-transform:uppercase;color:var(--muted)}
    #leistungen{padding:var(--sp) 0;background:var(--navy)}
    #leistungen .lbl{color:var(--gold)}
    #leistungen .ttl{color:#fff}
    #leistungen .sub{color:rgba(255,255,255,.58)}
    #leistungen .bar{background:var(--gold)}
    .lh{margin-bottom:clamp(40px,5vw,60px)}
    .lgrid{display:grid;grid-template-columns:repeat(2,1fr);gap:2px}
    .lcard{background:rgba(255,255,255,.04);padding:clamp(28px,4vw,44px);transition:background .25s;position:relative;overflow:hidden}
    .lcard::before{content:'';position:absolute;top:0;left:0;width:3px;height:0;background:var(--gold);transition:height .35s}
    .lcard:hover{background:rgba(255,255,255,.07)}
    .lcard:hover::before{height:100%}
    .lico{width:50px;height:50px;background:rgba(193,154,75,.1);border:1px solid rgba(193,154,75,.22);display:flex;align-items:center;justify-content:center;margin-bottom:22px}
    .lico svg{width:22px;height:22px;fill:var(--gold)}
    .ltit{font-family:Georgia,serif;font-size:19px;color:#fff;margin-bottom:14px;font-weight:normal}
    .llist{list-style:none;display:flex;flex-direction:column;gap:7px}
    .llist li{font-size:13.5px;color:rgba(255,255,255,.52);padding-left:16px;position:relative;line-height:1.5}
    .llist li::before{content:'\\2014';position:absolute;left:0;color:var(--gold);font-size:11px;top:2px}
    #warum{padding:var(--sp) 0;background:var(--off)}
    .wgrid{display:grid;grid-template-columns:1fr 1.4fr;gap:clamp(40px,6vw,80px);align-items:start}
    .wstick{position:sticky;top:100px}
    .wimg{width:100%;aspect-ratio:3/4;object-fit:cover;margin-top:36px}
    .usplist{display:flex;flex-direction:column;gap:20px}
    .uspitem{display:flex;gap:22px;align-items:flex-start;padding:26px;background:#fff;border-bottom:2px solid transparent;transition:border-color .25s,box-shadow .25s,transform .25s}
    .uspitem:hover{border-color:var(--gold);box-shadow:0 8px 32px rgba(0,0,0,.07);transform:translateX(4px)}
    .uspnum{font-family:Georgia,serif;font-size:34px;color:var(--border);line-height:1;flex-shrink:0;width:38px;transition:color .25s}
    .uspitem:hover .uspnum{color:var(--gold)}
    .usptx h3{font-size:17px;margin-bottom:7px;font-weight:normal}
    .usptx p{font-size:14px;line-height:1.7;color:var(--muted)}
    #kontakt{padding:var(--sp) 0;background:#fff}
    .kgrid{display:grid;grid-template-columns:1fr 1.2fr;gap:clamp(40px,6vw,80px);align-items:start}
    .kinfo{padding-top:8px}
    .kdet{display:flex;gap:16px;margin-bottom:24px;align-items:flex-start}
    .kdico{width:42px;height:42px;background:var(--navy);display:flex;align-items:center;justify-content:center;flex-shrink:0}
    .kdico svg{width:17px;height:17px;fill:var(--gold)}
    .kdtx strong{display:block;font-size:11px;letter-spacing:1.5px;text-transform:uppercase;color:var(--navy);margin-bottom:3px}
    .kdtx a,.kdtx span{font-size:15px;color:var(--muted);transition:color .2s;display:block}
    .kdtx a:hover{color:var(--gold)}
    .knote{margin-top:36px;padding:22px;background:var(--off);border-left:3px solid var(--gold);font-size:14px;color:var(--muted);line-height:1.75}
    .kform{background:var(--navy);padding:clamp(28px,4vw,44px)}
    .fgrp{margin-bottom:18px}
    .frow{display:grid;grid-template-columns:1fr 1fr;gap:14px}
    .fgrp label{display:block;font-size:10px;letter-spacing:1.5px;text-transform:uppercase;color:rgba(255,255,255,.45);margin-bottom:7px}
    .fgrp input,.fgrp textarea{width:100%;background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.1);color:#fff;padding:13px 15px;font-size:15px;font-family:inherit;transition:border-color .2s,background .2s;outline:none;-webkit-appearance:none;border-radius:0}
    .fgrp input::placeholder,.fgrp textarea::placeholder{color:rgba(255,255,255,.28)}
    .fgrp input:focus,.fgrp textarea:focus{border-color:var(--gold);background:rgba(255,255,255,.09)}
    .fgrp textarea{min-height:110px;resize:vertical}
    .fchk{display:flex;align-items:flex-start;gap:10px;margin:18px 0}
    .fchk input[type=checkbox]{width:16px;height:16px;flex-shrink:0;margin-top:3px;accent-color:var(--gold);cursor:pointer}
    .fchk label{font-size:12px;color:rgba(255,255,255,.45);line-height:1.55;cursor:pointer}
    .fchk a{color:var(--gold);text-decoration:underline;text-underline-offset:2px}
    .fsub{width:100%;background:var(--gold);color:var(--navy);border:none;padding:16px;font-size:12px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;cursor:pointer;transition:background .2s,transform .2s;font-family:inherit}
    .fsub:hover{background:var(--goldl);transform:translateY(-1px)}
    .fpv{font-size:11px;color:rgba(255,255,255,.28);margin-top:10px;line-height:1.6}
    footer{background:var(--navyd);padding:48px 0 28px}
    .finner{display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:22px;margin-bottom:28px;padding-bottom:28px;border-bottom:1px solid rgba(255,255,255,.07)}
    .flogo{display:flex;align-items:center;gap:11px}
    .flogo svg{width:38px;height:38px}
    .flt .b{font-family:Georgia,serif;font-size:15px;font-weight:bold;letter-spacing:3px;color:#fff}
    .flt .s{font-size:8px;letter-spacing:2px;text-transform:uppercase;color:var(--gold);margin-top:2px}
    .flinks{display:flex;gap:28px;flex-wrap:wrap}
    .flinks a{font-size:11px;letter-spacing:1px;text-transform:uppercase;color:rgba(255,255,255,.38);transition:color .2s}
    .flinks a:hover{color:var(--gold)}
    .fbot{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:14px}
    .fcopy{font-size:12px;color:rgba(255,255,255,.22);letter-spacing:.5px}
    .ftag{font-size:12px;color:rgba(255,255,255,.18);font-style:italic}
    .fu{opacity:0;transform:translateY(28px);transition:opacity .7s ease,transform .7s ease}
    .fu.vis{opacity:1;transform:translateY(0)}
    @keyframes fadeUp{from{opacity:0;transform:translateY(28px)}to{opacity:1;transform:translateY(0)}}
    .hcon>*{animation:fadeUp .9s ease both}
    .hbdg{animation-delay:.1s}.htit{animation-delay:.25s}.hsub{animation-delay:.4s}.hact{animation-delay:.55s}.hstats{animation-delay:.7s}
    @media(max-width:900px){.nlinks{display:none}.hbtn{display:flex}.ug{grid-template-columns:1fr}.uiw{order:-1}.uacc{bottom:-14px;right:-8px;width:110px;height:110px}.lgrid{grid-template-columns:1fr}.wgrid{grid-template-columns:1fr}.wstick{position:static}.wimg{display:none}.kgrid{grid-template-columns:1fr}.frow{grid-template-columns:1fr}.ufacts{grid-template-columns:1fr 1fr}}
    @media(max-width:560px){.hstats{gap:20px}.ufacts{grid-template-columns:1fr}.finner{flex-direction:column;align-items:flex-start}.fbot{flex-direction:column;align-items:flex-start}.hact{flex-direction:column;align-items:flex-start}}
"""

# ── JS ────────────────────────────────────────────────────────────────────────
JS = """
    // Nav scroll
    const nav = document.getElementById('nav');
    window.addEventListener('scroll', () => {
      nav.classList.toggle('scrolled', window.scrollY > 40);
    }, {passive: true});
    // Hamburger
    function toggleMenu(btn) {
      btn.classList.toggle('open');
      document.getElementById('mobm').classList.toggle('open');
    }
    function closeMenu() {
      document.querySelector('.hbtn').classList.remove('open');
      document.getElementById('mobm').classList.remove('open');
    }
    // Scroll animations
    const obs = new IntersectionObserver((entries) => {
      entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('vis'); obs.unobserve(e.target); } });
    }, {threshold: 0.12});
    document.querySelectorAll('.fu').forEach(el => obs.observe(el));
    // Form
    document.getElementById('cform').addEventListener('submit', function(e) {
      e.preventDefault();
      const n = this.querySelector('[name=name]').value;
      const em = this.querySelector('[name=email]').value;
      const tel = this.querySelector('[name=tel]').value;
      const msg = this.querySelector('[name=msg]').value;
      const body = encodeURIComponent(
        'Sehr geehrter Herr Honne,\\n\\nSie haben eine Anfrage erhalten:\\n\\nName: ' + n +
        '\\nE-Mail: ' + em + '\\nTelefon: ' + tel + '\\n\\nNachricht:\\n' + msg +
        '\\n\\nMit freundlichen Gr\\u00fc\\u00dfen'
      );
      window.location.href = 'mailto:uwehonne@honne-hausverwaltung.de?subject=' +
        encodeURIComponent('Anfrage von ' + n) + '&body=' + body;
    });
"""

# ── INDEX.HTML ────────────────────────────────────────────────────────────────
INDEX = f"""<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Honne Hausverwaltung Hamburg \u2013 Ihre WEG-Verwaltung in besten H\u00e4nden. Pers\u00f6nlich, zuverl\u00e4ssig und mit Herz.">
  <title>Honne Hausverwaltung Hamburg</title>
  <style>{CSS}</style>
</head>
<body>

<!-- NAV -->
<nav id="nav">
  <div class="wrap">
    <div class="navin">
      <a href="#hero" class="nlogo" aria-label="Honne Hausverwaltung">
        {LOGO_NAV}
        <div class="nlt">
          <span class="b">HONNE</span>
          <span class="s">Hausverwaltung</span>
        </div>
      </a>
      <ul class="nlinks">
        <li><a href="#ueber">\u00dcber uns</a></li>
        <li><a href="#leistungen">Leistungen</a></li>
        <li><a href="#warum">Warum wir</a></li>
        <li><a href="#kontakt" class="ncta">Anfrage senden</a></li>
      </ul>
      <button class="hbtn" aria-label="Men\u00fc" onclick="toggleMenu(this)">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
</nav>
<div class="mobm" id="mobm">
  <a href="#ueber" onclick="closeMenu()">\u00dcber uns</a>
  <a href="#leistungen" onclick="closeMenu()">Leistungen</a>
  <a href="#warum" onclick="closeMenu()">Warum wir</a>
  <a href="#kontakt" onclick="closeMenu()" style="color:var(--gold);font-weight:700">Jetzt anfragen</a>
</div>

<!-- HERO -->
<section id="hero">
  <div class="hbg"></div>
  <div class="hov"></div>
  <div class="wrap">
    <div class="hcon">
      <div class="hbdg">
        <span class="dot"></span>
        <span>Hausverwaltung Hamburg</span>
        <span class="dot"></span>
      </div>
      <h1 class="htit">Ihre Immobilie<br>in <em>besten H\u00e4nden</em></h1>
      <p class="hsub">Pers\u00f6nlich, zuverl\u00e4ssig und mit Herz. Wir betreuen Ihre Wohnungseigent\u00fcmergemeinschaft so, als w\u00e4re es unsere eigene.</p>
      <div class="hact">
        <a href="#kontakt" class="btn1">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>
          Jetzt anfragen
        </a>
        <a href="#leistungen" class="btn2">
          Unsere Leistungen
          <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/></svg>
        </a>
      </div>
      <div class="hstats">
        <div><div class="hsn">10<span class="g">+</span></div><div class="hsl">Betreute WEGs</div></div>
        <div><div class="hsn"><span class="g">100%</span></div><div class="hsl">Full-Service</div></div>
        <div><div class="hsn"><span class="g">1</span></div><div class="hsl">Ihr Ansprechpartner</div></div>
        <div><div class="hsn" style="font-size:clamp(20px,3vw,32px);letter-spacing:2px">HH</div><div class="hsl">Hamburg</div></div>
      </div>
    </div>
  </div>
</section>

<!-- \u00dcBER UNS -->
<section id="ueber">
  <div class="wrap">
    <div class="ug">
      <div class="uiw fu">
        <img class="uimg"
          src="https://images.unsplash.com/photo-1486325212027-8081e485255e?w=800&q=85&auto=format&fit=crop&crop=center"
          alt="Hamburger Altbau" loading="lazy">
        <div class="uacc">
          <span class="un">10<span style="color:var(--gold)">+</span></span>
          <span class="ul">Jahre Erfahrung</span>
        </div>
      </div>
      <div class="ucont fu" style="transition-delay:.15s">
        <span class="lbl">\u00