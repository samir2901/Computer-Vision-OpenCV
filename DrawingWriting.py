import cv2
import numpy as np 

i = np.zeros((500,500,3),dtype=np.uint8)
cv2.rectangle(i,(10,10),(120,120),(0,0,255),3,lineType=8)
cv2.line(i,(10,10),(300,300),(255,0,0),3,lineType=8)
cv2.circle(i,(60,60),40,(0,255,0),3,lineType=8)
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(i,"OpenCV",(60,60),font,0.9,(0,255,50),1,cv2.LINE_AA)
cv2.imshow("Image",i)
cv2.waitKey(0)
cv2.destroyAllWindows()


