import cv2

cap=cv2.VideoCapture(0) #0->webcam no(can be diff for all systems)
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))
#VideoWriter->to create a video 
#20->no of frames per sec,
#(640,480)->size in which we are capturing

while (cap.isOpened()):
    ret, frame=cap.read() #ret->return frame->object that is read if return gives true

    #cv2.imshow('frame',frame) #for original color video

    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    out.write(frame) 

    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)

    if cv2.waitKey(1) & 0xff==ord('q'): #if q key is pressed loop will break, window closes
        break

cap.release()
out.release()
cv2.destroyAllWindows()
