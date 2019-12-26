import cv2
import numpy as np 

img = cv2.imread('Data/butterfly.jpg')
cols = img.shape[1]
rows = img.shape[0]
transformationMatrix = np.array([[1,0,150],[0,1,70]],dtype=np.float)
shifted = cv2.warpAffine(img,transformationMatrix,(cols,rows))
cv2.imshow("Image",shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()