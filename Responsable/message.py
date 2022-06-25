from PyQt5.uic import loadUi
from PyQt5 import QtWidgets,QtCore
from Supprimer_Acceptation import Ui_sup
from Rechercher_Acceptation import Ui_rech
import sqlite3
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
import Resources_rc
class msg(QtWidgets.QDialog):
    def __init__(self,contenu,id_conge):
        super().__init__()
        loadUi("msg.ui",self)
        self.contenu = contenu
        self.id_conge = id_conge
        self.pushButton.setToolTip("Supprimer la demande")
        self.textEdit.setPlainText(str(self.contenu))
        self.pushButton.clicked.connect(self.SupprimerMessage)
        self.pushButton_2.clicked.connect(self.Accepter)

    def open_connection(self):
        return sqlite3.connect("appp.db")

    def Accepter(self):
        db = self.open_connection()
        cursor = db.cursor()
        cursor.execute(f"""UPDATE Conge SET Validation = 'H' WHERE Id = {self.id_conge};""")
        db.commit()
        db.close()
        self.close()
        
    def SupprimerMessage(self):
        db = self.open_connection()
        cursor = db.cursor()
        cursor.execute(f"""DELETE FROM Message WHERE Id_Conge = {self.id_conge};""")
        cursor.execute(f"""DELETE FROM Conge WHERE Id = {self.id_conge};""")
        db.commit()
        db.close()
        self.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = msg()
    ui.show()
    sys.exit(app.exec_())