#create and join points with a line
import numpy as np
import cv2

def click_event(event, x, y, flags, param):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 20, (0,0,255), -1)
        # 20 represents size of points that are circular
        points.append((x,y))
        if len(points) >= 2:
            cv2.line(img, points[-1], points[-2], (255, 0, 0), 5) 
            # -1 & -2 are last and second last element of array of points since they are to be joined
        cv2.imshow('image', img)

#img= np.zeros((512,512,3), np.uint8)
img=cv2.imread('lena.jpg')
cv2.imshow('image', img)
points=[]
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows