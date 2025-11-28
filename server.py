"""
Flask server for emotion detector application.
This moedule provides endpoint for analyzing text sentiment using Watson NLP.
"""

from flask import Flask, render_template, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detector_route():
    """Detect emotion of provided text."""

    text_to_analyze = request.args.get("textToAnalyze", "")

    if not text_to_analyze or not text_to_analyze.strip():
        return "Invalid input! Try again.", 400
    
    response = emotion_detector(text_to_analyze)

    if response is None:
        return "Invalid input! Try again.", 500
    
    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']}, "
        f"'sadness': {response['sadness']}. "
        f"<b>The dominant emotion is {response['dominant_emotion']}</b>."
    )
    return formatted_response 

@app.route("/")
def render_index_page():
    """Render the main page."""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)