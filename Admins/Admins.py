from sqlite3.dbapi2 import Row
import sys
from typing import Text
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5 import QtGui,QtCore,QtGui
from PyQt5.QtCore import Qt
from NotificationForcer import NotificationForcerClasse
#from db_connect import mydb as db
from Notification import NotificationClasse
from Pointage_1 import PointageClasse
import Resources_rc
from DoubleClick import setup_ui
from msg_env import message_ui
from sentEmails import Emails
from send_Message_Modification import msg_modification as msg_modification_mod
from Pointage import msg_modification
from Bilan import bilan
from datetime import timedelta
from Sauvegarder import save_pointage
from Add_emp import add_employe
from supp_emp import supp_employe
from Imprimer import Imprimer_class
import datetime
from Pdf_Pointage import create_pdf
import sqlite3
SituationFamilial = {"Célibataire":0,"Veuf":1,"Marié":2,"Divorcé":3}
Mois_Fr = {'Janvier':1,'Février':2,'Mars':3,'Avril':4,'Mai':5,'Juin':6,'Juillet':7,'Août':8,'Septembre':9,'Octobre':10,'Novembre':11,'Décembre':12}

check_nbr_samedi_1 = {'-':0,'22h -> 06h':1,'06h -> 14h': 2,'14h -> 22h':3}
check_nbr_samedi = {'-':True,'22h -> 06h':True,'06h -> 14h': False,'14h -> 22h':False}
Etats_Conge = {'R':'Refusé','V':'Accepté','C':'En attente','S':'Annulé par Responsable','M':'Renvoyer après modification','H':'Accepté par le RH'}
id_emp_global = 0
check_Image = True
class Login(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        loadUi("Login_1.ui",self)
        self.Aujourdhuit = datetime.datetime.today().strftime("%Y-%m-%d")
        print(self.Aujourdhuit)
        self.setWindowIcon(QtGui.QIcon('AEROAUTO_ADM.ico'))
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
        self.pushButton_2.clicked.connect(self.checkInfo)
        self.pushButton_6.clicked.connect(self.sortir)
        self.pushButton_7.clicked.connect(self.btn_min_clicked)


    def btn_min_clicked(self):
        self.showMinimized()

    def sortir(self):
        self.close()



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


    def open_connection(self):
        return sqlite3.connect("C:/Users/EL BAHTI/Desktop/Conge/Connection/appp.db")


    def checkInfo(self):
        global id_emp_global
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        db = self.open_connection()
        cursor = db.cursor()
        cursor.execute(f'''SELECT * FROM Administrateur;''')
        session = cursor.fetchall()
        db.close()
        for i in session:
            if i[2] == self.lineEdit.text() and i[3] == self.lineEdit_2.text():
                id_emp_global = i[1]
                self.window_entrer = Admins()
                self.close()
                self.window_entrer.show()
            else :
                self.label_8.setText('Username ou Mot de passe incorrect !')



class Admins(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        loadUi("Admins.ui",self)
        self.tabWidget.removeTab(1)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        #self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowTitle('Administrateur')
        self.setWindowIcon(QtGui.QIcon('AEROAUTO_ADM.ico'))
        self.check_validation = False
        
        header = self.tableWidget_2.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(7, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(8, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(9, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(10, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(11, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(12, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(13, QtWidgets.QHeaderView.ResizeToContents)

        self.tableWidget_2.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.pushButton_17.clicked.connect(self.AjouterEmploye)
        self.pushButton_23.clicked.connect(self.SupprimerEmploye)
        self.comboBox.currentIndexChanged.connect(self.WeekEnd_Ferier)
        self.test = True
       # just for illustration
        self.pushButton_9.setIcon(QtGui.QIcon(":/Icons/Icons/refresh-removebg-preview.png"))
        self.pushButton_9.setStyleSheet("QPushButton{"
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

                             "background-color : rgb(255, 51, 51) ;"
                             "}"
                             )


        self.pushButton_11.setIcon(QtGui.QIcon(":/Icons/Icons/refresh-removebg-preview.png"))
        self.pushButton_11.setStyleSheet("QPushButton{"
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
	        "font-size: 10px;"


"qproperty-iconSize: 15px 15px;"
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

                             "background-color : rgb(255, 51, 51) ;"
                             "}"
                             )

        self.pushButton_8.setIcon(QtGui.QIcon(":/Icons/Icons/search-icon.png"))
        self.pushButton_8.setStyleSheet("QPushButton{"
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
	        "font-size: 10px;"
	        
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

                             "background-color : rgb(255, 51, 51) ;"
                             "}"
                             )
        self.pushButton_10.setIcon(QtGui.QIcon(":/Icons/Icons/historiques.png"))
        self.pushButton_10.setStyleSheet("QPushButton {"
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

                             "background-color : rgb(255, 51, 51) ;"
                             "}"
                             )
        self.checkBox.clicked.connect(self.Off)
        self.Aujourdhuit = datetime.datetime.today().strftime("%Y-%m-%d")
        self.lineEdit_2.setText(str(self.Aujourdhuit))
        print(self.Aujourdhuit)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.pushButton_16.clicked.connect(self.fermer)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.loading_movie = QtGui.QMovie("Loading_mg.gif")
        self.label.setMovie(self.loading_movie)
        self.loading_movie.start()
        #self.setGeometry(50,50,200,200)
        #self.label.show()
        names = self.getListNoms()
        self.miseAjours_Tab_Conge()
        self.CheckingPointage()
        self.Hinding_grpBoux()
        db = sqlite3.connect("C:/Users/EL BAHTI/Desktop/Conge/Connection/appp.db")
        print('db connected')
        Cursor = db.cursor()
        Cursor.execute(f"""SELECT Date_Jour,Id FROM Pointage WHERE Modification = 0 and Date_Jour != '{self.Aujourdhuit}' ORDER BY Date_Jour;""")
        result = Cursor.fetchall()
        liste_1 = []
        j = ' '
        for i in result:
            if j != i[0]:
                liste_1.append(i[0])
            j = i[0]
        db.close()
        if len(liste_1) != 0:
            text = ''
            for b in liste_1:
                text = text + ' | ' + b
            self.msg = NotificationClasse(text)
            self.msg.show()
            
        
        self.fonction = self.getFonction()
        if self.fonction == 'Admin':
            self.tab_4.setEnabled(False)
        self.pushButton_9.clicked.connect(self.Actualiser)
        self.tableWidget.doubleClicked.connect(self.doubleclicked)
        self.tableWidget_2.doubleClicked.connect(self.doubleclicked_2)
        self.pushButton_2.clicked.connect(self.Hinding_grpBoux)
        self.pushButton_6.clicked.connect(self.Refuser)
        self.pushButton_25.clicked.connect(self.ShutDown)
        
        self.pushButton_25.setIcon(QtGui.QIcon(":/Icons/Icons/button-305726_960_720-removebg-preview.png"))
        self.pushButton_25.setStyleSheet("QPushButton {"
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
        self.tabWidget_2.setCurrentIndex(0)
        self.pushButton_5.clicked.connect(self.Accepter)
        self.pushButton_10.clicked.connect(self.Historique)
        self.pushButton.clicked.connect(self.Ouvrirconge)
        self.pushButton_13.clicked.connect(self.OuvrirEmployees)
        self.pushButton_14.clicked.connect(self.OuvrirLogin)
        self.pushButton_20.clicked.connect(self.ResherchEmployees)
        self.Login_Info()
        self.pushButton_3.clicked.connect(self.OuvrirTousDemandes)
        self.spinBox.valueChanged.connect(self.spin_selected)
        self.pushButton_15.clicked.connect(self.Modfier)
        self.pushButton_8.clicked.connect(self.List_Employees)
        self.pushButton_11.clicked.connect(self.Bilan)
        self.pushButton_12.clicked.connect(self.btn_min_clicked)
        self.pushButton_18.clicked.connect(self.Annuler)
        self.pushButton_26.clicked.connect(self.miseAjours_tab_pointage)
        stylesheet = "::section{Background-color:#69DFE8}"
        self.tableWidget.horizontalHeader().setStyleSheet(stylesheet)
        names = self.getListNoms()
        completer = QtWidgets.QCompleter(names)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.lineEdit_29.setCompleter(completer)
        self.tableWidget.verticalHeader().setVisible(False)


    def ShutDown(self):
        self.lg = Login()
        self.close()
        self.lg.show()

    def traitementAbsenceOff(self):
        db = self.open_connection()
        cursor = db.cursor()
        print(f"""SELECT id_emp,Absence,HeuresSupp FROM Pointage WHERE Date_Jour = '{self.lineEdit_2.text()}' AND ( Absence = 1 OR HeuresSupp != 0 );""")
        cursor.execute(f"""SELECT id_emp,Absence,heures_récupération FROM Pointage WHERE Date_Jour = '{self.lineEdit_2.text()}' AND ( Absence = 1 OR HeuresSupp != 0 );""")
        result = cursor.fetchall()
        if len(result) != 0:
            for i in result:
                if i[1] == 1:
                    cursor.execute(f"""DELETE FROM AbsenceJ WHERE mat_emp = {i[0]} AND Date_absence = '{self.lineEdit_2.text()}';""")
        cursor.execute(f"""UPDATE RecupererHeures SET Heure = 0 WHERE mat_emp = {i[0]};""")
        db.commit()
        db.close()
    def Off(self):
        if self.checkBox.isChecked():
            self.traitementAbsenceOff()
            db = self.open_connection()
            cursor = db.cursor()
            print(f"""UPDATE Pointage SET Off = 1,Modification = 1,Temps_de_travail = '--',Heure_Entrer = '--',Heure_mise_en_consideration = 0,Heure_Sortir = '--,NbrHeures = 0,HeuresSupp = 0,vintCinq = 0,cinquante = 0,cent = 0,heures_récupération = 0,
            Absence = 0,Retard = 0 WHERE Date_Jour = '{self.lineEdit_2.text()}';""")
            cursor.execute(f"""UPDATE Pointage SET Off = 1,Modification = 1,Temps_de_travail = '--',Heure_Entrer = '--',Heure_mise_en_consideration = 0,Heure_Sortir = '--',NbrHeures = 0,HeuresSupp = 0,vintCinq = 0,cinquante = 0,cent = 0,heures_récupération = 0,
            Absence = 0,Retard = 0 WHERE Date_Jour = '{self.lineEdit_2.text()}';""")
            
            db.commit()
            db.close()
        else:
            db = self.open_connection()
            cursor = db.cursor()
            cursor.execute(f"""UPDATE Pointage SET Off = 0,Modification = 0 WHERE Date_Jour = '{self.lineEdit_2.text()}';""")
            db.commit()
            db.close()
        self.miseAjours_tab_pointage()


    def WeekEnd_Ferier(self):
        if self.comboBox.currentText() == "Férier":
            self.msg = NotificationForcerClasse(self.getListIds())
    def nouveauPointage(self,date):
        ids = self.getListIds()
        db = self.open_connection()
        cursor = db.cursor()
        for i in ids:
            requete = f"""INSERT INTO Pointage(Date_Jour,id_emp) VALUES('{date}',{i});"""
            print(requete)
            cursor.execute(requete)
        db.commit()
        db.close()

    def getMatricule(self,names_emp):
        db = self.open_connection()
        cursor = db.cursor()
        cursor.execute(f"""SELECT Mat_Emp,Nom FROM Employees WHERE Nom || ' ' || Prenom = '{names_emp}';""")
        test = cursor.fetchone()
        db.close()
        return test[0]


    def CheckingPointage(self):
        self.requete_Date = f"""AND P.Date_Jour = '{self.Aujourdhuit}' """
        if self.TesterNouveauJour():
            print('bonjour vous etes dans nouveau jour')
            dateFin = self.GetFinDatePointage()
            listeJ = self.ListerLesJoursAvants(dateFin,self.Aujourdhuit)
            for i in listeJ:
                self.nouveauPointage(i)
            self.miseAjours_tab_pointage()
        else:
            print('bonjour vous etes dans meme jours')
            self.miseAjours_tab_pointage()

    #fonction des jours

    def GetFinDatePointage(self):
        db = sqlite3.connect("C:/Users/EL BAHTI/Desktop/Conge/Connection/appp.db")
        print('db connected')
        Cursor = db.cursor()
        Cursor.execute("SELECT * FROM Pointage WHERE Modification = 1 ORDER BY Date_Jour;")
        result = Cursor.fetchall()
        db.close()
        for i in result:
            l = i[3]
        return l


#fonctions des temps

    def ListerLesJoursAvants(self,dateDebut,dateEnd):
        dateDebut = datetime.datetime.today().strptime(dateDebut,"%Y-%m-%d")
        dateEnd = datetime.datetime.strptime(dateEnd,"%Y-%m-%d")
        ss = dateEnd - dateDebut
        ss = ss.days +1
        liste = []
        for i in range(ss):
            day = dateDebut+timedelta(days=i)
            liste.append(day.strftime("%Y-%m-%d"))
        return liste

    def TesterNouveauJour(self):
        Aujourdhuit = datetime.datetime.today().strftime("%Y-%m-%d")
        db = self.open_connection()
        cursor = db.cursor()
        print(f"""SELECT * FROM Pointage WHERE Date_Jour = '{Aujourdhuit}';""")
        cursor.execute(f"""SELECT * FROM Pointage WHERE Date_Jour = '{Aujourdhuit}';""")
        result = cursor.fetchall()
        db.close()
        if len(result) == 0:
            return True
        else:
            return False


    def SupprimerEmploye(self):
        mat_emp = self.getMatricule(str(self.lineEdit_29.text()))
        print('employe detecter = ',mat_emp)
        db = self.open_connection()
        cursor = db.cursor()
        cursor.execute(f"""SELECT COUNT(*),Id,Mat_Emp FROM Conge WHERE Mat_Emp = {mat_emp} ORDER BY Id DESC""")
        id_conge = cursor.fetchone()
        print(id_conge)
        if id_conge[0] != 0:
            cursor.execute(f"""DELETE FROM Message WHERE Id_Conge = {id_conge[1]};""")
        cursor.execute(f"""DELETE FROM CongePaye WHERE id_emp = {mat_emp};""")
        cursor.execute(f"""DELETE FROM CongeRecupere WHERE id_emp = {mat_emp};""")
        cursor.execute(f"""DELETE FROM CongeEvenement WHERE id_emp = {mat_emp};""")
        cursor.execute(f"""DELETE FROM CongeCSS WHERE mat_emp = {mat_emp};""")
        cursor.execute(f"""DELETE FROM Conge WHERE Mat_Emp = {mat_emp};""")
        cursor.execute(f"""DELETE FROM Absence WHERE mat_emp = {mat_emp};""")
        cursor.execute(f"""DELETE FROM HeureNormales WHERE mat_emp = {mat_emp};""")
        cursor.execute(f"""DELETE FROM HeureSupplémentaires WHERE mat_emp = {mat_emp};""")
        cursor.execute(f"""DELETE FROM Pointage WHERE id_emp = {mat_emp};""")
        cursor.execute(f"""DELETE FROM Employees WHERE Mat_Emp = {mat_emp};""")
        db.close()
        self.msg = supp_employe()
        self.msg.show()
    def Get_Date_Fin(self,nbr):
        from datetime import date,datetime,timedelta
        Begindate = datetime.today()
        Enddate = Begindate + timedelta(years=nbr)
        return Enddate.strftime("%Y-%m-%d")

    def Annuler(self):
        self.lineEdit_10.setText(' ')
        self.lineEdit_11.setText(' ')
        self.lineEdit_12.setText(' ')
        self.lineEdit_13.setText(' ')
        self.lineEdit_17.setText(' ')
        self.lineEdit_16.setText(' ')
        self.lineEdit_14.setText(' ')
        self.lineEdit_15.setText(' ')
        self.lineEdit_18.setText(' ')
        self.lineEdit_19.setText(' ')
        self.lineEdit_20.setText(' ')
        self.lineEdit_21.setText(' ')
        self.lineEdit_22.setText(' ')
        self.lineEdit_23.setText(' ')
        self.lineEdit_24.setText(' ')
        self.lineEdit_25.setText(' ')
        self.lineEdit_26.setText(' ')
        self.lineEdit_27.setText(' ')
        self.lineEdit_28.setText(' ')
        self.lineEdit_30.setText(' ')
        self.lineEdit_31.setText(' ')
        self.lineEdit_29.setText(' ')

    def from_dob_to_age(self,born):
            today = datetime.date.today()
            return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    def AjouterEmploye(self):
        dob = datetime.datetime.strptime(str(self.lineEdit_16.text()), '%Y-%m-%d')
        dob = self.from_dob_to_age(dob)
        print(dob)
        anciennte = datetime.datetime.strptime(str(self.lineEdit_28.text()), '%Y-%m-%d')
        anciennte_days = datetime.datetime.now()-anciennte
        if not self.lineEdit_22.text() != '':
            self.lineEdit_22.setText('NULL')
        db = self.open_connection()
        cursor = db.cursor()
        cursor.execute('SELECT COUNT(*),COUNT(*) FROM Employees')
        mat_emp = cursor.fetchone()
        rr = f"""INSERT INTO Employees(Mat_Emp,Nom,Prenom,LieuDeLicence,NumTelephone,Cin,Age,Adresse,SituationFamiliale,NbrEnfants,NiveauEtude,Formation,Diplome,Fonction,Mat_Responsable,TypeContrat,Service,NumCnss,SalaireNet,Taux_Horaire,DateEntree,DateDeNaissance,Anciennete) VALUES ( 
{mat_emp[0]+1},
'{self.lineEdit_10.text()}',
'{self.lineEdit_11.text()}',
'{self.lineEdit_12.text()}',
'{self.lineEdit_13.text()}',
'{self.lineEdit_17.text()}',
{dob},
'{self.lineEdit_14.text()}',
'{self.comboBox_2.currentText()}',
{self.lineEdit_15.text()},
'{self.lineEdit_18.text()}',
'{self.lineEdit_19.text()}',
'{self.lineEdit_20.text()}',
'{self.lineEdit_21.text()}',
{self.lineEdit_22.text()},
'{self.lineEdit_23.text()}',
'{self.lineEdit_24.text()}',
'{self.lineEdit_25.text()}',
{self.lineEdit_26.text()},
{self.lineEdit_27.text()},
'{self.lineEdit_28.text()}',
'{self.lineEdit_16.text()}',
{anciennte_days.days}
);"""
        print(rr)
        cursor.execute(rr)
        cursor.execute(f"""INSERT INTO CongePaye(id_emp,nbr_jours) VALUES ({mat_emp[0]+1},18);""")
        cursor.execute(f"""INSERT INTO CongeRecupere(id_emp) VALUES ({mat_emp[0]+1});""")
        cursor.execute(f"""INSERT INTO CongeEvenement(id_emp) VALUES ({mat_emp[0]+1});""")
        cursor.execute(f"""INSERT INTO CongeCSS(Id,mat_emp,nbr_jours) VALUES ({mat_emp[0]+1},{mat_emp[0]+1},0.00);""")
        cursor.execute(f"""INSERT INTO Absence(mat_emp,mois,Annee) VALUES ({mat_emp[0]+1},6,2021);""")
        cursor.execute(f"""INSERT INTO HeureNormales(mat_emp,mois,Annee) VALUES ({mat_emp[0]+1},6,2021);""")
        cursor.execute(f"""INSERT INTO HeureSupplémentaires(mat_emp,mois,Annee) VALUES ({mat_emp[0]+1},6,2021);""")
        db.commit()
        db.close()
        names = self.getListNoms()
        completer = QtWidgets.QCompleter(names)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.lineEdit_29.setCompleter(completer)
        self.msg = add_employe()
        self.msg.show()
        self.Annuler()
    def btn_min_clicked(self):
        self.showMinimized()

    def fermer(self):
        self.close()

    def ResherchEmployees(self):
        global SituationFamilial
        print(' nom == ',self.lineEdit_29.text())
        db = self.open_connection()
        cursor = db.cursor()
        rq = f"""SELECT Nom,Prenom,LieuDeLicence,NumTelephone,Cin,Mat_Emp,Adresse,SituationFamiliale,NbrEnfants,NiveauEtude,Formation,Diplome,Fonction,Mat_Responsable,TypeContrat,Service,NumCnss,SalaireNet,Taux_Horaire,DateEntree,DateDeNaissance,Anciennete from Employees WHERE Nom || ' ' || Prenom = '{self.lineEdit_29.text()}';"""
        print(rq)
        cursor.execute(rq)
        add = cursor.fetchone()
        db.close()
        self.lineEdit_10.setText(str(add[0]))
        self.lineEdit_11.setText(str(add[1]))
        self.lineEdit_12.setText(str(add[2]))
        self.lineEdit_13.setText(str(add[3]))
        self.lineEdit_17.setText(str(add[4]))
        self.lineEdit_30.setText(str(add[5]))
        self.lineEdit_14.setText(str(add[6]))
        self.comboBox_2.setCurrentIndex(SituationFamilial[str(add[7])])
        self.lineEdit_15.setText(str(add[8]))
        self.lineEdit_18.setText(str(add[9]))
        self.lineEdit_19.setText(str(add[10]))
        self.lineEdit_20.setText(str(add[11]))
        self.lineEdit_21.setText(str(add[12]))
        self.lineEdit_22.setText(str(add[13]))
        self.lineEdit_23.setText(str(add[14]))
        self.lineEdit_24.setText(str(add[15]))
        self.lineEdit_25.setText(str(add[16]))
        self.lineEdit_26.setText(str(add[17]))
        self.lineEdit_27.setText(str(add[18]))
        self.lineEdit_28.setText(str(add[19]))
        self.lineEdit_16.setText(str(add[20]))
        self.lineEdit_31.setText(f"""{str(add[21])} jours""")




    def Bilan(self):
        info = ['AYOUB',Mois_Fr[str(self.comboBox.currentText())],str(self.lineEdit_2.text())]
        self.bilan_dialog = bilan(info)
        self.bilan_dialog.show()
    #SELECT id_emp,concat(E.Nom,' ',E.Prenom),SUM(NbrHeures),SUM(P.Retard),SUM(P.Absence),SUM(P.HeuresSupp),SUM(P.vintCinq),SUM(P.cinquante),SUM(P.cent) FROM Pointage P INNER JOIN Employees E ON concat(E.Nom,' ',E.Prenom) = 'EL BAHTI AYOUB'  AND E.Mat_Emp = P.id_emp AND (SELECT EXTRACT(MONTH FROM P.Date_Jour)) = 6 AND (SELECT EXTRACT(YEAR FROM P.Date_Jour)) = 2021;

    def getListIds(self):
        db = self.open_connection()
        cursor = db.cursor()
        cursor.execute("SELECT Nom || ' ' || Prenom,Mat_Emp FROM Employees;")
        v = cursor.fetchall()
        db.close()
        list_nom = []
        for a in v:
            list_nom.append(int(a[1]))
        return list_nom

    def getListNoms(self):
        db = self.open_connection()
        cursor = db.cursor()
        cursor.execute("SELECT Nom || ' ' || Prenom,Mat_Emp FROM Employees;")
        v = cursor.fetchall()
        db.close()
        list_nom = []
        for a in v:
            list_nom.append(str(a[0]))
        return list_nom

    def List_Employees(self):
        self.requete_Date = f"""AND P.Date_Jour = '{self.lineEdit_2.text()}' """
        self.miseAjours_tab_pointage()
        #SELECT * from Pointage P INNER JOIN Employees E ON concat(E.Nom,' ',E.Prenom) = 'EL BAHTI Ayoub';
        
        

    def spin_selected(self):
        self.nbrjours = self.spinBox.value()



    def Modfier(self):
        self.rest = self.getRestJours(self.id_emps)
        print('rest = ',self.rest)
        if self.rest >= 0:
            db = self.open_connection()
            cursor = db.cursor()
            cursor.execute(f"""SELECT * FROM Administrateur WHERE Num_Mat = {id_emp_global};""")
            ver = cursor.fetchone()
            db.close()
            print('idemp = ',self.id_responsable)
            nom_emeteur = self.get_nom_prenom(id_emp_global)
            email_responsable = self.get_email_responsable(self.id_responsable)
            print('email de responsable = ',email_responsable)
            print('email de moi = ',ver[4])
            self.mod = msg_modification_mod(self.Id_Conge,self.nbrjours)
            self.mod.Initialiser(str(ver[4]),str(ver[5]),str(email_responsable))
            self.mod.show()
        else:
            print('impossible')
            self.msg = QtWidgets.QMessageBox()
            self.msg.setWindowTitle('Erreur')
            self.msg.setText(f""" Impossible d'ajouter {self.nbrjours} !! """ )
            self.msg.show()
            #ajouter valeur lwla dyal spinbox
            #db = self.open_connection()
            #cursor = db.cursor()
            #cursor.execute(f"""UPDATE CongePaye SET nbr_jours = {self.rest} WHERE id_emp = {id_emp_global};""")
            #db.commit()
            #db.close()




    def OuvrirCompte(self):
        self.tabWidget_2.setCurrentIndex(2)



    def OuvrirTousDemandes(self):
        self.tabWidget_2.setCurrentIndex(1)
    def OuvrirEmployees(self):
        self.tabWidget_2.setCurrentIndex(2)
    def OuvrirLogin(self):
        self.tabWidget_2.setCurrentIndex(3)

    def Ouvrirconge(self):
        self.tabWidget_2.setCurrentIndex(0)



    def Actualiser(self):
        self.check_validation = False
        self.miseAjours_Tab_Conge()



    def Historique(self):
        self.check_validation = True
        self.miseAjours_Tab_Conge()

        print('hiding ... ')

    def Login_Info(self):
        global id_emp_global
        db = self.open_connection()
        cursor = db.cursor()
        cursor.execute(f"""SELECT Nom,Prenom FROM Employees WHERE Mat_Emp = {int(id_emp_global)};""")
        inf = cursor.fetchone()
        print(inf)
        self.label_35.setText(str(id_emp_global))
        self.label_33.setText(inf[0])
        self.label_34.setText(inf[1])
        db.close()

    def getFonction(self):
        db = self.open_connection()
        cursor = db.cursor()
        cursor.execute(f"""SELECT Fonction,Cin FROM Employees WHERE Mat_Emp = {id_emp_global};""")
        result = cursor.fetchone()
        db.close()
        return result[0]


    def get_nom_directeur(self):
        db = self.open_connection()
        cursor = db.cursor()
        cursor.execute("SELECT Nom | ' ' | Prenom ,Mat_Emp FROM Employees WHERE Fonction = 'Admin';")
        adminName = cursor.fetchone()[0]
        db.close()
        return adminName
        
    def Accepter(self):
        self.accept = True
        if self.validation == 'Annulé par Responsable':
            pass
        else :
            self.rest = self.getRestJours(self.id_emps)
            if self.fonction == 'Admin':
                self.tab_4.setEnabled(False)
                db = self.open_connection()
                Cursor = db.cursor()
                print('temp de trvail ',self.tempDeTravail)
                if self.tempDeTravail in ("Normal","22h -> 06h"):
                    Cursor.execute(f'''UPDATE Employees SET nbr_Samedi = {self.nbrsamedi} WHERE Mat_Emp = {self.id_emps};''')

                    # creé unr=e fonction pour retourner la fonction d'administrateur
                if self.typeconge_v == 'CP':
                        Cursor.execute(f"""UPDATE CongePaye SET nbr_jours = {self.rest} WHERE id_emp = {self.id_emps};""")
                        print('congepaye updating')
                elif self.typeconge_v == 'CE':
                         Cursor.execute(f"""UPDATE CongeEvenement SET NbrJours = {self.rest} WHERE id_emp = {self.id_emps};""")
                elif self.typeconge_v == 'CR':
                         Cursor.execute(f"""UPDATE CongeRecupere SET heures_récupération = {self.rest} WHERE id_emp = {self.id_emps};""")
                elif self.typeconge_v == 'CSS':
                    Cursor.execute(f"""UPDATE CongeCSS SET nbr_jours = {self.nbrjours} WHERE mat_emp = {self.id_emps};""")
                Cursor.execute(f"""UPDATE Conge SET Validation = 'V' WHERE Id = {self.Id_Conge};""")
                db.commit()
                db.close()
                    
                self.msg = QtWidgets.QMessageBox()
                self.msg.setWindowTitle('Info')
                self.msg.setText("Pouvez-vous imprimer l'attestation de Congé avant de sauvegarder ?")
                    #self.msg.addButton(self.msg.Ok)
                    #self.msg.addButton(self.msg.No)
                self.msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
                self.msg.buttonClicked.connect(self.nextWindow)
                self.msg.exec_()

                self.text = f""" Demande de{self.lineEdit_5.text()} été accepté """
                
            else :
                db = self.open_connection()
                cursor = db.cursor()
                cursor.execute(f"""SELECT * FROM Administrateur WHERE Num_Mat = {id_emp_global};""")
                ver = cursor.fetchone()
                cursor_1 = db.cursor()
                cursor_1.execute(f"""UPDATE Conge SET Validation = 'H' WHERE Id = {self.Id_Conge};""")
                db.commit()
                db.close()
                nom_emeteur = self.get_nom_prenom(id_emp_global)
                email_admin = self.get_email_admin()
                print('email de admin = ',email_admin)
                print('email de moi = ',ver[4])
                text = f"""{nom_emeteur} a envoyé une demande de congé pour vérifier"""
                self.email = Emails(str(ver[4]),str(ver[5]),str(email_admin),text)
                self.text = f""" Demande de{self.lineEdit_5.text()} été accepté,mais en attente la main de l'administrateur"""
                
            if self.accept:
                self.msg = message_ui(self.text,1)
        self.miseAjours_Tab_Conge()




    def nextWindow(self, button):
        print('h')
        print(button.text())
        if button.text() == 'OK':
            print('imprimer ...')
            #nom complet,matricule,nomresponsable,nom directeur,type congé,date debut,date fin
            list_information = [str(self.lineEdit_5.text()),self.id_emp,str(self.lineEdit_4.text()),str(self.get_nom_directeur()),self.names_conge[str(self.typeconge_v)],str(self.DateDebut),str(self.DateFinCongé)]
            print(len(list_information))
            self.Imprimer_wind = Imprimer_class(list_information)

        elif button.text() == 'Cancel':
            self.msg.close()



    def get_email_admin(self):
        db = self.open_connection()
        cursor = db.cursor()
        cursor.execute(f"""SELECT Employees.Mat_Emp,Administrateur.Email FROM Administrateur INNER JOIN Employees ON Employees.Fonction = 'Admin' AND Employees.Mat_Emp = Administrateur.Num_Mat""")
        result = cursor.fetchone()
        db.close()
        return result[1]
    def get_email_responsable(self,id_emp):
        db = self.open_connection()
        cursor = db.cursor()
        cursor.execute(f"""SELECT * FROM Responsable WHERE Num_Mat = {id_emp};""")
        result = cursor.fetchone()
        db.close()
        return result[4]



    def Refuser(self):
        if self.validation == 'Annulé par Responsable':
            pass
        else :
            db = self.open_connection()
            Cursor = db.cursor()
            Cursor.execute(f"""UPDATE Conge SET Validation = 'R' WHERE Id = {self.Id_Conge};""")
            db.commit()
            db.close()
            self.text = f""" Demande de{self.lineEdit_5.text()} été refusé"""
            self.msg = message_ui(self.text,2)
        self.miseAjours_Tab_Conge()



    def update_tous_1(self,id_emp,id_conge_,nbrSamedi_set,nbrSamedi,check,valeurDeTemps):
        db = self.open_connection()
        cursor = db.cursor()
        print('nbr samedi avant ',nbrSamedi_set)
        if check == True:
            if valeurDeTemps == 0:
                nbrSamedi_set = 0
        else :
            print('hhhh mchiti fiha')
            nbrSamedi_set = nbrSamedi_set - nbrSamedi
        print('nbr samedi = ',nbrSamedi)
        print('check = ',check)
        print('id_emp = ',id_emp)
        print('id ocge = ',id_conge_)
        print('nbr samedi apres ',nbrSamedi_set)
        print('valeur',valeurDeTemps)
        cursor.execute(f"""UPDATE Employees SET nbr_Samedi = {nbrSamedi_set} WHERE Mat_Emp = {id_emp};""")
        #cursor.execute(f'''UPDATE Conge SET nbr_Samedi_Consommer = {nbrSamedi} WHERE Id = {id_conge_};''')
        #cursor.execute(f'''UPDATE Conge SET nbr_Samedi = {nbrSamedi_set} WHERE Id = {id_conge_};''')
        db.commit()
        db.close()



    def get_nom_prenom(self,idemp):
        db = self.open_connection()
        cursor = db.cursor()
        ids = idemp
        cursor.execute(f""" SELECT Nom,Prenom FROM Employees WHERE Mat_Emp = {ids};""")
        idd = cursor.fetchone()
        db.close()
        return f'''{idd[0]}  {idd[1]}'''


    def doubleclicked_2(self):
        print('heelo')
        row = self.tableWidget_2.currentRow()
        print(row)
        if row > -1:
            info = [self.num_matricule_Pointage[row]]
            for i in range(14):
                info.append(self.tableWidget_2.item(row, i).text())
            print(info)
            #SEND ARGUMENTS
            self.InterfaceDePointage = PointageClasse(info)
            self.InterfaceDePointage.show()
    
    def open_connection(self):
        return sqlite3.connect("C:/Users/EL BAHTI/Desktop/Conge/Connection/appp.db")

    def doubleclicked(self):
        self.Show_grpBoux()
        print('heelo')
        row = self.tableWidget.currentRow()
        print(row)
        if row > -1:
            self.DateDebut = self.tableWidget.item(row, 3).text()
            self.DateFinCongé = self.tableWidget.item(row, 4).text()
            self.validation = self.tableWidget.item(row,2).text()
            self.tempDeTravail = self.tableWidget.item(row,5).text()
            self.typeconge_v = self.typeconge[row]
            self.id_responsable = self.num_matricule_R[row]
            print(self.typeconge_v)
            print('mat = ',self.num_matricule[row])
            print('validation = ',self.validation)
            self.pushButton_5.setEnabled(True)
            self.pushButton_6.setEnabled(True)
            self.pushButton_15.setEnabled(True)
            if self.validation == 'Accepté':
                self.pushButton_5.setEnabled(False)
                self.pushButton_6.setEnabled(False)
                self.pushButton_15.setEnabled(False)
            if self.validation == 'Annulé par Responsable':
                print('vous selectionner annuler')
                self.pushButton_5.setChecked(True)
                self.pushButton_6.setCheckable(False)
            print(self.DateDebut)
            datedebut = str(self.DateDebut)
            self.id_emp = self.num_matricule[row]
            self.heuresRecup = self.getJoursRecuperer(self.id_emp)
            db = self.open_connection()
            cursor = db.cursor()
            # il faut ajouter nbr de jour demandé
            cursor.execute(f"""SELECT Employees.Nom,Employees.Prenom,R.Nom,R.Prenom,Employees.nbr_Samedi FROM Employees INNER JOIN Employees R ON Employees.Mat_Emp = {self.num_matricule[row]} AND R.Mat_Emp = {self.num_matricule_R[row]}""")
            Info_box = cursor.fetchone()
            self.lineEdit_5.setText('    ' + Info_box[0] +' '+ Info_box[1])
            self.lineEdit_4.setText('    ' + Info_box[2] + ' '+Info_box[3])
            self.lineEdit_3.setText('    ' + str(Info_box[4]))
            cursor.execute(f"""SELECT COUNT(*),Id,nbr_Samedi FROM Conge WHERE Mat_Emp = {self.num_matricule[row]};""")
            nbrDemandes = cursor.fetchone()
            self.lineEdit_6.setText('          ' + str(nbrDemandes[0]))
            self.nbrsamedi = nbrDemandes[2]
            self.lineEdit_9.setText('          ' + str(self.heuresRecup))
            
            cursor.execute(f"""SELECT Id,Mat_Emp,NbrJours FROM Conge WHERE Mat_Emp = {self.num_matricule[row]} AND DateDebut = '{self.DateDebut}'""")
            Id_Cg = cursor.fetchone()
            self.Id_Conge = Id_Cg[0]
            self.nbrjours = int(Id_Cg[2])
            self.spinBox.setValue(self.nbrjours)
            db.close()
            self.id_emps = self.num_matricule[row]
            
    def getJoursRecuperer(self,id_emp):
        db = self.open_connection()
        cursor = db.cursor()
        cursor.execute(f"""SELECT * FROM CongeRecupere WHERE id_emp = {id_emp};""")
        result = cursor.fetchone()
        db.close()
        return result[2]
            
    def getRestJours(self,id_emp):
        db = self.open_connection()
        cursor = db.cursor()
        if self.typeconge_v == 'CP':
            cursor.execute(f"""SELECT nbr_jours,Id FROM CongePaye WHERE id_emp = {id_emp};""")
        elif self.typeconge_v == 'CE':
            cursor.execute(f"""SELECT NbrJours,Id FROM CongeEvenement WHERE id_emp = {id_emp};""")
        elif self.typeconge_v == 'CSS':
            cursor.execute(f"""SELECT nbr_jours,Id FROM CongeCSS WHERE mat_emp = {id_emp};""")
        elif self.typeconge_v == 'CR':
            cursor.execute(f"""SELECT heures_récupération,Id FROM CongeRecupere WHERE id_emp = {id_emp};""")

        result = cursor.fetchone()
        db.close()
        return result[0] - self.nbrjours   



    def setColortoRow(self, table, row, color):
        print('colonne count',table.columnCount())
        for j in range(table.columnCount()):
            table.item(row, j).setBackground(color)



    def Supprimer_Demande(self):
        print('supp ...')
        row = self.tableWidget.currentRow()
        print(row)
        if row > -1:
            self.DateDebut = self.tableWidget.item(row, 3).text()
            print('date debut',self.DateDebut)
            print('num matricule : ',self.num_matricule[row])
            db = self.open_connection()
            cursor = db.cursor()
            cursor.execute(f"""SELECT Id,Mat_Emp FROM Conge WHERE Mat_Emp = {self.num_matricule[row]} AND DateDebut = '{self.DateDebut}';""")
            idcg = cursor.fetchone()
            cursor.execute(f"""DELETE FROM Message WHERE Id_Conge = {idcg[0]};""")
            cursor.execute(f"""DELETE FROM Conge WHERE Mat_Emp = {self.num_matricule[row]} AND DateDebut = '{self.DateDebut}';""")
            db.commit()
            db.close()
        self.miseAjours_Tab_Conge()



    def Hinding_grpBoux(self):
        self.groupBox_3.hide()



    def Show_grpBoux(self):
        self.groupBox_3.show()

    def List_Nom_Ids(self):
        db = sqlite3.connect("C:/Users/EL BAHTI/Desktop/Conge/Connection/appp.db")
        cursor = db.cursor()
        cursor.execute(f"""SELECT E.Nom || ' ' || E.Prenom,P.id_emp,P.Date_Jour,P.Heure_Entrer,P.Heure_mise_en_consideration,P.Heure_Sortir,P.NbrHeures,P.HeuresSupp,P.vintCinq,P.cinquante,P.cent,P.heures_récupération,P.Absence,P.Retard FROM Pointage P INNER JOIN Employees E ON E.Mat_Emp = P.id_emp;""")
        result = cursor.fetchall()
        print(len(result))
        Nom_Prenom = {}
        for v in result:
            Nom_Prenom[v[0]] = v[1]
        print(Nom_Prenom)
        db.close()
        return Nom_Prenom

    def miseAjours_tab_pointage(self):
        Nom_Prenom = self.List_Nom_Ids()
        self.tableWidget_2.setRowCount(0)
        if self.test:
            self.requete = 'E.Mat_Emp = P.id_emp'
        print(self.requete)
        print(f"""SELECT Nom || ' ' || Prenom,P.Temps_de_travail,P.Date_Jour,P.Heure_Entrer,P.Heure_mise_en_consideration,P.Heure_Sortir,P.NbrHeures,P.HeuresSupp,P.vintCinq,P.cinquante,P.cent,P.heures_récupération,P.Absence,P.Retard FROM Pointage P INNER JOIN Employees E ON {self.requete}  {self.requete_Date};""")
        db = self.open_connection()
        self.connection = db.cursor()
        self.connection.execute(f"""SELECT Nom || ' ' || Prenom,P.Temps_de_travail,P.Date_Jour,P.Heure_Entrer,P.Heure_mise_en_consideration,P.Heure_Sortir,P.NbrHeures,P.HeuresSupp,P.vintCinq,P.cinquante,P.cent,P.heures_récupération,P.Absence,P.Retard,P.Modification FROM Pointage P INNER JOIN Employees E ON {self.requete} {self.requete_Date};""")
        self.result = self.connection.fetchall()
        print('result = ',self.result)
        self.num_matricule_Pointage = {}
        self.num_matricule_R_1 = {}
        for lignes,row_data in enumerate(self.result):
            self.tableWidget_2.insertRow(lignes)
            self.nom_prenom = ''
            nomComplet = ''
            for colonne,self.resultat_colonne in enumerate(row_data):    
                str_colonne = str(self.resultat_colonne)
                if colonne == 0:
                    self.num_matricule_Pointage[lignes] = Nom_Prenom[self.resultat_colonne]
                if colonne in (1,3,4,5):
                    if str_colonne == 'None':
                        str_colonne = '--'
                if colonne == 12:
                    print('absent = ',str_colonne)
                    if str_colonne == '0':
                        str_colonne = 'Non'
                    else:
                        str_colonne = 'Oui'
                if colonne == 14:
                    if str_colonne == '1':
                        self.setColortoRow(self.tableWidget_2,lignes,QtGui.QColor(164, 237, 139))
                item1 = QtWidgets.QTableWidgetItem(str_colonne)
                item1.setFlags(item1.flags() ^ Qt.ItemIsEditable)
                self.tableWidget_2.setItem(lignes, colonne,item1)
        print('colonne count table 2',self.tableWidget_2.columnCount())
        db.close()
        print(self.num_matricule)
        self.label.hide()



    def miseAjours_Tab_Conge(self):
        self.tableWidget.setRowCount(0)
        db = self.open_connection()
        self.connection = db.cursor()
        self.SetValidaton_S = " AND Conge.Validation != 'S' "
        if self.check_validation == True:
            self.SetValidaton_S = " "
        print(self.SetValidaton_S)
        self.connection.execute(f"""SELECT e.Mat_Emp,m.Mat_Emp,Conge.Validation,Conge.DateDebut,Conge.DateFin,Conge.tempDeTravail,secondTemp,Conge.nbr_Samedi_Consommer,Conge.Type_de_Conge FROM  Employees e INNER JOIN Employees m ON e.Mat_Responsable = m.Mat_Emp INNER JOIN Conge ON Conge.Mat_Emp = e.Mat_Emp{self.SetValidaton_S}ORDER BY Conge.Type_de_Conge ;""")
        self.result = self.connection.fetchall()
        print('result = ',self.result)
        dict_color = {'CE':QtGui.QColor(0, 255, 0),'CP':QtGui.QColor(255, 140, 0),'CR':QtGui.QColor(219, 112, 147),'CSS':QtGui.QColor(30, 144, 255)}
        self.names_conge = {'CE':"Congé Evénement",'CP':"Congé payé",'CR':"Congé recupérer",'CSS':"Congé sans solde"}
        self.num_matricule = {}
        self.typeconge = {}
        self.num_matricule_R = {}
        for lignes,row_data in enumerate(self.result):
            self.tableWidget.insertRow(lignes)
            self.nom_prenom = ''
            for colonne,self.resultat_colonne in enumerate(row_data):              
                str_colonne = str(self.resultat_colonne)
                if colonne in (0,1):
                    str_colonne = 'Mat ' + str(self.resultat_colonne)
                    if colonne == 0:
                        self.num_matricule[lignes] = self.resultat_colonne
                    if colonne == 1:
                        self.num_matricule_R[lignes] = self.resultat_colonne
                if colonne == 2:
                    str_colonne = Etats_Conge[str_colonne]
                if colonne == 8:
                    print(str_colonne)
                    self.var = dict_color[str_colonne]
                    self.typeconge[lignes] = self.resultat_colonne
                    str_colonne = self.names_conge[str_colonne]
                
                    #self.searchBtn=QtWidgets.QPushButton('Supprimer')
                    #self.searchBtn.setDown(True)
                    #self.searchBtn.setStyleSheet("""QPushButton{
                     #   Vertical Size : 30px;
                      #  margin:3px;
                    #qproperty-icon:url(dd.png);
                    #qproperty-iconSize: 20px 20px;}
                     # .QPushButton:hover {
	        
	        #background-color:#DCFF9B ;
            #}
             #     """)

                #    self.tableWidget.setCellWidget(lignes,colonne,self.searchBtn)
                #    self.searchBtn.clicked.connect(self.Supprimer_Demande)

                item1 = QtWidgets.QTableWidgetItem(str_colonne)
                item1.setFlags(item1.flags() ^ Qt.ItemIsEditable)
                self.tableWidget.setItem(lignes, colonne,item1)
            print(self.var)
            print('colonne count',self.tableWidget.columnCount())
        db.close()
        print(self.num_matricule)



if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = Login()
    ui.show()
    sys.exit(app.exec_())