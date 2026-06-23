#!/usr/bin/env python3
"""
Honne Hausverwaltung — Print Materials Builder v3
Helles Design: Off-White Hintergrund, Navy Text, Gold Akzente
Logo kommt perfekt raus (kein Kontrast-Problem mehr)
"""

from playwright.sync_api import sync_playwright
from pathlib import Path
import base64

BASE = Path(__file__).parent.parent
LOGO = BASE / "assets/logo/honne_logo_real_512.png"
OUT  = Path(__file__).parent

logo_b64 = base64.b64encode(LOGO.read_bytes()).decode()

NAVY  = "#1B2A4A"
GOLD  = "#C19A4B"
WHITE = "#FFFFFF"
OFF   = "#F8F6F2"
LIGHT = "#EEE9E1"
MUTED = "#6B6B6B"
TEXT  = "#2C2C2C"

# ── VISITENKARTE VORDERSEITE (hell) ─────────────────────────────────────────
VCARD_FRONT = f"""<!DOCTYPE html><html><head><meta charset="UTF-8">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:85mm;height:55mm;background:{OFF};overflow:hidden;position:relative;font-family:Arial,sans-serif}}

/* Goldener Streifen oben */
.topbar{{position:absolute;top:0;left:0;right:0;height:2.5px;background:linear-gradient(90deg,{NAVY},{GOLD})}}

/* Navy Block links */
.left-block{{position:absolute;left:0;top:0;bottom:0;width:28mm;background:{NAVY};display:flex;align-items:center;justify-content:center}}
.left-block img{{width:22mm;height:22mm;object-fit:contain}}

/* Goldene Trennlinie */
.divider{{position:absolute;left:28mm;top:0;bottom:0;width:2px;background:{GOLD}}}

/* Rechte Seite */
.right{{position:absolute;left:32mm;top:0;bottom:0;right:0;padding:6mm 5mm 5mm 4mm;display:flex;flex-direction:column;justify-content:space-between}}

.name{{font-family:Georgia,serif;font-size:13pt;color:{NAVY};font-weight:normal;line-height:1.15;letter-spacing:.3px}}
.role{{font-size:5.5pt;color:{GOLD};letter-spacing:3px;text-transform:uppercase;font-weight:700;margin-top:1.5mm}}
.firm{{font-size:7.5pt;color:{MUTED};margin-top:1mm}}

.contact-block{{border-top:.5px solid #D4C9BB;padding-top:3mm}}
.contact-line{{font-size:6.5pt;color:{TEXT};line-height:1.9}}
.web{{font-size:6pt;color:{GOLD};letter-spacing:.5px;margin-top:.5mm}}

/* Goldener Streifen unten */
.botbar{{position:absolute;bottom:0;left:0;right:0;height:1.5px;background:{GOLD};opacity:.4}}
</style></head><body>
<div class="topbar"></div>
<div class="left-block">
  <img src="data:image/png;base64,{logo_b64}">
</div>
<div class="divider"></div>
<div class="right">
  <div>
    <div class="name">Uwe Honne</div>
    <div class="role">Geschäftsführer</div>
    <div class="firm">Honne Hausverwaltung</div>
  </div>
  <div class="contact-block">
    <div class="contact-line">
      +49 40 000 000 00<br>
      uwe@honnehausverwaltung.de
    </div>
    <div class="web">honnehausverwaltung.de</div>
  </div>
</div>
<div class="botbar"></div>
</body></html>"""

# ── VISITENKARTE RÜCKSEITE (hell) ────────────────────────────────────────────
VCARD_BACK = f"""<!DOCTYPE html><html><head><meta charset="UTF-8">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:85mm;height:55mm;background:{WHITE};overflow:hidden;position:relative;font-family:Arial,sans-serif}}
.topbar{{position:absolute;top:0;left:0;right:0;height:2.5px;background:linear-gradient(90deg,{NAVY},{GOLD})}}
.botbar{{position:absolute;bottom:0;left:0;right:0;height:2.5px;background:linear-gradient(90deg,{GOLD},{NAVY})}}

/* Zentriertes Logo */
.center{{position:absolute;top:50%;left:50%;transform:translate(-50%,-54%);text-align:center}}
.center img{{width:24mm;display:block;margin:0 auto 2mm}}
.tagline{{font-size:5.5pt;letter-spacing:2.5px;text-transform:uppercase;color:{NAVY};font-weight:600}}
.gold-line{{width:20mm;height:1px;background:{GOLD};margin:2mm auto}}

/* Services unten */
.services{{position:absolute;bottom:6mm;left:0;right:0;display:flex;justify-content:center}}
.svc{{font-size:5pt;color:{MUTED};letter-spacing:.8px;text-transform:uppercase;padding:0 3.5mm;border-left:.5px solid {GOLD}}}
.svc:first-child{{border-left:none}}
</style></head><body>
<div class="topbar"></div>
<div class="center">
  <img src="data:image/png;base64,{logo_b64}">
  <div class="gold-line"></div>
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

# ── BRIEFBOGEN DIN A4 (hell) ─────────────────────────────────────────────────
LETTERHEAD = f"""<!DOCTYPE html><html><head><meta charset="UTF-8">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:210mm;height:297mm;background:{WHITE};font-family:Arial,sans-serif;position:relative;overflow:hidden}}

/* HEADER: weißer Hintergrund, Logo links groß, Firma rechts */
.header{{position:absolute;top:0;left:0;right:0;height:38mm;background:{WHITE};border-bottom:none}}
.header-inner{{display:flex;align-items:center;justify-content:space-between;padding:5mm 18mm 0}}
.logo-area img{{width:36mm;height:36mm;object-fit:contain}}
.header-right{{text-align:right}}
.firm-name{{font-family:Georgia,serif;font-size:16pt;color:{NAVY};letter-spacing:.3px;line-height:1.1}}
.firm-sub{{font-size:6.5pt;color:{GOLD};letter-spacing:3px;text-transform:uppercase;margin-top:2mm;font-weight:700}}
.firm-contact{{font-size:7pt;color:{MUTED};margin-top:3mm;line-height:2}}

/* Doppelter Trennstreifen: Navy + Gold */
.bar-navy{{position:absolute;top:38mm;left:0;right:0;height:3px;background:{NAVY}}}
.bar-gold{{position:absolute;top:41mm;left:0;right:0;height:1.5px;background:{GOLD}}}

/* Absenderzeile */
.sender{{position:absolute;top:47mm;left:20mm;font-size:6.5pt;color:#aaa;border-bottom:.5px solid #e8e8e8;padding-bottom:1.5mm;width:85mm;letter-spacing:.2px}}

/* Empfänger */
.recipient{{position:absolute;top:53mm;left:20mm;font-size:9.5pt;color:{TEXT};line-height:1.85}}

/* Datum */
.date{{position:absolute;top:53mm;right:20mm;font-size:9pt;color:{MUTED};text-align:right}}

/* Betreff */
.subject{{position:absolute;top:82mm;left:20mm;right:20mm;font-size:10.5pt;font-weight:bold;color:{NAVY};font-family:Georgia,serif}}
.subject-line{{position:absolute;top:88mm;left:20mm;width:40mm;height:1.5px;background:{GOLD}}}

/* Brieftext */
.body{{position:absolute;top:96mm;left:20mm;right:20mm;font-size:9.5pt;color:#333;line-height:1.85}}
.body p{{margin-bottom:5mm}}
.closing{{margin-top:10mm}}
.sig-gap{{margin-top:16mm;border-top:.5px solid #ddd;padding-top:3mm}}
.sig-name{{font-size:10pt;font-weight:bold;color:{NAVY};font-family:Georgia,serif}}
.sig-role{{font-size:7.5pt;color:{MUTED};margin-top:1mm}}

/* Footer */
.footer{{position:absolute;bottom:0;left:0;right:0;height:22mm;background:{OFF};border-top:2px solid {NAVY}}}
.footer-gold{{position:absolute;bottom:22mm;left:0;right:0;height:1px;background:{GOLD}}}
.footer-inner{{display:flex;justify-content:space-between;align-items:flex-start;padding:4mm 18mm}}
.fcol{{font-size:6pt;color:{MUTED};line-height:2}}
.fcol strong{{display:block;font-size:5.5pt;color:{NAVY};text-transform:uppercase;letter-spacing:1px;margin-bottom:.5mm}}
.fdiv{{width:.5px;background:#ccc;align-self:stretch;margin:1mm 0}}
</style></head><body>

<div class="header">
  <div class="header-inner">
    <div class="logo-area"><img src="data:image/png;base64,{logo_b64}"></div>
    <div class="header-right">
      <div class="firm-name">Honne Hausverwaltung</div>
      <div class="firm-sub">WEG-Verwaltung Hamburg</div>
      <div class="firm-contact">
        Uwe Honne · Geschäftsführer<br>
        +49 40 000 000 00<br>
        uwe@honnehausverwaltung.de<br>
        honnehausverwaltung.de
      </div>
    </div>
  </div>
</div>
<div class="bar-navy"></div>
<div class="bar-gold"></div>

<div class="sender">Honne Hausverwaltung · Kupferteichweg 20 · 22399 Hamburg</div>

<div class="recipient">
  Max Mustermann<br>
  Musterstraße 1<br>
  20000 Hamburg
</div>
<div class="date">Hamburg, 23. Juni 2026</div>

<div class="subject">Betreff: [Ihre Betreffzeile hier]</div>
<div class="subject-line"></div>

<div class="body">
  <p>Sehr geehrte Damen und Herren,</p>
  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Hier steht Ihr individueller Brieftext. Diese Vorlage ist bereit für Ihren persönlichen Inhalt und kann direkt weiterverwendet werden.</p>
  <p>Bei Fragen stehe ich Ihnen jederzeit persönlich zur Verfügung. Als inhabergeführte Hausverwaltung legen wir größten Wert auf direkte und vertrauensvolle Kommunikation mit unseren Eigentümern.</p>
  <div class="closing">Mit freundlichen Grüßen</div>
  <div class="sig-gap">
    <div class="sig-name">Uwe Honne</div>
    <div class="sig-role">Geschäftsführer · Honne Hausverwaltung</div>
  </div>
</div>

<div class="footer-gold"></div>
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
      Instandhaltung &amp; Vergabe
    </div>
  </div>
</div>

</body></html>"""


def build():
    OUT.mkdir(exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        print("📇 Visitenkarte Vorderseite (hell)...")
        page.set_viewport_size({"width": 322, "height": 208})
        page.set_content(VCARD_FRONT, wait_until="networkidle")
        page.wait_for_timeout(600)
        page.pdf(path=str(OUT / "visitenkarte_vorderseite.pdf"),
                 width="85mm", height="55mm", print_background=True,
                 margin={"top":"0","bottom":"0","left":"0","right":"0"})
        print("  ✅ visitenkarte_vorderseite.pdf")

        print("📇 Visitenkarte Rückseite (hell)...")
        page.set_content(VCARD_BACK, wait_until="networkidle")
        page.wait_for_timeout(600)
        page.pdf(path=str(OUT / "visitenkarte_rueckseite.pdf"),
                 width="85mm", height="55mm", print_background=True,
                 margin={"top":"0","bottom":"0","left":"0","right":"0"})
        print("  ✅ visitenkarte_rueckseite.pdf")

        print("📄 Briefbogen A4 (hell)...")
        page.set_viewport_size({"width": 794, "height": 1123})
        page.set_content(LETTERHEAD, wait_until="networkidle")
        page.wait_for_timeout(800)
        page.pdf(path=str(OUT / "briefbogen_a4.pdf"),
                 format="A4", print_background=True,
                 margin={"top":"0","bottom":"0","left":"0","right":"0"})
        print("  ✅ briefbogen_a4.pdf")

        browser.close()
    print("\n✅ Fertig!", OUT)


if __name__ == "__main__":
    build()
