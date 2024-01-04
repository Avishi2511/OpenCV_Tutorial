#changed original image
import numpy as np
import cv2

img = cv2.imread('messi5.jpg')
img2= cv2.imread('opencv-logo.png')

print(img.shape) #returns tupple of rows,columns and channels
print(img.size) #returns total no of pixels
print(img.dtype) #returns image datatype
b,g,r=cv2.split(img) #splits img in b,g and r
img=cv2.merge((b,g,r))

#working on roi(region of interest)
ball= img[280:340, 330:390] #copying ball from an roi in image
img[273:333, 100:160] = ball #pasting ball in image


#adding two images(size of images must be same)
img = cv2.resize(img, (512,512))
img2 = cv2.resize(img2, (512,512))
#dst = cv2.add(img, img2)
#weight is between 0 and 1, scalar value(img gets brighter)=0
dst = cv2.addWeighted(img, 0.9, img2, 0.1, 0)

#cv2.imshow('image', img)
cv2.imshow('image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows