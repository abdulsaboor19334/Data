import cv2
import numpy as np
from pyzbar.pyzbar import decode

# img = cv2.imread('C:\\Users\Abdul Saboor\VS projects\CK\c.png')
# code = decode(img)
# print(code[0][0])

# cv2.imshow('image',img)
# cv2.waitKey(0)

cap =cv2.VideoCapture(0)

while True:

    ret, img = cap.read()
    code = decode(img)
    for bar in code:
        print(bar.data)
    cv2.imshow('my vid', img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
