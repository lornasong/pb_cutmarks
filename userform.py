
#http://stackoverflow.com/questions/18716530/python-tkinter-embed-a-matplotlib-plot-in-a-widget
#http://stackoverflow.com/questions/9263181/using-entry-box-data-from-previous-session-tkinter
#http://bytes.com/topic/python/answers/939533-tkinter-table-menu
import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QMainWindow):
    
    closeApp = QtCore.pyqtSignal() 
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        self.closeApp.connect(self.close)       
        
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emit signal')
        self.show()
        
    def mousePressEvent(self, event):
        
        self.closeApp.emit()
        
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()