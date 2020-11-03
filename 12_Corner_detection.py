import numpy as np 
import cv2 
from matplotlib import pyplot as plt 
  
  
# read the image 
img = cv2.imread('hexagons.PNG') 
  
# convert image to gray scale image 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
  

#Shi-Tomasi Method
corners1 = cv2.goodFeaturesToTrack(gray, 30, 0.01, 10) 

#Visualise Corner detection using SHI-Tomasi method
for i in corners1: 
    x, y = i.ravel() 
    cv2.circle(img, (x, y), 1, (105, 0, 200), 3) 
plt.title('SHI-Tomasi Method')

plt.imshow(img)
plt.show() 

#Harris corner Detection
operatedImage = np.float32(gray) 
dest = cv2.cornerHarris(operatedImage, 2, 5, 0.1) 
cv2.imshow('After Harris method', dest) 
cv2.waitKey(0)

dest = cv2.dilate(dest, None) 
img[dest > 0.01 * dest.max()]=[0, 0,255] 

#Visualise Corner detection using Harris method
cv2.imshow('Dilated image', dest) 
cv2.waitKey(0)
cv2.imshow('Harris Method', img) 



cv2.waitKey(0)
cv2.destroyAllWindows()
