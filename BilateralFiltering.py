import cv2
import numpy as np 

img = cv2.imread('Data/butterfly.jpg')
cv2.imshow("Image",img)

dimPixel = 10 #diameter from the center
color = 100
space = 100
filterImg = cv2.bilateralFilter(img,dimPixel,color,space)
cv2.imshow("Filter",filterImg)

cv2.waitKey(0)
cv2.destroyAllWindows()