from Tkinter import *
import FileName

class sc(Frame):
    
    def __init__(self, parent):
        Frame.__init__(self, parent)
        statusTextFrame = Frame(self)
        statusTextFrame.pack()

        Label(statusTextFrame, text="Status").pack(fill = X)

        sc.textScroll = Scrollbar(self)
        sc.statusText = Text(self, height=20,  width=30)
        sc.textScroll.pack(side=RIGHT, fill = Y)
        sc.statusText.pack(side=LEFT, fill = Y)

        sc.textScroll.config(command = sc.statusText.yview)
        sc.statusText.config(yscrollcommand = sc.textScroll.set, state=DISABLED)

        
    @staticmethod
    def appendStatusText(txt):
        sc.statusText.configure(state="normal")
        sc.statusText.insert(END, "\n%s\n"%txt)
        sc.statusText.yview(END)
        sc.statusText.configure(state="disabled")

        
    @staticmethod
    def clearLog():
        sc.statusText.configure(state="normal")
        sc.statusText.delete("1.0", END)
        sc.statusText.configure(state="disabled")

        
    @staticmethod
    def saveLog():
        sc.statusText.configure(state="normal")
        logFileName = FileName.getNewFileName("LogFiles", "logFile", ".txt")
        sc.appendStatusText("Log File Saved :- %s"%logFileName)
        fo = open(logFileName, "wb")
        fo.write(sc.statusText.get("1.0", END));

        # Close opend file
        fo.close()
        sc.statusText.configure(state="disabled")

