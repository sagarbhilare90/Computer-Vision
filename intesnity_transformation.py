import cv2 
import numpy as np 
  
# Open the image. 
img = cv2.imread('cup2.jpg') 

img= cv2.resize(img, (img.shape[1]*50//100,img.shape[0]*50//100),cv2.INTER_NEAREST)

# Apply log transform. 
c = 255/(np.log(1 + np.max(img))) 
log_transformed = c * np.log(1 + img) 
  
# Specify the data type. 
log_transformed = np.array(log_transformed, dtype = np.uint8)
gamma_corrected1 = np.array(255*(img / 255) ** 0.1, dtype = 'uint8') 
gamma_corrected2 = np.array(255*(img / 255) ** 0.5, dtype = 'uint8') 
gamma_corrected3 = np.array(255*(img / 255) ** 1.0, dtype = 'uint8') 
gamma_corrected4 = np.array(255*(img / 255) ** 1.5, dtype = 'uint8') 
gamma_corrected5 = np.array(255*(img / 255) ** 2.5, dtype = 'uint8') 

 


cv2.imshow("original image", img)
cv2.waitKey(0)
  
cv2.imshow("Transformed image", log_transformed)
cv2.waitKey(0)

cv2.imshow("GAMMA 0.1 image", gamma_corrected1)
cv2.waitKey(0)
cv2.imshow("GAMMA 0.5 image", gamma_corrected2)
cv2.waitKey(0)
cv2.imshow("GAMMA 1.0 image image", gamma_corrected3)
cv2.waitKey(0)
cv2.imshow("GAMMA 1.5 image image", gamma_corrected4)
cv2.waitKey(0)
cv2.imshow("GAMMA 2.5 image image", gamma_corrected5)
cv2.waitKey(0)

cv2.destroyAllWindows()