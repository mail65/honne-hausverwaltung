# Übergabe Honne Hausverwaltung Website

## Aktueller Stand
- Live unter: https://mail65.github.io/honne-hausverwaltung/
- Repo: https://github.com/mail65/honne-hausverwaltung

## Auf Sarahs GitHub übertragen — 3 Schritte

### 1. GitHub-Account für Sarah/Uwe anlegen
- Gehe auf https://github.com/signup
- Username z.B. `honnehausverwaltung` oder `uwehonne`
- E-Mail: uwehonne@honnehausverwaltung.de

### 2. Repo übertragen
Tobias (oder Felix-KI) kann das Repo per Fork oder Transfer übergeben:
- In GitHub: Settings → Danger Zone → Transfer Repository
- Ziel: neuer Account von Sarah/Uwe

### 3. Eigene Domain einrichten (honnehausverwaltung.de)
Im GitHub Repo → Settings → Pages → Custom Domain: `honnehausverwaltung.de`

Beim Domain-Anbieter (wo die Domain registriert ist) folgende DNS-Einträge setzen:
```
A     @    185.199.108.153
A     @    185.199.109.153
A     @    185.199.110.153
A     @    185.199.111.153
CNAME www  honnehausverwaltung.github.io
```

→ Nach ~30 Minuten läuft die Seite unter honnehausverwaltung.de. Kostenlos!

## 🎂 Anlass & Deadline
- Uwe Honne Geburtstag ~25.06.2026
- Sarah will ihm die fertige Website zeigen
- **Wunsch:** Schon unter honnehausverwaltung.de erreichbar, aber mit Passwortschutz (noch nicht öffentlich)
- **Status:** Noch NICHT deployen — warten auf Sarahs GitHub-Account und Tobias' Freigabe

## Was noch offen ist
- [ ] Foto für Über-uns-Section (aktuell: Hamburger Altbau-Stockfoto)
- [ ] Echte Telefonnummer von Uwe eintragen
- [ ] Testimonials durch echte Kundenstimmen ersetzen (sobald vorhanden)
- [ ] Kontaktformular ggf. mit Formspree/Netlify Forms verbinden (statt mailto)

## Dateien im Repo
- `index.html` — gesamte One-Page-Website
- `impressum.html` — Impressum (§5 DDG-konform)
- `assets/logo/honne_logo_original.jpg` — Original-Logo von Uwe
- `assets/images/hamburg_speicherstadt.jpg` — Hero-Bild (iStock, von Tobias gekauft)
- `assets/images/hamburg_altbau_ueber.jpg` — Über-uns-Bild
- `assets/images/uwe_honne_team.jpg` — Uwe Honne mit Tochter (Warum-Wir-Section)
