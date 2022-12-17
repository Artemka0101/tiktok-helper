import numpy as np
import cv2
import mediapipe as mp
from fer import FER
import keyboard

detector = FER()
image = cv2.imread("lilsmile.jpg")
emo = detector.detect_emotions(image)
print(emo)
print(emo[0]['emotions']['happy']+emo[0]['emotions']['surprise']-emo[0]['emotions']['neutral']-emo[0]['emotions']['angry']*3-emo[0]['emotions']['sad']*2)
