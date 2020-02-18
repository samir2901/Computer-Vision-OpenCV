import cv2 

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
scale_factor = 1.6
while True:
    _, frame = cap.read()    
    #cv2.imshow("Original",frame)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(frame,scale_factor)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
        facepart_gray = gray[y:y+h,x:x+w]
        facepart_color = frame[y:y+h,x:x+w]
        eyes = eye_cascade.detectMultiScale(facepart_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(facepart_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),3)    
    cv2.imshow("Detector",frame)    
    print("FPS:",cv2.CAP_PROP_FPS)
    print("Number of faces:",len(faces))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()