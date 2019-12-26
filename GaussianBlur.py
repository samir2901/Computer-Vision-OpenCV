import cv2
import numpy as np 

img = cv2.imread('Data/butterfly.jpg')
cv2.imshow("Image",img)

M = (9,9)

blur = cv2.GaussianBlur(img,M,8)
cv2.imshow("BlurredImage",blur)
cv2.waitKey(0)
cv2.destroyAllWindows()