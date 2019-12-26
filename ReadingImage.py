import cv2
import numpy as np 
import matplotlib.pyplot as plt 

img = cv2.imread("Data/butterfly.jpg",-1)
cv2.imshow("Frame",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

