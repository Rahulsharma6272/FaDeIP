from Tkinter import *
from tkFileDialog import askopenfilename
#file inport 
import ScrollText
import DetectAndCompareFace
import ExtractFace
import Surv
import CaptureImage
import DetectFaces
import FadeIPMenu
import ExtractUniqueFace
import mm
import EmailAddresses
import DetectObjOfPartColor



root = Tk()
root.geometry("400x450")
root.resizable(width=False,height=False)
root.title("FaDeIP- A Soluion for Mulitmedia World")


#menu bar
FadeIPMenu.TopMenu(root)
Label(root,text="Welcome To FaDeIP", bg="yellow", fg="blue", font = "Chiller 22 bold").pack(fill = X)

#Buttons
#frame to hold buttons and Status bar text bar
btnTxtFrame = Frame(root, bd = 2, relief = SUNKEN)
btnTxtFrame.pack()

#frame to hold buttons
buttonFrame = Frame(btnTxtFrame)
buttonFrame.grid(row = 0, column = 0)


def fun1():
    window = Toplevel(root)
    window.resizable(width=False,height=False)
    FadeIPMenu.TopMenu(window)
    CaptureImage.secondWindow(window).pack()
    window.mainloop()
    
def fun2():
    window = Toplevel(root)
    window.resizable(width=False,height=False)
    FadeIPMenu.TopMenu(window)
    DetectFaces.secondWindow(window).pack()
    window.mainloop()
    
def fun3():
    window = Toplevel(root)
    window.resizable(width=False,height=False)
    FadeIPMenu.TopMenu(window)
    ExtractFace.secondWindow(window).pack()
    window.mainloop()
    
def fun4():
    window = Toplevel(root)
    window.resizable(width=False,height=False)
    FadeIPMenu.TopMenu(window)
    ExtractUniqueFace.secondWindow(window).pack()
    window.mainloop()
    
def fun5():
    ScrollText.sc.appendStatusText("-----------------------------")
    ScrollText.sc.appendStatusText("------- Mouse Control -------")
    ScrollText.sc.appendStatusText("-----------------------------") 
    window = Toplevel(root)
    window.resizable(width=False,height=False)
    mm.mm(window).pack()
    window.mainloop()
    
def fun6():
    ScrollText.sc.appendStatusText("-----------------------------")
    ScrollText.sc.appendStatusText("---- Survallence System -----")
    ScrollText.sc.appendStatusText("-----------------------------")
    window = Toplevel(root)
    window.resizable(width=False,height=False)
    Surv.secondWindow(window).pack()
    window.mainloop()
  

def fun7():
    ScrollText.sc.appendStatusText("-----------------------------")
    ScrollText.sc.appendStatusText("---- Detect Color Object ----")
    ScrollText.sc.appendStatusText("-----------------------------")
    window = Toplevel(root)
    window.resizable(width=False,height=False)
    DetectObjOfPartColor.secondWindow(window).pack()
    window.mainloop()


Button(buttonFrame, text="Capture & Open", width=15, height=2, command = fun1).grid(row=0, padx = 10, pady = 3)
Button(buttonFrame, text="Detect Faces", width=15, height=2, command = fun2).grid(row=1, padx = 10, pady = 3)
Button(buttonFrame, text="Extract Faces", width=15, height=2, command = fun3).grid(row=2, padx = 10, pady = 3)
Button(buttonFrame, text="Entry Face Record", width=15, height=2, command=fun4).grid(row=3, padx = 10, pady = 3)
Button(buttonFrame, text="Mouse Control", width=15, height=2, command = fun5).grid(row=4, padx = 10, pady = 3)
Button(buttonFrame, text="Survellience System", width=15, height=2, command = fun6).grid(row=5, padx = 10, pady = 3)
Button(buttonFrame, text="Detect Color", width=15, height=2, command = fun7).grid(row=6, padx = 10, pady = 3)


frame1 = ScrollText.sc(btnTxtFrame)
frame1.grid(row=0, column=1, pady = 2)

def clearLogFun():
    ScrollText.sc.clearLog()
    
def saveLogFun():
    ScrollText.sc.appendStatusText("-----------------------------")
    ScrollText.sc.appendStatusText("--------- Log Saved ---------")
    ScrollText.sc.appendStatusText("-----------------------------")
    ScrollText.sc.saveLog()
    
btnFrame = Frame(btnTxtFrame)
btnFrame.grid(row = 1, column = 1)
Button(btnFrame, width = 17, text = 'Clear Log', command=clearLogFun).grid(row = 0, column = 0)
Button(btnFrame, width = 17, text = 'Save Log', command = saveLogFun).grid(row = 0, column = 1)
        
def editEmail():
    window = Toplevel(root)
    window.resizable(width=False,height=False)
    FadeIPMenu.TopMenu(window)
    EmailAddresses.emailFrame(window).pack()
    window.mainloop()
    
Button(btnTxtFrame, width = 17, text = 'Edit Email', command = editEmail).grid(row = 1, column = 0)


Button(root, text="QUIT", width=15, bg='yellow', height=2, command = root.destroy).pack(fill=X)


#Button(root, text="EXIT",bg="grey", command=root.destroy).pack(fill=X, ipady=10, pady=10)

#frame to hold scroll bar and text field
root.mainloop()