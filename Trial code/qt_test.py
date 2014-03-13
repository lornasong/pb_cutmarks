#basis for userform_qt.py

import sys
from PyQt4 import QtGui, QtCore
import pandas as pd

class Example(QtGui.QWidget):

	def __init__(self):
		super(Example, self).__init__()
		
		self.initUI()
		
	def initUI(self):
		
		#Buttons
		apply = QtGui.QPushButton('Apply', self)
		export = QtGui.QPushButton('Export', self)
		quit = QtGui.QPushButton('Print', self)
		quit.clicked.connect(QtCore.QCoreApplication.instance().quit)
		
		#Labels
		QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
		color_l = QtGui.QLabel('Color Meaning:', self)
		color_l.setToolTip('Yellow: gap between cutmarks\nBlue: avg is not between interims\nRed: CI over lap\nGreen: yellow & blue')
		color_l.resize(color_l.sizeHint())
		color_l.move(100, 100)
		
		grid = QtGui.QGridLayout()
		grid.setSpacing(10)
		
		grid.addWidget(apply, 5, 0)
		grid.addWidget(export, 6, 0)
		grid.addWidget(quit, 7, 0)
		grid.addWidget(color_l, 8, 0)
		
		#Read in files
		filename = "df_cutmarks(test).csv"
		df = pd.read_csv(filename, header = 0)
		self.datatable = QtGui.QTableWidget()
		self.datatable.setColumnCount(len(df.columns))
		self.datatable.setRowCount(len(df.index))
		
		#Cutmarks
		for i in range(len(df.index)):
			for j in range(len(df.columns)):
				labell = QtGui.QLabel(str(df.iget_value(i, j)))
				grid.addWidget(labell, j, i)
				#self.datatable.setItem(i, j, QtGui.QTableWidgetItem(str(df.iget_value(i, j))))
		
		#grid.addWidget(self.datatable, 1, 0)

		self.setLayout(grid)
		self.setGeometry(300, 300, 250, 150)
		self.setWindowTitle('A2 MI 5th Grade ELA')
		self.show()
		
def main():

	app = QtGui.QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()