"""P-009 resume — the login edition.

Serves the same index.html as the public page, plus private.json (contact details, CV link) once
signed in. Session login, one shared reviewer account + owner account, no data stored client-side.
"""
import os, hmac, secrets
from flask import Flask, request, session, redirect, send_file, jsonify, Response

PREFIX = os.environ.get("BASE_PATH", "/showcase/resume")
HERE = os.path.dirname(os.path.abspath(__file__))
PAGE = os.path.join(HERE, "index.html")                       # docker: copied beside app.py
if not os.path.exists(PAGE):
    PAGE = os.path.join(os.path.dirname(HERE), "index.html")  # local dev: repo root
PRIVATE = os.path.join(HERE, "data", "private.json")   # mounted volume; never in git
USERS = {  # password via env; the reviewer account is what you hand to interviewers
    "eric":     os.environ.get("OWNER_PW", "change-me"),
    "reviewer": os.environ.get("REVIEWER_PW", "change-me-too"),
}

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY") or secrets.token_hex(32)
app.config.update(SESSION_COOKIE_HTTPONLY=True, SESSION_COOKIE_SAMESITE="Lax")

LOGIN_HTML = """<!doctype html><html data-mode="dark"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>印 · sign in</title>
<link href="https://fonts.googleapis.com/css2?family=Zen+Old+Mincho:wght@700&family=IBM+Plex+Mono&display=swap" rel="stylesheet">
<style>
body{margin:0;min-height:100vh;display:flex;align-items:center;justify-content:center;
 background:#111318;color:#efe9da;font:15px "IBM Plex Mono",monospace}
form{border:1px solid #3a3a38;border-radius:4px;padding:44px 40px;text-align:center;background:rgba(255,255,255,.02)}
h1{font:700 30px "Zen Old Mincho",serif;margin:0 0 4px;letter-spacing:.2em}
p{color:#8d8677;font-size:12px;margin:0 0 26px}
input{display:block;width:240px;margin:10px auto;padding:10px 12px;background:#0c0e12;color:#efe9da;
 border:1px solid #3a3a38;border-radius:3px;font:inherit}
button{margin-top:14px;padding:10px 34px;background:#c9503a;border:0;border-radius:3px;color:#f4efe2;
 font:inherit;letter-spacing:.15em;cursor:pointer}
.err{color:#c9503a;font-size:12px;margin-top:12px}
</style></head><body><form method="post">
<h1>印</h1><p>the private edition · resume of Eric Lu</p>
<input name="u" placeholder="user" autofocus autocomplete="username">
<input name="p" placeholder="password" type="password" autocomplete="current-password">
<button>Enter</button>{err}</form></body></html>"""


def authed():
    return bool(session.get("u"))


@app.route(PREFIX + "/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        u = (request.form.get("u") or "").strip()
        p = request.form.get("p") or ""
        if u in USERS and hmac.compare_digest(USERS[u], p):
            session["u"] = u
            return redirect(PREFIX + "/")
        return LOGIN_HTML.replace("{err}", '<div class="err">wrong user or password</div>'), 401
    return LOGIN_HTML.replace("{err}", "")


@app.get(PREFIX + "/logout")
def logout():
    session.clear()
    return redirect(PREFIX + "/login")


@app.get(PREFIX + "/")
@app.get(PREFIX)
def page():
    if not authed():
        return redirect(PREFIX + "/login")
    return send_file(PAGE)


@app.get(PREFIX + "/private.json")
def private_json():
    if not authed():
        return jsonify(error="sign in"), 401
    if os.path.exists(PRIVATE):
        return send_file(PRIVATE, mimetype="application/json")
    return jsonify({}), 404


@app.get(PREFIX + "/health")
def health():
    return jsonify(ok=True, private=os.path.exists(PRIVATE))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8202)))
