# Anleitung für Sarah — Website & Domain

Hey Sarah! 👋

Hier steht alles was du wissen musst, um die Website live zu schalten und später Änderungen zu machen. Alles kostenlos, kein technisches Vorwissen nötig.

---

## 🔑 Schritt 0: Eigenen GitHub-Account anlegen (einmalig, ~5 Min)

Damit du die volle Kontrolle über deine Website hast, brauchst du einen eigenen GitHub-Account:

1. Gehe auf [github.com](https://github.com) und klicke auf **Sign up**
2. Username empfehlung: `honne-hausverwaltung` oder `uwehonne`
3. Email: `uwehonne@honne-hausverwaltung.de`
4. Passwort wählen
5. Account bestätigen
6. Tobias kurz Bescheid geben mit Username + Passwort → Felix deployt die Website einmalig auf deinen Account
7. Danach Passwort ändern — du hast die volle Hoheit! 🔐

**Warum eigener Account?** So hängt deine Website nicht am Account von Tobias. Du kannst jederzeit selbst Änderungen machen, ohne jemanden fragen zu müssen.

---

## 🌐 Wie funktioniert das?

Die Website läuft auf **GitHub Pages** — das ist ein kostenloser Hosting-Service von GitHub.
Deine Domain `honne-hausverwaltung.de` (bei Checkdomain) zeigt einfach auf diese GitHub-Seite.

**Kosten:** €0 für das Hosting. Nur die Domain bei Checkdomain kostet (was sie eh schon tut).

---

## 🔗 Domain mit GitHub Pages verbinden (einmalig, ~10 Min)

### Schritt 1: Bei Checkdomain einloggen
1. Gehe auf [checkdomain.de](https://www.checkdomain.de) und logge dich ein
2. Klicke auf deine Domain `honne-hausverwaltung.de`
3. Gehe zu **DNS-Verwaltung** oder **DNS-Einstellungen**

### Schritt 2: DNS-Einträge setzen
Füge folgende Einträge hinzu (alte A-Records vorher löschen!):

**4× A-Records** (für die Hauptdomain):
```
Typ: A    Name: @    Wert: 185.199.108.153
Typ: A    Name: @    Wert: 185.199.109.153
Typ: A    Name: @    Wert: 185.199.110.153
Typ: A    Name: @    Wert: 185.199.111.153
```

**1× CNAME** (für www):
```
Typ: CNAME    Name: www    Wert: mail65.github.io
```

### Schritt 3: In GitHub die Domain eintragen
1. Gehe zu: https://github.com/mail65/honne-hausverwaltung/settings/pages
2. Unter **Custom domain** eingeben: `honne-hausverwaltung.de`
3. Auf **Save** klicken
4. Haken setzen bei **Enforce HTTPS**

### Schritt 4: Warten
DNS-Änderungen brauchen **bis zu 24 Stunden** — meist aber nur 15-30 Minuten.
Danach ist die Website unter `https://honne-hausverwaltung.de` erreichbar! ✅

---

## ✏️ Wie mache ich später Änderungen?

Für kleine Textänderungen direkt über GitHub (kein Download nötig):

1. Gehe zu: https://github.com/mail65/honne-hausverwaltung
2. Klicke auf `index.html`
3. Klicke auf den **Stift** (✏️) oben rechts
4. Text ändern
5. Unten auf **Commit changes** klicken
6. Fertig! Die Website aktualisiert sich automatisch in ~2 Minuten.

---

## 📞 Bei größeren Änderungen

Einfach Felix (den KI-Assistenten von Tobias) fragen! Der hat alle Projektdaten gespeichert und kann:
- Neue Abschnitte bauen
- Design anpassen
- Bilder austauschen (z.B. echtes Foto von deinem Vater einbauen)
- Neue Seiten hinzufügen

Einfach schreiben: *"Ich brauche eine Änderung an der Honne-Website"* — der Rest geht von alleine. 😊

---

## 📁 Wo sind die Dateien?

Alle Projektdateien liegen hier:
```
/Users/felix/.openclaw/workspace/honne-hausverwaltung/
├── index.html          ← Die Website
├── impressum.html      ← Impressum
├── LEISTUNGEN.md       ← Alle Leistungen (Quelle für Website-Texte)
├── README.md           ← Projektübersicht
└── assets/logo/        ← Logo in allen Varianten (SVG + PNG)
```

---

*Erstellt am 22.06.2026 — bei Fragen einfach Tobias fragen oder Felix direkt anschreiben!*
