#!/usr/bin/env python3
"""
Honne Hausverwaltung — Print Materials Builder
Erzeugt druckfertige PDFs: Visitenkarte (V+R) + Briefbogen
"""

from playwright.sync_api import sync_playwright
from pathlib import Path
import base64

BASE = Path(__file__).parent.parent
LOGO_PNG = BASE / "assets/logo/honne_logo_1024_transparent.png"
LOGO_DARK = BASE / "assets/logo/honne_logo_1024.png"
OUT = Path(__file__).parent

# Logo als base64 einbetten
logo_b64_white = base64.b64encode(LOGO_PNG.read_bytes()).decode()
logo_b64_dark  = base64.b64encode(LOGO_DARK.read_bytes()).decode()

# ── FARBEN (aus Website) ─────────────────────────────────────────────────────
NAVY   = "#1B2A4A"
GOLD   = "#C19A4B"
WHITE  = "#FFFFFF"
OFF    = "#F8F6F2"
MUTED  = "#5C5C5C"

# ── VISITENKARTE VORDERSEITE ─────────────────────────────────────────────────
VCARD_FRONT = f"""<!DOCTYPE html><html><head><meta charset="UTF-8">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:85mm;height:55mm;background:{NAVY};font-family:Georgia,serif;overflow:hidden;position:relative}}
.bg-pattern{{position:absolute;inset:0;opacity:0.04;background-image:repeating-linear-gradient(45deg,#fff 0,#fff 1px,transparent 0,transparent 50%);background-size:8px 8px}}
.gold-bar{{position:absolute;left:0;top:0;bottom:0;width:3px;background:{GOLD}}}
.gold-line{{position:absolute;bottom:12mm;left:8mm;right:8mm;height:0.5px;background:{GOLD};opacity:0.4}}
.logo{{position:absolute;top:6mm;right:7mm;width:18mm;opacity:0.95}}
.name{{position:absolute;top:8mm;left:8mm;font-size:15pt;color:{WHITE};font-weight:normal;letter-spacing:0.5px;line-height:1.2}}
.title{{position:absolute;top:18mm;left:8mm;font-size:6.5pt;color:{GOLD};letter-spacing:3px;text-transform:uppercase;font-family:Arial,sans-serif;font-weight:600}}
.divider{{position:absolute;top:23mm;left:8mm;width:30px;height:1px;background:{GOLD}}}
.company{{position:absolute;top:25.5mm;left:8mm;font-size:8pt;color:rgba(255,255,255,0.7);font-family:Arial,sans-serif;letter-spacing:0.3px}}
.contact{{position:absolute;bottom:5mm;left:8mm;font-size:6.5pt;color:rgba(255,255,255,0.65);font-family:Arial,sans-serif;line-height:1.8}}
.web{{position:absolute;bottom:5mm;right:8mm;font-size:6pt;color:{GOLD};font-family:Arial,sans-serif;letter-spacing:0.5px}}
</style></head><body>
<div class="bg-pattern"></div>
<div class="gold-bar"></div>
<img class="logo" src="data:image/png;base64,{logo_b64_white}">
<div class="name">Uwe Honne</div>
<div class="title">Geschäftsführer</div>
<div class="divider"></div>
<div class="company">Honne Hausverwaltung</div>
<div class="gold-line"></div>
<div class="contact">
  📞 &nbsp;+49 40 000 000 00<br>
  ✉ &nbsp;uwe@honnehausverwaltung.de
</div>
<div class="web">honnehausverwaltung.de</div>
</body></html>"""

# ── VISITENKARTE RÜCKSEITE ───────────────────────────────────────────────────
VCARD_BACK = f"""<!DOCTYPE html><html><head><meta charset="UTF-8">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:85mm;height:55mm;background:{OFF};font-family:Arial,sans-serif;overflow:hidden;position:relative}}
.top-bar{{position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg,{NAVY},{GOLD})}}
.logo-wrap{{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);text-align:center}}
.logo-wrap img{{width:28mm;margin:0 auto 2mm}}
.tagline{{font-size:6pt;letter-spacing:2.5px;text-transform:uppercase;color:{GOLD};font-weight:600;text-align:center;white-space:nowrap}}
.services{{position:absolute;bottom:7mm;left:0;right:0;display:flex;justify-content:center;gap:5mm}}
.svc{{font-size:5.5pt;color:{MUTED};letter-spacing:1px;text-transform:uppercase;text-align:center;border-left:1px solid {GOLD};padding-left:5mm}}
.svc:first-child{{border-left:none;padding-left:0}}
.bottom-bar{{position:absolute;bottom:0;left:0;right:0;height:2px;background:{GOLD};opacity:0.3}}
</style></head><body>
<div class="top-bar"></div>
<div class="logo-wrap">
  <img src="data:image/png;base64,{logo_b64_dark}">
  <div class="tagline">Persönlich · Zuverlässig · Mit Herz</div>
</div>
<div class="services">
  <div class="svc">WEG-Verwaltung</div>
  <div class="svc">Buchhaltung</div>
  <div class="svc">Instandhaltung</div>
  <div class="svc">Hamburg</div>
</div>
<div class="bottom-bar"></div>
</body></html>"""

# ── BRIEFBOGEN DIN A4 ────────────────────────────────────────────────────────
LETTERHEAD = f"""<!DOCTYPE html><html><head><meta charset="UTF-8">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
@page{{size:A4;margin:0}}
body{{width:210mm;height:297mm;background:{WHITE};font-family:Arial,sans-serif;position:relative;overflow:hidden}}

/* HEADER */
.header{{position:absolute;top:0;left:0;right:0;height:42mm;background:{NAVY};padding:0}}
.header-inner{{padding:7mm 20mm 0;display:flex;align-items:flex-start;justify-content:space-between}}
.logo-area img{{width:35mm}}
.header-contact{{text-align:right;padding-top:2mm}}
.header-contact p{{font-size:7.5pt;color:rgba(255,255,255,0.75);line-height:1.9}}
.header-contact .web{{color:{GOLD};font-size:7pt;letter-spacing:0.5px}}
.gold-stripe{{position:absolute;top:42mm;left:0;right:0;height:2.5px;background:linear-gradient(90deg,{NAVY} 0%,{GOLD} 40%,{GOLD} 100%)}}

/* ABSENDER-ZEILE */
.sender-line{{position:absolute;top:48mm;left:20mm;font-size:6.5pt;color:{MUTED};border-bottom:0.5px solid #ddd;padding-bottom:1mm;width:85mm;letter-spacing:0.3px}}

/* EMPFÄNGER */
.recipient{{position:absolute;top:53mm;left:20mm;font-size:9.5pt;color:#222;line-height:1.7}}

/* DATUM & ORT */
.date{{position:absolute;top:53mm;right:20mm;font-size:9pt;color:{MUTED};text-align:right}}

/* BETREFF */
.subject{{position:absolute;top:85mm;left:20mm;right:20mm}}
.subject-label{{font-size:9pt;font-weight:bold;color:{NAVY};font-family:Georgia,serif}}

/* INHALTSBEREICH */
.content{{position:absolute;top:97mm;left:20mm;right:20mm;font-size:9.5pt;color:#333;line-height:1.75}}
.content p{{margin-bottom:4mm}}
.salutation{{margin-bottom:6mm}}
.closing{{margin-top:8mm}}
.signature{{margin-top:16mm;border-top:0.5px solid #ddd;padding-top:3mm}}
.sig-name{{font-size:9pt;font-weight:bold;color:{NAVY};font-family:Georgia,serif}}
.sig-title{{font-size:7.5pt;color:{MUTED};margin-top:1mm}}

/* FOOTER */
.footer{{position:absolute;bottom:0;left:0;right:0;height:22mm;background:{OFF};border-top:1px solid #E0D9CE}}
.footer-inner{{padding:4mm 20mm;display:flex;justify-content:space-between;align-items:flex-start}}
.footer-col{{font-size:6.5pt;color:{MUTED};line-height:1.8}}
.footer-col strong{{color:{NAVY};font-size:6.5pt;letter-spacing:0.5px;text-transform:uppercase}}
.footer-divider{{width:0.5px;background:#ddd;align-self:stretch}}
.footer-gold{{font-size:6pt;color:{GOLD};text-align:center;padding-top:1mm;letter-spacing:1px}}
</style></head><body>

<div class="header">
  <div class="header-inner">
    <div class="logo-area">
      <img src="data:image/png;base64,{logo_b64_white}">
    </div>
    <div class="header-contact">
      <p>Uwe Honne · Geschäftsführer</p>
      <p>+49 40 000 000 00</p>
      <p>uwe@honnehausverwaltung.de</p>
      <p class="web">honnehausverwaltung.de</p>
    </div>
  </div>
</div>
<div class="gold-stripe"></div>

<div class="sender-line">Honne Hausverwaltung · Kupferteichweg 20 · 22399 Hamburg</div>

<div class="recipient">
  Max Mustermann<br>
  Musterstraße 1<br>
  20000 Hamburg
</div>

<div class="date">
  Hamburg, 23. Juni 2026
</div>

<div class="subject">
  <div class="subject-label">Betreff: [Ihre Betreffzeile hier]</div>
</div>

<div class="content">
  <p class="salutation">Sehr geehrte Damen und Herren,</p>
  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Hier steht Ihr individueller Brieftext. Die Vorlage ist bereit für Ihren persönlichen Inhalt.</p>
  <p>Bei Fragen stehe ich Ihnen jederzeit persönlich zur Verfügung. Als inhabergeführte Hausverwaltung legen wir größten Wert auf eine direkte und vertrauensvolle Kommunikation.</p>
  <p>Mit freundlichen Grüßen</p>
  <div class="closing">
    <div class="signature">
      <div class="sig-name">Uwe Honne</div>
      <div class="sig-title">Geschäftsführer · Honne Hausverwaltung</div>
    </div>
  </div>
</div>

<div class="footer">
  <div class="footer-inner">
    <div class="footer-col">
      <strong>Honne Hausverwaltung</strong><br>
      Uwe Honne · Geschäftsführer<br>
      Kupferteichweg 20 · 22399 Hamburg
    </div>
    <div class="footer-divider"></div>
    <div class="footer-col">
      <strong>Kontakt</strong><br>
      Tel: +49 40 000 000 00<br>
      uwe@honnehausverwaltung.de
    </div>
    <div class="footer-divider"></div>
    <div class="footer-col">
      <strong>Web</strong><br>
      honnehausverwaltung.de<br>
      <span style="color:{GOLD}">WEG-Verwaltung Hamburg</span>
    </div>
  </div>
</div>

</body></html>"""


def build():
    OUT.mkdir(exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        # ── Visitenkarte Vorderseite ──────────────────────────────────────
        print("Building: Visitenkarte Vorderseite...")
        page = browser.new_page()
        page.set_viewport_size({"width": 322, "height": 208})  # 85x55mm @ 96dpi
        page.set_content(VCARD_FRONT, wait_until="networkidle")
        page.wait_for_timeout(500)
        page.pdf(
            path=str(OUT / "visitenkarte_vorderseite.pdf"),
            width="85mm", height="55mm",
            print_background=True,
            margin={"top":"0","bottom":"0","left":"0","right":"0"}
        )
        print("  ✅ visitenkarte_vorderseite.pdf")

        # ── Visitenkarte Rückseite ────────────────────────────────────────
        print("Building: Visitenkarte Rückseite...")
        page.set_content(VCARD_BACK, wait_until="networkidle")
        page.wait_for_timeout(500)
        page.pdf(
            path=str(OUT / "visitenkarte_rueckseite.pdf"),
            width="85mm", height="55mm",
            print_background=True,
            margin={"top":"0","bottom":"0","left":"0","right":"0"}
        )
        print("  ✅ visitenkarte_rueckseite.pdf")

        # ── Briefbogen A4 ────────────────────────────────────────────────
        print("Building: Briefbogen DIN A4...")
        page.set_viewport_size({"width": 794, "height": 1123})
        page.set_content(LETTERHEAD, wait_until="networkidle")
        page.wait_for_timeout(800)
        page.pdf(
            path=str(OUT / "briefbogen_a4.pdf"),
            format="A4",
            print_background=True,
            margin={"top":"0","bottom":"0","left":"0","right":"0"}
        )
        print("  ✅ briefbogen_a4.pdf")

        browser.close()
    print("\n✅ Alle Print-Materialien erstellt in:", OUT)


if __name__ == "__main__":
    build()
