import numpy as np
import cv2
from Tkinter import *
import tkMessageBox
from tkFileDialog import askopenfilename
from tkMessageBox import showerror
import webbrowser
import FileName
import ScrollText
import FadeIPMenu
import time
sppp = 41
speed = 41
class secondWindow(Frame): 
    def __init__(self, parent):
	Frame.__init__(self,parent)
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
        
        Button(self, text="EXIT", width=15, height=2,bg='yellow', command=parent.destroy).pack(fill=X)
        
	
    def detImageFace(self):
        fileName = askopenfilename()
        if fileName == '':
            showerror("Error", "No file selected.\nTry Again")
            ScrollText.sc.appendStatusText("File Not selected. Try Again")
            return
        
        
        #face_cascade = cv2.CascadeClassifier('C:\opencv\sources\data\haarcascades\haarcascade_frontalface_default.xml')
        face_cascade = cv2.CascadeClassifier(self.xmlFileName)
        img = cv2.imread(fileName)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        count = 1
        for (x,y,w,h) in faces:

            imga = img[y:y+h, x:x+w]

            name = FileName.getNewFileName("ExtractedFaces", "ExtFace", ".jpg")

            ScrollText.sc.appendStatusText("Image saved :- %s"%name)
            count+=1
            cv2.imwrite(name, imga)

        for (x,y,w,h) in faces:
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

        cv2.imshow('img',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        self.parent.focus_force()
        
    def liveImageFace(self):
        global sppp
        face_cascade = cv2.CascadeClassifier(self.xmlFileName)
        cap = cv2.VideoCapture(0)
        while cap.isOpened():

            ret, img = cap.read()
            if ret == True:
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                flag = False
                for (x,y,w,h) in faces:
                    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                    flag = True
                    
                cv2.imshow('Capture Face',img)
                if cv2.waitKey(sppp) & 0xFF == ord('s'):
                    if not flag:
                        continue
                    count = 1
                    for (x,y,w,h) in faces:

                        imga = img[y:y+h, x:x+w]

                        name = FileName.getNewFileName("ExtractedFaces", "ExtFace", ".jpg")

                        ScrollText.sc.appendStatusText("Image saved :- %s"%name)
                        count+=1
                        
						
                        font = cv2.FONT_HERSHEY_SIMPLEX  
                        h,w,z = imga.shape
                        cv2.putText(imga,time.strftime("%d/%m/%Y"),(w - 80,h - 10), font, .3,(255,255,255),1,cv2.LINE_AA)
                        cv2.putText(imga,time.strftime("%H:%M:%S "),(w - 60,h - 20), font, .3,(255,255,255),1,cv2.LINE_AA)


                        cv2.imwrite(name, imga)

						
                        cv2.imshow('Capture Face', imga)
                        if cv2.waitKey(0) & 0xFF == ord('q'):
                            break
                    break
        cv2.destroyWindow('Capture Face')
        self.parent.focus_force()
        
    def detFaceVideoWebCam(self):
        global sppp
        face_cascade = cv2.CascadeClassifier(self.xmlFileName)
        cap = cv2.VideoCapture(0)
        outputFileName = FileName.getNewFileName("ExtractVideoHavingFace", "extVid", ".avi")
        ScrollText.sc.appendStatusText("Extracted Video saved :- %s"%outputFileName)
        
        fourcc = cv2.VideoWriter_fourcc(*'MJPG')
        out = cv2.VideoWriter(outputFileName,fourcc, 20.0, (640,480))
        while cap.isOpened():

            ret, img = cap.read()
            if ret == True:
                img = cv2.flip(img,1)
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                
                #count = 1
                
                #for (x,y,w,h) in faces:
                #    imga = img[y:y+h, x:x+w]
                #    name = FileName.getNewFileName("ExtractedFaces", "ExtFace", ".jpg")
                #   ScrollText.sc.appendStatusText("Image saved :- %s"%name)
                #   count+=1
                #    cv2.imwrite(name, imga)
                font = cv2.FONT_HERSHEY_SIMPLEX  
                h,w,z = img.shape
                cv2.putText(img,time.strftime("%d/%m/%Y  %H:%M:%S "),(w - 350,h - 20), font, .7,(255,255,255),1,cv2.LINE_AA)
                
                flag = False
                for (x,y,w,h) in faces:
                    flag = True
                    
                if flag:
                    out.write(img)
                for (x,y,w,h) in faces:
                    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                cv2.imshow('Extract Faces',img)
                if cv2.waitKey(sppp) & 0xFF == ord('q'):
                    break
        cv2.destroyWindow('Extract Faces')
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
        
        outputFileName = FileName.getNewFileName("ExtractVideoHavingFace", "extVid", ".avi")
        ScrollText.sc.appendStatusText("Extracted Video saved :- %s"%outputFileName)
                        
        fourcc = cv2.VideoWriter_fourcc(*'MJPG')
        out = cv2.VideoWriter(outputFileName,fourcc, 20.0, (640,480))
        face_cascade = cv2.CascadeClassifier(self.xmlFileName)
        cap = cv2.VideoCapture(fileName)
        while cap.isOpened():

            ret, img = cap.read()
            if img is None:
                break
            if ret == True:
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                
                flag = False
                for (x,y,w,h) in faces:
                    flag = True
                    
                if flag:
                    out.write(img)
                
                
                #count = 1
                #for (x,y,w,h) in faces:
                #    imga = img[y:y+h, x:x+w]
                #    name = FileName.getNewFileName("ExtractedFaces", "ExtFace", ".jpg")
                #    ScrollText.sc.appendStatusText("Image saved :- %s"%name)
                #    count+=1
                #    cv2.imwrite(name, imga)
                    
                for (x,y,w,h) in faces:
                    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

                cv2.imshow('img',img)
                
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

                
        cv2.destroyAllWindows()
        self.parent.focus_force()