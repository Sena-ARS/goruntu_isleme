import cv2
import numpy as np
from matplotlib import pyplot as plt

#Dosyadan resim okuma
foto = cv2.imread('resim2.jpg')
cv2.imshow('goruntu',foto)

B = foto[:,:,0]
G = foto[:,:,1]
R = foto[:,:,2]

cv2.imshow('mavi',B)
cv2.imshow('yesil',G)
cv2.imshow('kirmizi',R)
#cv2.waitKey()
print(foto.shape)
print(R.shape)
x = 4 #Sutun
y = 3 #Satir
kanal = 0
yogunluk_b = foto[y,x,kanal]
print("yogunluk:",yogunluk_b)
yogunluk_r = R[y,x]
print("yogunluk_gray:",yogunluk_r)
maksimum_yogunluk = np.max(B)
minimum_yogunluk = np.min(B)
print("Maks:",maksimum_yogunluk,"Min: ",minimum_yogunluk)
print(foto[y,x])#Tam kordinatın RGB değerlerini döner

#Gorüntünün belirli piksellerini elde etme ve ekranda gösterme
parca2 = R[20:180,40:280]
print(parca2)
cv2.imshow("parca",parca2)
cv2.waitKey()
