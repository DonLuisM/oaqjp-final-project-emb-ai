import requests 

def emotion_detector(text_to_analyse): 

    URL= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload= { "raw_document": { "text": text_to_analyse } }

    response = requests.post(URL, headers=Headers, json=payload)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Request failed with status {response.status_code}"}