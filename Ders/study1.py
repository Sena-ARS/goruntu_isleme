#Open the Camera
import cv2
camera = cv2.VideoCapture(0)
while (True):
    ret, goruntu = camera.read()
    cv2.imshow('goruntu',goruntu)
    if cv2.waitKey(50) & 0xFF  == ord('x'):
        break

camera.release()
cv2.destroyAllWindows()