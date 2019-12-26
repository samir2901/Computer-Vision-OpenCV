import cv2
import numpy as np 

img = cv2.imread('Data/butterfly.jpg')
cv2.imshow("Image",img)

kernalSize = 5
blur = cv2.medianBlur(img,kernalSize)

cv2.imshow("BlurredImage",blur)
cv2.waitKey(0)
cv2.destroyAllWindows()