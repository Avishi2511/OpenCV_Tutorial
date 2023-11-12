import cv2

# 1->color image
# 0->grayscale image 
img=cv2.imread('lena.jpg', 1)

#to know if img name is correct -> print(img)

cv2.imshow('image',img) #to show image
cv2.waitKey(5000) #5000->time after which img will disappear(if 0 doesnt disappear)
cv2.destroyWindow

cv2.imwrite('lena_copy.png', img) #copy file