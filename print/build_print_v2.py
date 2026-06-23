#!/usr/bin/env python3
"""
Honne Hausverwaltung — Print Materials Builder v2
Verwendet NUR das originale Logo (honne_logo_real_512.png)
"""

from playwright.sync_api import sync_playwright
from pathlib import Path
import base64

BASE = Path(__file__).parent.parent
LOGO = BASE / "assets/logo/honne_logo_real_512.png"   # Das echte Original
OUT  = Path(__file__).parent

logo_b64 = base64.b64encode(LOGO.read_bytes()).decode()

NAVY  = "#1B2A4A"
GOLD  = "#C19A4B"
WHITE = "#FFFFFF"
OFF   = "#F8F6F2"
MUTED = "#5C5C5C"

# ── VISITENKARTE VORDERSEITE ─────────────────────────────────────────────────
VCARD_FRONT = f"""<!DOCTYPE html><html><head><meta charset="UTF-8">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:85mm;height:55mm;background:{NAVY};overflow:hidden;position:relative;font-family:Arial,sans-serif}}
/* Subtiles Muster */
.bg{{position:absolute;inset:0;background:repeating-linear-gradient(45deg,rgba(255,255,255,.015) 0,rgba(255,255,255,.015) 1px,transparent 1px,transparent 8px)}}
/* Goldener Rand links */
.rail{{position:absolute;left:0;top:0;bottom:0;width:3px;background:linear-gradient(180deg,{GOLD},{NAVY})}}
/* Logo rechts oben */
.logo{{position:absolute;top:4mm;right:5mm;width:20mm;height:20mm;object-fit:contain}}
/* Name */
.name{{position:absolute;top:7mm;left:8mm;font-size:14pt;color:{WHITE};font-family:Georgia,serif;font-weight:normal;letter-spacing:.3px;line-height:1.2}}
/* Titel */
.role{{position:absolute;top:17.5mm;left:8mm;font-size:6pt;color:{GOLD};letter-spacing:3px;text-transform:uppercase;font-weight:700}}
/* Trennlinie */
.sep{{position:absolute;top:21.5mm;left:8mm;width:28mm;height:1px;background:{GOLD};opacity:.5}}
/* Firma */
.firm{{position:absolute;top:23.5mm;left:8mm;font-size:8pt;color:rgba(255,255,255,.65);letter-spacing:.2px}}
/* Kontakt unten */
.contact{{position:absolute;bottom:5.5mm;left:8mm;font-size:6.5pt;color:rgba(255,255,255,.7);line-height:2}}
/* Web rechts unten */
.web{{position:absolute;bottom:5.5mm;right:7mm;font-size:6pt;color:{GOLD};letter-spacing:.5px;text-align:right;line-height:2}}
/* Goldene Linie über Kontakt */
.footline{{position:absolute;bottom:12mm;left:8mm;right:8mm;height:.5px;background:{GOLD};opacity:.25}}
</style></head><body>
<div class="bg"></div>
<div class="rail"></div>
<img class="logo" src="data:image/png;base64,{logo_b64}">
<div class="name">Uwe Honne</div>
<div class="role">Geschäftsführer</div>
<div class="sep"></div>
<div class="firm">Honne Hausverwaltung</div>
<div class="footline"></div>
<div class="contact">
  +49 40 000 000 00<br>
  uwe@honnehausverwaltung.de
</div>
<div class="web">
  honnehausverwaltung.de<br>
  Hamburg
</div>
</body></html>"""

# ── VISITENKARTE RÜCKSEITE ───────────────────────────────────────────────────
VCARD_BACK = f"""<!DOCTYPE html><html><head><meta charset="UTF-8">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:85mm;height:55mm;background:{OFF};overflow:hidden;position:relative;font-family:Arial,sans-serif}}
.topbar{{position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg,{NAVY} 0%,{GOLD} 100%)}}
.center{{position:absolute;top:50%;left:50%;transform:translate(-50%,-52%);text-align:center}}
.center img{{width:26mm;margin:0 auto 2.5mm;display:block}}
.tagline{{font-size:5.5pt;letter-spacing:3px;text-transform:uppercase;color:{GOLD};font-weight:700}}
.services{{position:absolute;bottom:6mm;left:0;right:0;display:flex;justify-content:center;gap:0}}
.svc{{font-size:5.5pt;color:{MUTED};letter-spacing:.8px;text-transform:uppercase;padding:0 4mm;border-left:1px solid {GOLD}}}
.svc:first-child{{border-left:none}}
.botbar{{position:absolute;bottom:0;left:0;right:0;height:2px;background:{NAVY};opacity:.12}}
</style></head><body>
<div class="topbar"></div>
<div class="center">
  <img src="data:image/png;base64,{logo_b64}">
  <div class="tagline">Persönlich · Zuverlässig · Mit Herz</div>
</div>
<div class="services">
  <div class="svc">WEG-Verwaltung</div>
  <div class="svc">Buchhaltung</div>
  <div class="svc">Instandhaltung</div>
  <div class="svc">Hamburg</div>
</div>
<div class="botbar"></div>
</body></html>"""

# ── BRIEFBOGEN DIN A4 ────────────────────────────────────────────────────────
LETTERHEAD = f"""<!DOCTYPE html><html><head><meta charset="UTF-8">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:210mm;height:297mm;background:{WHITE};font-family:Arial,sans-serif;position:relative;overflow:hidden}}

.header{{position:absolute;top:0;left:0;right:0;height:40mm;background:{NAVY}}}
.header-inner{{display:flex;align-items:center;justify-content:space-between;padding:6mm 18mm 0}}
.logo-wrap img{{width:38mm;height:38mm;object-fit:contain}}
.header-right{{text-align:right}}
.header-right .firm{{font-family:Georgia,serif;font-size:13pt;color:{WHITE};letter-spacing:.5px;line-height:1.2}}
.header-right .sub{{font-size:7pt;color:{GOLD};letter-spacing:3px;text-transform:uppercase;margin-top:2mm}}
.header-right .contact{{font-size:7pt;color:rgba(255,255,255,.7);margin-top:3mm;line-height:1.9}}

.goldbar{{position:absolute;top:40mm;left:0;right:0;height:3px;background:linear-gradient(90deg,{NAVY},{GOLD})}}

.sender-line{{position:absolute;top:47mm;left:20mm;font-size:6.5pt;color:#999;border-bottom:.5px solid #e0e0e0;padding-bottom:1mm;width:80mm}}

.recipient{{position:absolute;top:52mm;left:20mm;font-size:9.5pt;color:#222;line-height:1.8}}

.date{{position:absolute;top:52mm;right:20mm;font-size:9pt;color:{MUTED};text-align:right}}

.subject{{position:absolute;top:82mm;left:20mm;right:20mm;font-size:10pt;font-weight:bold;color:{NAVY};font-family:Georgia,serif}}

.body{{position:absolute;top:93mm;left:20mm;right:20mm;font-size:9.5pt;color:#333;line-height:1.8}}
.body p{{margin-bottom:4.5mm}}
.closing{{margin-top:10mm}}
.sig-line{{margin-top:16mm;border-top:.5px solid #ddd;padding-top:3mm}}
.sig-name{{font-size:10pt;font-weight:bold;color:{NAVY};font-family:Georgia,serif}}
.sig-role{{font-size:7.5pt;color:{MUTED};margin-top:1mm}}

.footer{{position:absolute;bottom:0;left:0;right:0;height:20mm;background:{OFF};border-top:1px solid #E0D9CE}}
.footer-inner{{display:flex;justify-content:space-between;padding:4.5mm 20mm}}
.fcol{{font-size:6pt;color:{MUTED};line-height:1.9}}
.fcol strong{{display:block;font-size:6pt;color:{NAVY};text-transform:uppercase;letter-spacing:.8px;margin-bottom:.5mm}}
.fdiv{{width:.5px;background:#ddd}}
</style></head><body>

<div class="header">
  <div class="header-inner">
    <div class="logo-wrap"><img src="data:image/png;base64,{logo_b64}"></div>
    <div class="header-right">
      <div class="firm">Honne Hausverwaltung</div>
      <div class="sub">WEG-Verwaltung Hamburg</div>
      <div class="contact">
        +49 40 000 000 00<br>
        uwe@honnehausverwaltung.de<br>
        honnehausverwaltung.de
      </div>
    </div>
  </div>
</div>
<div class="goldbar"></div>

<div class="sender-line">Honne Hausverwaltung · Kupferteichweg 20 · 22399 Hamburg</div>

<div class="recipient">
  Max Mustermann<br>
  Musterstraße 1<br>
  20000 Hamburg
</div>

<div class="date">Hamburg, 23. Juni 2026</div>

<div class="subject">Betreff: [Ihre Betreffzeile hier eintragen]</div>

<div class="body">
  <p>Sehr geehrte Damen und Herren,</p>
  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Hier steht Ihr individueller Brieftext. Diese Vorlage ist bereit für Ihren persönlichen Inhalt und kann direkt weiterverwendet werden.</p>
  <p>Bei Fragen stehe ich Ihnen jederzeit persönlich zur Verfügung. Als inhabergeführte Hausverwaltung legen wir größten Wert auf direkte und vertrauensvolle Kommunikation mit unseren Eigentümern.</p>
  <div class="closing">Mit freundlichen Grüßen</div>
  <div class="sig-line">
    <div class="sig-name">Uwe Honne</div>
    <div class="sig-role">Geschäftsführer · Honne Hausverwaltung</div>
  </div>
</div>

<div class="footer">
  <div class="footer-inner">
    <div class="fcol">
      <strong>Adresse</strong>
      Honne Hausverwaltung<br>
      Kupferteichweg 20<br>
      22399 Hamburg
    </div>
    <div class="fdiv"></div>
    <div class="fcol">
      <strong>Kontakt</strong>
      Tel: +49 40 000 000 00<br>
      uwe@honnehausverwaltung.de<br>
      honnehausverwaltung.de
    </div>
    <div class="fdiv"></div>
    <div class="fcol">
      <strong>Leistungen</strong>
      WEG-Verwaltung<br>
      Buchhaltung &amp; Abrechnung<br>
      Instandhaltung
    </div>
  </div>
</div>

</body></html>"""


def build():
    OUT.mkdir(exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        print("📇 Visitenkarte Vorderseite...")
        page.set_viewport_size({"width": 322, "height": 208})
        page.set_content(VCARD_FRONT, wait_until="networkidle")
        page.wait_for_timeout(600)
        page.pdf(path=str(OUT / "visitenkarte_vorderseite.pdf"),
                 width="85mm", height="55mm", print_background=True,
                 margin={"top":"0","bottom":"0","left":"0","right":"0"})
        print("  ✅ visitenkarte_vorderseite.pdf")

        print("📇 Visitenkarte Rückseite...")
        page.set_content(VCARD_BACK, wait_until="networkidle")
        page.wait_for_timeout(600)
        page.pdf(path=str(OUT / "visitenkarte_rueckseite.pdf"),
                 width="85mm", height="55mm", print_background=True,
                 margin={"top":"0","bottom":"0","left":"0","right":"0"})
        print("  ✅ visitenkarte_rueckseite.pdf")

        print("📄 Briefbogen A4...")
        page.set_viewport_size({"width": 794, "height": 1123})
        page.set_content(LETTERHEAD, wait_until="networkidle")
        page.wait_for_timeout(800)
        page.pdf(path=str(OUT / "briefbogen_a4.pdf"),
                 format="A4", print_background=True,
                 margin={"top":"0","bottom":"0","left":"0","right":"0"})
        print("  ✅ briefbogen_a4.pdf")

        browser.close()
    print("\n✅ Fertig! Alle PDFs in:", OUT)


if __name__ == "__main__":
    build()
