import cv2
import numpy
import pyzbar.pyzbar as pyzbar
import pyqrcode

# QR code Generator
# ........................................................
# qr = pyqrcode.create('shantam sultania')
#
# qr.png('qr.png',11)

# just un comment them
# ..........................................................
# # reader in an image only
#
# img =cv2.imread('qr.png')
# cv2.imshow('qrcode',img)
# cv2.waitKey(0)
#
# # decoder
#
# decode = pyzbar.decode(img)
# for i in decode:
#     print(i.data)
#..........................................................

# for live that is in a Video

cam = cv2.VideoCapture(0)

while True:
    check,frame = cam.read()
    decode = pyzbar.decode(frame)
    for i in decode:
        cv2.putText(frame,str(i.data),(50,50),cv2.FONT_ITALIC,1,(0,255,0),3)
    cv2.imshow('qr code reader',frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
