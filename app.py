from flask import Flask, request, render_template
import os
import openai

app = Flask(__name__)

# Load OpenAI API key from environment variable 
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=["GET", "POST"])
def index():
    bot_reply = ""
    user_input = ""
    if request.method == "POST":
        user_input = request.form.get("user_input")
        if user_input:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_input}],
                max_tokens=200
            )
            bot_reply = response.choices[0].message["content"].strip()
    return render_template("index.html", user_input=user_input, bot_reply=bot_reply)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use $PORT if deployed
    app.run(host="0.0.0.0", port=port, debug=True)
