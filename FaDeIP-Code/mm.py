from Tkinter import *
import cv2
import numpy as np
import pyautogui, sys
from win32api import GetSystemMetrics
import pyautogui
from math import sqrt
import thread
import time

class mm(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        inst = '''Mouse Control
        Use Blue Color Circle to Control
        Hold Circle for 5 - 10 second to Click
        Click on Start       



















        '''
        self.flag = True
        def funn():
            thread.start_new_thread(self.mouseMotion, ())
        
        def funn1():
            self.flag = False
            time.sleep(1)
            parent.destroy()
            
        self.logo = PhotoImage(file="mouse.gif")
        self.label = Label(self, image=self.logo, compound = CENTER, text = inst)
        self.label.pack()
        Button(self, text="START", bg='yellow', command=funn).pack(fill=X)
        Button(self, text="EXIT", bg='yellow', command=funn1).pack(fill=X)
        
    def mouseMotion(self):
        width = GetSystemMetrics(0)
        height = GetSystemMetrics(1)

        # Create a black image, a window
        cap = cv2.VideoCapture(0)
        cap.set(3, width)
        cap.set(4, height)
        kernel = np.ones((5,5),np.uint8)
        sttImage = cv2.imread("people.jpg")
        count = 0

        while(cap.isOpened()):
            # Take each frame
            _, frame = cap.read()
            frame = cv2.flip(frame, 1)
            # Convert BGR to HSV
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


            # define range of blue color in HSV
            lower = np.array([110,75, 54])
            upper = np.array([144,164,147])

            # Threshold the HSV image to get only blue colors
            mask = cv2.inRange(hsv, lower, upper)

            erosion = cv2.erode(mask,kernel,iterations = 2)

            # Bitwise-AND mask and original image
            mask = cv2.dilate(erosion,kernel,iterations = 7)

            res = cv2.bitwise_and(frame,frame, mask= mask)

            cimg = cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)

            circles = cv2.HoughCircles(cimg,cv2.HOUGH_GRADIENT,1,20, param1=50,param2=30,minRadius=10,maxRadius=100)
            if(circles is None):
                x1, y1 = pyautogui.position()
                x1 = int(x1)
                y1 = int(y1)
            else:    
                circles = np.uint16(np.around(circles))

                for i in circles[0,:]:
                    # draw the outer circle
                    pyautogui.moveTo(i[0], i[1])
                    x2,y2= i[0], i[1]
                    x1 = int(x2)
                    y1 = int(y2)
                    dist=sqrt((x2-x1)**2 + (y2-y1)**2)
                    if dist > 100:
                        count = 0
                        (x1, y1) = (x2, y2)
                    else:
                        count += 1

                    if(count > 50 and dist < 50):		
                            pyautogui.click(button='left')
                            pyautogui.click(button='left')
                            count = 0

                    #cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)

            #cv2.imshow('detected circles',cimg)

            #cv2.imshow('frame',frame)
            #cv2.imshow('mask',mask)
            #cv2.imshow('res',res)
            #cv2.imshow('Hold', sttImage)
            
            if self.flag == False:
                break
            
            if cv2.waitKey(5) & 0xFF == ord('q'):
                cv2.destroyWindow('Hold')
                break
        cap.release()
        #cv2.destroyAllWindows()
S