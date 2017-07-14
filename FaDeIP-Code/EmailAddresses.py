from Tkinter import *
from tkMessageBox import showerror, showinfo
import EmailVald
import Surv
import ScrollText




mainEmail = 'sutharkailash1211@gmail.com'
class emailFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        Label(self,text="Welcome To FaDeIP", bg="yellow", fg="blue", font = "Chiller 22 bold").pack(fill = X)
        
        emailFrame = Frame(self, bd = 2, relief = SUNKEN)
        emailFrame.pack(pady = 5)
        Label(emailFrame, text='Email To Receive Mail :-', pady = 30).grid(row = 0, column = 0)
        self.e = Entry(emailFrame, width = 30 )
        self.e.grid(row = 0, column = 1, ipady = 5, ipadx = 5, padx = 10)
        
        self.fun()
        self.e.insert(0, self.email)
        
        
        btnFrame = Frame(self)
        btnFrame.pack(fill = X)
        
        def clearEmail():
            self.e.delete(0, END)
            self.parent.focus_force()
            
        def saveEmail():
            self.email = self.e.get()
            if EmailVald.validateEmail(self.email):
                ScrollText.sc.appendStatusText("-----------------------------")
                ScrollText.sc.appendStatusText("Receiver Email Address Changed To -- \n%s"%self.email)
                ScrollText.sc.appendStatusText("-----------------------------")
                fo = open("EmailToSendMail.txt", "wb")
                fo.write(self.e.get());
                # Close opend file
                fo.close()
                showinfo('Email Changed', 'Receiver Email Address changed to--\n%s'%self.email)
            else:
                showerror('Error', 'Not Valid Email\n Try again!!')
            self.parent.focus_force()
            
            
        Button(btnFrame, text = 'Clear Email', width = 24, command = clearEmail).grid(row = 0, column = 0)
        Button(btnFrame, text = 'Save Email', width = 24, command = saveEmail).grid(row = 0, column = 1)
        Button(self, text = 'EXIT', bg = 'yellow', command = parent.destroy).pack(fill=X)
        
    
    def fun(self):
        global mainEmail
        try:
            fo = open("EmailToSendMail.txt", "r")
            str = fo.readline()
            if EmailVald.validateEmail(str):
                self.email = str
            else:
                showerror('Error', 'Not Valid Email\n Try again!!')
                self.email = mainEmail
                
                fo = open("EmailToSendMail.txt", "wb")
                fo.write(mainEmail);
                # Close opend file
                fo.close()
                
            fo.close()
        except:
            self.email = mainEmail
            if EmailVald.validateEmail(self.email):
                fo = open("EmailToSendMail.txt", "wb")
                fo.write(mainEmail);
                # Close opend file
                fo.close()
            else:
                showerror('Error', 'Not Valid Email\n Try again!!')
        self.parent.focus_force()
     