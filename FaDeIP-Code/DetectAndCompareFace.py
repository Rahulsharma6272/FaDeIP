import cv2
import numpy as np
import PIL
from PIL import Image
from skimage.measure import compare_ssim as ssim
import pyautogui, sys
from win32api import GetSystemMetrics
import FileName
import ScrollText


def compFaces():
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
    width = GetSystemMetrics(0)
    height = GetSystemMetrics(1)

    # Create a black image, a window
    cap = cv2.VideoCapture(0)

    face_cascade = cv2.CascadeClassifier('C:\opencv\sources\data\haarcascades\haarcascade_frontalface_default.xml')

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
                cv2.imwrite(name, imga) 

        for (x,y,w,h) in faces:

            y -= 10
            x -= 10
            h += 20
            w += 20

            frame= cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)


        cv2.imshow('img',frame)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
    