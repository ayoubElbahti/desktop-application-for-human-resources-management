from PyQt5.uic import loadUi
from PyQt5 import QtGui,QtCore
from PyQt5 import QtWidgets,QtCore
from db_connect import mydb as db
from sentEmails import Emails
check_Image = True
import Resources_rc
class msg_modification(QtWidgets.QDialog):
    def __init__(self,id_conge,nbr):
        super().__init__()
        loadUi("msg.ui",self)
        self.envoyer = False
        self.idconge = id_conge
        self.test = False
        self.nbrjours = nbr
        self.setWindowTitle('Modification')
        self.pushButton.clicked.connect(self.mod)
        self.pushButton.setIcon(QtGui.QIcon(":/Icons/Icons/msg_env.jpeg"))
        self.pushButton.setStyleSheet("QPushButton{"
	        "box-shadow:inset 0px 1px 0px 0px #276873;"
	        "background:linear-gradient(to bottom, #006387 5%, #408c99 100%);"
	        "background-color:#E9ECE5;"
	        "border:1px solid #29668f;"
	        "display:inline-block;"
	        "cursor:pointer;"
            "border-radius:3px;"
            "border-radius:0px;"
            	        "font-family:Arial;"
            "text-align: left;"
	        "font-size:15px;"


"qproperty-iconSize: 20px 20px;"
	        "color:#000000;"
	        "font-family:Arial;"
	        "font-size:15;"
	        
	        "text-decoration:none;"
            "}"
            ".QPushButton:hover {"
	        "background:linear-gradient(to bottom, #408c99 5%, #006387 100%);"
	        "background-color:#ADAEAC;"
            "}"
            ".QPushButton:active {"
	        "position:relative;"
	        "top:1px;"
            "}"
            ".QPushButton::pressed  {"

                             "background-color : #92F760;"
                             "}"
                             )
    def modifer_jours(self):
        print('modofier nombre jours ',self.nbrjours)
        db._open_connection()
        cursor = db.cursor()
        cursor.execute(f"""UPDATE Conge set NbrJours = {self.nbrjours} WHERE Id = {self.idconge} ;""")
        db.commit()
        db.close()
    def mod(self):
        db._open_connection()
        cursor = db.cursor()
        cursor.execute(f"""INSERT INTO Message(Id_Conge,Contenu) VALUES({self.idconge},'{self.textEdit.toPlainText()}');""")
        cursor.execute(f"""UPDATE Conge SET Messages = 1 WHERE Id = {self.idconge};""")
        db.commit()
        db.close()
        self.modifer_jours()
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText('Modification envoyé ')
        self.msg.setWindowTitle('Envoyer')
        self.msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.sentEmail_mod()
        self.msg.show()
        self.close()
        self.test = True
    def Initialiser(self,email,motdepasse,email_responsable):
        self.email = email
        self.modepasse = motdepasse
        self.email_responsable = email_responsable
    def sentEmail_mod(self):
        text = f"""{self.textEdit.toPlainText()}"""
        self.mail = Emails(self.email,self.modepasse,self.email_responsable,str(text))
        pass
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = msg_modification(314,1)
    ui.show()
    sys.exit(app.exec_())