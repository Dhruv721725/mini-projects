import cv2 as cv
import numpy as np

file=open(r'people.txt')
peoples=file.readlines()
file.close()

features=np.load(r'features.npy',allow_pickle=True)
labels=np.load(r'labels.npy',allow_pickle=True)
hc=cv.CascadeClassifier(r'face.xml',)

face_recognizer=cv.face.LBPHFaceRecognizer.create()
face_recognizer.read(r'faces_trained.yml')

cap=cv.VideoCapture(0)

while True:
    istrue, frame=cap.read()
    gry=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    blur=cv.GaussianBlur(gry,(3,3),0)
    faces_rect=hc.detectMultiScale(blur,1.1,4)

    for (x,y,w,h) in faces_rect:
        face=blur[y:y+h,x:x+w]
        label, confidence=face_recognizer.predict(face)

        cv.rectangle(frame,(x,y),(x+w,y+h),(0,160,255),1)
        cv.putText(frame,f'Hi, {peoples[label][:-1]}, ...{int(confidence)}',(x,y+h+10),cv.FONT_ITALIC,0.5,(0,255,0),1)
    
    cv.imshow('Video Captured',frame)

    if cv.waitKey(0)&0xFF==ord('q'):
        break

cap.release()
cv.destroyAllWindows()

