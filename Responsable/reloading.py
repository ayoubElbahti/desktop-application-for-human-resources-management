
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt,QTimer
from reloading_screen import Relaoding
import sys
class ayoub(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.btn = QPushButton('click')
        self.layot = QVBoxLayout()
        self.layot.addWidget(self.btn)
        self.setLayout(self.layot)
        self.btn.clicked.connect(self.connected)
        self.show()
    def connected(self):
        self.rr = Relaoding(self)
        timer = QTimer(self)
        timer.singleShot(5000,self.activer)  
        
    def activer(self):
        try:
            print('bonjour ..')
            #self.rr.close()
            self.__init__()
        except:
            print('zmr')
app = QApplication(sys.argv)

exe = ayoub()
app.exit(app.exec_())
