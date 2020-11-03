import cv2
import numpy as np

img = cv2.imread('shapes.PNG') 
img= cv2.resize(img, (img.shape[1]*200//100,img.shape[0]*200//100),cv2.INTER_NEAREST)

cv2.imshow('Original Image', img) 
cv2.waitKey(0)

# Convert the img to grayscale 
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
  
# Apply edge detection method on the image 
#gaussian blur t0 reduce noise
#Gradient calculation
#nonmaximum suprression will thin out the edges
#double thresholding will detect pixels varying from strong, medium and weak
#edge tracking by hysteresis will transform weak pixels into stronger ones

edges = cv2.Canny(gray,50,150,apertureSize = 3) 
cv2.imshow('Canny Image', edges) 
cv2.waitKey(0)

  
lines = cv2.HoughLines(edges,1,np.pi/180, 200) 

  
for r,theta in lines[0]:       
    a = np.cos(theta) 
    b = np.sin(theta) 
    x0 = a*r 
    y0 = b*r 
    x1 = int(x0 + 1000*(-b)) 
    y1 = int(y0 + 1000*(a)) 
    x2 = int(x0 - 1000*(-b)) 
    y2 = int(y0 - 1000*(a))   
    cv2.line(img,(x1,y1), (x2,y2), (0,0,255),2) 

      
cv2.imshow('linesDetected', img) 
cv2.waitKey(0)
cv2.destroyAllWindows()
