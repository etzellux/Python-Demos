import cv2
import numpy as np


#VARIABLES

drawing = False
ix,iy = -1,-1



#FUNCTION
def draw_rectangle(event,x,y,flags,param):
    
    global drawing,ix,iy
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img,(ix,iy),(x,y),color=(0,0,255),thickness=-1)
            
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img,(ix,iy),(x,y),color=(0,0,255),thickness=-1)



#SHOWING THE IMAGE

img = np.zeros((512,512,3))

cv2.namedWindow(winname="my_drawing")

cv2.setMouseCallback("my_drawing",draw_rectangle)

while True:
    cv2.imshow("my_drawing",img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()