import threading
import time
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
import smtplib
import ScrollText
import EmailVald

strFrom = 'fadeipimage@gmail.com'
strTo = 'fadeipimage@gmail.com'
mainEmail = 'fadeipimage@gmail.com'
password = 'Image&&FaDeIP@2000'

class sendMailThread(threading.Thread):
    flag = True
    def __init__(self, imageToSend):
        threading.Thread.__init__(self)
        self.imageToSend = imageToSend
        
    def run(self):
        if sendMailThread.flag:
            sendMailThread.flag = False
           
            sendMail(self.imageToSend)
            time.sleep(40)
            sendMailThread.flag = True


def sendMail(fileName):
    # Send an HTML email with an embedded image and a plain text message for
    # email clients that don't want to display the HTML.

    global strFrom
    global strTo

    global mainEmail
    try:
        fo = open("EmailToSendMail.txt", "r")
        str = fo.read()
        if EmailVald.validateEmail(str):
            strTo = str
            
        else:
            showerror('Error', 'Not Valid Email\n Try again!!')
            strTo = mainEmail

        fo.close()
    except:
        strTo = mainEmail


    ScrollText.sc.appendStatusText("Mail Sent:-%s"%fileName)
    
    
    # Define these once; use them twice!
    
    # Create the root message and fill in the from, to, and subject headers
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = 'FeDeIP'
    msgRoot['From'] = strFrom
    msgRoot['To'] = strTo

    # Encapsulate the plain and HTML versions of the message body in an
    # 'alternative' part, so message agents can decide which they want to display.
    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)

    # We reference the image in the IMG SRC attribute by the ID we give it below
    mailBody = "<div><center style='background-color:yellow; font-family:arial; font-size:25px; color:blue; padding:20px; margin:0px'>Image from <b>FeDeIP</b></center><img src='cid:image1' style='width:100%;'><center style='background-color:yellow; font-family:arial; font-size:25px; color:blue; padding:20px; margin:0px'>Created by <b>kailash</b></center></div>"
    msgText = MIMEText(mailBody, 'html')
    msgAlternative.attach(msgText)

    # This example assumes the image is in the current directory
    fp = open(fileName, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

    # Define the image's ID as referenced above
    msgImage.add_header('Content-ID', '<image1>')
    msgRoot.attach(msgImage)

    # Send the email (this example assumes SMTP authentication is required)
    
    smtp = smtplib.SMTP('smtp.gmail.com:587')
    smtp.ehlo()
    smtp.starttls()
    smtp.login(strFrom, password)
    smtp.sendmail(strFrom, strTo, msgRoot.as_string())
    smtp.quit()

