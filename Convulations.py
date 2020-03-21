import cv2
import numpy as np 

img = cv2.imread("Data/lena.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

kernel0 = np.array([[0,0,0],[0,1,0],[0,0,0]]) #returns same
kernel1 = np.array([[1,0,-1],[0,0,0],[-1,0,1]]) #edge detection
kernel2 = np.array([[0,1,0],[1,-4,1],[0,1,0]]) #edge detection
kernel3 = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]) #edge detection


convulated_image0 = cv2.filter2D(img,-1,kernel0)
convulated_image1 = cv2.filter2D(img,-1,kernel1)
convulated_image2 = cv2.filter2D(img,-1,kernel2)
convulated_image3 = cv2.filter2D(img,-1,kernel3)


cv2.imshow("Original Image",img)
cv2.imshow("Convulated Image0",convulated_image0)
cv2.imshow("Convulated Image1",convulated_image1)
cv2.imshow("Convulated Image2",convulated_image2)
cv2.imshow("Convulated Image3",convulated_image3)
cv2.waitKey(0)
cv2.destroyAllWindows()
