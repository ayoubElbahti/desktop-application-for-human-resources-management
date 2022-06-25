from PyQt5.uic import loadUi
from PyQt5 import QtWidgets,QtCore,QtGui
import Resources_rc
import sys
class save_pointage(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        loadUi("sauvegard.ui",self)
        self.setWindowTitle('Sauvegarder')
        self.setWindowIcon(QtGui.QIcon('save.png'))
if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = save_pointage()
    ui.show()
    sys.exit(app.exec_())