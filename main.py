import cv2
import numpy as np
import face_recognition
import os
import datetime


def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


def markAttendance(name):
    with open('attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split()
            nameList.append(entry[0])
            now = datetime.datetime.now()
            dtString = now.strftime("%H:%M:%S")
            date = datetime.date.today()
            f.write(f'\n{name},{date},{dtString}')


path = 'photo'
img = []
classNames = []
mylist = os.listdir(path)
print(mylist)

for cls in mylist:
    curImg = cv2.imread(f'{path}/{cls}')
    img.append(curImg)
    classNames.append(os.path.splitext(cls)[0])
print(classNames)

encodeListKnown = findEncodings(img)
print("Encoding Complete")

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0,0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodeCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDistance = face_recognition.face_distance(encodeListKnown, encodeFace)
        # print(faceDistance)
        matchIndex = np.argmin(faceDistance)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            print(name)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0),2)
            cv2.rectangle(img, (x1, y2-35), (x2,y2), (0,255,0), cv2.FILLED)
            cv2.putText(img, name, (x1+6, y2-6),cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            markAttendance(name)


    cv2.imshow('webcam', img)
    cv2.waitKey(1)