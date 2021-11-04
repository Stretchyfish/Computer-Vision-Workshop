# Opgave 10

import cv2 as cv


# Lav et program som bruger dit camera til at detektere ansigter
# Genbrug gerne koden fra forrige opgave

    #HINT:
    # https://docs.opencv.org/master/d8/dfe/classcv_1_1VideoCapture.html


# Lav et videocapture objekt med cv.VideoCapture()
cap =

while True:
    ret, frame = cap.read()

    cv.imshow("video", frame)

    if cv.waitKey(25) & 0xFF == ord('q'): # stop videovisning ved at trykke på "q"
        break

cap.release() #release videodevice, så systemet kan se den igen


cv.destroyAllWindows() # lukker alle video vinduer.


