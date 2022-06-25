import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from db_connect import mydb as db
from Message import message_ui
import Resources_rc
class setup_ui(QtWidgets.QDialog):
    def __init__(self,id_conge):
        super().__init__()
        loadUi("DoubleClik.ui",self)
        self.radioButton.toggled.connect(self.Samedi)    
        self.pushButton.clicked.connect(self.Envoyer)
        self.pushButton_3.clicked.connect(self.Accepter)
        self.pushButton_2.clicked.connect(self.Refuser)
        self.id_cong = id_conge

    def Refuser(self):
        db._open_connection()
        cursor = db.cursor(buffered=True)
        cursor.execute(f'''UPDATE Conge set Validation = 'R' WHERE Id = {self.id_cong}''')
        db.commit()
        db.close()
        self.close()
    def Accepter(self):
        db._open_connection()
        cursor = db.cursor(buffered=True)
        cursor.execute(f'''UPDATE Conge set Validation = 'V' WHERE Id = {self.id_cong}''')
        db.commit()
        db.close()
        self.close()
    def Samedi(self):
        self.lineEdit_5.setReadOnly(False)
        print(self.id_cong)
    def Envoyer(self):
        if self.lineEdit_5.text() != '':
            db._open_connection()
            cursor = db.cursor(buffered=True)
            cursor.execute(f'''UPDATE Conge set NbrJours = {float(self.lineEdit_5.text())} WHERE Id = {self.id_cong}''')
            cursor.execute(f'''UPDATE Conge set Validation = 'E' WHERE Id = {self.id_cong}''')
            db.commit()
            db.close()
        self.msg = message_ui(self.id_cong)
        self.msg.show()
        self.close()
if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = setup_ui()
    ui.show()
    sys.exit(app.exec_())