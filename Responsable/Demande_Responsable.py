from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from datetime import datetime
from PyQt5.uic import loadUi
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt,QTimer
from Calendrier import *
from demandeEnvoyer import Ui_self_1
import Resources_rc
from sentEmails import Emails
from reloading_screen import waiting
from cal import cal_1
close_calendrier = False
i = 0
grp_value_dict = {'normale':1,'équipe':2}
check_nbr_samedi = {'Normal':True,'22h -> 06h':True,'06h -> 14h': False,'14h -> 22h':False,'Aucun':None}
check_nbr_samedi_1 = {'-':0,'22h -> 06h':1,'06h -> 14h': 2,'14h -> 22h':3}
class Ui_Form(QtWidgets.QMainWindow):
    def __init__(self,id_g):
        super().__init__()
        self.setStyleSheet("background-color:#E2E2F4;")
        loadUi("Conge_Client.ui",self)
        self.CSS.setToolTip("Congé sans soldé")
        self.CE.setToolTip("Congé spécial")
        self.CP.setToolTip("Congé payé")
        self.CR.setToolTip("Congé Recupérer")
        self.class_calendrier = Calendrier_class()
        self.id_global = id_g
        self.lineEdit.setStyleSheet("QLineEdit"" {"
	        "box-shadow:inset 0px 1px 0px 0px #276873;"
	        "background:linear-gradient(to bottom, #C4F21A 5%, #DCFF9B  100%);"
	        "background-color:#5387EE;"
	        "border:1px solid #DCFF9B ;"
	        "display:inline-block;"
	        "cursor:pointer;"
	        "color:#000000;"
	        "font-family:Arial;"
	        "font-size:15px;"
	        "padding:6px 12px;"
	        "text-decoration:none;"
            "}"
            ".QLineEdit:hover {"
	        "background:linear-gradient(to bottom, #DCFF9B 5%, #DCFF9B  100%);"
	        "background-color:#DCFF9B;"
            "}"
            ".QLineEdit:active {"
	        "position:relative;"
	        "top:1px;"
            "}"
        )
        self.Jours.setStyleSheet("QLineEdit"" {"
	        "box-shadow:inset 0px 1px 0px 0px #276873;"
	        "background:linear-gradient(to bottom, #C4F21A 5%, #DCFF9B  100%);"
	        "background-color:#5387EE;"
	        "border:1px solid #DCFF9B ;"
	        "display:inline-block;"
	        "cursor:pointer;"
	        "color:#000000;"
	        "font-family:Arial;"
	        "font-size:15px;"
	        
	        "padding:6px 12px;"
	        "text-decoration:none;"
            "}"
            ".QLineEdit:hover {"
	        "background:linear-gradient(to bottom, #DCFF9B 5%, #DCFF9B  100%);"
	        "background-color:#DCFF9B;"
            "}"
            ".QLineEdit:active {"
	        "position:relative;"
	        "top:1px;"
            "}"
        )
        self.Num_Mat.setStyleSheet("QLineEdit"" {"
	        "box-shadow:inset 0px 1px 0px 0px #276873;"
	        "background:linear-gradient(to bottom, #C4F21A 5%, #DCFF9B  100%);"
	        "background-color:#5387EE;"
	        "border:1px solid #DCFF9B ;"
	        "display:inline-block;"
	        "cursor:pointer;"
	        "color:#000000;"
	        "font-family:Arial;"
	        "font-size:15px;"
	        
	        "padding:6px 12px;"
	        "text-decoration:none;"
            "}"
            ".QLineEdit:hover {"
	        "background:linear-gradient(to bottom, #DCFF9B 5%, #DCFF9B  100%);"
	        "background-color:#DCFF9B;"
            "}"
            ".QLineEdit:active {"
	        "position:relative;"
	        "top:1px;"
            "}"
        )
        #self.radioButton.setChecked(True)
        self.Valider.clicked.connect(self.Valider_fct)
        self.pushButton.clicked.connect(self.get_calendrier)
        


     
    def check_champs(self,radio_v):
        if self.Num_Mat.text() != '' and len(radio_v) != 0:
            return True
        else :
            return False
    def Valider_fct(self):
        global close_calendrier
        self.setEnabled(False)
        if close_calendrier == True:
            self.ui_calendrier.close()
        try :
            self.radio_value = [btn.text() for btn in self.Typedeconge.findChildren(QtWidgets.QRadioButton) if btn.isChecked()]
            print('valeur de radio ',len(self.radio_value))
            if self.check_champs(self.radio_value) and self.comboBox.currentText() != 'Aucun': 
                
                #               exeption matricule

                self.nbr_jours = float(self.Jours.text())
                print(self.nbr_jours)
#calculer nombre de  dimanches
        
                self.num_matricule = int(self.Num_Mat.text())
                self.lineEdit.setText(self.ui_calendrier.printDateInfo())
                self.Date_Fin = self.class_calendrier.Get_Date_Fin(str(self.lineEdit.text()),self.nbr_jours)
                Date_Debut =  self.class_calendrier.Get_Date_Fin(str(self.lineEdit.text()),0)
                dateDebut_format_date = datetime.strptime(Date_Debut,"%Y-%m-%d")
                datefinsansdimanche = datetime.strptime(self.Date_Fin,"%Y-%m-%d")
                self.nbr_Samedi = self.class_calendrier.get_nbr_samedi(dateDebut_format_date,datefinsansdimanche)
                self.nbr_Vendredi = self.class_calendrier.get_nbr_vendredi(dateDebut_format_date,datefinsansdimanche)
                self.getnbrSamedi = self.nbr_Samedi
                self.nbr_Samedi = self.nbr_Vendredi
                self.temp_travail = self.comboBox.currentText()
                print(self.temp_travail,'         ')
                self.nbr_dimanche = self.class_calendrier.GetNbrDimanche(dateDebut_format_date,datefinsansdimanche)
                self.Date_Fin = self.class_calendrier.Get_Date_Fin(str(self.lineEdit.text()),self.nbr_jours+self.nbr_dimanche)
                print('nbr de dimanches : ',self.nbr_dimanche)
                print('nbr de samedi : ',self.class_calendrier.get_nbr_samedi(dateDebut_format_date,datefinsansdimanche))
                
                print('date fin = ',self.Date_Fin)
                #→ ajouter nombre des samedi
    
                
                if self.class_calendrier.get_id_responsable(self.num_matricule) == self.id_global:
                    db = self.open_connection()
                    cursor = db.cursor()
                    cursor.execute(f"""INSERT INTO Conge (Mat_Emp,Type_de_Conge,DateDebut,DateFin,NbrJours,tempDeTravail,secondTemp) VALUES ({self.num_matricule},'{self.radio_value[0]}','{self.lineEdit.text()}','{self.Date_Fin}',{self.nbr_jours},'{self.temp_travail}','{self.comboBox_2.currentText()}')""")
                    # Analyser les statistiques de samedi pour la demande 
                    db.commit()
                    db.close()
                    id_conge = self.class_calendrier.get_id_conge(self.num_matricule,self.lineEdit.text())
                    self.class_conge = Conge(id_conge,self.nbr_jours,self.nbr_Samedi,check_nbr_samedi[self.temp_travail],check_nbr_samedi[self.comboBox_2.currentText()],self.temp_travail)
                    self.class_conge.GetNbrDimanche = self.nbr_dimanche
                    self.class_conge.nbrsamedi = self.getnbrSamedi
                    self.class_conge.nbrVendredi = self.nbr_Samedi
                    #si il chosis CP
                    print('radio value = ',self.radio_value )
                    if self.radio_value[0] == 'CP':
                        self.class_conge.CongePaye()
                        print('je selectionner cp ')
                    elif self.radio_value[0] == 'CE':
                        self.class_conge.CongeEvenement()
                    elif self.radio_value[0] == 'CSS':
                        self.class_conge.makeTrue()
                    elif self.radio_value[0] == 'CR':
                        self.class_conge.CongeRecuperer()
                    if self.class_conge.traiter == False:
                        self.setEnabled(True)
                        
                        msg = QtWidgets.QMessageBox.warning(self,"Impossible ! ","Cette demande n'a pas pu être envoyée ! . Vous avez dépassé le nombre de jours disponibles pour ce type de congé",QtWidgets.QMessageBox.Ok)
                        
                    else :
                        db = self.open_connection()
                        cursor = db.cursor()
                        cursor.execute(f"""SELECT * FROM Responsable WHERE Num_Mat = {self.id_global};""")
                        ver = cursor.fetchone()
                        cursor.execute(f'''SELECT DateFin,DateDebut FROM Conge WHERE Id = {id_conge};''')
                        Df = cursor.fetchone()
                        self.verifier_jour_conger = False
                        print('jour fin  ',self.get_Jours(str(Df[0])))
                        if self.get_Jours(str(Df[0])) == 'Friday':
                            if self.class_conge.verfier == True:
                                print('donc arret a vendredi ..')
                                self.add = 0
                            else:
                                self.add = 2
                                dateFinAvecDimanche = self.class_calendrier.Get_Date_Fin(str(Df[0]),3)
                                cursor.execute(f'''UPDATE Conge set DateFin = '{str(dateFinAvecDimanche)}' WHERE Id = {id_conge};''')
                                db.commit()
                            self.verifier_jour_conger = True
                        if self.get_Jours(str(Df[0])) == 'Saturday':
                            self.add = 1
                            print('date fin est samedi ..')
                            dateFinAvecDimanche = self.class_calendrier.Get_Date_Fin(str(Df[0]),2)
                            cursor.execute(f'''UPDATE Conge set DateFin = '{str(dateFinAvecDimanche)}' WHERE Id = {id_conge};''')
                            db.commit()
                            self.verifier_jour_conger = True
                        if self.get_Jours(str(Df[0])) == 'Sunday':
                            print('date fin est dimanche ..')
                            
                            dateFinAvecDimanche = self.class_calendrier.Get_Date_Fin(str(Df[0]),2)
                            cursor.execute(f'''UPDATE Conge set DateFin = '{str(dateFinAvecDimanche)}' WHERE Id = {id_conge};''')
                            db.commit()

                        db.close()
                        if self.verifier_jour_conger :
                            print('updating nbrjour ..')
                            db = self.open_connection()
                            cursor = db.cursor()
                            cursor.execute(f""" UPDATE Conge SET NbrJours = {self.nbr_jours + self.add} WHERE Id = {id_conge};""")
                            db.commit()
                            db.close()

                        nom_emeteur = self.class_calendrier.get_nom_prenom(self.id_global)
                        email_admin = self.get_email_admin()
                        self.email = Emails(str(ver[4]),str(ver[5]),str(email_admin),nom_emeteur) 
                        icon = QIcon(":/Icons/Icons/277-2778613_success-icon-png-transparent-png-removebg-preview.png")
                        self.setEnabled(True)
                        msg = QtWidgets.QMessageBox()
                        msg.setWindowTitle("Envoyer")
                        msg.setIconPixmap(icon.pixmap(60, 60))
                        msg.setText("Demande envoyé à l'administrateur pour la traiter")
                        msg.exec_()
                        
                    self.Initialiser()
                    del self.class_conge
                    
                else :
                    
                    self.setEnabled(True)
                    msg = QtWidgets.QMessageBox.warning(self,'Permission refusée! ',"Vous n'avez pas le droit de soumettre cette demande. L'employé appartient à une autre service",QtWidgets.QMessageBox.Ok)


            else :
                self.setEnabled(True)
                
                msg = QtWidgets.QMessageBox.warning(self,'Erreur ! ','Vous avez oublié des champs Vides ou les insertions ne sont pas compatibles!',QtWidgets.QMessageBox.Ok)

        except IndexError:
            self.setEnabled(True)
            
            msg = QtWidgets.QMessageBox.warning(self,'Erreur ! ','Vous avez oublié des champs Vides !',QtWidgets.QMessageBox.Ok)

    def getDernierGrp(self):
        if check_nbr_samedi[self.comboBox.currentText()] in (True,False):
            if check_nbr_samedi[self.comboBox_2.currentText()] in (True,False):
                return True
            else:
                return False
    def open_connection(self):
        return sqlite3.connect("appp.db")
    def get_Jours(self,date):
        day_dimanche = datetime.strptime(str(date),"%Y-%m-%d")
        return day_dimanche.strftime("%A")
    def get_email_admin(self):
        db = self.open_connection()
        cursor = db.cursor()
        cursor.execute(f"""SELECT Employees.Mat_Emp,Administrateur.Email FROM Administrateur INNER JOIN Employees ON Employees.Fonction = 'DH' AND Employees.Mat_Emp = Administrateur.Num_Mat""")
        result = cursor.fetchone()
        db.close()
        return result[1]


    def get_calendrier(self):
        global close_calendrier
        self.ui_calendrier = cal_1(self.lineEdit)
        close_calendrier = True
        self.ui_calendrier.show()


    
    def cleanLayout(self):
        for i in reversed(range(self.horizontalLayout.count())):
            try:
                self.horizontalLayout.itemAt(i).widget().setParent(None)
            
            except AttributeError as err:
                pass
        print(self.horizontalLayout.count())
    def setup(self):
        self.CSS = QtWidgets.QRadioButton("CSS")
        self.horizontalLayout.addWidget(self.CSS)
        self.CE = QtWidgets.QRadioButton("CE")
        self.horizontalLayout.addWidget(self.CE)
        self.CP = QtWidgets.QRadioButton("CP")
        self.horizontalLayout.addWidget(self.CP)
        self.CR = QtWidgets.QRadioButton("CR")
        self.horizontalLayout.addWidget(self.CR)
        self.CSS.setToolTip("Congé sans soldé")
        self.CE.setToolTip("Congé spécial")
        self.CP.setToolTip("Congé payé")
        self.CR.setToolTip("Congé Recupérer")


    def Initialiser(self):
        global close_calendrier
        close_calendrier = False
        self.Num_Mat.setText('')
        self.lineEdit.setText('')
        self.Jours.setText('')
        self.comboBox.setCurrentIndex(0)
        self.cleanLayout()   
        self.setup()
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Form(6)
    ui.show()
    sys.exit(app.exec_())
