# Secure Feedback Project 🛡️✨

## Descriere
Secure Feedback Project este o aplicație web completă și securizată, construită în Flask, destinată colectării și gestionării feedback-ului utilizatorilor într-un mod profesionist, estetic și sigur. Această aplicație a fost dezvoltată cu accent pe experiența utilizatorului (UX), performanță, securitate și ușurință în administrare.

## 🛠️ Funcționalități

### Pentru utilizatori:
- Formular simplu și intuitiv pentru trimiterea feedback-ului.
- Vizualizare publică a feedback-urilor trimise anterior.
- Feedback-urile noi apar primele în listă pentru accesibilitate.
- Interfață modernă, ușor navigabilă, stilizată cu Tailwind CSS.

### Pentru admini:
- Autentificare securizată (multiple conturi admin disponibile).
- Interfață separată și securizată pentru gestionarea feedback-ului.
- Posibilitatea de ștergere feedback-uri direct din panoul admin.
- Export rapid al feedback-ului în formate CSV și JSON.

## 🛡️ Măsuri de Securitate Implementate:
- **Protecție Anti-Spam:** Utilizarea Flask-Limiter pentru a preveni trimiterea automată excesivă a feedback-ului.
- **Sanitizare Input (Anti-XSS):** Utilizarea Bleach pentru a curăța input-ul utilizatorilor și a preveni atacurile Cross-Site Scripting (XSS).
- **Prevenție SQL Injection:** Folosirea parametrilor în interogările SQL pentru protecție împotriva SQL Injection.
- **Gestionare sigură sesiuni:** Utilizare chei secrete robuste pentru gestionarea sigură a sesiunilor adminilor.

## 🎨 Design și Estetică:
- **Interfață vizuală modernă:** Dezvoltată cu Tailwind CSS, oferă un aspect plăcut și profesionist.
- **Dark Mode:** Aplicat implicit pentru o experiență vizuală optimă și uniformă.
- **Animații subtile și feedback vizual:** Implementarea unor animații și efecte vizuale subtile pentru o experiență îmbunătățită.

## 🚀 Tehnologii Folosite:
- **Flask** (Backend)
- **Tailwind CSS** (Frontend)
- **SQLite** (Bază de date)
- **Bleach** (Securizare input)
- **Flask-Limiter** (Prevenție spam)

## 📦 Cum rulezi proiectul local:

1. **Clonează repository-ul:**
   ```bash
   git clone https://github.com/Vasi2105/Secure-Feedback-Project.git
   cd Secure-Feedback-Project
   ```

2. **Instalează dependințele:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Rulează serverul Flask folosind script-ul:**
   ```bash
   start_feedback_app.bat
   ```

4. **Logare admin:**
   - Folosește script-ul dedicat:
   ```bash
   login_admin.bat
   ```
   - Credențiale exemplu:
     - user: `admin1` | parola: `parola1`
     - user: `admin2` | parola: `parola2`
     - user: `admin3` | parola: `parola3`

## 📁 Structură Proiect
```
Secure-Feedback-Project/
├── app.py                     # Server Flask
├── templates/                 # Șabloane HTML
│   ├── index.html             # Formular utilizatori
│   ├── all_feedbacks.html     # Lista feedback-uri
│   ├── admin_login.html       # Autentificare admin
│   └── feedback_submitted.html # Confirmare feedback
├── feedback.db                # Baza de date SQLite
├── requirements.txt           # Dependințe Python
├── start_feedback_app.bat     # Script pornire aplicație
└── login_admin.bat            # Script acces admin
```

## 🧑‍💻 Despre mine
Acest proiect a fost creat din dorința de a învăța și aplica principiile bune de dezvoltare web și cybersecurity, punând accent pe siguranță și estetică. Sunt deschis către feedback și colaborări pentru îmbunătățiri viitoare!

---

Dacă ai întrebări sau sugestii, contactează-mă prin [GitHub](https://github.com/Vasi2105)! 🚀📬