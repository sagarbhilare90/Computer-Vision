import cv2 
      
# Reading an image in default mode 
image = cv2.imread('white.jpg') 
    
# Window name in which image is displayed 
window_name = 'Image'
  
  
# org 
org = (50, 50) 
org1 = (200, 200) 
org2 = (350, 350) 
org3 = (600, 400) 
org4 = (700, 300) 
  
# fontScale 
fontScale = 1
   
# Blue color in BGR 
color = (255, 0, 0) 
  
# Line thickness of 2 px 
thickness = 2
   
# Using cv2.putText() method 
image = cv2.putText(image, 'FONT_HERSHEY_SIMPLEX', org, cv2.FONT_HERSHEY_SIMPLEX,  
                   fontScale, color, thickness) 
image = cv2.putText(image, 'FONT_HERSHEY_PLAIN', org1, cv2.FONT_HERSHEY_PLAIN,  
                   fontScale, color, thickness) 
image = cv2.putText(image, 'FONT_HERSHEY_DUPLEX', org2, cv2.FONT_HERSHEY_DUPLEX,  
                   fontScale, color, thickness) 
image = cv2.putText(image, 'FONT_HERSHEY_COMPLEX', org3, cv2.FONT_HERSHEY_COMPLEX,  
                   fontScale, color, thickness) 
image = cv2.putText(image, 'FONT_HERSHEY_TRIPLEX', org4, cv2.FONT_HERSHEY_TRIPLEX,  
                   fontScale, color, thickness) 
  
# Displaying the image 
cv2.imshow(window_name, image)  
cv2.waitKey(0)
cv2.destroyAllWindows()
