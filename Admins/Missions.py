from PyQt5.uic import loadUi
from PyQt5 import QtWidgets,QtCore,QtGui
import Resources_rc
import sys
class MissionsClasse(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        loadUi("Missions.ui",self)
        self.setWindowTitle('Missions')

if __name__ == "__main__":
    import sys
    liste = [2, 'Bensam jalal', '--', '2021-07-28', '--', '0', '--', '0', '0', '0', '0', '0', '0', 'Non', '0']
    app = QtWidgets.QApplication(sys.argv)
    ui = MissionsClasse()
    ui.show()
    sys.exit(app.exec_())