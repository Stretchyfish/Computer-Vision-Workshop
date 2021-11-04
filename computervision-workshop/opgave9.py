# Opgave 9

import cv2 as cv
import numpy as np

# Brug HAAR-Cascades til at finde ansigter i billedet face.jpg
# Eventuel udfordring, prøv at finde øjne også

    # HINT:
    # https://docs.opencv.org/master/db/d28/tutorial_cascade_classifier.html

cascPath = cv.data.haarcascades

facePath = cascPath + "haarcascade_frontalface_default.xml"
faceCascade = cv.CascadeClassifier(facePath)

# Inlæs billede
image =

# Konveter til gray #hint : cvtColor, cv.COLOR_BGR2GRAY
gray =

faces = faceCascade.detectMultiScale(gray)

for (x, y, w, h) in faces:
    center = (x + w // 2, y + h // 2)
    image = cv.ellipse(image, center, (w // 2, h // 2), 0, 0, 360, (255, 0, 255), 4)

cv.imshow("text", image)
cv.waitKey(0)