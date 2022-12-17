import numpy as np
import cv2
import mediapipe as mp
from fer import FER
import keyboard

cap = cv2.VideoCapture(0) #получение видео с камеры
detector = FER() #создание детектора лица
handsDetector = mp.solutions.hands.Hands() #создание детектора рук

positions = []
count = 0
liked = False #переменная, обозначающая, лайкнули мы текущее видео или нет

while(cap.isOpened()):
    ret, frame = cap.read()
    if cv2.waitKey(1) & 0xFF == ord('q') or not ret:
        break
    flipped = np.fliplr(frame)
    flippedRGB = cv2.cvtColor(flipped, cv2.COLOR_BGR2RGB) # переводим изображение в формат RGB для распознавания

    emo = detector.detect_emotions(flippedRGB) #получение значений для всех эмоций с детектора
    if len(emo) == 0:
        continue
    emo = emo[0]
    emo = emo['emotions']
    #print(emo, end=' ')
    score = emo['happy']+emo['surprise']-emo['neutral']-emo['angry']*3-emo['sad']*2 #расчёт, насколько понравилось пользователю видео
    #print(score)
    if score > 0.3 and liked==False: #проверка, понравилось ли пользователю видео
        keyboard.send('l') #ставим лайк
        liked = True

    results = handsDetector.process(flippedRGB) #получаем информацию с детектора рук
    if results.multi_hand_landmarks is not None:
        # нас интересует только подушечка указательного пальца (индекс 8)
        # нужно умножить координаты а размеры картинки
        x_tip = int(results.multi_hand_landmarks[0].landmark[8].x *
                    flippedRGB.shape[1])
        y_tip = int(results.multi_hand_landmarks[0].landmark[8].y *
                    flippedRGB.shape[0])
        print(x_tip, y_tip) #получаем текущие координаты указательного пальца
        #cv2.circle(flippedRGB, (x_tip, y_tip), 10, (255, 0, 0), -1)

        positions.append([[x_tip, y_tip], count]) #добавляем полученные координаты в список
        while positions[len(positions)-1][1] - positions[0][1] > 1100:
            positions.pop(0) #удаляем из списка координаты, полученные слишком давно
        for i in range(0, len(positions)):
            if abs(positions[i][0][0] - positions[len(positions)-1][0][0]) < 100: #проверяем, что по оси x движение было коротким
                if positions[i][0][0] - positions[len(positions)-1][0][1] > 30 and positions[i][0][0] - positions[len(positions)-1][0][1] < 300 and "Right" in str(results.multi_handedness[0]): #проверяем движение вверх по оси y и что его делает правая рука
                    keyboard.send("down") #идём к следующему видео
                    liked = False
                    break
                if positions[i][0][0] - positions[len(positions)-1][0][1] < -30 and positions[i][0][0] - positions[len(positions)-1][0][1] > -300 and "Left" in str(results.multi_handedness[0]): #проверяем движение вниз по оси y и что его делает левая рука
                    keyboard.send("up") #идём к предыдущему видео
                    break

        #cv2.circle(flippedRGB, (x_tip, y_tip), 10, (255, 0, 0), -1)
    res_image = cv2.cvtColor(flippedRGB, cv2.COLOR_RGB2BGR)
    cv2.imshow("TT-helper", res_image)
    count += 1

handsDetector.close()
