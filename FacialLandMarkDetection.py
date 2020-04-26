import cv2
import numpy as np

cap = cv2.VideoCapture(0)
face_haarcascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
landmark_detector = cv2.face.createFacemarkLBF()
landmark_detector.loadModel("lbfmodel.yaml")
scale = 2

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_haarcascade.detectMultiScale(gray,scale)    
    for (x,y,w,h) in faces:
        _, landmarks = landmark_detector.fit(gray,np.array(faces))
        #cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)
        for landmark in landmarks:            
            for (x,y) in landmark[0]:
                cv2.circle(frame,(x,y), 1, (0,255,0))                
        
        #print(landmarks)
    
    cv2.imshow("Frame",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
