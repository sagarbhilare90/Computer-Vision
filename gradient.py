import numpy as np
import cv2

#read the image
image= cv2.imread("minions.jpg")

width=image.shape[1]*50//100
height=image.shape[0]*40//100

#creating new image matrix resized with different interpolation
dim=(width,height)
resized_NEAREST= cv2.resize(image,dim,cv2.INTER_NEAREST)


hsv = cv2.cvtColor(resized_NEAREST, cv2.COLOR_BGR2HSV)
    
lower_red = np.array([50,150,50])
upper_red = np.array([255,255,180])
mask = cv2.inRange(hsv, lower_red, upper_red)
#res = cv2.bitwise_and(resized_NEAREST,resized_NEAREST, mask= mask)
kernel = np.ones((5,5),np.uint8)

gradient = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)

cv2.imshow('Original',resized_NEAREST)
cv2.waitKey(0)
 
cv2.imshow('Gradient', gradient) 
cv2.waitKey(0)

cv2.destroyAllWindows()

