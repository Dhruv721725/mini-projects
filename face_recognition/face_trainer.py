import numpy as np
import cv2 as cv

features=[]
labels=[]
person=input('Enter Person name and other details:')

file=open(r'people.txt','+a') # add here path of peoples file relative to cmd.
file.write(person+'\n')
file.seek(0)
label_index=len(file.readlines())-1
file.close()

cap=cv.VideoCapture(0)
hc=cv.CascadeClassifier(r'face.xml') # add here path relative to cmd of an xml file

for i in range(50):
    istrue, frame=cap.read()
    gry=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    blur=cv.GaussianBlur(gry,(3,3),0)
    faces_rect=hc.detectMultiScale(blur,1.1,4)

    for (x,y,w,h) in faces_rect:
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,160,255),1)
        cv.putText(frame,'Detecting Face...',(x,y+h+10),cv.FONT_ITALIC,0.5,(0,0,255),1)
        face=gry[y:y+h,x:x+w]
        features.append(face)
        labels.append(label_index)
    cv.imshow('WebCam',frame)
    
    if cv.waitKey(20)& 0xFF==ord('q') or i>=49:
        break

cap.release()
cv.destroyAllWindows()

features_object=np.array(features,dtype='object')
labels_array=np.array(labels)
face_recognizer=cv.face.LBPHFaceRecognizer.create()

try:
    pre_features=np.load(r'features.npy')
    upd_features=np.append(pre_features,features_object)

    pre_labels=np.load(r'labels.npy')
    upd_labels=np.append(pre_labels,labels_array)

except Exception as e:
    upd_features=features_object
    upd_labels=labels_array

np.save(r'labels.npy',upd_labels)
np.save(r'features.npy',upd_features)
face_recognizer.train(upd_features,upd_labels)
face_recognizer.save(r'faces_trained.yml')

print(f'{person} your face has been recognized.')