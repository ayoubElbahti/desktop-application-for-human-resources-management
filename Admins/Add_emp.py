from PyQt5.uic import loadUi
from PyQt5 import QtWidgets,QtCore,QtGui
import Resources_rc
import sys
class add_employe(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        loadUi("Sauvegarder_employees.ui",self)
        self.setWindowTitle('Ajouter Employé')
