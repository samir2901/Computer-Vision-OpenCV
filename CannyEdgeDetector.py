import cv2
import numpy as np 

img = cv2.imread('Data/sudoku.png')
cv2.imshow("Image",img)

thresholdValue1 = 50
thresholdValue2 = 100

canny = cv2.Canny(img,thresholdValue1,thresholdValue2)
cv2.imshow("Edges",canny)
cv2.waitKey(0)
cv2.destroyAllWindows()