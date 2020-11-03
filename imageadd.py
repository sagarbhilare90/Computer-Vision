import cv2

triangles= cv2.imread('triangles.jpg',1)
circles= cv2.imread('circles.jpg',1)

added_image= cv2.add(triangles,circles)
weighted_add= cv2.addWeighted(triangles,0.7,circles,0.3,0)

cv2.imshow('triangles', triangles)
cv2.waitKey(0)

cv2.imshow('Circles', circles)
cv2.waitKey(0)

cv2.imshow('added image', added_image)
cv2.waitKey(0)

cv2.imshow('Weighted addition', weighted_add)
cv2.waitKey(0)

cv2.destroyAllWindows()