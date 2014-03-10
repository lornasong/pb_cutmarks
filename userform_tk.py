#(travis)

from Tkinter import *

import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler

class MainApplication:
	def __init__(self, parent):
		frame = Frame(parent)
		frame.grid(row = 0, column = 0)
		
		#cutmarks
		self.label_A1c = Label(frame, text = "A1 Cutmarks").grid(row=0, sticky = W)
		self.label_A2c = Label(frame, text = "A2 Cutmarks").grid(row=1, sticky = W)
		self.label_Avgc = Label(frame, text = "Avg Cutmarks").grid(row=2, sticky = W)
		self.e_A1c1 = Entry(frame, width = 5).grid(row=0, column=1)
		self.e_A1c2 = Entry(frame, width = 5).grid(row=0, column=2)
		self.e_A1c3 = Entry(frame, width = 5).grid(row=0, column=3)
		self.e_A1c4 = Entry(frame, width = 5).grid(row=0, column=4)
		self.e_A2c1 = Entry(frame, width = 5).grid(row=1, column=1)
		self.e_A2c2 = Entry(frame, width = 5).grid(row=1, column=2)
		self.e_A2c3 = Entry(frame, width = 5).grid(row=1, column=3)
		self.e_A2c4 = Entry(frame, width = 5).grid(row=1, column=4)
		self.e_Avc1 = Entry(frame, width = 5).grid(row=2, column=1)
		self.e_Avc2 = Entry(frame, width = 5).grid(row=2, column=2)
		self.e_Avc3 = Entry(frame, width = 5).grid(row=2, column=3)
		self.e_Avc4 = Entry(frame, width = 5).grid(row=2, column=4)
		
		#CI
		self.label_A1c = Label(frame, text = "A1 CI").grid(row=0, column=5, sticky = W)
		self.label_A2c = Label(frame, text = "A2 CI").grid(row=1, column=5, sticky = W)
		self.label_Avgc = Label(frame, text = "Avg CI").grid(row=2, column=5, sticky = W)
		self.e_A1ci1 = Entry(frame, width = 5).grid(row=0, column=6)
		self.e_A1ci2 = Entry(frame, width = 5).grid(row=0, column=7)
		self.e_A1ci3 = Entry(frame, width = 5).grid(row=0, column=8)
		self.e_A1ci4 = Entry(frame, width = 5).grid(row=0, column=9)
		self.e_A2ci1 = Entry(frame, width = 5).grid(row=1, column=6)
		self.e_A2ci2 = Entry(frame, width = 5).grid(row=1, column=7)
		self.e_A2ci3 = Entry(frame, width = 5).grid(row=1, column=8)
		self.e_A2ci4 = Entry(frame, width = 5).grid(row=1, column=9)
		self.e_Avci1 = Entry(frame, width = 5).grid(row=2, column=6)
		self.e_Avci2 = Entry(frame, width = 5).grid(row=2, column=7)
		self.e_Avci3 = Entry(frame, width = 5).grid(row=2, column=8)
		self.e_Avci4 = Entry(frame, width = 5).grid(row=2, column=9)
		
		#Analysis Label
		self.l_plot = Label(frame, text = "A2 Analysis:").grid(row=4, sticky = W)
		
		#Canvas for two plots
		self.c1 = Canvas(frame, width=300, height = 300, bg='white').grid(row=5,columnspan = 4)
		self.c2 = Canvas(frame, width=300, height = 300, bg='white').grid(row=5, column=5,columnspan = 5)

root = Tk()
MainApplication(root)
root.mainloop()