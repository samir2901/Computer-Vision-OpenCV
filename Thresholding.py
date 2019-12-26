import cv2
import numpy as np 

def threshold(img,thresholdValue):
    x= img
    cols = x.shape[1]
    rows = x.shape[0]
    for i in range(0,rows):
        for j in range(0,cols):
            if(x[i][j]> thresholdValue):
                x[i][j]=255
            else:
                x[i][j]=0
    return x

img = cv2.imread('Data/butterfly.jpg',0)
cv2.imshow("Original",img)
#x = threshold(img,100)
_, x = cv2.threshold(img,10,255,cv2.THRESH_BINARY_INV)
cv2.imshow("Thresh",x)
cv2.waitKey(0)
cv2.destroyAllWindows()