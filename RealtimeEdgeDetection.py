import cv2

cap = cv2.VideoCapture(1)

while True:
    _, frame = cap.read()
    cv2.imshow("Original",frame)
    thresholdValue1 = 50
    thresholdValue2 = 100
    canny = cv2.Canny(frame,thresholdValue1,thresholdValue2)
    cv2.imshow("Edges",canny)    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

