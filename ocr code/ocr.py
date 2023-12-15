import cv2
import easyocr
import requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("./FirebaseKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://visioassist-6231e-default-rtdb.asia-southeast1.firebasedatabase.app/'
})


def ocr():
    video_url = "http://10.16.35.199:8080//video" 
    cap = cv2.VideoCapture(video_url) 
 
    reader = easyocr.Reader(['en'])   
 
    ret, frame = cap.read() 
 
    if ret: 
        results = reader.readtext(frame) 
 
        extracted_text = "" 
 
    for (bbox, text, prob) in results: 
        extracted_text += text + " " 
 
    print(extracted_text) 

    ref = db.reference('/ocr/content')  
    ref.set(extracted_text)  

    ref = db.reference('/ocr/value')  
    ref.set(0)  
 
    cap.release()

def listen_to_firebase_change():
    ref = db.reference('/ocr')  # Replace with the actual Firebase path
    snapshot = ref.get()

    while True:
        if snapshot is not None and 'value' in snapshot:
            if snapshot['value'] == 1:
                ocr()
        # Wait for changes in the Firebase value
        snapshot = ref.get()

if __name__ == "__main__":
    listen_to_firebase_change()
