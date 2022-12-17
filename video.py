import numpy as np
import cv2
import mediapipe as mp
from fer import FER
import keyboard

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    ret, frame = cap.read()
    if cv2.waitKey(1) & 0xFF == ord('q') or not ret:
        break
    frame = np.fliplr(frame)
    cv2.imshow("TT-helper", frame)
