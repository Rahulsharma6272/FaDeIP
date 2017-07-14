from Tkinter import Menu        
import Tkinter as tk
import tkMessageBox
import webbrowser
class TopMenu(Menu):
    def __init__(self, parent):
        
        def donothing():
            filewin = Toplevel(root)
            button = Button(filewin, text="Do nothing button")
            button.pack()

	def about():
                tkMessageBox.showinfo("About Software",""" 
             About FaDeIP :-

             This software version 1.0.0.
             + FaDeIP  is a python based software for video and image analysis.
             This Software Can Be used in Malls ,Banks ,Institutes ,Public Places for Surveillance and Security purposes.
             This Software is Using Open CV For Python And Developed on Python.

             This Software is developed  as a project of TCS Internship Program Which Is Guided By Mr.Shudhanshu Sharma TCS-Delhi  And Prof.Jyoti Gajrani GEC,Ajmer.
             Developed BY :- FadeIP Team """)
  



        def about2():
            tkMessageBox.showinfo("About Us","""   
                 About Us:

                 As a TCS Intern We Developed This Software.
                 Our Team Consist of 3 Members 
                 1) Rahul Kumar Gupta
                        Computer Science 
                        B.Tech(2013-2017)
                        Govt. Engineering College ,Ajmer

                2) Rahul Sharma
                        Computer Science 
                        B.Tech(2013-2017)
                        Govt. Engineering College ,Ajmer	

                3)  Kailash Suthar(CTO)
                        Computer Science 
                        B.Tech(2013-2017)
                        Govt. Engineering College ,Ajmer	""") 

	def learn():
            tkMessageBox.showinfo("Learn Software",""" 		
        FaDeIP:- A Solution Of Multimedia World 

        This software is used for Surveillance and Security purposes and consists of many applications

        HOW TO USE FaDeIP :-

        1)  please click any of the below buttons to perform the specific Application.
        2)  Another pop-up will be opened for choosing Image or Video (Live Or Browse).
        3)  After Choosing the option the specific operation is performed.
        4)  Result will be displayed in the main frame.""")  
	
        
        def OpenUrl():
            webbrowser.open_new(url)


	
        
        Menu.__init__(self, parent)
        filemenu = Menu(self, tearoff=0)
	filemenu.add_command(label="About Software", command=about)
	filemenu.add_command(label="About Us", command=about2)
	#filemenu.add_command(label="Save", command=donothing)
	#filemenu.add_command(label="Save as...", command=donothing)
	#filemenu.add_command(label="Close", command=donothing)

	filemenu.add_separator()
        filemenu.add_command(label="Exit", command=parent.quit)
	self.add_cascade(label="About", menu=filemenu)
	editmenu = Menu(self, tearoff=0)
	editmenu.add_command(label="Learn the Software", command=learn)

        self.add_cascade(label="Learn", menu=editmenu)
	helpmenu = Menu(self, tearoff=0)
	helpmenu.add_command(label="Visit Website", command=OpenUrl)
	#helpmenu.add_command(label="About...", command=donothing)
	self.add_cascade(label="Help", menu=helpmenu)

	parent.config(menu=self)
        