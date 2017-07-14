import cv2
import numpy as np

from tkFileDialog import askopenfilename
from tkMessageBox import showerror
from Tkinter import *
import FileName
import FadeIPMenu
import time
import PIL
from PIL import Image
from skimage.measure import compare_ssim as ssim
import ScrollText
sppp = 41
speed = 41

class secondWindow(Frame) :
    def __init__(self, parent):
	self.parent = parent
	Frame.__init__(self, parent)
	Label(self,text="Welcome To FaDeIP", bg="yellow", fg="blue", font = "Chiller 22 bold").pack(fill = X)
        
        buttonFrame = Frame(self,  bd = 2, relief = SUNKEN)
        buttonFrame.pack(pady=20)
        Button(buttonFrame, text="Use WebCam", width=15, height=2, command=self.capVideo).grid(row=1, column = 0, padx = 10, pady = 3)
        Button(buttonFrame, text="Open Video", width=15, height=2, command=self.openVideo).grid(row=1, column = 1, padx = 10, pady = 3)
        
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
        
        Button(self, text="EXIT", width=15, height=2, bg = 'yellow', command=parent.destroy).pack(fill=X)
        
	



    def capVideo(self):
        global sppp
        #value of height and width, size of image for comparision all images of faces are converted into this size the comparision will take place
        height_width = 150


        flag = True


        def getSsimValude(imageA, imageB):
            comp_img1 = imageA
            comp_img2 = imageB

            comp_img1 = cv2.cvtColor(comp_img1, cv2.COLOR_BGR2RGB)
            comp_img2 = cv2.cvtColor(comp_img2, cv2.COLOR_BGR2RGB)

            pil1 = Image.fromarray(comp_img1)
            pil2= Image.fromarray(comp_img2)

            pil1 = pil1.resize((height_width, height_width), PIL.Image.ANTIALIAS)
            pil2 = pil2.resize((height_width, height_width), PIL.Image.ANTIALIAS)

            comp_img1 = cv2.cvtColor(np.array(pil1), cv2.COLOR_RGB2BGR)
            comp_img2 = cv2.cvtColor(np.array(pil2), cv2.COLOR_RGB2BGR)

            comp_img1 = cv2.cvtColor(comp_img1, cv2.COLOR_RGB2GRAY)
            comp_img2 = cv2.cvtColor(comp_img2, cv2.COLOR_RGB2GRAY)

            ssimValue = ssim(comp_img1, comp_img2)
            return ssimValue



        #creating blank image used for comparision as first image
        blank_image = np.zeros((height_width,height_width,3), np.uint8)
        #laptop resolution
        
        # Create a black image, a window
        cap = cv2.VideoCapture(0)

        face_cascade = cv2.CascadeClassifier(self.xmlFileName)

        #face_cascade = cv2.CascadeClassifier('C:\opencv\sources\data\lbpcascades\HS.xml')
        count = 1
        while cap.isOpened():
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.5, 5)



            for (x,y,w,h) in faces:
                if(flag):
                    prevImage1 = blank_image
                    prevImage2 = blank_image
                    prevImage3 = blank_image
                    prevImage4 = blank_image

                    flag = False

                y -= 10
                x -= 10
                h += 20
                w += 20

                imga = frame[y:y+h, x:x+w]

                s1 = getSsimValude(prevImage1, imga)
                s2 = getSsimValude(prevImage2, imga)
                s3 = getSsimValude(prevImage3, imga)
                s4 = getSsimValude(prevImage4, imga)

                if(s1 < 0.55 and s2 < 0.55 and s3 < 0.55 and s4 < 0.55):
                    prevImage4 = imga
                    prevImage3 = prevImage4
                    prevImage2 = prevImage3
                    prevImage1 = prevImage2
                    name = FileName.getNewFileName("EntryFaceRecord", "ERecod", ".jpg")
                    ScrollText.sc.appendStatusText("Image Saved:-%s"%name)
                    count+=1
                    font = cv2.FONT_HERSHEY_SIMPLEX  
                    h,w,z = imga.shape
                    imgaa = imga
                    cv2.putText(imgaa,time.strftime("%d/%m/%Y"),(w - 80,h - 10), font, .3,(255,255,255),1,cv2.LINE_AA)
                    cv2.putText(imgaa,time.strftime("%H:%M:%S "),(w - 60,h - 20), font, .3,(255,255,255),1,cv2.LINE_AA)
                    
                    cv2.imwrite(name, imgaa) 

            for (x,y,w,h) in faces:

                y -= 10
                x -= 10
                h += 20
                w += 20

                frame= cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

            font = cv2.FONT_HERSHEY_SIMPLEX
            h,w,z = frame.shape
            cv2.putText(frame,time.strftime("%d/%m/%Y  %H:%M:%S "),(w - 350,h - 20), font, .7,(255,255,255),1,cv2.LINE_AA)
               
            cv2.imshow('img',frame)
            if cv2.waitKey(sppp) & 0xFF == ord('q'):
                break
        cv2.destroyAllWindows()
        self.parent.focus_force()
    def openVideo(self):
        global speed
        height_width = 150


        flag = True


        def getSsimValude(imageA, imageB):
            comp_img1 = imageA
            comp_img2 = imageB

            comp_img1 = cv2.cvtColor(comp_img1, cv2.COLOR_BGR2RGB)
            comp_img2 = cv2.cvtColor(comp_img2, cv2.COLOR_BGR2RGB)

            pil1 = Image.fromarray(comp_img1)
            pil2= Image.fromarray(comp_img2)

            pil1 = pil1.resize((height_width, height_width), PIL.Image.ANTIALIAS)
            pil2 = pil2.resize((height_width, height_width), PIL.Image.ANTIALIAS)

            comp_img1 = cv2.cvtColor(np.array(pil1), cv2.COLOR_RGB2BGR)
            comp_img2 = cv2.cvtColor(np.array(pil2), cv2.COLOR_RGB2BGR)

            comp_img1 = cv2.cvtColor(comp_img1, cv2.COLOR_RGB2GRAY)
            comp_img2 = cv2.cvtColor(comp_img2, cv2.COLOR_RGB2GRAY)

            ssimValue = ssim(comp_img1, comp_img2)
            return ssimValue



        #creating blank image used for comparision as first image
        blank_image = np.zeros((height_width,height_width,3), np.uint8)
        #laptop resolution
        
        fileName = askopenfilename()
        if fileName == '':
            showerror("Error", "No file selected.\nTry Again")
            ScrollText.sc.appendStatusText("File Not selected. Try Again")
            return
        if not fileName.endswith(".avi"):
            showerror("Error", "Not valid Format.")
            ScrollText.sc.appendStatusText("Invalid File Format:-%s"%fileName)
            return
        # Create a black image, a window
        cap = cv2.VideoCapture(fileName)

        face_cascade = cv2.CascadeClassifier(self.xmlFileName)

        #face_cascade = cv2.CascadeClassifier('C:\opencv\sources\data\lbpcascades\HS.xml')
        count = 1
        while cap.isOpened():
            
            ret, frame = cap.read()
            if frame is None:
                break
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)



            for (x,y,w,h) in faces:
                if(flag):
                    prevImage1 = blank_image
                    prevImage2 = blank_image
                    prevImage3 = blank_image
                    prevImage4 = blank_image

                    flag = False

                y -= 10
                x -= 10
                h += 20
                w += 20

                imga = frame[y:y+h, x:x+w]

                s1 = getSsimValude(prevImage1, imga)
                s2 = getSsimValude(prevImage2, imga)
                s3 = getSsimValude(prevImage3, imga)
                s4 = getSsimValude(prevImage4, imga)

                if(s1 < 0.55 and s2 < 0.55 and s3 < 0.55 and s4 < 0.55):
                    prevImage4 = imga
                    prevImage3 = prevImage4
                    prevImage2 = prevImage3
                    prevImage1 = prevImage2
                    name = FileName.getNewFileName("EntryFaceRecord", "ERecod", ".jpg")
                    ScrollText.sc.appendStatusText("Image Saved:-%s"%name)
                    count+=1
                    
                    font = cv2.FONT_HERSHEY_SIMPLEX  
                    h,w,z = imga.shape
                    imgaa = imga
                    cv2.putText(imgaa,time.strftime("%d/%m/%Y"),(w - 80,h - 10), font, .3,(255,255,255),1,cv2.LINE_AA)
                    cv2.putText(imgaa,time.strftime("%H:%M:%S "),(w - 60,h - 20), font, .3,(255,255,255),1,cv2.LINE_AA)
                    
                    cv2.imwrite(name, imgaa) 

            for (x,y,w,h) in faces:

                y -= 10
                x -= 10
                h += 20
                w += 20

                frame= cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
               
            cv2.imshow('img',frame)
            
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