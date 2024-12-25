import cv2
import time as t

# Open the default camera
cam = cv2.VideoCapture(0)

chars = " `.-':_,^=;><+!rc*/z?sLTv)J7(|Fi}C{fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@"

def ascii(image):
    print("\033[H\033[3J", end="")
    for i in range(len(image)):
        for n in range(len(image[i])):
            val = chars[round(image[i][n]*0.3607843137254902)-1]
            print(f'{val}', end='')
        print('')

while True:
    ret, frame = cam.read() # 640 x480 resolution
    resize = cv2.resize(frame, (320, 120))
    greyFrame = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)
    ascii(greyFrame)
    t.sleep(.0001)
