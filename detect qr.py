
import cv2
import numpy as np
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    ret, frame = cap.read()
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        print(myData)
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        pts2 = barcode.rect
        cv2.putText(img,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.9,(255,0,255),2)
        (x, y, w, h) = barcode.rect
        cv2.rectangle(frame, (x, y), (x +w, y + h), (0, 0, 255), 3)
        
        medium_x = int((x + x+w)/2)
        medium_y = int((y + y+h)/2)
        center_y = 220
        center_x = 340

        print("CENTER X:",center_x)
        print("CENTER Y:",center_y)
        print("MEDIUM X:",medium_x)
        print("MEDIUM Y:",medium_y)

        text = "x = "+str(x)+"y = "+str(y)
        cv2.putText(frame, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.50, (0, 0, 255))
        cv2.line(frame, (medium_x,0),(medium_x,680),(0,255,0),2)
        text2 = "mediumX = " + str(medium_x)
        cv2.putText(frame, text2, (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.50, (0, 255, 50))
        cv2.line(frame, (0, medium_y), (680, medium_y), (0, 255, 0), 2)
        text3 = "mediumY = " + str(medium_y)
        cv2.putText(frame, text3, (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.50, (0, 255, 50))
        area = w*h
        
        print("AREA:",area)
        
        if medium_y > center_y+40:
            print('top','↑')
        if medium_y < center_y-40:
            print('bottom','↓')
        if medium_x > center_x+40:
            print('LEFT','<========')
        if medium_x < center_x-40:
            print('RIGHT','=======>')
        if area > 10000:
            print('UPPP !')

    cv2.imshow('Result',frame)
    cv2.waitKey(1)
