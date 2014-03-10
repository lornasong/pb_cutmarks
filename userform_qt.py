import sys
from PyQt4 import QtGui, QtCore
import pandas as pd
import cutmarks_check

class Example(QtGui.QWidget):

	def __init__(self):
		super(Example, self).__init__()
		
		self.initUI()
		
	def initUI(self):
		
		#Buttons
		apply = QtGui.QPushButton('Apply', self)
		apply.clicked.connect(self.applyClicked)
		export = QtGui.QPushButton('Export', self)
		quit = QtGui.QPushButton('Print', self)
		quit.clicked.connect(QtCore.QCoreApplication.instance().quit)
		
		#Labels
		QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
		color_l = QtGui.QLabel('Color Meaning:', self)
		color_l.setToolTip('Interim Cutmarks: gap between cutmarks too small\nAvg Cutmarks: avg is not between interims\nConfidence Intervals: CIs over lap\n')
		A1c_l = QtGui.QLabel('A1 Cutmarks: ', self)
		A2c_l = QtGui.QLabel('A2 Cutmarks: ', self)
		Avgc_l = QtGui.QLabel('Avg Cutmarks: ', self)
		plot_l = QtGui.QLabel('A2 Analysis: ', self)
		A1ci_l = QtGui.QLabel('A1 CI: ', self)
		A2ci_l = QtGui.QLabel('A2 CI: ', self)
		Avgci_l = QtGui.QLabel('Avg CI: ', self)
		
		#Set up Grid
		grid = QtGui.QGridLayout()
		grid.setSpacing(10)
		
		grid.addWidget(apply, 5, 9)
		grid.addWidget(export, 6, 9)
		grid.addWidget(quit, 7, 9)
		grid.addWidget(color_l, 8, 9)
		grid.addWidget(A1c_l, 0, 0)
		grid.addWidget(A2c_l, 1, 0)
		grid.addWidget(Avgc_l, 2, 0)
		grid.addWidget(A1ci_l, 0, 5)
		grid.addWidget(A2ci_l, 1, 5)
		grid.addWidget(Avgci_l, 2, 5)
		grid.addWidget(plot_l, 4, 0)
		
		#Read in files
		filename = "df_cutmarks(test).csv"
		df = pd.read_csv(filename, header = 0)
		
		#Interim Cutmarks & Check 1
		for i in range(4):
			for j in range(2):
				if cutmarks_check.df_check.iget_value(i, j) == True:
					c_line = QtGui.QLineEdit()
					c_line.setText(str(df.iget_value(i, j)))
					yellow = "QWidget {background-color: #FFFF66;}"
					c_line.setStyleSheet(yellow)
					grid.addWidget(c_line, j, i + 1)
				else:
					c_line = QtGui.QLineEdit()
					c_line.setText(str(df.iget_value(i, j)))
					grid.addWidget(c_line, j, i + 1)
				print c_line.text()
					
		#Average Cutmarks & Check 2
		for i in range(4):
			for j in range(2, 3):
				if cutmarks_check.df_check.iget_value(i, j) == True:
					c_line = QtGui.QLineEdit()
					c_line.setText(str(df.iget_value(i, j)))
					yellow = "QWidget {background-color: #FFFF66;}"
					c_line.setStyleSheet(yellow)
					grid.addWidget(c_line, j, i + 1)
				else:
					c_line = QtGui.QLineEdit()
					c_line.setText(str(df.iget_value(i, j)))
					grid.addWidget(c_line, j, i + 1)
				print c_line.text()
				
		#CI & Check 3
		for i in range(4):
			for j in range(9, 12):
				if cutmarks_check.df_check.iget_value(i, j - 6) == True:
					ci_l = QtGui.QLabel(str(df.iget_value(i, j)))
					ci_l.setStyleSheet(yellow)
					grid.addWidget(ci_l, j - 9, i + 6)
				else:
					ci_l = QtGui.QLabel(str(df.iget_value(i, j)))
					grid.addWidget(ci_l, j - 9, i + 6)

		self.setLayout(grid)
		self.setGeometry(300, 300, 250, 150)
		self.setWindowTitle('A2 MI 5th Grade ELA')
		self.resize(700, 400)
		self.emit(SIGNAL("
		self.show()
	
	def applyClicked(self, c_line):
		print "applied"
		print c_line.text()
def main():

	app = QtGui.QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()