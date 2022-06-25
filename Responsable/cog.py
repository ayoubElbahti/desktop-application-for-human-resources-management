import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets,QtCore
from Supprimer_Acceptation import Ui_sup
from Rechercher_Acceptation import Ui_rech
from PyQt5.QtCore import Qt
from Demande_Responsable import Ui_Form
from reloading_screen import waiting
from PyQt5 import QtGui
from message import msg
import Resources_rc
import sqlite3
check = False
check_Image = True
id_emp_global = 0
class Login(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        loadUi("Login_1.ui",self)
        self.setWindowIcon(QtGui.QIcon('responsable_ico.ico'))
        self.pushButton_3.setStyleSheet("""
 QPushButton#pushButton_3{
image: url(:/Icons/Icons/hidepass-removebg-preview.png);
border:none;
}
QPushButton#pushButton_3:hover{
background-color:#E2EEEE;
border-radius: 3px;
}
            """)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.pushButton_3.clicked.connect(self.ShowPassword) 
        self.pushButton_2.clicked.connect(self.checkInfo_1)
        self.pushButton_6.clicked.connect(self.sortir)
        self.pushButton_7.clicked.connect(self.btn_min_clicked)


    def open_connection(self):
        return sqlite3.connect("appp.db")

    def btn_min_clicked(self):
        self.showMinimized()

    def sortir(self):
        self.close()

    def checkInfo_1(self):
        timer = QtCore.QTimer()
        timer.singleShot(3000,self.checkInfo)

    def ShowPassword(self):
        global check_Image
        if check_Image:
            self.pushButton_3.setStyleSheet("""
    QPushButton#pushButton_3{
image: url(:/Icons/Icons/showpass-removebg-preview.png);
border:none;
}
QPushButton#pushButton_3:hover{
background-color:#E2EEEE;
border-radius: 3px;
}            
            """)
            self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
            check_Image = False
        else :
            self.pushButton_3.setStyleSheet("""border : none;
            image: url(:/Icons/Icons/hidepass-removebg-preview.png);
            """)
            check_Image = True
            self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)



    def checkInfo(self):
        global id_emp_global
        
        self.setEnabled(False)
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        db = self.open_connection()
        cursor = db.cursor()
        cursor.execute(f'''SELECT * FROM Responsable;''')
        session = cursor.fetchall()
        db.close()
        for i in session:
            if i[2] == self.lineEdit.text() and i[3] == self.lineEdit_2.text():
                id_emp_global = i[1]
                self.setEnabled(True)
                self.window_entrer = mainwind()
                self.close()
                self.window_entrer.show()
            else :
                self.setEnabled(True)
                self.label_8.setText('Username ou Mot de passe incorrect !')



class mainwind(QtWidgets.QMainWindow):
    
    def refresh(self):
        if self.pushButton_16.isChecked():
            self.verifier = False
        self.tableWidget_3.setRowCount(0)
        self.refresh_Attente()
    
    

    def setColortoRow(self, table, row, color):
        for j in range(table.columnCount()):
            table.item(row, j).setBackground(color)
    
    def doubleclicked(self):
        print('heelo')
        row = self.tableWidget_3.currentRow()
        print(row)
        if row > -1:
            self.product_id = []
            self.product_id.append(self.tableWidget_3.item(row, 4).text())
            print('date debut',self.product_id[0])
            print('num matricule : ',self.num_matricules[row])
            db = self.open_connection()
            cursor = db.cursor()
            cursor.execute(f"""SELECT M.Contenu,Conge.Id FROM Conge INNER JOIN Message M ON Conge.Mat_Emp = {self.num_matricules[row]} AND Conge.DateDebut = '{self.product_id[0]}' AND M.Id_Conge = Conge.Id;""")
            self.Contenu = cursor.fetchone()            
            db.commit()
            db.close()
            if self.verifier == True:
                self.msg = msg(self.Contenu[0],self.Contenu[1])
                self.msg.show()
            
    def Supprimer_Demande(self):
        print('supp ...')
        row = self.tableWidget_3.currentRow()
        print(row)
        if row > -1:
            self.product_id = []
            self.product_id.append(self.tableWidget_3.item(row, 4).text())
            print('date debut',self.product_id[0])
            print('num matricule : ',self.num_matricules[row])
            db = self.open_connection()
            cursor = db.cursor()
            cursor.execute(f"""UPDATE  Conge SET Validation = 'S' WHERE Mat_Emp = {self.num_matricules[row]} AND DateDebut = '{self.product_id[0]}';""")
            db.commit()
            db.close()
        self.refresh()
            
    def refresh_Attente(self):
        global check
        self.num_matricules = {}
        dict_color = {'C':QtGui.QColor(252, 237, 191),'R':QtGui.QColor(252, 161, 148),'V':QtGui.QColor(190, 254, 179),'H':QtGui.QColor(183, 254, 213)}
        db = self.open_connection()
        self.connection = db.cursor()
        if check == False:
            print('button recherecher not selected')
            self.Requete = f"""SELECT Employees.Mat_Emp, Employees.Nom, Employees.Prenom,Conge.Type_de_Conge,Conge.DateDebut,Conge.NbrJours,Conge.DateFin,Conge.Validation FROM Employees INNER JOIN Conge ON Employees.Mat_Emp=Conge.Mat_Emp AND Employees.Mat_Responsable = {id_emp_global} AND Conge.Validation != 'S' ORDER BY Conge.Validation;"""
        check = False
        print(self.Requete)
        self.connection.execute(self.Requete)
        self.result = self.connection.fetchall()
        if self.result == []:
            self.label_7.setHidden(False)
        else:
            self.label_7.setHidden(True)
        db.close()
        for lignes,row_data in enumerate(self.result):
            self.tableWidget_3.insertRow(lignes)
            for colonne,self.resultat_colonne in enumerate(row_data):
                
                str_colonne = str(self.resultat_colonne)
                if colonne == 0:
                    self.num_matricules[lignes] = self.resultat_colonne
                    str_colonne = 'Mat ' + str(self.resultat_colonne)
                item1 = QtWidgets.QTableWidgetItem(str_colonne)
                item1.setFlags(item1.flags() ^ Qt.ItemIsEditable)
                
                self.tableWidget_3.setItem(lignes, colonne,item1)
                if colonne == 7:
                    self.searchBtn=QtWidgets.QPushButton('Supprimer')
                    self.searchBtn.setDown(True)
                    self.searchBtn.setStyleSheet("""QPushButton{
                        Vertical Size : 30px;
                        margin:3px;
                    qproperty-icon:url(dd.png);
                    qproperty-iconSize: 20px 20px;}
                      .QPushButton:hover {
	        
	        background-color:#DCFF9B ;
            }
                  """)
    
                    self.tableWidget_3.setCellWidget(lignes,colonne,self.searchBtn)
                    var = dict_color[str_colonne]
                    if str_colonne == 'V':
                        self.searchBtn.setEnabled(False)
                    self.searchBtn.clicked.connect(self.Supprimer_Demande)
                if colonne == 7:
                    # hadi 3ndak tnsaha !!!!
                    item1 = QtWidgets.QTableWidgetItem(' ')
                self.tableWidget_3.setItem(lignes, colonne,item1)
            self.setColortoRow(self.tableWidget_3,lignes,var)
        print(self.num_matricules)
        
        
#je peux faire un ductioannaire pour optimiser refresh

    
    
    def rechercher(self):
        global check
        check = True
        print('rechercher selected')
        num_matricule = 2
        self.Requete = f"""SELECT Employees.Mat_Emp, Employees.Nom, Employees.Prenom,Conge.Type_de_Conge,Conge.DateDebut,Conge.NbrJours,Conge.DateFin,Conge.Validation FROM Employees INNER JOIN Conge ON Employees.Mat_Emp= {num_matricule} ORDER BY Conge.Validation;"""
        self.refresh()
    def OuvrirCompte(self):
        self.Conge.setCurrentIndex(2)
    def OuvrirTousDemandes(self):
        self.Conge.setCurrentIndex(1)
    def Ouvrirconge(self):
        self.Conge.setCurrentIndex(0)
    def __init__(self):
        global id_emp_global
        super().__init__()
        loadUi("Auto_Aeroport.ui",self)
        self.setWindowTitle('Conge Responsable')
        self.setWindowIcon(QtGui.QIcon('responsable_ico.ico'))
        self.cg = Ui_Form(id_emp_global)
        self.horiz_ayoub.addWidget(self.cg)
        self.refresh_Attente()
        stylesheet = "::section{Background-color:rgb(114, 123, 184)}"
        self.tableWidget_3.horizontalHeader().setStyleSheet(stylesheet)
        self.tableWidget_3.verticalHeader().setVisible(False)
        self.Login_Info()
        self.Ouvrirconge()
        #self.tableWidget_2.verticalHeader().setVisible(False)
        #self.tableWidget_4.verticalHeader().setVisible(False)
        self.pushButton_16.clicked.connect(self.refresh)
        self.pushButton_16.setStyleSheet("QPushButton {"
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
                             "background-color : #54E141 ;"
                             "}"
                             )
        self.pushButton_16.setIcon(QtGui.QIcon(":/Icons/Icons/refresh-removebg-preview.png"))

        self.pushButton_9.setIcon(QtGui.QIcon(":/Icons/Icons/button-305726_960_720-removebg-preview.png"))
        self.pushButton_9.setStyleSheet("QPushButton {"
	        "box-shadow:inset 0px 1px 0px 0px #276873;"
	        "background:linear-gradient(to bottom, #006387 5%, #408c99 100%);"
	        "background-color:#E9ECE5;"
	        "border:1px solid #29668f;"
	        "display:inline-block;"
	        "cursor:pointer;"
            "border-radius:3px;"
            "padding : -2px;"
            "font-family:Arial;"
            "text-align: left;"
	        "font-size:15px;"


"qproperty-iconSize: 30px 30px;"
	        "color:#000000;"
	        "font-family: Barlow, sans-serif;"
	        "font-size:15;"
	        
	        "text-decoration:none;"
            "}"
            ".QPushButton:hover {"
	        "background:linear-gradient(to bottom, #408c99 5%, #006387 100%);"
	        "background-color:#ADAEAC;"
            "}"
            ".QPushButton:active {"
	        "position:relative;"
	        "top: 2px;"
            "}"
            ".QPushButton::pressed  {"

                             "background-color : rgb(255, 51, 51) ;"
                             "}"
                             )
        self.pushButton_17.setIcon(QtGui.QIcon(":/Icons/Icons/notifi.png"))
        self.pushButton_17.setStyleSheet("QPushButton {"
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

                             "background-color : #F8FA81 ;"
                             "}"
                             )


        self.pushButton_2.clicked.connect(self.Ouvrirconge)
        self.pushButton_3.clicked.connect(self.OuvrirTousDemandes)
        self.pushButton_7.clicked.connect(self.OuvrirCompte)
        self.pushButton_9.clicked.connect(self.ShutDown)
        self.pushButton_17.clicked.connect(self.Notification)
        self.tableWidget_3.doubleClicked.connect(self.doubleclicked)
        self.verifier = False
    def Notification(self):
        global check
        check = True
        self.verifier = True
        self.Requete = f"""SELECT Employees.Mat_Emp, Employees.Nom, Employees.Prenom,Conge.Type_de_Conge,Conge.DateDebut,Conge.NbrJours,Conge.DateFin,Conge.Validation FROM Employees INNER JOIN Conge ON Employees.Mat_Emp=Conge.Mat_Emp AND Employees.Mat_Responsable = {id_emp_global} AND Conge.Validation != 'S' AND Conge.Messages = 1 ORDER BY Conge.Validation;"""
        self.refresh()
        #self.pushButton_14.clicked.connect(self.refresh)
        #self.pushButton_15.clicked.connect(self.refresh)
    def open_connection(self):
        return sqlite3.connect("appp.db")
    def ShutDown(self):
        self.lg = Login()
        self.close()
        self.lg.show()
    def Login_Info(self):
        global id_emp_global
        db = self.open_connection()
        cursor = db.cursor()
        cursor.execute(f"""SELECT Nom,Prenom FROM Employees WHERE Mat_Emp = {int(id_emp_global)};""")
        inf = cursor.fetchone()
        print(inf)
        self.label_2.setText(str(id_emp_global))
        self.label_3.setText(inf[0])
        self.label_4.setText(inf[1])
        db.close()
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = Login()
    ui.show()
    sys.exit(app.exec_())