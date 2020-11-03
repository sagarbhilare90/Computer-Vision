import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('shades.PNG',0) 

  
# calculate frequency of pixels in range 0-255 
histg = cv2.calcHist([img],[0],None,[256],[0,256])      #using open cv
plt.plot(histg)
plt.show()



#image equalization or contrast setting
equ = cv2.equalizeHist(img) 
  
equalized = cv2.calcHist([equ],[0],None,[256],[0,256])      #using open cv
plt.plot(equalized)
plt.show()


cv2.imshow('Original image', img) 
cv2.waitKey(0) 

cv2.imshow('After Equalisation', equ) 
cv2.waitKey(0) 


cv2.destroyAllWindows()