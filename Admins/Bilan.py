from PyQt5.uic import loadUi
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import Qt
from db_connect import mydb as db
from db_connect import db as dbs
from Imprimer import Imprimer_class
check_Image = True
check_retard = False
import Resources_rc
import datetime
class bilan(QtWidgets.QDialog):
    def __init__(self,list_info):
        super().__init__()
        loadUi("Bilan.ui",self)
        self.setWindowTitle('Bilan de travail')
        self.setWindowIcon(QtGui.QIcon("Bilan_icon.png"))
        #self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.info_List = list_info
        db._open_connection()
        Cursor = db.cursor(buffered=True)
            #SELECT id_emp,concat(E.Nom,' ',E.Prenom),SUM(NbrHeures),SUM(P.Retard),SUM(P.Absence),SUM(P.HeuresSupp),SUM(P.vintCinq),SUM(P.cinquante),SUM(P.cent) FROM Pointage P INNER JOIN Employees E ON concat(E.Nom,' ',E.Prenom) = 'EL BAHTI AYOUB'  AND E.Mat_Emp = P.id_emp AND (SELECT EXTRACT(MONTH FROM P.Date_Jour)) = 6 AND (SELECT EXTRACT(YEAR FROM P.Date_Jour)) = 2021;
        Cursor.execute(f"""SELECT id_emp,concat(E.Nom,' ',E.Prenom),SUM(NbrHeures),SUM(Heure_mise_en_consideration),SUM(P.Retard),SUM(P.Absence),SUM(P.HeuresSupp),SUM(P.vintCinq),SUM(P.cinquante),SUM(P.cent) FROM Pointage P INNER JOIN Employees E ON concat(E.Nom,' ',E.Prenom) = '{self.info_List[0]}'  AND E.Mat_Emp = P.id_emp AND (SELECT EXTRACT(MONTH FROM P.Date_Jour)) = {self.info_List[1]} AND (SELECT EXTRACT(YEAR FROM P.Date_Jour)) = {self.info_List[2]};""")
        donnees = Cursor.fetchone()
        db.close()
        print(donnees)
        self.lineEdit.setText(f"""{self.info_List[1]}-{self.info_List[2]} """)
        self.label.setText(str(donnees[1]))
        self.lineEdit_2.setText(str(donnees[2]))
        self.lineEdit_3.setText(str(donnees[3]))
        self.lineEdit_4.setText(str(donnees[4]))
        self.lineEdit_5.setText(str(donnees[5]))
        self.lineEdit_6.setText(str(donnees[6]))
        self.lineEdit_8.setText(str(donnees[7]))
        self.lineEdit_9.setText(str(donnees[8]))
        self.lineEdit_10.setText(str(donnees[9]))
        self.pushButton_3.clicked.connect(self.fermer)
        self.pushButton_2.clicked.connect(self.valider)

    def valider(self):
        self.msg = QtWidgets.QMessageBox()
        self.msg.setWindowTitle('Info')
        self.msg.setText("Pouvez-vous imprimer l'attestation avant de sauvegarder ?")
        #self.msg.addButton(self.msg.Ok)
        #self.msg.addButton(self.msg.No)
        self.msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        self.msg.buttonClicked.connect(self.nextWindow)
        self.msg.exec_()


    def get_nom_directeur(self):
        db._open_connection()
        cursor = db.cursor(buffered=True)
        cursor.execute("SELECT CONCAT(Nom,' ',Prenom ),Mat_Emp FROM Employees WHERE Fonction = 'Admin';")
        adminName = cursor.fetchone()[0]
        db.close()
        return str(adminName)


    def nextWindow(self, button):
        print('h')
        print(button.text())
        if button.text() == 'OK':
            print('imprimer ...')
            print('ok')
            list_information = [str(self.label.text()),str(self.lineEdit.text()),self.get_nom_directeur(),str(self.lineEdit_2.text()),str(self.lineEdit_3.text()),str(self.lineEdit_4.text()),str(self.lineEdit_5.text()),str(self.lineEdit_6.text())]
            print(len(list_information))
            self.Imprimer_wind = Imprimer_class(list_information)
        elif button.text() == 'Cancel':
            self.msg.close()

    def fermer(self):
        self.close()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = bilan()
    ui.show()
    sys.exit(app.exec_())