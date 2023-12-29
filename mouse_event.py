import numpy as np
import cv2

#for finding all event
#events={i for i in dir(cv2) if 'EVENT' in i}
#print(events)

def click_event(event, x, y, flags, param):

    #when left button 
    if event==cv2.EVENT_LBUTTONDOWN:
        print(x, ', ',y)
        font=cv2.FONT_HERSHEY_COMPLEX
        strXY=str(x)+', '+str(y)
        cv2.putText(img, strXY, (x,y), font, 1, (255,255,0), 2)
        cv2.imshow('image', img)
    
    if event==cv2.EVENT_RBUTTONDOWN:
        blue=img[y,x,0]
        green=img[y,x,1]
        red=img[y,x,2]
        font=cv2.FONT_HERSHEY_COMPLEX
        strXY=str(x)+str(y)

#creates black screen of 512,512 size having unit8 as data type
img=np.zeros((512,512,3), np.uint8)
cv2.imshow('image', img)

#for calling click_event function defined earlier
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()