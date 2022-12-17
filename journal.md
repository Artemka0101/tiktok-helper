## Особенности модуля fer
Детектор эмоций лица fer возвращает для каждой из эмоций 'angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral' значение от 0 до 1, соответствующее тому, насколько выражение лица отражает данную эмоцию.
Посмотрим, какие значения он будет выдавать для типичных выражений лица при просмотре TikTok:  
- Спокойное лицо (1)
![WIN_20221217_12_39_13_Pro](https://user-images.githubusercontent.com/64738836/208235896-98092e5b-7f64-44f2-b1c6-c42173a30e84.jpg)
{'angry': 0.11, 'disgust': 0.0, 'fear': 0.06, 'happy': 0.0, 'sad': 0.18, 'surprise': 0.03, 'neutral': 0.62}
- Лицо с улыбкой (2)
![smile](https://user-images.githubusercontent.com/64738836/208235951-6feed6ee-a80b-42da-b301-b58e8033cae0.jpg)
{'angry': 0.0, 'disgust': 0.0, 'fear': 0.0, 'happy': 0.83, 'sad': 0.0, 'surprise': 0.0, 'neutral': 0.17}
- Смеющееся лицо (3)
![happy](https://user-images.githubusercontent.com/64738836/208236133-5e2b3bc2-f890-473b-9d6b-f4d0d9d365d4.jpg)
{'angry': 0.0, 'disgust': 0.0, 'fear': 0.0, 'happy': 0.99, 'sad': 0.0, 'surprise': 0.0, 'neutral': 0.01}
- Удивленное лицо (4)
![WIN_20221217_12_45_40_Pro](https://user-images.githubusercontent.com/64738836/208236001-feab1964-fe63-43ba-9c77-7a0959f1c528.jpg)
{'angry': 0.0, 'disgust': 0.0, 'fear': 0.01, 'happy': 0.0, 'sad': 0.0, 'surprise': 0.99, 'neutral': 0.0}
- Грустное лицо (5)
![sad](https://user-images.githubusercontent.com/64738836/208236083-ed81ccbf-c903-49fa-bb95-e4825350c48d.jpg)
{'angry': 0.07, 'disgust': 0.0, 'fear': 0.04, 'happy': 0.0, 'sad': 0.17, 'surprise': 0.0, 'neutral': 0.71}  
- Смущённое лицо (6)
![disgust](https://user-images.githubusercontent.com/64738836/208236424-53394d25-6bd9-4548-a3e5-398a78b43a17.jpg)
{'angry': 0.28, 'disgust': 0.01, 'fear': 0.14, 'happy': 0.0, 'sad': 0.43, 'surprise': 0.0, 'neutral': 0.13}
  
Стоит задача все эти 7 значений объединить в одно, которое будет обозначать, насколько человеку нравится данное видео. 
В первой версии этим значением была просто разность между положительными и отрицательными эмоциями:  
score = 'happy'+'surprise'-'angry'-'disgust'-'fear'-'sad'  
Нам нужно, чтобы лайк ставился при эмоциях (2), (3) и (4). Можно заметить, что от эмоций (1) и (5) их отличает большое значение 'happy' или 'surprise', а также маленькое значение 'neutral', 'sad' и 'angry'.
При этом, параметры 'happy', 'surprise' и 'neutral' очень чувствительны, а 'angry' и 'sad' - не так сильно.
Так что, новый score можно сделать так:  
score = 'happy'+'surprise'-'neutral'-'sad'x2-'angry'x3
Тогда, параметры score для наших эмоций будут такие:  
(1) -1.2799999999999998  

(2) 0.6599999999999999  

(3) 0.98  

(4) 0.99  

(5) -1.26  

(6) -1.83  

Опытным путем было выявлено, что граница score (т.е. значение score, начиная с которого на видео будет ставиться лайк) равная 0.3, хорошо подходит.


