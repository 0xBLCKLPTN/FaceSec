import cv2
import numpy as np
import face_recognition
import os

directory: str = 'FaceBase'

images: list = []
names: list = []
images_list: list = os.listdir(directory)

for name in images_list:
    curimg= cv2.imread(f'{directory}/{name}')
    images.append(curimg)
    names.append(os.path.splitext(name)[0])

def ogencodings(images):
    encList=[]
    for img in images:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encList.append(encode)
    return encList

encog= ogencodings(images)
print("Encoding process complete! Please wait for Results...")

cap= cv2.VideoCapture(0)
while(True):
    ret,frame=cap.read()
    window=cv2.resize(frame,(0,0),None,0.25,0.25)
    window=cv2.cvtColor(window,cv2.COLOR_BGR2RGB)
    faceCam = face_recognition.face_locations(window)
    encCam = face_recognition.face_encodings(window,faceCam)

    for encWin,faceloc in zip(encCam,faceCam):
        match= face_recognition.compare_faces(encog,encWin)
        dist=face_recognition.face_distance(encog,encWin)
        print(dist)
        matchval= np.argmin(dist)

        if match[matchval]:
            name1= names[matchval].upper()
            print(name1)
            y1,x2,y2,x1=faceloc
            y1, x2, y2, x1=y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(frame,(x1,y1),(x2,y2),(255,255,0),2)
            cv2.rectangle(frame,(x1,y2-35),(x2,y2),(255,255,0),cv2.FILLED)
            cv2.putText(frame,name1,(x1+6,y2-6),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,255),2)

    cv2.imshow('Cam number ',frame)
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break



