#!/usr/bin/env python3
"""
Briefbogen v4 – Honne Hausverwaltung
Frisches, modernes Design: Navy #1B2A4A, Gold #C19A4B
"""

import base64
import os
from pathlib import Path
from playwright.sync_api import sync_playwright

# ── Paths ──────────────────────────────────────────────────────────────────
SCRIPT_DIR = Path(__file__).parent
LOGO_PATH  = Path("/Users/felix/.openclaw/workspace/honne-hausverwaltung/assets/logo/honne_logo_real_512.png")
PDF_OUT    = SCRIPT_DIR / "briefbogen_v4.pdf"
PNG_OUT    = SCRIPT_DIR / "briefbogen_v4_preview.png"

# ── Logo → base64 ──────────────────────────────────────────────────────────
with open(LOGO_PATH, "rb") as f:
    logo_b64 = base64.b64encode(f.read()).decode()
logo_src = f"data:image/png;base64,{logo_b64}"

# ── HTML ───────────────────────────────────────────────────────────────────
HTML = f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Inter:wght@300;400;500;600&display=swap');

  :root {{
    --navy:  #1B2A4A;
    --gold:  #C19A4B;
    --gold2: #D4AF70;
    --off:   #F8F7F4;
    --light: #EEF0F5;
    --text:  #2C3A52;
    --muted: #6B7A94;
  }}

  * {{ margin: 0; padding: 0; box-sizing: border-box; }}

  html, body {{
    width: 210mm;
    min-height: 297mm;
    background: white;
    font-family: 'Inter', 'Helvetica Neue', Arial, sans-serif;
    color: var(--text);
  }}

  /* ── PAGE WRAPPER ─────────────────────────────── */
  .page {{
    width: 210mm;
    min-height: 297mm;
    background: white;
    position: relative;
    display: flex;
    flex-direction: column;
  }}

  /* ── HEADER ───────────────────────────────────── */
  .header {{
    background: var(--navy);
    padding: 18mm 14mm 12mm 14mm;
    display: flex;
    align-items: center;
    justify-content: space-between;
    position: relative;
    overflow: hidden;
  }}

  /* subtle geometric accent in header background */
  .header::before {{
    content: '';
    position: absolute;
    top: -40px;
    right: -40px;
    width: 180px;
    height: 180px;
    border: 1px solid rgba(193,154,75,0.15);
    border-radius: 50%;
  }}
  .header::after {{
    content: '';
    position: absolute;
    top: -20px;
    right: -20px;
    width: 120px;
    height: 120px;
    border: 1px solid rgba(193,154,75,0.10);
    border-radius: 50%;
  }}

  /* ── LOGO BOX ─────────────────────────────────── */
  .logo-box {{
    flex: 0 0 auto;
    display: flex;
    align-items: center;
  }}

  .logo-box img {{
    width: 110px;
    height: 110px;
    object-fit: contain;
    object-position: center;
    display: block;
    filter: brightness(0) invert(1);  /* white version on dark */
  }}

  /* vertical gold divider */
  .header-divider {{
    width: 1px;
    height: 70px;
    background: linear-gradient(to bottom, transparent, var(--gold), transparent);
    margin: 0 18px;
    flex-shrink: 0;
  }}

  /* ── FIRM INFO (right side) ───────────────────── */
  .firm-info {{
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 2px;
  }}

  .firm-name {{
    font-family: 'Playfair Display', Georgia, serif;
    font-size: 22px;
    font-weight: 700;
    color: white;
    letter-spacing: 0.5px;
    line-height: 1.1;
  }}

  .firm-tagline {{
    font-size: 9.5px;
    font-weight: 400;
    color: var(--gold);
    letter-spacing: 2.5px;
    text-transform: uppercase;
    margin-top: 4px;
    margin-bottom: 8px;
  }}

  .contact-row {{
    display: flex;
    align-items: center;
    gap: 6px;
    font-size: 8.5px;
    color: rgba(255,255,255,0.75);
    font-weight: 300;
    margin-top: 2px;
  }}

  .contact-row .dot {{
    width: 3px;
    height: 3px;
    border-radius: 50%;
    background: var(--gold);
    flex-shrink: 0;
  }}

  .contact-row a {{
    color: rgba(255,255,255,0.75);
    text-decoration: none;
  }}

  /* ── GRADIENT RULE ────────────────────────────── */
  .header-rule {{
    height: 4px;
    background: linear-gradient(to right, var(--navy) 0%, var(--gold) 40%, var(--gold2) 60%, var(--navy) 100%);
  }}

  .sub-rule {{
    height: 1px;
    background: linear-gradient(to right, transparent, var(--gold), transparent);
    margin: 0 14mm;
  }}

  /* ── ADDRESS WINDOW STRIP ─────────────────────── */
  .addr-strip {{
    padding: 7mm 14mm 4mm 14mm;
    display: flex;
    align-items: flex-end;
    justify-content: space-between;
  }}

  .addr-window {{
    font-size: 7.5px;
    color: var(--muted);
    border-bottom: 1px solid #ddd;
    padding-bottom: 2px;
    min-width: 85mm;
  }}

  .addr-window .return-addr {{
    font-size: 6.5px;
    color: var(--muted);
    letter-spacing: 0.3px;
    margin-bottom: 3px;
    padding-bottom: 2px;
    border-bottom: 1px dotted #ccc;
  }}

  .addr-window .recipient {{
    font-size: 9px;
    color: var(--text);
    line-height: 1.7;
    padding-top: 3px;
  }}

  .date-ref {{
    text-align: right;
    font-size: 8.5px;
    color: var(--muted);
    line-height: 1.8;
  }}

  .date-ref .label {{
    font-size: 7px;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: var(--gold);
    font-weight: 600;
  }}

  /* ── CONTENT AREA ─────────────────────────────── */
  .content {{
    flex: 1;
    padding: 6mm 14mm 8mm 14mm;
  }}

  .subject-line {{
    font-size: 12px;
    font-weight: 600;
    color: var(--navy);
    margin-bottom: 6mm;
    padding-bottom: 3mm;
    border-bottom: 1.5px solid var(--light);
    position: relative;
  }}

  .subject-line::after {{
    content: '';
    position: absolute;
    bottom: -1.5px;
    left: 0;
    width: 40px;
    height: 1.5px;
    background: var(--gold);
  }}

  .salutation {{
    font-size: 10px;
    color: var(--text);
    margin-bottom: 4mm;
    line-height: 1.6;
  }}

  .body-text {{
    font-size: 10px;
    color: var(--text);
    line-height: 1.75;
  }}

  .body-text p {{
    margin-bottom: 4mm;
  }}

  /* ── SIGNATURE AREA ───────────────────────────── */
  .signature-area {{
    padding: 8mm 14mm 6mm 14mm;
  }}

  .sig-line {{
    width: 50mm;
    height: 1px;
    background: var(--navy);
    margin-bottom: 2mm;
  }}

  .sig-name {{
    font-size: 9.5px;
    font-weight: 600;
    color: var(--navy);
  }}

  .sig-title {{
    font-size: 8.5px;
    color: var(--muted);
    margin-top: 1mm;
  }}

  /* ── FOOTER ───────────────────────────────────── */
  .footer-rule {{
    height: 3px;
    background: linear-gradient(to right, var(--navy) 0%, var(--gold) 40%, var(--gold2) 60%, var(--navy) 100%);
    margin-top: auto;
  }}

  .footer {{
    background: var(--navy);
    padding: 6mm 14mm 5mm 14mm;
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 10mm;
    align-items: start;
  }}

  .footer-col {{
    display: flex;
    flex-direction: column;
    gap: 3px;
  }}

  .footer-col-title {{
    font-size: 6.5px;
    font-weight: 600;
    color: var(--gold);
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-bottom: 4px;
    padding-bottom: 3px;
    border-bottom: 1px solid rgba(193,154,75,0.3);
  }}

  .footer-col-line {{
    font-size: 8px;
    color: rgba(255,255,255,0.70);
    line-height: 1.6;
    font-weight: 300;
  }}

  .footer-col-line strong {{
    color: white;
    font-weight: 500;
  }}

  .footer-col-line a {{
    color: rgba(255,255,255,0.70);
    text-decoration: none;
  }}

  .footer-bottom {{
    background: rgba(0,0,0,0.25);
    padding: 3mm 14mm;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}

  .footer-bottom-text {{
    font-size: 6.5px;
    color: rgba(255,255,255,0.35);
    letter-spacing: 0.5px;
  }}

  .footer-gold-mark {{
    font-size: 6.5px;
    color: rgba(193,154,75,0.5);
    letter-spacing: 1px;
  }}
</style>
</head>
<body>
<div class="page">

  <!-- ═══════════ HEADER ═══════════ -->
  <header class="header">
    <div class="logo-box">
      <img src="{logo_src}" alt="Honne Hausverwaltung Logo"/>
    </div>

    <div class="header-divider"></div>

    <div class="firm-info">
      <div class="firm-name">Honne Hausverwaltung</div>
      <div class="firm-tagline">Ihr Immobilienpartner in Hamburg</div>

      <div class="contact-row">
        <span class="dot"></span>
        <span>Uwe Honne · Geschäftsführer</span>
      </div>
      <div class="contact-row">
        <span class="dot"></span>
        <span>Poppenbütteler Bogen 92, 22399 Hamburg</span>
      </div>
      <div class="contact-row">
        <span class="dot"></span>
        <span>+49 40 000 000 00</span>
        <span style="color:rgba(255,255,255,0.3)">·</span>
        <span>uwe@honnehausverwaltung.de</span>
        <span style="color:rgba(255,255,255,0.3)">·</span>
        <span>honnehausverwaltung.de</span>
      </div>
    </div>
  </header>

  <!-- gradient rule -->
  <div class="header-rule"></div>

  <!-- ═══════════ ADDRESS WINDOW + DATE ═══════════ -->
  <div class="addr-strip">
    <div class="addr-window">
      <div class="return-addr">Honne Hausverwaltung · Poppenbütteler Bogen 92 · 22399 Hamburg</div>
      <div class="recipient">
        Empfänger<br/>
        Straße Nr.<br/>
        PLZ Ort
      </div>
    </div>
    <div class="date-ref">
      <div class="label">Datum</div>
      <div>Hamburg, den _______________</div>
      <br/>
      <div class="label">Aktenzeichen</div>
      <div>_______________</div>
    </div>
  </div>

  <div class="sub-rule"></div>

  <!-- ═══════════ CONTENT ═══════════ -->
  <div class="content">
    <div class="subject-line">Betreff: &nbsp;&nbsp;_______________________________________________</div>

    <div class="salutation">Sehr geehrte Damen und Herren,</div>

    <div class="body-text">
      <p>
        &nbsp;
      </p>
      <p>&nbsp;</p>
      <p>&nbsp;</p>
      <p>&nbsp;</p>
      <p>&nbsp;</p>
      <p>&nbsp;</p>
      <p>&nbsp;</p>
      <p>&nbsp;</p>
      <p>&nbsp;</p>
      <p>&nbsp;</p>
    </div>

    <div style="font-size:10px; color:var(--text); margin-top: 6mm;">
      Mit freundlichen Grüßen
    </div>
  </div>

  <!-- ═══════════ SIGNATURE ═══════════ -->
  <div class="signature-area">
    <div class="sig-line"></div>
    <div class="sig-name">Uwe Honne</div>
    <div class="sig-title">Geschäftsführer · Honne Hausverwaltung</div>
  </div>

  <!-- ═══════════ FOOTER ═══════════ -->
  <div class="footer-rule"></div>

  <footer class="footer">
    <div class="footer-col">
      <div class="footer-col-title">Adresse</div>
      <div class="footer-col-line"><strong>Honne Hausverwaltung</strong></div>
      <div class="footer-col-line">Poppenbütteler Bogen 92</div>
      <div class="footer-col-line">22399 Hamburg</div>
    </div>
    <div class="footer-col">
      <div class="footer-col-title">Kontakt</div>
      <div class="footer-col-line">Tel: <strong>+49 40 000 000 00</strong></div>
      <div class="footer-col-line">E-Mail: <a href="mailto:uwe@honnehausverwaltung.de">uwe@honnehausverwaltung.de</a></div>
    </div>
    <div class="footer-col">
      <div class="footer-col-title">Online</div>
      <div class="footer-col-line"><a href="https://honnehausverwaltung.de">honnehausverwaltung.de</a></div>
      <div class="footer-col-line" style="margin-top:4px; font-size:7px; color:rgba(255,255,255,0.35);">
        Professionelle Verwaltung<br/>Ihrer Immobilie
      </div>
    </div>
  </footer>

  <div class="footer-bottom">
    <span class="footer-bottom-text">Honne Hausverwaltung · Poppenbütteler Bogen 92 · 22399 Hamburg · Deutschland</span>
    <span class="footer-gold-mark">✦ HAMBURG</span>
  </div>

</div>
</body>
</html>
"""

# ── Generate PDF ────────────────────────────────────────────────────────────
print("Generating PDF...")
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.set_content(HTML, wait_until='networkidle')
    page.wait_for_timeout(3000)   # let fonts settle

    page.pdf(
        path=str(PDF_OUT),
        format="A4",
        print_background=True,
        margin={"top": "0", "bottom": "0", "left": "0", "right": "0"},
    )

    # Also grab a PNG screenshot for preview
    page.set_viewport_size({"width": 794, "height": 1123})  # ~A4 at 96dpi
    page.screenshot(path=str(PNG_OUT), full_page=True)

    browser.close()

print(f"✅  PDF  → {PDF_OUT}")
print(f"✅  PNG  → {PNG_OUT}")
print("Done.")
