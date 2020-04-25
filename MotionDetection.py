import cv2 

cap = cv2.VideoCapture(0)

_, init_frame = cap.read()
_, frame = cap.read()

font = cv2.FONT_HERSHEY_SIMPLEX
org = (15,15)
while True:    
    diff = cv2.absdiff(init_frame,frame)
    gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    _, thresh = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh,None,iterations=3)
    contours, _ = cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        (x,y,w,h) = cv2.boundingRect(contour)
        area = cv2.contourArea(contour)
        if area > 700:
            cv2.rectangle(init_frame,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(init_frame,"Status: Motion Detected",org,font,0.6,(0,0,255),2)        
               
    cv2.imshow("Frame",init_frame)
    init_frame = frame
    _, frame = cap.read()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
