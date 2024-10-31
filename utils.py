import requests
import cv2
import numpy as np

def load_image(image_file):
    img = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_COLOR)
    return img

def identify_face(image_file, api_key, api_endpoint):
    headers = {
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': api_key
    }

    response = requests.post(api_endpoint, headers=headers, data=image_file)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API Error: {response.status_code} - {response.text}")

