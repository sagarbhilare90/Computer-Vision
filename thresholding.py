import cv2  
import numpy as np  

image1 = cv2.imread('monkey.jpg')  

cv2.imshow('original image', image1) 
cv2.waitKey(0)

width=image1.shape[1]*50//100
height=image1.shape[0]*30//100

#creating new image matrix resized with different interpolation
dim=(width,height)
resized_NEAREST= cv2.resize(image1,dim,cv2.INTER_NEAREST)

cv2.imshow('REDUCED IMAGE', resized_NEAREST) 
cv2.waitKey(0)


img = cv2.cvtColor(resized_NEAREST, cv2.COLOR_BGR2GRAY) 
  
ret, thresh1 = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY) 
ret, thresh2 = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY_INV) 
ret, thresh3 = cv2.threshold(img, 150, 255, cv2.THRESH_TRUNC) 
ret, thresh4 = cv2.threshold(img, 150, 255, cv2.THRESH_TOZERO) 
ret, thresh5 = cv2.threshold(img, 150, 255, cv2.THRESH_TOZERO_INV) 
ret, thresh6 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)      
  
thresh7 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 199, 5) 
  
thresh8 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 199, 5) 

    
cv2.imshow('Binary Threshold', thresh1) 
cv2.waitKey(0)

cv2.imshow('Binary Threshold Inverted', thresh2) 
cv2.waitKey(0)


cv2.imshow('Truncated Threshold', thresh3) 
cv2.waitKey(0)


cv2.imshow('Set TOZERO', thresh4) 
cv2.waitKey(0)

cv2.imshow('Set TOZERO_Inverted', thresh5) 
cv2.waitKey(0)

  
cv2.imshow('OTSU Thresholding', thresh6) 
cv2.waitKey(0)

cv2.imshow('Adaptive Mean', thresh7) 
cv2.waitKey(0)

cv2.imshow('Adaptive Gaussian', thresh7) 
cv2.waitKey(0)



cv2.destroyAllWindows()  
