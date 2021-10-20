import cv2
import numpy as np
from pynput.mouse import Button ,Controller
import wx

mouse=Controller()

app=wx.App(False)
(sx,sy)=wx.GetDisplaySize()
(camx,camy)=(320,240)
cap=cv2.VideoCapture(0)
cap.set(3,camx)
cap.set(4,camy)


lower_g=np.array([33,70,30])
upper_g=np.array([102,255,255])


kernelOpen=np.ones((5,5))
kernelClose=np.ones((20,20))

mLocOld=np.array([0,0])
mouseLoc=np.array([0,0])

DampingFactor=2

isPressed=0
openx,openy,openw,openh=(0,0,0,0)

while True:

    ret,img=cap.read()

    img=cv2.resize(img,(340,220))
    imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(imgHSV,lower_g,upper_g)

    new_mask=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
    another_mask=cv2.morphologyEx(new_mask,cv2.MORPH_CLOSE,kernelClose)
    final_mask=another_mask
    
    conts,h=cv2.findContours(final_mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)


    if(len(conts)==2):
        if(isPressed==1):
            isPressed=0
            mouse.release(Button.left)
        x1,y1,w1,h1=cv2.boundingRect(conts[0])
        x2,y2,w2,h2=cv2.boundingRect(conts[1])
        cv2.rectangle(img,(x1,y1),(x1+w1,y1+h1),(255,0,0),2)
        cv2.rectangle(img,(x2,y2),(x2+w2,y2+h2),(255,0,0),2)


        cx1=int(x1+w1/2)
        cy1=int(y1+h1/2)
        cx2=int(x2+w2/2)
        cy2=int(y2+h2/2)
        cv2.line(img,(cx1,cy1),(cx2,cy2),(255,0,0),2)

        
        clx=int((cx1+cx2)/2)
        cly=int((cy1+cy2)/2)
        cv2.circle(img,(clx,cly),2,(0,0,255),2)

        
        mouseLoc=mLocOld+((clx,cly)-mLocOld)/DampingFactor
        mouse.position=(sx-int((mouseLoc[0]*sx)/camx),int((mouseLoc[1]*sy)/camy))
        while mouse.position!=(sx-int((mouseLoc[0]*sx)/camx),int((mouseLoc[1]*sy)/camy)):
            pass

        
        mLocOld=mouseLoc

        
        openx,openy,openw,openh=cv2.boundingRect(np.array([[[x1,y1],[x1+w1,y1+h1],[x2,y2],[x2+w2,y2+h2]]]))

    
    elif(len(conts)==1):
        x,y,w,h=cv2.boundingRect(conts[0])

    
        if(isPressed==0):

            if(abs((w*h-openw*openh)*100/(w*h))<30): 
                isPressed=1                          
                mouse.press(Button.left)
                openx,openy,openw,openh=(0,0,0,0)

    
        else:
    
            x,y,w,h=cv2.boundingRect(conts[0])
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    
            cx=int(x+w/2)
            cy=int(y+h/2)
            cv2.circle(img,(cx,cy),int((w+h)/4),(0,0,255),2)

            mouseLoc=mLocOld+((cx,cy)-mLocOld)/DampingFactor
            mouse.position=(sx-int((mouseLoc[0]*sx)/camx),int((mouseLoc[1]*sy)/camy))
            while mouse.position!=(sx-int((mouseLoc[0]*sx)/camx),int((mouseLoc[1]*sy)/camy)):
                pass
            mLocOld=mouseLoc
    
    cv2.imshow("Virtual mouse",img)

    if cv2.waitKey(1) & 0xFF==ord('w'):
        break

cap.release()
cv2.destroyAllWindows()