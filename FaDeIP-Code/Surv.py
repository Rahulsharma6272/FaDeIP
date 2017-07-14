import cv2
from Tkinter import *
from tkFileDialog import askopenfilename
import numpy as np
import PIL
from PIL import Image
from skimage.measure import compare_ssim as ssim
import pyautogui, sys
from win32api import GetSystemMetrics
import sendMailThread
import ScrollText
import FileName
import time



speed = 41
sppp = 41
class secondWindow(Frame) :
    
    def __init__(self, parent):
            
	self.parent = parent
	Frame.__init__(self, parent)
	Label(self,text="Welcome To FaDeIP", bg="yellow", fg="blue", font = "Chiller 22 bold").pack(fill = X)
        
        buttonFrame = Frame(self,  bd = 2, relief = SUNKEN)
        buttonFrame.pack(pady=20)
        Button(buttonFrame, text="Use WebCam", width=15, height=2, command=self.vidAndSendEmail).grid(row=1, column = 0, padx = 10, pady = 3)
        Button(buttonFrame, text="Open Video", width=15, height=2, command=self.vidUpAndSendEmail).grid(row=1, column = 1, padx = 10, pady = 3)
        
        
        Button(self, text="EXIT", width=15, height=2,bg='yellow', command=parent.destroy).pack(fill=X)
        

    #value of height and width, size of image for comparision all images of faces are converted into this size the comparision will take place
    def vidAndSendEmail(self):
        global sppp
        flag = True
        sValue = 0.80

        def getSsimValude(imageA, imageB, height, width):
            comp_img1 = imageA
            comp_img2 = imageB

            comp_img1 = cv2.cvtColor(comp_img1, cv2.COLOR_RGB2GRAY)
            comp_img2 = cv2.cvtColor(comp_img2, cv2.COLOR_RGB2GRAY)

            ssimValue = ssim(comp_img1, comp_img2)
            return ssimValue


        #creating blank image used for comparision as first image
        #laptop resolution
        width = GetSystemMetrics(0)
        height = GetSystemMetrics(1)

        # Create a black image, a window
        cap = cv2.VideoCapture(0)
        height = int(cap.get(4))
        width = int(cap.get(3))
        blank_image = np.zeros((height,width,3), np.uint8)

        count = 1
        while cap.isOpened():
            ret, frame = cap.read()
            font = cv2.FONT_HERSHEY_SIMPLEX  
            h,w,z = frame.shape
            cv2.putText(frame,time.strftime("%d/%m/%Y  %H:%M:%S "),(w - 350,h - 20), font, .7,(255,255,255),1,cv2.LINE_AA)

            if(flag):
                prevImage1 = blank_image
                prevImage2 = blank_image
                prevImage3 = blank_image
                prevImage4 = blank_image    
                flag = False

            s1 = getSsimValude(prevImage1, frame, height, width)
            s2 = getSsimValude(prevImage2, frame, height, width)
            s3 = getSsimValude(prevImage3, frame, height, width)
            s4 = getSsimValude(prevImage4, frame, height, width)

            if(s1 < sValue and s2 < sValue and s3 < sValue and s4 < sValue):
                prevImage4 = frame
                prevImage3 = prevImage4
                prevImage2 = prevImage3
                prevImage1 = prevImage2

                #send mail using defferent thread

                name = FileName.getNewFileName("SurvlImage", "survImage", ".jpg")
                ScrollText.sc.appendStatusText("Image Saved:-%s"%name)
                count+=1

                cv2.imwrite(name, frame) 

                thread = sendMailThread.sendMailThread(name)
                thread.start()
            
            cv2.imshow('Surveillance System',frame)
            if cv2.waitKey(sppp) & 0xFF == ord('q'):
                break
        cv2.destroyWindow('Surveillance System')
        
        
        
    def vidUpAndSendEmail(self):
        flag = True
        sValue = 0.80
        
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
        def getSsimValude(imageA, imageB, height, width):
            comp_img1 = imageA
            comp_img2 = imageB

            comp_img1 = cv2.cvtColor(comp_img1, cv2.COLOR_RGB2GRAY)
            comp_img2 = cv2.cvtColor(comp_img2, cv2.COLOR_RGB2GRAY)

            ssimValue = ssim(comp_img1, comp_img2)
            return ssimValue


        #creating blank image used for comparision as first image
        #laptop resolution
        width = GetSystemMetrics(0)
        height = GetSystemMetrics(1)

        # Create a black image, a window
        cap = cv2.VideoCapture(fileName)
        height = int(cap.get(4))
        width = int(cap.get(3))
        blank_image = np.zeros((height,width,3), np.uint8)

        count = 1
        while cap.isOpened():
            ret, frame = cap.read()

            if(flag):
                prevImage1 = blank_image
                prevImage2 = blank_image
                prevImage3 = blank_image
                prevImage4 = blank_image    
                flag = False

            s1 = getSsimValude(prevImage1, frame, height, width)
            s2 = getSsimValude(prevImage2, frame, height, width)
            s3 = getSsimValude(prevImage3, frame, height, width)
            s4 = getSsimValude(prevImage4, frame, height, width)

            if(s1 < sValue and s2 < sValue and s3 < sValue and s4 < sValue):
                prevImage4 = frame
                prevImage3 = prevImage4
                prevImage2 = prevImage3
                prevImage1 = prevImage2

                #send mail using defferent thread

                name = FileName.getNewFileName("SurvlImage", "survImage", ".jpg")
                ScrollText.sc.appendStatusText("Image Saved:-%s"%name)
                count+=1

  
                cv2.imwrite(name, frame) 

                thread = sendMailThread.sendMailThread(name)
                thread.start()

            cv2.imshow('Surveillance System',frame)
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
        cv2.destroyWindow('Surveillance System')