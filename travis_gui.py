import sys
from PyQt4 import QtGui, QtCore
import pandas as pd
import cutmarks_check

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

		self.setGeometry(300, 300, 250, 150)
		self.resize(700, 400)
		self.show()
	
		
def main():

	app = QtGui.QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()