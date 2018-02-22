Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> import cv2
>>> 
>>> detector = cv2.CascadeClassifier('C:\Python27\Projects\FaceRec\haarcascade_frontalface_default.xml')
>>> cap = cv2.VideoCapture(0)

>>> while(True):
    ret, img = cap.read()
    makeGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(makeGray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow('frame',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

        
>>> cap.release()
>>> cv2.destroyAllWindows()

