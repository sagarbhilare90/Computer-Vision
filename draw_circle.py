import cv2 
   
   
# Reading an image in default mode
image = cv2.imread('white.jpg')
   
# Window name in which image is displayed
window_name = 'Image'
  
# Center coordinates
center_coordinates = (700, 300)
 
# Radius of circle
radius = 200
  
# Blue color in BGR
color = (255, 0, 0)
  
# Line thickness of 2 px
thickness = 2
  
# Using cv2.circle() method
# Draw a circle with blue line borders of thickness of 2 px
image = cv2.circle(image, center_coordinates, radius, color, thickness)
image = cv2.circle(image, center_coordinates, 1, (0,0,255), 3)
 
# Displaying the image 
cv2.imshow(window_name, image)  
cv2.waitKey(0)
cv2.destroyAllWindows()
