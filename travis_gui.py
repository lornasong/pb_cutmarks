import sys
from PyQt4 import QtGui, QtCore
import pandas as pd
import cutmarks_check
import numpy as np

from numpy import arange, sin, pi
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        # We want the axes cleared every time plot() is called
        self.axes.hold(False)

        self.compute_initial_figure()

        #
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)



    def compute_initial_figure(self):
        pass

		
class MyStaticMplCanvas(MyMplCanvas):
    """Simple canvas with a sine plot."""
    def compute_initial_figure(self):
        t = arange(0.0, 3.0, 0.01)
        s = sin(2*pi*t)
        self.axes.plot(t, s)

class Example(QtGui.QWidget):

	def __init__(self):
		super(Example, self).__init__()
		
		self.initUI()
		
	def initUI(self):

		#Set up Grid
		grid = QtGui.QGridLayout()
		grid.setSpacing(10)
		
		#Quit Button
		quit = QtGui.QPushButton('QUIT', self)
		quit.clicked.connect(QtCore.QCoreApplication.instance().quit)
		grid.addWidget(quit, 1, 0)
		
		hello = QtGui.QPushButton('Hello', self)
		hello.clicked.connect(QtCore.QCoreApplication.instance().quit)
		grid.addWidget(hello, 1, 2)
		
		vbox = QtGui.QVBoxLayout()
		#sc = MyStaticMplCanvas(self, width=5, height=4, dpi=100)
		vbox.addLayout(grid)
		
		self.setLayout(grid)
		self.setGeometry(300, 300, 250, 150)
		self.setWindowTitle('A2 MI 5th Grade ELA')
		self.resize(700, 400)
		self.show()
	
		
def main():

	app = QtGui.QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()