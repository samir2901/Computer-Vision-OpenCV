import cv2
import numpy as np 
import matplotlib.pyplot as plt 

img = cv2.imread("Data/butterfly.jpg")
img = cv2.imwrite("Data/image.png",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

