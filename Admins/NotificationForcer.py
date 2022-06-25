from sqlite3.dbapi2 import Cursor
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets,QtCore,QtGui
import Resources_rc
import sys
import sqlite3
class NotificationForcerClasse(QtWidgets.QDialog):
    def __init__(self,id_emp):
        super().__init__()
        loadUi("NotificationForcer.ui",self)
        #self.lineEdit.setText()
        #self.lineEdit_2.setText()
        self.pushButton.clicked.connect(self.Valider)
        self.id_emp = id_emp
    def Valider(self):
        self.TraiterCongePaye()
        
    def TraiterCongePaye(self):
        db = self.open_connection()
        Cursor = db.cursor()
        for i in self.id_emp:
            self.result = int(self.lineEdit.text()) - int(self.lineEdit_2.text())
            Cursor.execute(f"""SELECT * FROM CongePaye WHERE id_emp = {i};""")
            valeur = Cursor.fetchone()
            print(self.result)
            self.result = self.result - valeur[2]
            print(self.result)
            if self.result >= 0:
                print('congé payé ...')
                Cursor.execute(f"""UPDATE CongePaye SET nbr_jours = 0 WHERE id_emp = {i};""")
                Cursor.execute(f"""SELECT * FROM CongeRecupere WHERE id_emp = {i};""")
                result_1 = Cursor.fetchone()
                self.result = self.result - int(result_1[2]/9)
                print('self.result = self.result - int(result_1[2]/9)   ',self.result ,int(result_1[2]/9))
                if self.result > 0:
                    print('congé Recupérer ...')
                    Cursor.execute(f"""UPDATE CongeRecupere SET heures_récupération = 0 WHERE id_emp = {i};""")
                    print('il rest ',self.result,'')
                elif self.result < 0:
                    Cursor.execute(f"""UPDATE CongeRecupere SET heures_récupération = {result_1[2] - (int(result_1[2]/9)*9)} WHERE id_emp = {i};""")
            else:
                print('congé payé ... sans result')
                Cursor.execute(f"""UPDATE CongePaye SET nbr_jours = {-self.result} WHERE id_emp = {i};""")
            db.commit()
        db.close()
        print('db closed')
    def open_connection(self):
        return sqlite3.connect("C:/Users/EL BAHTI/Desktop/Conge/Connection/appp.db")
if __name__ == "__main__":
    import sys
    liste = [2, 'Bensam jalal', '--', '2021-07-28', '--', '0', '--', '0', '0', '0', '0', '0', '0', 'Non', '0']
    app = QtWidgets.QApplication(sys.argv)
    ui = NotificationForcerClasse([1,2])
    ui.show()
    sys.exit(app.exec_())
