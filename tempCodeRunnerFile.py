from flask import Flask, render_template, request, jsonify
from chatbot import get_response
from database import init_db, save_chat

app = Flask(__name__)

init_db()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():

    user_msg = request.json["message"]

    bot_reply = get_response(user_msg)

    save_chat(user_msg, bot_reply)

    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)