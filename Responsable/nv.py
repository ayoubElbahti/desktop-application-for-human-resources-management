from PyQt5 import QtCore, QtGui, QtWidgets
from db_connect import mydb as db,dbb
from datetime import datetime
from PyQt5.uic import loadUi
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt,QTimer
from Calendrier import *
from demandeEnvoyer import Ui_self_1
import Resources_rc
from sentEmails import Emails
from cal import cal_1
from reloading_screen import Relaoding
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
        self.Valider.clicked.connect(self.hid_rel)
        self.pushButton.clicked.connect(self.get_calendrier)

    def get_calendrier(self):
        global close_calendrier
        self.ui_calendrier = cal_1(self.lineEdit)
        close_calendrier = True
        self.ui_calendrier.show()
    def hid_rel(self):
        self.rr = Relaoding()
        #_self.setEnabled(False)
        timer = QTimer(self)
        timer.singleShot(5000,self.hhh)

    def check_champs(self,radio_v):
        if self.Num_Mat.text() != '' and len(radio_v) != 0:
            return True
        else :
            return False
    def hhh(self):
        self.rr.loading_movie.start() 
        self.Valider_fct()
    def Valider_fct(self):
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
                if self.class_calendrier.get_id_responsable(self.num_matricule) == self.id_global:
                    db._open_connection()
                    cursor = db.cursor(buffered=True)
                    cursor.execute(f"""INSERT INTO Conge (Mat_Emp,Type_de_Conge,DateDebut,DateFin,NbrJours,tempDeTravail,secondTemp) VALUES ({self.num_matricule},'{self.radio_value[0]}','{self.lineEdit.text()}','{self.Date_Fin}',{self.nbr_jours},'{self.temp_travail}','{self.comboBox_2.currentText()}')""")
                    # Analyser les statistiques de samedi pour la demande 
                    db.commit()
                    db.close()
                    id_conge = self.class_calendrier.get_id_conge(self.num_matricule,self.lineEdit.text())
                    self.class_conge = Conge(id_conge,self.nbr_jours,self.nbr_Samedi,check_nbr_samedi[self.temp_travail],check_nbr_samedi[self.comboBox_2.currentText()])
                    self.class_conge.GetNbrDimanche = self.nbr_dimanche
                    self.class_conge.nbrsamedi = self.getnbrSamedi
                    self.class_conge.nbrVendredi = self.nbr_Samedi
                    #si il chosis CP
                    print('radio value = ',self.radio_value )
                
        except:
            self.rr.stop_fct()
            print('hhhh')
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Form(6)
    ui.show()
    sys.exit(app.exec_())
