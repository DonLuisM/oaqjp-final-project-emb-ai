import requests
import json

def emotion_detector(text_to_analyse): 

    URL= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload= { "raw_document": { "text": text_to_analyse } }

    response = requests.post(URL, headers=Headers, json=payload)

    if response.status_code == 200:
        response_dict = response.json()
        
        emotions = response_dict.get("emotionPredictions", [{}])[0].get("emotion", {})

        if not emotions:  # Si la API no devuelve emociones, manejar el caso
            return {"error": "No emotions detected"}

        anger = emotions.get("anger", 0)
        disgust = emotions.get("disgust", 0)
        fear = emotions.get("fear", 0)
        joy = emotions.get("joy", 0)
        sadness = emotions.get("sadness", 0)

        dominant_emotion = max(emotions, key=emotions.get)
        
        result = {
            "anger": anger,
            "disgust": disgust,
            "fear": fear,
            "joy": joy,
            "sadness": sadness,
            "dominant emotion": dominant_emotion
        }

        return result
    else:
        return {"error": f"Request failed with status {response.status_code}"}