from PyQt5.uic import loadUi
from PyQt5 import QtWidgets,QtCore

import Resources_rc
class waiting(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        loadUi("waiting.ui",self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
            #msg = QtWidgets.QMessageBox.show(self,'CHAMP INVALID ! ','Vous été oublié des champs Vides !',QtWidgets.QMessageBox.Ok)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = waiting()
    ui.show()
    sys.exit(app.exec_())