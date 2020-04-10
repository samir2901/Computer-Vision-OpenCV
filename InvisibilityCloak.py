import cv2
import numpy as np 
import time

cap = cv2.VideoCapture(0)

time.sleep(30)


#######This section is for storing the background information#######
background = 0

for i in range(30):
    _, background = cap.read()
    background = np.flip(background,axis=1)

##################################################################

while True:
    
    _, frame = cap.read()
    img = np.flip(frame,axis=1)
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    ## Detects green colored objects for making it invisible

    #mask1 
    lower_green = np.array([25,52,72])
    upper_red = np.array([102,255,255])
    mask1 = cv2.inRange(hsv,lower_green,upper_red)


    #mask2
    lower_green1 = np.array([186,42,255])
    upper_red1 = np.array([180,255,255])
    mask2 = cv2.inRange(hsv,lower_green1,upper_red1)

    mask1 = mask1 + mask2
    mask1 = cv2.morphologyEx(mask1,cv2.MORPH_OPEN,np.ones((3,3),dtype=np.uint8))
    mask1 = cv2.morphologyEx(mask1,cv2.MORPH_DILATE,np.ones((3,3),dtype=np.uint8))

    mask2 = cv2.bitwise_not(mask1)
    res1 = cv2.bitwise_and(img,img,mask=mask2)
    res2 = cv2.bitwise_and(background,background,mask=mask1)

    final = cv2.addWeighted(res1,1,res2,1,0)
    cv2.imshow("Res",np.hstack([img,final]))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()