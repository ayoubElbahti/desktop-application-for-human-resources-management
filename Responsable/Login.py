from PyQt5.uic import loadUi
from PyQt5 import QtWidgets,QtCore
from db_connect import mydb as db
check_Image = True
import Resources_rc
class Login(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        loadUi("Login.ui",self)
        self.pushButton_2.setStyleSheet("""border : none;
            image: url(:/Icons/Icons/hidepass-removebg-preview.png);
            """)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.pushButton_2.clicked.connect(self.ShowPassword) 
        self.pushButton.clicked.connect(self.checkInfo)
    def ShowPassword(self):
        global check_Image
        if check_Image:
            self.pushButton_2.setStyleSheet("""border : none;
            image: url(:/Icons/Icons/hidepass-removebg-preview.png);
            """)
            self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
            check_Image = False
        else :
            self.pushButton_2.setStyleSheet("""border : none;
            image: url(:/Icons/Icons/showpass-removebg-preview.png);
            """)
            check_Image = True
            self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)

    def checkInfo(self):
        
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        db._open_connection()
        cursor = db.cursor()
        cursor.execute(f'''SELECT Id,Num_Mat FROM Responsable WHERE Username = '{username}' AND MotDePasse = '{password}';''')
        session = cursor.fetchone()
        print(session)
        if len(session) != 0:
            print('user exist ...')
        db.close()
            #☺self.error_dialog = QtWidgets.Qmsg
            #self.error_dialog.showMessage('Oh no!')
            #msg = QtWidgets.QMessageBox.show(self,'CHAMP INVALID ! ','Vous été oublié des champs Vides !',QtWidgets.QMessageBox.Ok)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Form()
    ui.show()
    sys.exit(app.exec_())