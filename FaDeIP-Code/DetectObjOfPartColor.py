import cv2
import numpy as np
from tkFileDialog import askopenfilename
from tkMessageBox import showerror
import ScrollText
from Tkinter import *
import tkMessageBox
import FileName
import FadeIPMenu
import time

speed = 41
sppp = 41
class secondWindow(Frame) :
    def __init__(self, parent):
	
	Frame.__init__(self, parent)
        self.parent = parent

        #self.geometry("300x200")
        #self.resizable(width=False,height=False)
	#self.title("FaDiP-a Soluion for mulitmedia world")
	
        Label(self,text="Welcome To FaDeIP", bg="yellow", fg="blue", font = "Chiller 22 bold").pack(fill = X)
        
        buttonFrame = Frame(self,  bd = 2, relief = SUNKEN)
        buttonFrame.pack(pady=20)
        Button(buttonFrame, text="Image Capture", width=15, height=2, command=self.capImage).grid(row=0, column = 0, padx = 10, pady = 3)
        Button(buttonFrame, text="Open Image", width=15, height=2, command=self.openImage).grid(row=0, column = 1, padx = 10, pady = 3)
        Button(buttonFrame, text="Video Capture", width=15, height=2, command=self.capVideo).grid(row=1, column = 0, padx = 10, pady = 3)
        Button(buttonFrame, text="Open Video", width=15, height=2, command=self.openVideo).grid(row=1, column = 1, padx = 10, pady = 3)
        
        def setColor():
            if self.var.get() == "Red":
                self.min_H = 0
                self.max_H = 10

                self.min_S = 100
                self.max_S = 255

                self.min_V = 100
                self.max_V = 255
                
            elif self.var.get() == "Green":
                self.min_H = 50
                self.max_H = 70

                self.min_S = 100
                self.max_S = 255

                self.min_V = 100
                self.max_V = 255
                
            elif self.var.get() == "Blue":
                self.min_H = 110
                self.max_H = 130

                self.min_S = 100
                self.max_S = 255

                self.min_V = 100
                self.max_V = 255
                
            elif self.var.get() == "Yellow":
                self.min_H = 20
                self.max_H = 40

                self.min_S = 100
                self.max_S = 255

                self.min_V = 100
                self.max_V = 255
                
            elif self.var.get() == "Cyan":
                self.min_H = 80
                self.max_H = 100

                self.min_S = 100
                self.max_S = 255

                self.min_V = 100
                self.max_V = 255
                
            elif self.var.get() == "Magenta":
                self.min_H = 140
                self.max_H = 160

                self.min_S = 100
                self.max_S = 255

                self.min_V = 100
                self.max_V = 255
                
           
        frame = Frame(self)
        frame.pack(fill=X)
        
        self.var = StringVar()
        self.var.set("Red") # initial value
        
        setColor()
        
        ops = ["Red", "Green", "Blue", "Yellow", "Cyan", "Magenta"]
        
        option = OptionMenu(frame, self.var, *ops )
        option.config(width = 17)
        option.grid(row = 0, column = 0)
        
        Button(frame, text = "Set Color", width = 19, command = setColor).grid(row = 0, column = 1)

        Button(self, text="EXIT", width=15, height=2,bg="yellow",fg="blue", command=parent.destroy).pack(fill=X)
    
    def openImage(self):
        fileName = askopenfilename()
        if fileName == '':
            showerror("Error", "No file selected.\nTry Again")
            ScrollText.sc.appendStatusText("File Not selected. Try Again")
            return
        kernel = np.ones((5,5),np.uint8)
        img = cv2.imread(fileName,1)
        ScrollText.sc.appendStatusText("Image Opened:-%s"%fileName)

        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


        # define range of blue color in HSV
        lower = np.array([self.min_H,self.min_S, self.min_V])
        upper = np.array([self.max_H,self.max_S,self.max_V])

        # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(hsv, lower, upper)
        res = cv2.bitwise_and(img,img, mask= mask)
        cv2.imshow('Detected Color', res)
        cv2.imshow("Image :- %s"%fileName, img)
        cv2.waitKey(0)
        cv2.destroyWindow("Image :- %s"%fileName)
        self.parent.focus_force()
    
    
    def capImage(self):
        global sppp
        cap = cv2.VideoCapture(0)
        kernel = np.ones((5,5),np.uint8)

        while(cap.isOpened()):
            # Take each frame
            _, frame = cap.read()
            frame = cv2.flip(frame, 1)
            # Convert BGR to HSV
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


            # define range of blue color in HSV
            lower = np.array([self.min_H,self.min_S, self.min_V])
            upper = np.array([self.max_H,self.max_S,self.max_V])

            # Threshold the HSV image to get only blue colors
            mask = cv2.inRange(hsv, lower, upper)
            
            res = cv2.bitwise_and(frame,frame, mask= mask)
            
            font = cv2.FONT_HERSHEY_SIMPLEX  
            h,w,z = res.shape
            cv2.putText(res,time.strftime("%d/%m/%Y  %H:%M:%S "),(w - 350,h - 20), font, .7,(255,255,255),1,cv2.LINE_AA)
            
            cv2.imshow('frame',frame)
            #cv2.imshow('mask',mask)
            cv2.imshow('res',res)
            if cv2.waitKey(sppp) & 0xFF ==ord('s'):
                outputFileName = FileName.getNewFileName("colorObjDetected", "colObj", ".jpg")
                
                cv2.imwrite(outputFileName,res)
                #cv2.imshow('image',image)
                ScrollText.sc.appendStatusText("Image Saved:-%s"%outputFileName)
                if cv2.waitKey(0) & 0xFF ==ord('q'):
                    break
                break
        cv2.destroyAllWindows()
        cap.release()
       	
        self.parent.focus_force()
    
    def capVideo(self):
        global sppp
        cap = cv2.VideoCapture(0)
        kernel = np.ones((5,5),np.uint8)

        while(cap.isOpened()):
            # Take each frame
            _, frame = cap.read()
            frame = cv2.flip(frame, 1)
            # Convert BGR to HSV
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            # define range of blue color in HSV
            lower = np.array([self.min_H,self.min_S, self.min_V])
            upper = np.array([self.max_H,self.max_S,self.max_V])

            # Threshold the HSV image to get only blue colors
            mask = cv2.inRange(hsv, lower, upper)

            res = cv2.bitwise_and(frame,frame, mask= mask)
            
            font = cv2.FONT_HERSHEY_SIMPLEX  
            h,w,z = res.shape
            cv2.putText(res,time.strftime("%d/%m/%Y  %H:%M:%S "),(w - 350,h - 20), font, .7,(255,255,255),1,cv2.LINE_AA)
            
            
            cv2.imshow('frame',frame)
            #cv2.imshow('mask',mask)
            cv2.imshow('res',res)
            k = cv2.waitKey(sppp) & 0xFF
            if k == ord('q') or k == ord('Q'):
                break
        cap.release()
        cv2.destroyAllWindows()
    
    def openVideo(self):
        global speed
        fileName = askopenfilename()
        if fileName == '':
            showerror("Error", "No file selected.\nTry Again")
            ScrollText.sc.appendStatusText("File Not selected. Try Again")
            return
        if not fileName.endswith(".avi"):
            showerror("Error", "Not valid Format.")
            ScrollText.sc.appendStatusText("Invalid File Format:-%s"%fileName)
            return
        
        cap = cv2.VideoCapture(fileName)
        kernel = np.ones((5,5),np.uint8)

        while(cap.isOpened()):
            # Take each frame
            _, frame = cap.read()
            frame = cv2.flip(frame, 1)
            # Convert BGR to HSV
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            # define range of blue color in HSV
            lower = np.array([self.min_H,self.min_S, self.min_V])
            upper = np.array([self.max_H,self.max_S,self.max_V])

            # Threshold the HSV image to get only blue colors
            mask = cv2.inRange(hsv, lower, upper)

            res = cv2.bitwise_and(frame,frame, mask= mask)

            cv2.imshow('frame',frame)
            #cv2.imshow('mask',mask)
            cv2.imshow('res',res)
            
            key = cv2.waitKey(speed)
            if key == ord('q') or key == ord('Q'):
                cv2.destroyAllWindows()
                break
            elif key == ord('f') or key == ord('F'):
                if speed > 1:
                    speed -= 5
            elif key == ord('g') or key == ord('G'):
                if speed < 1000:
                    speed += 5
        cap.release()
        cv2.destroyAllWindows()
        self.parent.focus_force()
