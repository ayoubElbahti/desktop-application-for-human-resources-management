import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from db_connect import mydb as db
import Resources_rc
class message_ui(QtWidgets.QDialog):
    def __init__(self,text,etat):
        super().__init__()
        loadUi("Message.ui",self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.pushButton.clicked.connect(self.Envoyer)
        self.label.setText(text)
        if etat == 1:
            self.pushButton_2.setStyleSheet("""
            border : none;
            image: url(:/Icons/277-2778613_success-icon-png-transparent-png-removebg-preview.png);"""
            )
        else :
            self.pushButton_2.setStyleSheet("""
            border : none;
            image: url(:/Icons/refuse-removebg-preview.png);"""
            )

    def Envoyer(self):
        self.close()
if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = message_ui('hello')
    ui.show()
    sys.exit(app.exec_())