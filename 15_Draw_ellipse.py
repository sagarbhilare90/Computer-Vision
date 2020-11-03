import cv2  
    
    
# Reading an image in default mode 
image = cv2.imread('white.jpg') 
    
# Window name in which image is displayed 
window_name = 'Image'
   
center_coordinates = (700, 300) 
  
axesLength = (200, 100) 
  
angle = 20
  
startAngle = 0
  
endAngle = 360
   
# Red color in BGR 
color = (0, 0, 255) 
   
# Line thickness of 5 px 
thickness = 5
   
# Using cv2.ellipse() method 
# Draw a ellipse with red line borders of thickness of 5 px 
image = cv2.ellipse(image, center_coordinates, axesLength, 
           angle, startAngle, endAngle, color, thickness) 

image = cv2.ellipse(image, center_coordinates, axesLength, 
          110, startAngle, endAngle, (0,255,0), thickness) 

image = cv2.circle(image, center_coordinates, 1, (0,0,255), 3)
image = cv2.circle(image, center_coordinates, 200, (255,0,0), thickness)
image = cv2.circle(image, center_coordinates, 100, (255,0,0), thickness)
   
# Displaying the image  
cv2.imshow(window_name, image)  
cv2.waitKey(0)
cv2.destroyAllWindows()
