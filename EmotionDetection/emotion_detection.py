"""
Emotion analysis module using Watson NLP API.
Provides functionality to analyze text emotions.
"""

import os
import requests
from dotenv import load_dotenv

load_dotenv()

def emotion_detector(text_to_analyze):
    """
        Analyzes the emotion of the given text using Watson NLP service.

    Args:
        text_to_analyse: Text string to analyze

    Returns:
        Dictionary with 'emotion' and 'score' keys
        Returns None values if analysis fails

    """
    if not text_to_analyze or not text_to_analyze.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    url = os.getenv("WATSON_NLP_URL")
    apikey = os.getenv("API_KEY")
    watson_version = os.getenv("WATSON_VERSION")

    if not url or not apikey:
        print("Error: Missing API credentials in .env file")
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    params = {
        "version": watson_version
    }

    payload = {
        "text": text_to_analyze,
        "features": {
            "emotion": {
                "document": True
            }
        }
    }

    headers = {
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(
            url,
            json=payload,
            headers=headers,
            params=params,
            auth=("apikey", apikey)
        )

        response.raise_for_status()

        data= response.json()

        emotion_data = data.get("emotion", {}).get("document", {}).get("emotion", {})

        if not emotion_data:
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }

        dominant_emotion = max(emotion_data, key=emotion_data.get)

        return {
            'anger': emotion_data.get('anger', 0.0),
            'disgust': emotion_data.get('disgust', 0.0),
            'fear': emotion_data.get('fear', 0.0),
            'joy': emotion_data.get('joy', 0.0),
            'sadness': emotion_data.get('sadness', 0.0),
            'dominant_emotion': dominant_emotion           
        }


    except requests.exceptions.HTTPError as error:
        print(f"HTTP Error during emotion analysis: {error}")
        if response:
            print(f"Response status: {response.status_code}")
            print(f"Response body: {response.text}")
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    except requests.exceptions.ConnectionError as error:
        print(f"Connection Error: Unable to reach Watson API - {error}")
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    except requests.exceptions.Timeout as error:
        print(f"Timeout Error: Whatson API took too long to respond - {error}")
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    except requests.exceptions.RequestException as error:
        print(f"Error during emotion analysis: {error}")
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    except (KeyError, ValueError) as error:
        print(f"Error parsing Watson NLU response: {error}")
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    