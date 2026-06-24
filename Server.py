from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"status": "API Live hai bhai!", "message": "Mubarak ho"})

@app.route('/hello')
def hello():
    return jsonify({"hello": "Duniya", "from": "Railway API"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
