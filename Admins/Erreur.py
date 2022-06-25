from PyQt5.uic import loadUi
from PyQt5 import QtWidgets,QtCore,QtGui
import Resources_rc
import sys
class erreur_pointage(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        loadUi("Erreur.ui",self)
        self.setWindowTitle('Erreur')
        self.setWindowIcon(QtGui.QIcon('refuserIcon.png'))
if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = erreur_pointage()
    ui.show()
    sys.exit(app.exec_())