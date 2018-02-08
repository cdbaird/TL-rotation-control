import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

import TLRot
 
class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 simple window - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        button = QPushButton('function', self)
        button.setToolTip('This is an example button')
        button.move(100,70) 
        button.clicked.connect(self.on_click)
 
        
        self.show()
 
    @pyqtSlot()
    def on_click(self):
        self.statusBar().showMessage('Clicked')
        print(TLRot.find_ports())
        
 


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())