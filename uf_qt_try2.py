import sys
from PyQt4 import QtGui, QtCore
import pandas as pd
import cutmarks_check
import uf_charts

import sys, os, random
from PyQt4 import QtGui, QtCore

import numpy
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


class Example(QtGui.QWidget):

	def __init__(self):
		QtGui.QWidget.__init__(self)
		
		#Buttons
		apply = QtGui.QPushButton('Apply', self)
		apply.clicked.connect(self.apply_clicked)
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
		
		grid.addWidget(apply, 5, 10)
		grid.addWidget(export, 6, 10)
		grid.addWidget(quit, 7, 10)
		grid.addWidget(color_l, 8, 10)
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
		
		self.label_name = ["self.input1", "self.input2", "self.input3", "self.input4", "self.input5", "self.input6", "self.input7", "self.input8", "self.input9", "self.input10", "self.input11", "self.input12"]

		#Interim Cutmarks & Check 1
		k = 0
		for i in range(4):
			for j in range(2):
				if cutmarks_check.df_check.iget_value(i, j) == True:
					self.label_name[k] = QtGui.QLineEdit()
					self.label_name[k].returnPressed.connect(self.apply_clicked)
					self.label_name[k].setText(str(df.iget_value(i, j)))
					yellow = "QWidget {background-color: #FFFF66;}"
					self.label_name[k].setStyleSheet(yellow)
					grid.addWidget(self.label_name[k], j, i + 1)
				else:
					self.label_name[k] = QtGui.QLineEdit()
					self.label_name[k].returnPressed.connect(self.apply_clicked)
					self.label_name[k].setText(str(df.iget_value(i, j)))
					grid.addWidget(self.label_name[k], j, i + 1)
				k = k+1
		
		#Average Cutmarks & Check 2
		for i in range(4):
			for j in range(2, 3):
				if cutmarks_check.df_check.iget_value(i, j) == True:
					self.label_name[k] = QtGui.QLineEdit(self)
					self.label_name[k].returnPressed.connect(self.apply_clicked)
					self.label_name[k].setText(str(df.iget_value(i, j)))
					yellow = "QWidget {background-color: #FFFF66;}"
					self.label_name[k].setStyleSheet(yellow)
					grid.addWidget(self.label_name[k], j, i + 1)
				else:
					self.label_name[k] = QtGui.QLineEdit(self)
					self.label_name[k].returnPressed.connect(self.apply_clicked)
					self.label_name[k].setText(str(df.iget_value(i, j)))
					grid.addWidget(self.label_name[k], j, i + 1)
				k = k+1
				
		
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
		
		#Adding plots
		self.figure = plt.figure()
		self.canvas1 = FigureCanvas(self.figure)
		grid.addWidget(self.canvas1, 5, 0, 9, 5)
		ax1 = self.figure.add_subplot(111)
		ax1.set_title('Distribution of Student Test Performance')
		ax1.set_ylabel('Count of Students')
		ax1.set_xlabel('Possible % Score')
		ax1.bar(uf_charts.plot_index, uf_charts.plot_df, width = 0.03)

		self.figure = plt.figure()
		self.canvas2 = FigureCanvas(self.figure)
		grid.addWidget(self.canvas2, 5, 5, 9, 5)
		ax2 = self.figure.add_subplot(111)
		ax2.set_title('% of Students by Performance Level')
		ax2.set_ylabel('% of Students')
		ax2.set_xlabel('Performance Levels')
		ax2.bar(numpy.arange(4), uf_charts.plot_df2, width = 0.3, color = 'r')
		ax2.set_xticks(numpy.arange(4)+0.3)
		ax2.set_xticklabels(uf_charts.plot_index2)
		
		
		#testing
		"""
		self.textInput1 = QtGui.QLineEdit(self)
		self.textInput1.returnPressed.connect(self.apply_clicked)
		self.textInput2 = QtGui.QLineEdit(self)
		self.textInput2.returnPressed.connect(self.apply_clicked)
		grid.addWidget(self.textInput1, 20, 0)
		grid.addWidget(self.textInput2, 20, 2)
		"""
		
		#Window Attributes
		self.setLayout(grid)
		self.setGeometry(300, 300, 250, 150)
		self.setWindowTitle('A2 MI 5th Grade ELA')
		self.resize(1200, 550)
		self.show()
	
	def apply_clicked(self):
	
		filename = "df_cutmarks(test).csv"
		df = pd.read_csv(filename, header = 0)
		print df
		
		k = 0
		for i in range(4):
			for j in range(2):
				new = self.label_name[k].text()
				new_float = float(new)
				df.replace[i, j] = new_float
				k = k+1
		
		#Average Cutmarks & Check 2
		for i in range(4):
			for j in range(2, 3):
				new = self.label_name[k].text()
				new_float = float(new)
				df.replace[i, j] = new_float
				k = k+1
		
		print "new df"
		print df
		
def main():

	app = QtGui.QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()