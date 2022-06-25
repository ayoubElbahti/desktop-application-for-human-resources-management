import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
import sqlite3
class Ui_rech(QtWidgets.QDialog):
    def supprimerDialoq_accepter(self):
        try:
            self.Refresh_Accept_Supp()
        except:
            self.close()
            print('aucun element !!!')
    def open_connection(self):
        return sqlite3.connect("appp.db")
    def Refresh_Accept_Supp(self):
        self.tableWidget.setRowCount(0)
        db = self.open_connection()
        connection_s = db.cursor()
        connection_s.execute(f""" SELECT Id,Type_de_Conge,DateDebut,DateFin FROM Conge WHERE Mat_Emp = {self.var[0]}""")
        self.result = connection_s.fetchall()
        for lignes,row_data in enumerate(self.result):
            self.tableWidget.insertRow(lignes)
            for colonne,self.resultat_colonne in enumerate(row_data):
                str_colonne = str(self.resultat_colonne)
                if self.resultat_colonne == 1:
                    str_colonne = 'N° ' + str(self.resultat_colonne)
                self.tableWidget.setItem(lignes, colonne,QtWidgets.QTableWidgetItem(str_colonne))
    def fermer_prg(self):
        self.close()
    def __init__(self,Nom,Prenom):
            super().__init__()
            loadUi("Rechercher_Acceptation.ui",self)
            self.tableWidget.verticalHeader().setVisible(False)
            self.lineEdit.setText(str(Nom)+' '+str(Prenom))
            db = self.open_connection()
            connection_s1 = db.cursor()
            connection_s1.execute(f"""SELECT Mat_Emp,Nom FROM Employees WHERE Nom = '{Nom}' and Prenom = '{Prenom}';""")
            self.var = connection_s1.fetchone()
            self.Refresh_Accept_Supp()
            self.pushButton.clicked.connect(self.fermer_prg)
    