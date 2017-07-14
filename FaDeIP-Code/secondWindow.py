from Tkinter import *
import tkMessageBox
import webbrowser

class secondWindow :
    def __init__(self, fun1, fun2, fun3, fun4):
	def donothing():
            filewin = Toplevel(root)
            button = Button(filewin, text="Do nothing button")
            button.pack()

	def about():
            tkMessageBox.showinfo("About Software","Here klfsghdfgkhgdsfslfhgh fksdghk usfgis guhjsgkhsd gskhklg gkhd kgdh")


	def about2():
            tkMessageBox.showinfo("About Us","Here klfsghdfgkhgdsfslfhgh fksdghk usfgis guhjsgkhsd gskhklg gkhd kgdh")

	def learn():
            tkMessageBox.showinfo("Learn the Software","1)Here klfsghdfgkhgdsfslfhgh fksdghk usfgis guhjsgkhsd gskhklg gkhd kgdh \n 2)hvbdsg")
            url='wwww.xvideos.com'

	def OpenUrl():
            webbrowser.open_new(url)


	root = Tk()
	root.geometry("300x200")
        root.resizable(width=False,height=False)

	root.title("FaDiP-a Soluion for mulitmedia world")
	menubar = Menu(root)
	filemenu = Menu(menubar, tearoff=0)
	filemenu.add_command(label="About Software", command=about)
	filemenu.add_command(label="About Us", command=about2)
	#filemenu.add_command(label="Save", command=donothing)
	#filemenu.add_command(label="Save as...", command=donothing)
	#filemenu.add_command(label="Close", command=donothing)

	filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.quit)
	menubar.add_cascade(label="About", menu=filemenu)
	editmenu = Menu(menubar, tearoff=0)
	editmenu.add_command(label="Learn the Software", command=learn)

        menubar.add_cascade(label="Learn", menu=editmenu)
	helpmenu = Menu(menubar, tearoff=0)
	helpmenu.add_command(label="Visit Website", command=OpenUrl)
	#helpmenu.add_command(label="About...", command=donothing)
	menubar.add_cascade(label="Help", menu=helpmenu)

	root.config(menu=menubar)
        
        Label(root,text="Welcome To FaDeIP", bg="yellow", fg="blue", font = "Chiller 22 bold").pack(fill = X)
        
        buttonFrame = Frame(root,  bd = 2, relief = SUNKEN)
        buttonFrame.pack(pady=20)
        Button(buttonFrame, text="Image Capture", width=15, height=2, command=fun1).grid(row=0, column = 0, padx = 10, pady = 3)
        Button(buttonFrame, text="Open Image", width=15, height=2, command=fun2).grid(row=0, column = 1, padx = 10, pady = 3)
        Button(buttonFrame, text="Video Capture", width=15, height=2, command=fun3).grid(row=1, column = 0, padx = 10, pady = 3)
        Button(buttonFrame, text="Open Video", width=15, height=2, command=fun4).grid(row=1, column = 1, padx = 10, pady = 3)
        
        radioButtonFrame = Frame(root)
        radioButtonFrame.pack(fill=X)
        RadioButton(radioButtonFrame, text="Only Face", variable = v, command = self.setXML, value=1).grid(column = 0)
        RadioButton(radioButtonFrame, text="Face & Shoulder", variable = v, command = self.setXML, value=2).grid(column = 1)
        
        Button(root, text="Quit", width=15, height=2, command=root.destroy).pack(fill=X)
        
	
        root.mainloop()

