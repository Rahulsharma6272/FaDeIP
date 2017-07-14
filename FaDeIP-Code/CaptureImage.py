import cv2
from tkFileDialog import askopenfilename
from tkMessageBox import showerror
import ScrollText
from Tkinter import *
import tkMessageBox
import webbrowser
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
        
        
        Button(self, text="EXIT", width=15, height=2,bg="yellow",fg="blue", command=parent.destroy).pack(fill=X)
    
    def capImage(self):
        global sppp
        camera=cv2.VideoCapture(0)
        while(camera.isOpened()):
            ret,image=camera.read()
            font = cv2.FONT_HERSHEY_SIMPLEX  
            h,w,z = image.shape
            cv2.putText(image,time.strftime("%d/%m/%Y  %H:%M:%S "),(w - 350,h - 20), font, .7,(255,255,255),1,cv2.LINE_AA)
            cv2.imshow('Image Capture',image)
            
            if cv2.waitKey(sppp) & 0xFF ==ord('s'):
                outputFileName = FileName.getNewFileName("CapturedImage", "capImg", ".jpg")
                
                cv2.imwrite(outputFileName,image)
                #cv2.imshow('image',image)
                ScrollText.sc.appendStatusText("Image Saved:-%s"%outputFileName)
                if cv2.waitKey(0) & 0xFF ==ord('q'):
                    break
                break
        camera.release()
        cv2.destroyWindow('Image Capture')	
        self.parent.focus_force()
    def capVideo(self):
        global sppp
        cap = cv2.VideoCapture(0)
        outputFileName = FileName.getNewFileName("CapturedVideo", "capVid", ".avi")
        fourcc = cv2.VideoWriter_fourcc(*'MJPG')
        out = cv2.VideoWriter(outputFileName,fourcc, 20.0, (640,480))
       
        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret==True:
                frame = cv2.flip(frame,1)
                font = cv2.FONT_HERSHEY_SIMPLEX  
                h,w,z = frame.shape
                cv2.putText(frame,time.strftime("%d/%m/%Y  %H:%M:%S "),(w - 350,h - 20), font, .7,(255,255,255),1,cv2.LINE_AA)

                out.write(frame)
                cv2.imshow(outputFileName,frame)
                if cv2.waitKey(sppp) & 0xFF == ord('q'):
                    ScrollText.sc.appendStatusText("Video Saved:-%s"%outputFileName)

                    break
            else:
                break

        cap.release()
        out.release()
        cv2.destroyWindow(outputFileName)
        self.parent.focus_force()
    def openImage(self):
        fileName = askopenfilename()
        if fileName == '':
            showerror("Error", "No file selected.\nTry Again")
            ScrollText.sc.appendStatusText("File Not selected. Try Again")
            return
        
        img = cv2.imread(fileName,1)
        ScrollText.sc.appendStatusText("Image Opened:-%s"%fileName)

        cv2.imshow("Image :- %s"%fileName, img)
        cv2.waitKey(0)
        cv2.destroyWindow("Image :- %s"%fileName)
        self.parent.focus_force()

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
        ScrollText.sc.appendStatusText("Video Opened:-%s"%fileName)
        while(cap.isOpened()):
            ret, frame = cap.read()
            if frame is None:
                break
            cv2.imshow("Video :- %s"%fileName,frame)
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
        cv2.destroyWindow("Video :- %s"%fileName)
        self.parent.focus_force()
