"""
Flask server for Emotion Detection API.
"""

from flask import Flask, request, render_template, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    """
    Making the home page with a HTML template.
    """
    return render_template("index.html")

@app.route("/emotionDetector", methods=["POST"])
def detect_emotion():
    """
    Emotion Detector function who receives text in a POST request, analyzes the feelings and 
    then return an JSON answer with the feeling's percentage.
    """
    data = request.get_json()
    result = emotion_detector(data["text"])

    if result["dominant emotion"] is None:
        return jsonify("Invalid text! Please try again!")

    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant emotion']}."
    )

    return jsonify(formatted_response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
