import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread("original/Computer-Vision-with-Python/DATA/dog_backpack.jpg")

def draw_circle(event,x,y,flags,param):
    cv2.putText(img,"Helloooo!",org=(20,200),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=2,color=(0,255,0),thickness=3)
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),50,color=(0,0,255),thickness=4)
        
cv2.namedWindow(winname="Image1")

cv2.setMouseCallback("Image1",draw_circle)

while True:
    
    cv2.imshow("Image1",img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()