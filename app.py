import os

from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import google.generativeai as genai


GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_MODEL = os.environ.get("GEMINI_MODEL", "gemini-1.5-flash")

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)


app = Flask(__name__)
app.secret_key = "change-this-in-production"


@app.route("/")
def index():
    if not session.get("user"):
        return redirect(url_for("login"))

    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    success = False
    if request.method == "POST":
        username = (request.form.get("username") or "").strip()
        password = request.form.get("password") or ""
        if username == "SICHANA" and password == "SURESH06":
            success = True
            session["user"] = username
            session["login_count"] = session.get("login_count", 0) + 1
            return redirect(url_for("vpn_details"))
        else:
            error = "Invalid username or password."

    return render_template("login.html", error=error, success=success)


@app.route("/vpn-details")
def vpn_details():
    if not session.get("user"):
        return redirect(url_for("login"))

    login_count = session.get("login_count", 0)
    # Demo values for data usage and battery; in a real app these would come
    # from your VPN/mobile client.
    data_spent_mb = session.get("data_spent_mb", 256)
    battery_impact = session.get("battery_impact", 4)

    return render_template(
        "vpn_details.html",
        login_count=login_count,
        data_spent_mb=data_spent_mb,
        battery_impact=battery_impact,
    )


@app.route("/api/ai-assistant", methods=["POST"])
def ai_assistant():
    data = request.get_json(silent=True) or {}
    message = (data.get("message") or "").strip()

    if not message:
        reply = "Ask me anything about secure, free cloud VPN access for your mobile devices."
    else:
        reply = None

        # Try Gemini first if an API key is configured.
        if GEMINI_API_KEY:
            try:
                system_prompt = (
                    "You are the AI mobile assistant for a service called "
                    "'VPN FOR SERVER FREE CLOUD ACCESS'. "
                    "Answer concisely and helpfully about VPNs, mobile security, "
                    "cloud servers, and this product. Keep answers short."
                )
                model = genai.GenerativeModel(GEMINI_MODEL)
                response = model.generate_content(
                    f"{system_prompt}\n\nUser: {message}"
                )
                reply_text = getattr(response, "text", "") or ""
                reply = reply_text.strip() or None
            except Exception:  # noqa: BLE001
                reply = None

        # Fallback to the previous rule-based responses if Gemini is not
        # available or fails.
        if reply is None:
            lower = message.lower()
            if "how" in lower and "start" in lower:
                reply = (
                    "Download the VPN client, scan the QR from this dashboard, and "
                    "tap Connect. Your traffic is routed via our secure cloud edge."
                )
            elif "secure" in lower or "safe" in lower:
                reply = (
                    "We use encrypted tunnels (TLS 1.3) and rotating keys on our "
                    "cloud edge to keep your mobile traffic private."
                )
            elif "free" in lower or "price" in lower:
                reply = (
                    "The base plan is free for typical mobile use. Power users can "
                    "upgrade for more bandwidth and dedicated servers."
                )
            elif "server" in lower:
                reply = (
                    "Our AI automatically chooses the best server region for speed "
                    "and privacy based on your location and load."
                )
            else:
                reply = (
                    "This is a demo AI assistant. For now I can answer general "
                    "questions about our VPN for secure cloud access on mobile."
                )

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True)
