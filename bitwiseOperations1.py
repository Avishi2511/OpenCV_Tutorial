import numpy as np
import cv2

#black rectangle 
img1= np.zeros((250,500,3), np.uint8)
#dimensions->(200,0),(300,100) color->(255,255,255), thickness-> -1(rectangle will be filled from white color)
img1=cv2.rectangle(img1, (200,0), (300,100), (255,255,255), -1) 
img2= cv2.imread("image_1.png")

#bitwise_and-> 0&0=0, 0&1=0 so on.(0->black, 1->white)
#bitwise_or-> 0+0=0 so on
bitAnd = cv2.bitwise_and(img2, img1)
bitOr = cv2.bitwise_or(img2,img1)
bitXor=cv2.bitwise_xor(img2,img1)
bitNot1=cv2.bitwise_not(img1)
bitNot2=cv2.bitwise_not(img2)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
#cv2.imshow('bitAnd', bitAnd)
#cv2.imshow('bitAnd', bitOr)
#cv2.imshow('bitAnd', bitXor)
cv2.imshow('bitNot1',bitNot1)
cv2.imshow('bitNot2',bitNot2)

cv2.waitKey(0)
cv2.destroyAllWindows()