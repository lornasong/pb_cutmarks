#path: Set-Location C:\Users\lsong\Documents\GitHub\pb_cutmarks
#pull data for cutmarks

from PyQt4 import QtCore, QtGui

class Window(QtGui.QWidget):
    def __init__(self):
		QtGui.QWidget.__init__(self)
		
		#Set up Grid
		grid = QtGui.QGridLayout()
		grid.setSpacing(10)
		
		#Quit Button
		quit = QtGui.QPushButton('QUIT', self)
		quit.clicked.connect(QtCore.QCoreApplication.instance().quit)
		grid.addWidget(quit, 1, 0)
		
		apply = QtGui.QPushButton('Apply', self)
		apply.clicked.connect(self.apply_clicked)
		grid.addWidget(apply, 1, 2)		
		
		self.textInput1 = QtGui.QLineEdit(self)
		self.textInput1.returnPressed.connect(self.apply_clicked)
		self.textInput2 = QtGui.QLineEdit(self)
		self.textInput2.returnPressed.connect(self.apply_clicked)

		grid.addWidget(self.textInput1, 2, 0)
		grid.addWidget(self.textInput2, 2, 2)
		
		self.setLayout(grid)
		self.setGeometry(300, 300, 250, 150)
		self.setWindowTitle('A2 MI 5th Grade ELA')
		self.resize(700, 400)
		
		name = ["self.textInput1"]
		
    def apply_clicked(self):
		hi = self.textInput1.text()
		hello = self.textInput2.text()
		print hi
		print hello

if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.setGeometry(500, 300, 300, 200)
    window.show()
    sys.exit(app.exec_())