import cv2;
import numpy as np;

camera=cv2.VideoCapture(0)

while(True):
    ret,video=camera.read()
    hsv=cv2.cvtColor(video, cv2.COLOR_BGR2HSV)
    dusukKirmizi=np.array([0,12,18])
    yuksekKirmizi=np.array([2,205,252])
    siyah_beyaz=cv2.inRange(hsv,yuksekKirmizi,dusukKirmizi)
    renk=cv2.bitwise_and(video,video,mask=siyah_beyaz)
    cv2=imshow("Renkli",renk)
    cv2=imshow("Siyah/Beyaz",siyah_beyaz)
    if cv2.waitkey(50)& 0xFF==ord('x'):
        break

camera.release()
cv2.destroyAllWindows()
