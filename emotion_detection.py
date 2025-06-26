import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze} }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    formated_response = json.loads(response.text)  # Return the response text from the API
    
    anger_score = formated_response['emotionPredictions'][0]['emotion']['anger']
    disgust_score = formated_response['emotionPredictions'][0]['emotion']['disgust']
    fear_score = formated_response['emotionPredictions'][0]['emotion']['fear']
    joy_score = formated_response['emotionPredictions'][0]['emotion']['joy']
    sadness_score = formated_response['emotionPredictions'][0]['emotion']['sadness']
    
    emotion_scores = {'anger': float(anger_score), 'disgust': float(disgust_score), 'fear': float(fear_score), 'joy': float(joy_score), 'sadness': float(sadness_score)}

    dominant_emotion_score = sorted(emotion_scores.values())[-1]
    for key, val in emotion_scores.items():
        if val == dominant_emotion_score:
            dominant_emotion = key

    return {
'anger': anger_score,
'disgust': disgust_score,
'fear': fear_score,
'joy': joy_score,
'sadness': sadness_score,
'dominant_emotion': dominant_emotion
}    

