#!/usr/bin/env python3
"""
Visitenkarten Generator v4 - Honne Hausverwaltung
Vorder- und Rückseite, 85×55mm, heller Hintergrund, Gold-Akzente
"""

import base64
import subprocess
from pathlib import Path
from playwright.sync_api import sync_playwright

# Paths
BASE_DIR = Path("/Users/felix/.openclaw/workspace/honne-hausverwaltung")
LOGO_PATH = BASE_DIR / "assets/logo/honne_logo_real_512.png"
OUTPUT_DIR = BASE_DIR / "print"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Encode logo as base64
with open(LOGO_PATH, "rb") as f:
    logo_b64 = base64.b64encode(f.read()).decode("utf-8")
logo_data_uri = f"data:image/png;base64,{logo_b64}"

# ─── VORDERSEITE HTML ────────────────────────────────────────────────────────
html_vorderseite = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Inter:wght@300;400;500;600&display=swap');

  * {{ margin: 0; padding: 0; box-sizing: border-box; }}

  html, body {{
    width: 85mm;
    height: 55mm;
    overflow: hidden;
    font-family: 'Inter', 'Helvetica Neue', Arial, sans-serif;
  }}

  .card {{
    width: 85mm;
    height: 55mm;
    background: #F8F6F2;
    position: relative;
    display: flex;
    flex-direction: row;
    overflow: hidden;
  }}

  /* Left navy accent strip */
  .left-strip {{
    width: 3.5mm;
    background: #1B2A4A;
    flex-shrink: 0;
    position: relative;
  }}

  .left-strip::after {{
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    height: 8mm;
    background: #C19A4B;
  }}

  /* Main content area */
  .content {{
    flex: 1;
    padding: 5mm 5mm 4.5mm 4.5mm;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}

  /* Top section: name + title */
  .top {{
    display: flex;
    flex-direction: column;
    gap: 0.5mm;
  }}

  .name {{
    font-family: 'Playfair Display', Georgia, serif;
    font-size: 14pt;
    font-weight: 700;
    color: #1B2A4A;
    letter-spacing: 0.3px;
    line-height: 1.1;
  }}

  .title-row {{
    display: flex;
    align-items: center;
    gap: 2.5mm;
    margin-top: 0.8mm;
  }}

  .gold-dot {{
    width: 1.5mm;
    height: 1.5mm;
    background: #C19A4B;
    border-radius: 50%;
    flex-shrink: 0;
  }}

  .title {{
    font-size: 7.5pt;
    font-weight: 500;
    color: #C19A4B;
    letter-spacing: 1.2px;
    text-transform: uppercase;
  }}

  /* Gold divider line */
  .divider {{
    height: 0.4mm;
    background: linear-gradient(to right, #C19A4B, #C19A4B88, transparent);
    margin: 3mm 0;
    width: 60%;
  }}

  /* Company name */
  .company {{
    font-size: 7pt;
    font-weight: 600;
    color: #1B2A4A;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 3mm;
  }}

  /* Contact info */
  .contacts {{
    display: flex;
    flex-direction: column;
    gap: 1.2mm;
  }}

  .contact-item {{
    display: flex;
    align-items: center;
    gap: 2mm;
  }}

  .contact-icon {{
    width: 3mm;
    font-size: 6pt;
    color: #C19A4B;
    text-align: center;
    flex-shrink: 0;
  }}

  .contact-text {{
    font-size: 6.5pt;
    color: #1B2A4A;
    font-weight: 400;
    letter-spacing: 0.2px;
  }}

  /* Right side with logo */
  .right-panel {{
    width: 24mm;
    background: white;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 4mm 3mm;
    border-left: 0.3mm solid #E8E4DC;
    flex-shrink: 0;
  }}

  .logo-img {{
    width: 17mm;
    height: 17mm;
    object-fit: contain;
  }}

  /* Bottom tagline strip */
  .bottom-strip {{
    position: absolute;
    bottom: 0;
    left: 3.5mm;
    right: 0;
    height: 6mm;
    background: #1B2A4A;
    display: flex;
    align-items: center;
    padding: 0 4.5mm;
  }}

  .tagline {{
    font-size: 5.5pt;
    color: #C19A4B;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    font-weight: 500;
  }}
</style>
</head>
<body>
<div class="card">
  <div class="left-strip"></div>

  <div class="content">
    <div>
      <div class="top">
        <div class="name">Uwe Honne</div>
        <div class="title-row">
          <div class="gold-dot"></div>
          <div class="title">Geschäftsführer</div>
        </div>
      </div>
      <div class="divider"></div>
      <div class="company">Honne Hausverwaltung</div>

      <div class="contacts">
        <div class="contact-item">
          <div class="contact-icon">☎</div>
          <div class="contact-text">+49 40 000 000 00</div>
        </div>
        <div class="contact-item">
          <div class="contact-icon">✉</div>
          <div class="contact-text">uwe@honnehausverwaltung.de</div>
        </div>
        <div class="contact-item">
          <div class="contact-icon">🌐</div>
          <div class="contact-text">honnehausverwaltung.de</div>
        </div>
      </div>
    </div>
  </div>

  <div class="right-panel">
    <img class="logo-img" src="{logo_data_uri}" alt="Honne Logo">
  </div>

  <div class="bottom-strip">
    <span class="tagline">Persönlich · Zuverlässig · Mit Herz</span>
  </div>
</div>
</body>
</html>"""

# ─── RÜCKSEITE HTML ──────────────────────────────────────────────────────────
html_rueckseite = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Inter:wght@300;400;500;600&display=swap');

  * {{ margin: 0; padding: 0; box-sizing: border-box; }}

  html, body {{
    width: 85mm;
    height: 55mm;
    overflow: hidden;
    font-family: 'Inter', 'Helvetica Neue', Arial, sans-serif;
  }}

  .card {{
    width: 85mm;
    height: 55mm;
    background: #F8F6F2;
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
  }}

  /* Top gold accent bar */
  .top-bar {{
    width: 100%;
    height: 1.5mm;
    background: linear-gradient(to right, #1B2A4A 0%, #1B2A4A 40%, #C19A4B 40%, #C19A4B 60%, #1B2A4A 60%, #1B2A4A 100%);
    flex-shrink: 0;
  }}

  /* Main center content */
  .center-content {{
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 2mm 6mm 1mm;
    width: 100%;
  }}

  /* Logo area - transparent, no background box */
  .logo-container {{
    background: transparent;
    padding: 2mm 3mm;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 3mm;
  }}

  .logo-img {{
    height: 18mm;
    width: auto;
    object-fit: contain;
    display: block;
  }}

  /* Tagline */
  .tagline {{
    font-size: 7pt;
    color: #C19A4B;
    letter-spacing: 2px;
    text-transform: uppercase;
    font-weight: 500;
    text-align: center;
    margin-bottom: 3mm;
  }}

  /* Gold line under tagline */
  .gold-line {{
    width: 20mm;
    height: 0.4mm;
    background: #C19A4B;
    margin: 0 auto 3.5mm;
    opacity: 0.6;
  }}

  /* Services grid */
  .services {{
    display: flex;
    gap: 2.5mm;
    align-items: center;
    justify-content: center;
    flex-wrap: wrap;
  }}

  .service-item {{
    display: flex;
    align-items: center;
    gap: 1.2mm;
  }}

  .service-dot {{
    width: 1mm;
    height: 1mm;
    background: #C19A4B;
    border-radius: 50%;
    flex-shrink: 0;
  }}

  .service-text {{
    font-size: 5.8pt;
    color: #1B2A4A;
    font-weight: 500;
    letter-spacing: 0.8px;
    text-transform: uppercase;
    white-space: nowrap;
  }}

  .service-sep {{
    color: #C19A4B88;
    font-size: 6pt;
  }}

  /* Bottom navy bar */
  .bottom-bar {{
    width: 100%;
    height: 5mm;
    background: #1B2A4A;
    flex-shrink: 0;
    display: flex;
    align-items: center;
    justify-content: center;
  }}

  .bottom-text {{
    font-size: 5.5pt;
    color: rgba(193,154,75,0.8);
    letter-spacing: 2px;
    text-transform: uppercase;
    font-weight: 400;
  }}
</style>
</head>
<body>
<div class="card">
  <div class="top-bar"></div>

  <div class="center-content">
    <div class="logo-container">
      <img class="logo-img" src="{logo_data_uri}" alt="Honne Hausverwaltung">
    </div>

    <div class="tagline">Persönlich · Zuverlässig · Mit Herz</div>
    <div class="gold-line"></div>

    <div class="services">
      <div class="service-item">
        <div class="service-dot"></div>
        <span class="service-text">WEG-Verwaltung</span>
      </div>
      <span class="service-sep">|</span>
      <div class="service-item">
        <div class="service-dot"></div>
        <span class="service-text">Buchhaltung</span>
      </div>
      <span class="service-sep">|</span>
      <div class="service-item">
        <div class="service-dot"></div>
        <span class="service-text">Instandhaltung</span>
      </div>
      <span class="service-sep">|</span>
      <div class="service-item">
        <div class="service-dot"></div>
        <span class="service-text">Hamburg</span>
      </div>
    </div>
  </div>

  <div class="bottom-bar">
    <span class="bottom-text">honnehausverwaltung.de</span>
  </div>
</div>
</body>
</html>"""

# ─── PDF GENERATION ──────────────────────────────────────────────────────────
def generate_pdf(html_content: str, output_path: Path, label: str):
    print(f"Generating {label}...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 323, "height": 208})  # ~85mm x 55mm at 96dpi
        page.set_content(html_content, wait_until='networkidle')
        page.wait_for_timeout(2000)
        page.pdf(
            path=str(output_path),
            width="85mm",
            height="55mm",
            print_background=True,
            margin={"top": "0mm", "bottom": "0mm", "left": "0mm", "right": "0mm"}
        )
        browser.close()
    print(f"  ✓ Saved: {output_path}")


def generate_preview_png(pdf_path: Path, output_path: Path, label: str):
    print(f"Generating preview PNG for {label}...")
    result = subprocess.run(
        ["sips", "-s", "format", "png",
         "--resampleWidth", "850",
         str(pdf_path),
         "--out", str(output_path)],
        capture_output=True, text=True
    )
    if result.returncode == 0:
        print(f"  ✓ Preview: {output_path}")
    else:
        print(f"  ⚠ sips error: {result.stderr}")
        # Try alternative: use Playwright screenshot instead
        print(f"  Trying Playwright screenshot as fallback...")
        html_content = None
        if "vorderseite" in str(pdf_path):
            html_content = html_vorderseite
        else:
            html_content = html_rueckseite
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page(viewport={"width": 850, "height": 550})
            page.set_content(html_content, wait_until='networkidle')
            page.wait_for_timeout(1500)
            page.screenshot(path=str(output_path), clip={"x": 0, "y": 0, "width": 850, "height": 550})
            browser.close()
        print(f"  ✓ Preview (screenshot): {output_path}")


# Main execution
pdf_vorder = OUTPUT_DIR / "visitenkarte_vorderseite_v4.pdf"
pdf_rueck = OUTPUT_DIR / "visitenkarte_rueckseite_v4.pdf"
png_vorder = OUTPUT_DIR / "visitenkarte_vorderseite_v4_preview.png"
png_rueck = OUTPUT_DIR / "visitenkarte_rueckseite_v4_preview.png"

generate_pdf(html_vorderseite, pdf_vorder, "Vorderseite")
generate_pdf(html_rueckseite, pdf_rueck, "Rückseite")
generate_preview_png(pdf_vorder, png_vorder, "Vorderseite")
generate_preview_png(pdf_rueck, png_rueck, "Rückseite")

print("\n✅ Alle Visitenkarten generiert!")
print(f"   PDF Vorderseite: {pdf_vorder}")
print(f"   PDF Rückseite:   {pdf_rueck}")
print(f"   PNG Vorderseite: {png_vorder}")
print(f"   PNG Rückseite:   {png_rueck}")
