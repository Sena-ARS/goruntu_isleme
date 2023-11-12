import cv2
import numpy as np
from matplotlib import pyplot as plt

#-----------RESİMİ OKUMA GRİYE DÖNÜŞTÜRME VE GÖSTERME-----------
gray = cv2.imread("resim2.jpg", 0)  # Resimi griye dönüştürdüm.
cv2.imshow("Gri Resim", gray)

#------------HİSTOGRAM HESAPLAMA ALGORİTMASI----------------
M, N = gray.shape[0] , gray.shape[1]       #Resimin satır ve sütünları boyutu
histogram = np.zeros(256,np.int32)  #0 değerli histogram adında matris oluşturdum
for i in range(0,M):
    for j in range(0,N):
        k = gray[i,j]
        histogram[k] += 1
print(histogram)
plt.imshow(gray,cmap="gray")
plt.show()
plt.plot(histogram)
plt.show()
cv2.waitKey()
