# Importando o cv2 (pois com ele iremos acessar a webcam)
import cv2

# Importando o mediapipe para podermos detectar dedos e mãos
# (nos refiriremos a ele como "mp")
import mediapipe as mp

#  Indicando que usaremos a webcam e também especificando qual webcam será
video = cv2.VideoCapture(0)

# Usando a solução "mãos" da biblioteca mediapipe
hand = mp.solutions.hands

# Especificando qual número máximo de mãos vamos detectar
Hands = hand.Hands(max_num_hands=1)

# Desenhando as ligações entre os pontos da mão
mpDraw = mp.solutions.drawing.utils

while True:
    check,img = video.read()
    # Convertendo as  imagens dos frames de BGR(cv2) para RGB(mediapipe)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # Detectar mãos em cada frame  do video      
    resultado = hand.process(imgRGB)

    # Coordenadas dos pontos da mão
    handPoints = results.multi_hand_landmarks
    if handPoints:
        for points in handPoints:
            print(points)

    # "Rodar" o vídeo para apreciação dessa A.I 
    cv2.imshow("resultado show de bola ",img)
    # Saia da tela ao pressionar a barra de espaços
    key = cv2.waitKey(1)
    if key == 32:
        break
cv2.destroyAllWindows()


'''

Posiveis soluções:

Digite no terminal:
python --version

Minha versão é: Python 3.11.1

A instalação do pip atualmente não funcionará com versões >= 3.9

Tente "py -m pip install mediapipe" ou "pip3 install mediapipe --user"
"pip install mediapipe-silicon"





'''