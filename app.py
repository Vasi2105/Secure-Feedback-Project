import sqlite3
import csv,io
import bleach
from flask import Flask, render_template, request, make_response, redirect, url_for, session
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

def sanitize_input(text):
    cleaned = bleach.clean(text, strip=True)
    return cleaned


app = Flask(__name__)
app.secret_key = "admin123"  # De inlocuit cu ceva mai sigur!!! 
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    #default_limits=["3 per minute"]
)


# ======================================
# RUTA HOME
# ======================================
@app.route('/')
def home():
    username = request.args.get('username', '')
    return render_template('index.html',username=username) 


# ======================================
# RUTA SUBMIT FEEDBACK (USER)
# ======================================
@limiter.limit("2 per minute")
@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username') 
    message = request.form.get('message') 

    username = sanitize_input(username)
    message = sanitize_input(message)

    if not message or len(message.strip()) < 10:
     return f'''
        ❌ Mesajul trebuie să conțină cel puțin 10 caractere!<br>
        <a href="/?username={username or ''}">⏪ Înapoi la formular</a>
    ''', 400
    conn = sqlite3.connect('feedback.db')
    cursor = conn.cursor()
    cursor.execute ('INSERT INTO feedback (username,message) VALUES (?, ?)', (username,message))
    conn.commit()
    conn.close()

    print(f"========= ✅ Feedback primit ✅ =========\n"
          f"Nume ----> {username or 'anonim'}\n"
          f"Message: {message}\n"
          + "-"*40)

    return render_template("feedback_submitted.html", username=username)


# ======================================
# RUTA ADMIN-LOGIN
# ======================================
VALID_ADMINS = {
    "admin1": "parola1",
    "admin2": "parola2",
    "admin3": "parola3"
}
@app.route("/admin-login", methods=["GET", "POST"])
def admin_login():
    error = None
    if request.method == "POST":
        user = request.form["username"]
        pw = request.form["password"]
        # verificăm în dicționar
        if user in VALID_ADMINS and VALID_ADMINS[user] == pw:
            session["admin"] = True
            return redirect("/all_feedbacks")
        else:
            error = "Credențiale invalide!"
    return render_template("admin_login.html", error=error)


# ======================================
# RUTA ADMIN-LOGOUT
# ======================================
@app.route("/admin-logout")
def admin_logout():
    session["admin"] = False  # Ne asiguram si ca daca userul a introdus vreodata credentialele corecte, sa nu ramana salvate
    return redirect("/admin-login") 


# ======================================
# RUTA ALL_FEEDBACKS
# ======================================
@app.route('/all_feedbacks')
def all_feedbacks():
    admin = session.get("admin", False) 
    conn = sqlite3.connect('feedback.db')
    cursor = conn.cursor()
    cursor.execute('SELECT rowid, username, message FROM feedback ORDER BY rowid DESC')
    feedbacks = cursor.fetchall()
    conn.close()
    print(feedbacks)

    return render_template('all_feedbacks.html', feedbacks=feedbacks, admin=admin)


# ======================================
# RUTA STERGERE FEEDBACK
# ======================================
@app.route("/delete-feedback", methods=["POST"])
@limiter.limit("100 per minute", override_defaults=True)
def delete_feedback():
    # Doar admin
    if not session.get("admin"):
        return "Acces interzis", 403

    fid = request.form.get("id")
    if fid:
        conn = sqlite3.connect("feedback.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM feedback WHERE rowid = ?", (fid,))
        conn.commit()
        conn.close()

    return redirect("/all_feedbacks")


# ======================================
# RUTE EXPORT CSV / JSON – doar admin
# ======================================
@app.route("/export-csv")
def export_csv():
    if not session.get("admin"):
        return "Acces interzis", 403

    conn = sqlite3.connect("feedback.db")
    cursor = conn.cursor()
    cursor.execute("SELECT username, message FROM feedback")
    all_data = cursor.fetchall()
    conn.close()

    si = io.StringIO()
    writer = csv.writer(si)
    writer.writerow(["Username", "Message"])
    for row in all_data:
        writer.writerow(row)

    output = make_response(si.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=feedback.csv"
    output.headers["Content-type"] = "text/csv"
    return output

@app.route("/export-json")
def export_json():
    if not session.get("admin"):
        return "Acces interzis", 403

    # Ca exemplu simplu:
    import json
    conn = sqlite3.connect("feedback.db")
    cursor = conn.cursor()
    cursor.execute("SELECT username, message FROM feedback")
    rows = cursor.fetchall()
    conn.close()

    # Transformam in structura JSON
    data_list = []
    for r in rows:
        data_list.append({"username": r[0], "message": r[1]})

    return make_response(json.dumps(data_list, indent=2), 200, {"Content-Type": "application/json"})


if __name__ == '__main__':
    app.run(debug=True)

