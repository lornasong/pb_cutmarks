
#http://stackoverflow.com/questions/18716530/python-tkinter-embed-a-matplotlib-plot-in-a-widget
#http://stackoverflow.com/questions/9263181/using-entry-box-data-from-previous-session-tkinter
#http://bytes.com/topic/python/answers/939533-tkinter-table-menu
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial 

In this example, we receive data from
a QtGui.QInputDialog dialog. 

author: Jan Bodnar
website: zetcode.com 
last edited: October 2011
"""
import sys
from PyQt4 import QtGui

class Example(QtGui.QMainWindow):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        btn1 = QtGui.QPushButton("Button 1", self)
        btn1.move(30, 50)

        btn2 = QtGui.QPushButton("Button 2", self)
        btn2.move(150, 50)
      
        btn1.clicked.connect(self.buttonClicked)            
        btn2.clicked.connect(self.buttonClicked)
        
        self.statusBar()
        
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.show()
        
    def buttonClicked(self):
      
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()