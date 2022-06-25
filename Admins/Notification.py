from PyQt5.uic import loadUi
from PyQt5 import QtWidgets,QtCore,QtGui
import Resources_rc
import sys
class NotificationClasse(QtWidgets.QDialog):
    def __init__(self,text):
        super().__init__()
        loadUi("Notification.ui",self)
        self.setWindowTitle('Notification')
        self.setWindowIcon(QtGui.QIcon('refuserIcon.png'))
        self.label.setText(f"""Vous oubliez dates {text}""")
        self.pushButton.clicked.connect(self.closeApk)
    def closeApk(self):
        self.close()
