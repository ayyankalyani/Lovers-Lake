from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

# 🔑 Apna Groq API key yahan likh
API_KEY = "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"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.form["user_input"]

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama-3.2-1b-preview",  # ✅ Updated & working model
        "messages": [{"role": "user", "content": user_input}]
    }

    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            data=json.dumps(data)
        )

        if response.status_code == 200:
            reply = response.json()["choices"][0]["message"]["content"]
            return render_template("index.html", user_input=user_input, bot_reply=reply)
        else:
            error = response.json().get("error", {}).get("message", "Unknown error occurred.")
            return render_template("index.html", bot_reply=f"⚠️ Error: {error}")

    except Exception as e:
        return render_template("index.html", bot_reply=f"⚠️ Something went wrong: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
