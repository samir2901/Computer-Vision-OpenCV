import cv2
import numpy as np 

img = cv2.imread('Data/butterfly.jpg')
cols = img.shape[1]
rows = img.shape[0]
center = (cols/2,rows/2)
angle = 56
M = cv2.getRotationMatrix2D(center,angle,1)
rotatedImage = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow("Rotated",rotatedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()