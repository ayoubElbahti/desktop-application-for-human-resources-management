from os import truncate
from sqlite3.dbapi2 import Cursor, Date
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import Qt
from db_connect import db as dbs
from Sauvegarder import save_pointage
from Missions import MissionsClasse
from Erreur import erreur_pointage
from datetime import timedelta
import sqlite3
check_Image = True
check_retard = False
import Resources_rc
import datetime
IndexShifts = {'Mi-Temps':0,'--':0,'Normal':1,'Shift1':2,'Shift2':3,'Shift3':4}
Mois_Fr = {1:'Janvier',2:'Février',3:'Mars',4:'Avril',5:'Mai',6:'Juin',7:'Juillet',8:'Août',9:'Septembre',10:'Octobre',11:'Novembre',12:'Décembre'}
HeureEntrer = {'Aucun':{0:' ',1:' '},'Mi-Temps':{0:'08',1:'00'},'Normal':{0:'08',1:'00'},'Shift1':{0:'14',1:'00'},'Shift2':{0:'06',1:'00'},'Shift3':{0:'22',1:'00'}}
HeureSortir = {'Aucun':{0:' ',1:' '},'Mi-Temps':{0:'11',1:'00'},'Normal':{0:'18',1:'00'},'Shift1':{0:'22',1:'00'},'Shift2':{0:'14',1:'00'},'Shift3':{0:'06',1:'00'}}
class PointageClasse(QtWidgets.QDialog):
    def __init__(self,listInfo):
        global IndexShifts
        super().__init__()
        loadUi("pointage.ui",self)
        self.setWindowTitle('Pointage')
        self.setWindowIcon(QtGui.QIcon('pointer.png'))
        self.liste = listInfo
        self.lineEdit.setText(self.liste[3])
        self.lineEdit_13.setText(str(self.liste[1]))
        self.comboBox.setCurrentIndex(IndexShifts[self.liste[2]])
        self.ChangerTime = False
        if IndexShifts[self.liste[2]] == 0:
            self.changeTimer()
        if self.liste[4] == '--':
            self.liste[4] = '00:00'
            self.liste[6] = '00:00'
        self.comboBox.currentIndexChanged.connect(self.changeTimer)
        self.hours,self.minutes = self.getHoursMinutes(self.liste[4])
        self.lineEdit_2.setText(self.hours)
        self.lineEdit_3.setText(self.minutes)
        self.hours,self.minutes = self.getHoursMinutes(self.liste[6])
        self.lineEdit_4.setText(self.minutes)
        self.lineEdit_5.setText(self.hours)
        self.ChangeCheckboxtomporary()
        self.changeHeuresTomporary()
        self.checkAbsenceTomporary()
        self.pushButton.clicked.connect(self.AjouterFct)
        self.checkBox.clicked.connect(self.Ouvrable)
        self.checkBox_2.clicked.connect(self.NuitJourOuvrable)
        self.checkBox_3.clicked.connect(self.NuitJourRepos)
        self.pushButton_5.clicked.connect(self.sommesSupp)
        self.pushButton_4.clicked.connect(self.ActualiserHeureNormal)
        self.checkBox_4.clicked.connect(self.Absence)
        self.checkBox_6.clicked.connect(self.NouvelleMission)

    def AjouterFct(self):
        #traiter aucun erreur
        try:
            if self.ChangerTime == True:
                print('comboBox timer change')
                self.ChangerTime = False
            else:
                print('comboBox timer not change')
                self.HeureEntrer = f"""{(HeureEntrer[self.comboBox.currentText()][0])}:{(HeureEntrer[self.comboBox.currentText()][1])}"""
                self.HeureSortir = f"""{(HeureSortir[self.comboBox.currentText()][0])}:{(HeureSortir[self.comboBox.currentText()][1])}"""
                self.mise_consideration = True
            print('etape 1 ')
            self.TempsTravail = self.comboBox.currentText()
            MyListe = self.liste
            MyListe[2] = self.TempsTravail
            #mi-temps
            if self.checkBox_4.isChecked():
                self.retard = 0
                #absence
                self.lineEdit_9.setReadOnly(False)
                self.groupBox.setEnabled(False)
                if self.lineEdit_9.text() == '':
                    self.lineEdit_9.setText('0')
                for i in range(5,15):
                    if i == 6:
                        pass
                    else:
                        MyListe[i] = 0
                MyListe[13] = 1
                MyListe[4] = '--'
                MyListe[6] = '--'
                print('Employee est absent le ',MyListe[3],' and liste est = ',MyListe)
                test = self.TraitementTableAbsence(MyListe)
                if test:
                    db = sqlite3.connect("C:/Users/EL BAHTI/Desktop/Conge/Connection/appp.db")
                    print('employé déja absent ,modifier les heures ...')
                    db.cursor().execute(f"""UPDATE AbsenceJ SET Heures = {float(str(self.lineEdit_9.text()))} WHERE mat_emp = {MyListe[0]} AND Date_absence = '{MyListe[3]}';""")
                    db.commit()
                    db.close()
                else:
                    db = sqlite3.connect("C:/Users/EL BAHTI/Desktop/Conge/Connection/appp.db")
                    print('aucun')
                    print('employé est devient absent ')
                    print(f""" ({MyListe[0]},'{MyListe[3]}');""")
                    requete = f"""INSERT INTO AbsenceJ(mat_emp,Date_absence,Heures) VALUES ({MyListe[0]},'{MyListe[3]}',{float(str(self.lineEdit_9.text()))});"""
                    print(requete)
                    db.cursor().execute(requete)
                    db.commit()
                    db.close()
                print('myliste = ',MyListe)
                self.UpdatePointage(MyListe)

            else:
                print('etape 2 ')
                self.ActualiserHeureNormal()
                print('etape 3 ')
                self.Retard()
                print('etape 4 ')
                print('rrrrrrrrrrrrrrrr')
                if self.lineEdit_11.text() == '':
                    self.lineEdit_11.setText('0.0')
                if self.lineEdit_12.text() == '':
                    self.lineEdit_12.setText('0.0')
                print(MyListe)
                test = self.TraitementTableAbsence(MyListe)
                if test == True:
                    print('syad deja absent')
                    self.DropTableAbsence()
                    print('drop succes')

                db = self.open_connection()
                Cursor = db.cursor()
                Cursor.execute(f"""SELECT * FROM RecupererHeures WHERE mat_emp = {MyListe[0]}""")
                result = Cursor.fetchone()
                Cursor.execute(f"""SELECT * FROM CongeRecupere WHERE id_emp = {MyListe[0]}""")
                result_1 = Cursor.fetchone()
                Cursor.execute(f"""UPDATE RecupererHeures SET Heure = {float(str(self.lineEdit_12.text()))} WHERE mat_emp = {MyListe[0]}""")
                total = result_1[2] - result[2]
                print('total1 = ',total)
                print('result1 = ',result[2],' et result2 = ',result_1[2])
                total = float(str(self.lineEdit_12.text())) + total
                requete = f"""UPDATE CongeRecupere SET heures_récupération = {total} WHERE id_emp = {MyListe[0]};"""
                print(requete)
                db.cursor().execute(requete)
                db.commit()
                db.close()

                MyListe[12] = float(str(self.lineEdit_12.text()))
                print('hhhhhhh')
                self.sommesSupp()
                print('comancer')
                test = self.TraitementTableDeHeureSupplementaires(MyListe)
                print(test)
                if test == True:
                    requete = f"""UPDATE HeureSupplémentaires SET Total = {self.sommesHeuresSupp} ,Vingt_cinq = {self.supp_1},cinquante = {self.supp_2},cent = {self.supp_3} WHERE mat_emp = {MyListe[0]} AND Jour = '{MyListe[3]}';"""
                    print(requete)
                    db = self.open_connection()
                    db.cursor().execute(requete)
                    db.commit()
                    db.close()
                else:
                    requete = f"""INSERT INTO HeureSupplémentaires(mat_emp,Jour,Total,Vingt_cinq,cinquante,cent) VALUES ({MyListe[0]},'{MyListe[3]}',{self.sommesHeuresSupp},{self.supp_1},{self.supp_2},{self.supp_3});"""
                    print(requete)
                    db = sqlite3.connect("C:/Users/EL BAHTI/Desktop/Conge/Connection/appp.db")
                    print('aucun')
                    db.cursor().execute(requete)
                    db.commit()
                    db.close()
                MyListe[4] = self.HeureEntrer
                MyListe[6] = self.HeureSortir
                MyListe[8] = self.sommesHeuresSupp
                MyListe[9] = self.supp_1
                MyListe[10] = self.supp_2
                MyListe[11] = self.supp_3
                MyListe[13] = 0
                MyListe[5] = self.mise_consideration_value
                MyListe[7] = self.HeuresDeTravail
                self.retard = self.TransfererToMinutes(self.retard)
                self.UpdatePointage(MyListe)

            self.msg = save_pointage()
            self.msg.show()
        except :
            self.msg = erreur_pointage()
            self.msg.show()


    def DropTableAbsence(self):
        db = self.open_connection()
        requete = f"""DELETE FROM AbsenceJ WHERE Date_absence = '{self.liste[3]}' AND mat_emp = {self.liste[0]};"""
        db.cursor().execute(requete)
        print(requete)
        db.commit()
        db.close()

    def TraitementTableDeHeureSupplementaires(self,liste):
        try:
            db = sqlite3.connect("C:/Users/EL BAHTI/Desktop/Conge/Connection/appp.db")
            print('db connected')
            Cursor = db.cursor()
            Cursor.execute(f"""
            SELECT * FROM HeureSupplémentaires WHERE mat_emp = {liste[0]} AND Jour = '{liste[3]}';""")
            result = Cursor.fetchone()
            db.close()
            print(len(result))
            print(result)
            return True
        except:
            return False

    def TraitementTableDeRecuperation(self,liste):
        try:
            db = sqlite3.connect("C:/Users/EL BAHTI/Desktop/Conge/Connection/appp.db")
            print('db connected')
            Cursor = db.cursor()
            requete = f"""SELECT * FROM CongeDeRecuperation WHERE mat_emp = {liste[0]} AND JourR = '{liste[3]}';"""
            print(requete)
            Cursor.execute(requete)
            result = Cursor.fetchone()
            db.close()
            print(len(result))
            return True
        except:
            print('erreur de recupération')
            return False

    def NouvelleMission(self):
        if self.checkBox_6.isChecked():
            self.lineEdit_9.setReadOnly(False)
            self.groupBox.setEnabled(False)
            for label in self.groupBox.findChildren(QtWidgets.QLineEdit):
                label.setText('')
            self.msg = MissionsClasse()
            self.msg.show()
            
        else:
            self.groupBox.setEnabled(True)

    def Absence(self):
        if self.checkBox_4.isChecked():
            self.lineEdit_9.setReadOnly(False)
            self.groupBox.setEnabled(False)
            for label in self.groupBox.findChildren(QtWidgets.QLineEdit):
                label.setText('')
            
        else:
            self.groupBox.setEnabled(True)

    def TraitementTableAbsence(self,liste):
        
        self.lineEdit_10.setText('0.0')
        try:
            db = sqlite3.connect("C:/Users/EL BAHTI/Desktop/Conge/Connection/appp.db")
            print('db connected')
            Cursor = db.cursor()
            print(f"""
            SELECT * FROM AbsenceJ WHERE mat_emp = {liste[0]} AND Date_absence = '{liste[3]}';""")
            Cursor.execute(f"""
            SELECT * FROM AbsenceJ WHERE mat_emp = {liste[0]} AND Date_absence = '{liste[3]}';""")
            result = Cursor.fetchone()
            print(len(result))
            print(result)
            db.close()
            return True
        except:
            return False

    def UpdatePointage(self,liste):
        print('updating pointage ...and retard = ',self.retard)
        print('updating pointage ...and retard = ',self.retard)
        requete = f"""UPDATE Pointage SET Temps_de_travail = '{liste[2]}',Heure_Entrer = '{liste[4]}',Heure_mise_en_consideration = {liste[5]},Heure_Sortir = '{liste[6]}',NbrHeures = {liste[7]},Modification = 1,HeuresSupp = {liste[8]},vintCinq = {liste[9]},cinquante = {liste[10]},cent = {liste[11]},heures_récupération = {liste[12]},
        Absence = {liste[13]},Retard = {self.retard} WHERE id_emp = {liste[0]} AND Date_Jour = '{liste[3]}';"""
        print(requete)
        db = self.open_connection()
        db.cursor().execute(requete)
        print('Updating of Pointage was succesfully')
        db.commit()
        db.close()

    def sommesSupp(self):
        self.sommesHeuresSupp = 0
        self.supp_1 = self.supp_2 = self.supp_3 = 0
        if self.lineEdit_6.text() != '':
            print('lineEdit_6.text() = ',self.lineEdit_6.text(),' and ',len(str(self.lineEdit_6.text())))
            self.supp_1 = self.supp_1 + float(str(self.lineEdit_6.text()))
            self.sommesHeuresSupp = self.sommesHeuresSupp + float(str(self.lineEdit_6.text()))
        if self.lineEdit_7.text() != '':
            self.supp_2 = self.supp_2 + float(str(self.lineEdit_7.text()))
            self.sommesHeuresSupp = self.sommesHeuresSupp + float(str(self.lineEdit_7.text()))
        if self.lineEdit_8.text() != '':
            self.supp_3 = self.supp_3 + float(str(self.lineEdit_8.text()))
            self.sommesHeuresSupp = self.sommesHeuresSupp + float(str(self.lineEdit_8.text()))
        self.lineEdit_11.setText(str(self.sommesHeuresSupp))
        print(self.sommesHeuresSupp)
        print(self.lineEdit_11.text())

    def getheuresrecuper(self):
        db = self.open_connection()
        cursor = db.cursor()
        cursor.execute(f"""SELECT * FROM CongeRecupere WHERE mat_emp = {self.liste[0]}""")
        rs = cursor.fetchone()
        db.close()
        return float(rs[2])

    def open_connection(self):
        return sqlite3.connect("C:/Users/EL BAHTI/Desktop/Conge/Connection/appp.db")
#fonction des jours
    def GetFinDatePointage(self):
        db = sqlite3.connect("C:/Users/EL BAHTI/Desktop/Conge/Connection/appp.db")
        print('db connected')
        Cursor = db.cursor()
        Cursor.execute("SELECT * FROM Pointage ORDER BY Date_Jour;")
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

    def TransfererToMinutes(self,minutes):
        if minutes.find('.') <0:
            minutes = float(minutes)
            minutes = minutes * 60
        else:
            hours = minutes[:minutes.find('.')]
            hours = float(hours)
            minutes = minutes[minutes.find('.')+1:]
            minutes = float(minutes)
            total = hours*60 + minutes
            minutes = total
        return minutes
    def Retard(self):
        global check_retard
        check_retard = True
        print('retard ',self.AncienTemp, '  ',self.HeureEntrer)
        self.retard = str(self.get_Heures(f"""{(HeureEntrer[self.comboBox.currentText()][0])}:{(HeureEntrer[self.comboBox.currentText()][1])}""",self.HeureEntrer))
        print(self.retard)
        self.retard = self.retard.replace(':','.')
        last_char = self.retard[-3:]
        print(last_char)
        self.retard = self.retard.replace(last_char,'')
        print(self.retard)
        print(self.retard.find('.'))
        if self.retard.find('.') <0:
            self.retard = f"""{self.retard}.00"""
        print(self.retard)
    def ActualiserHeureNormal(self):
        self.AncienTemp = self.HeureEntrer
        self.HeureEntrer = f"""{self.lineEdit_2.text()}:{self.lineEdit_3.text()}"""
        self.HeureSortir = f"""{self.lineEdit_5.text()}:{self.lineEdit_4.text()}"""
        print('heures entre = ',self.HeureEntrer,' and heures sortir = ',self.HeureSortir)
        self.ChangeHeureTravail()
    def changeTimer(self):
        self.ChangerTime = True
        if self.comboBox.currentText() == 'Aucun':
            self.TempsTravail = '--'
            self.groupBox.setEnabled(False)
            for label in self.groupBox.findChildren(QtWidgets.QLineEdit):
                label.setText('')
        else:
            self.groupBox.setEnabled(True)
            self.mise_consideration = True
            self.lineEdit_2.setText(str(HeureEntrer[self.comboBox.currentText()][0]))
            self.lineEdit_3.setText(str(HeureEntrer[self.comboBox.currentText()][1]))
            self.lineEdit_5.setText(str(HeureSortir[self.comboBox.currentText()][0]))
            self.lineEdit_4.setText(str(HeureSortir[self.comboBox.currentText()][1]))
            self.HeureEntrer = f"""{(HeureEntrer[self.comboBox.currentText()][0])}:{(HeureEntrer[self.comboBox.currentText()][1])}"""
            self.HeureSortir = f"""{(HeureSortir[self.comboBox.currentText()][0])}:{(HeureSortir[self.comboBox.currentText()][1])}"""
            print('heures entre = ',self.HeureEntrer,' and heures sortir = ',self.HeureSortir)
            self.ChangeHeureTravail()


    def checkAbsenceTomporary(self):
        if self.liste[13]=='Oui':
            self.checkBox_4.setChecked(True)
            self.lineEdit_9.setText('')
            self.groupBox.setEnabled(False)


    def changeHeuresTomporary(self):
        self.lineEdit_10.setText(self.liste[7])
        self.lineEdit_11.setText(self.liste[8])
        self.lineEdit_12.setText(self.liste[12])

    def ChangeCheckboxtomporary(self):
        if not self.liste[9] == '0':
            print('25 is not checked')
            self.checkBox.setChecked(True)
            self.lineEdit_6.setText(self.liste[9])
        if not self.liste[10] == '0':
            print('50 is not checked')
            self.checkBox_2.setChecked(True)
            self.lineEdit_7.setText(self.liste[10])
        if not self.liste[11] == '0':
            print('100 is not checked')
            self.checkBox_3.setChecked(True)
            self.lineEdit_8.setText(self.liste[11])


    def getHoursMinutes(self,first):
        print(first.find(':'))
        index = first.find(':')
        hours = first[0:index]
        if len(hours)==1:
            hours = '0'+hours
        minutes = first[index+1:]
        print('minutes = ',minutes)
        print('hours = ',hours)
        return hours,minutes

    def ChangeHeureTravail(self):
        self.HeuresDeTravail = str(self.get_Heures(self.HeureEntrer,self.HeureSortir))
        self.HeuresDeTravail = self.HeuresDeTravail.replace(':','.')
        last_char = self.HeuresDeTravail[-3:]
        print(last_char)
        self.HeuresDeTravail = self.HeuresDeTravail.replace(last_char,'')
        print('heures normals = ',self.HeuresDeTravail)
        print(self.HeuresDeTravail.find('.'))
        if self.HeuresDeTravail.find('.') <0:
            self.lineEdit_10.setText(self.HeuresDeTravail + '.00')
        else:
            self.lineEdit_10.setText(self.HeuresDeTravail)
        if self.mise_consideration:
            self.mise_consideration = False
            self.mise_consideration_value = float(str(self.lineEdit_10.text()))
            
    def get_Heures(self,s1,s2):
        global check_retard
        from datetime import datetime,timedelta
        FMT = '%H:%M'
        tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
        if tdelta.days < 0:
            tdelta = timedelta(
                days=0,
                seconds=tdelta.seconds,
                microseconds=tdelta.microseconds
                )
        if self.comboBox.currentText() == 'Normal' and check_retard == False:
            tdelta = tdelta - timedelta(hours = 1)
        elif check_retard:
            check_retard = False
        return tdelta

    def Ouvrable(self):
        if self.checkBox.isChecked():
            self.lineEdit_6.setReadOnly(False)
        else:
            self.lineEdit_6.setText('')
            self.lineEdit_6.setReadOnly(True)

    def NuitJourRepos(self):
        if self.checkBox_3.isChecked():
            self.lineEdit_8.setReadOnly(False)
        else:
            self.lineEdit_8.setText('')
            self.lineEdit_8.setReadOnly(True)

    def Mi_Temps(self):
        pass

    def NuitJourOuvrable(self):
        if self.checkBox_2.isChecked():
            self.lineEdit_7.setReadOnly(False)
        
        else:
            self.lineEdit_7.setText('')
            self.lineEdit_7.setReadOnly(True)
if __name__ == "__main__":
    import sys
    liste = [2, 'Bensam jalal', '--', '2021-07-28', '--', '0', '--', '0', '0', '0', '0', '0', '0', 'Non', '0']
    app = QtWidgets.QApplication(sys.argv)
    ui = PointageClasse(liste)
    ui.show()
    sys.exit(app.exec_())
#self.comboBox.setCurrentIndex(SituationFamilial[str(add[7])])

    