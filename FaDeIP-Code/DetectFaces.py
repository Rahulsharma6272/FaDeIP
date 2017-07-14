import numpy as np
import cv2
from Tkinter import *
import tkMessageBox
import webbrowser
from tkFileDialog import askopenfilename
from tkMessageBox import showerror
import FadeIPMenu
import ScrollText
import time
sppp = 41
speed = 41
class secondWindow (Frame):
    
    def __init__(self, parent):
	
	Frame.__init__(self, parent)
        self.parent = parent
	Label(self,text="Welcome To FaDeIP", bg="yellow", fg="blue", font = "Chiller 22 bold").pack(fill = X)
        buttonFrame = Frame(self,  bd = 2, relief = SUNKEN)
        buttonFrame.pack(pady=20)
        Button(buttonFrame, text="Image Capture", width=15, height=2, command=self.liveImageFace).grid(row=0, column = 0, padx = 10, pady = 3)
        Button(buttonFrame, text="Open Image", width=15, height=2, command=self.detImageFace).grid(row=0, column = 1, padx = 10, pady = 3)
        Button(buttonFrame, text="Video Capture", width=15, height=2, command=self.detFaceVideoWebCam).grid(row=1, column = 0, padx = 10, pady = 3)
        Button(buttonFrame, text="Open Video", width=15, height=2, command=self.detFaceVideoBrowse).grid(row=1, column = 1, padx = 10, pady = 3)
        
        v = IntVar()
        v.set(1)
        radioButtonFrame = Frame(self)
        radioButtonFrame.pack(fill=X)
        def radioFun():
            if v.get() == 1:
                self.xmlFileName = 'casXML\haarcascades\haarcascade_frontalface_default.xml'
            elif v.get() == 2:    
                self.xmlFileName = 'casXML\haarcascades\HS.xml'

        radioFun()
        
        Radiobutton(radioButtonFrame, text="Only Face", variable = v, command = radioFun, value=1).grid(row = 0, column = 0)
        Radiobutton(radioButtonFrame, text="Face & Shoulder", variable = v, command = radioFun, value=2).grid(row = 0, column = 1)
        
        
        
        
        
        Button(self, text="Quit", width=15, height=2,bg = 'yellow', command=parent.destroy).pack(fill=X)
        



    def detImageFace(self):
        #face_cascade = cv2.CascadeClassifier('C:\opencv\sources\data\haarcascades\haarcascade_frontalface_default.xml')
        fileName = askopenfilename()
        if fileName == '':
            showerror("Error", "No file selected.\nTry Again")
            ScrollText.sc.appendStatusText("File Not selected. Try Again")
            return
        
        
        face_cascade = cv2.CascadeClassifier(self.xmlFileName)
        img = cv2.imread(fileName)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        count = 0
        #for (x,y,w,h) in faces:

        #    imga = img[y:y+h, x:x+w]

        #    name = "C:\Users\Kapil\Desktop\pic\img%d.jpg"%count

        #    print name
        #    count+=1
        #    cv2.imwrite(name, imga)

        for (x,y,w,h) in faces:
            count += 1
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        h,w,z = img.shape
        cv2.putText(img,'Face Detected %d'%count,(10, 30), font, .7,(255,255,255),1,cv2.LINE_AA)
        cv2.putText(img,time.strftime("%d/%m/%Y  %H:%M:%S "),(w - 350,h - 20), font, .7,(255,255,255),1,cv2.LINE_AA)

        cv2.imshow('Face Detection',img)
        cv2.waitKey(0)
        cv2.destroyWindow('Face Detection')
        self.parent.focus_force()
    
    def liveImageFace(self):
        self.parent.focus_force()
        pass


    def detFaceVideoWebCam(self):
        global sppp
        face_cascade = cv2.CascadeClassifier(self.xmlFileName)
        cap = cv2.VideoCapture(0)
        while cap.isOpened():

            ret, img = cap.read()
            if ret == True:
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                count = 0
                for (x,y,w,h) in faces:
                    count += 1
                    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                font = cv2.FONT_HERSHEY_SIMPLEX
                h,w,z = img.shape
                cv2.putText(img,'Face Detected %d'%count,(10, 30), font, .7,(255,255,255),1,cv2.LINE_AA)
                cv2.putText(img,time.strftime("%d/%m/%Y  %H:%M:%S "),(w - 350,h - 20), font, .7,(255,255,255),1,cv2.LINE_AA)
                cv2.imshow('Face Detection',img)
                if cv2.waitKey(sppp) & 0xFF == ord('q'):
                    break
        cv2.destroyWindow('Face Detection')
        self.parent.focus_force()
        
    def detFaceVideoBrowse(self):
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
        
        
        
        face_cascade = cv2.CascadeClassifier(self.xmlFileName)
        cap = cv2.VideoCapture(fileName)
        while cap.isOpened():

            ret, img = cap.read()
            if img is None:
                break
            if ret == True:
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                count = 0
                for (x,y,w,h) in faces:
                    count += 1
                    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

                #font = cv2.FONT_HERSHEY_SIMPLEX
                #h,w,z = img.shape
                #cv2.putText(img,'Face Detected %d'%count,(10, 30), font, .7,(255,255,255),1,cv2.LINE_AA)
                #cv2.putText(img,time.strftime("%d/%m/%Y  %H:%M:%S "),(w - 350,h - 20), font, .7,(255,255,255),1,cv2.LINE_AA)
                
                font = cv2.FONT_HERSHEY_SIMPLEX
                h,w,z = img.shape
                cv2.putText(img,'Face Detected %d'%count,(10, 30), font, .7,(255,255,255),1,cv2.LINE_AA)
                cv2.putText(img,time.strftime("%d/%m/%Y  %H:%M:%S "),(w - 350,h - 20), font, .7,(255,255,255),1,cv2.LINE_AA)
                

                cv2.imshow('Face Detection',img)
                
                
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

                
        cv2.destroyWindow('Face Detection')
        self.parent.focus_force()
