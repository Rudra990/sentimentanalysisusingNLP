from flask import render_template, request, jsonify
from app import app, sentiment_pipeline

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    text = request.json.get("text")
    if not text:
        return jsonify({"error": "No text provided"}), 400
    result = sentiment_pipeline(text)[0]
    return jsonify(result)