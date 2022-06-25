from PyQt5.uic import loadUi
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import Qt
from db_connect import db as dbs
from Sauvegarder import save_pointage
from Erreur import erreur_pointage
import sqlite3
check_Image = True
check_retard = False
import Resources_rc
import datetime
Mois_Fr = {1:'Janvier',2:'Février',3:'Mars',4:'Avril',5:'Mai',6:'Juin',7:'Juillet',8:'Août',9:'Septembre',10:'Octobre',11:'Novembre',12:'Décembre'}
HeureEntrer = {'Aucun':{0:' ',1:' '},'Normal':{0:'08',1:'00'},'Shift1':{0:'14',1:'00'},'Shift2':{0:'06',1:'00'},'Shift3':{0:'22',1:'00'}}
HeureSortir = {'Aucun':{0:' ',1:' '},'Normal':{0:'18',1:'00'},'Shift1':{0:'22',1:'00'},'Shift2':{0:'14',1:'00'},'Shift3':{0:'06',1:'00'}}
class msg_modification(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        loadUi("pointage.ui",self)
        self.setWindowTitle('Pointage')
        self.setWindowIcon(QtGui.QIcon('pointer.png'))
        self.pushButton_2.clicked.connect(self.close_app)
        self.comboBox.currentIndexChanged.connect(self.changeTimer)
        self.pushButton_7.clicked.connect(self.changeEmployees)
        self.checkBox.clicked.connect(self.Ouvrable)
        self.checkBox_5.clicked.connect(self.Mi_Temps)
        self.checkBox_2.clicked.connect(self.NuitJourOuvrable)
        self.checkBox_3.clicked.connect(self.NuitJourRepos)
        self.checkBox_4.clicked.connect(self.Absence)
        self.pushButton.clicked.connect(self.valider)
        self.pushButton_5.clicked.connect(self.sommesSupp)
        self.pushButton_4.clicked.connect(self.ActualiserHeureNormal)
        self.pushButton_3.clicked.connect(self.modiferJoursP)
        self.year = datetime.datetime.today().year
        self.moiss = datetime.datetime.today().month
        self.Aujourdhuit = datetime.datetime.today().strftime("%Y-%m-%d")
        self.lineEdit.setText(str(self.Aujourdhuit))
        names = self.getListNoms()

        print(type(names))
        print(names)
        self.test = True
        completer = QtWidgets.QCompleter(names)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.lineEdit_13.setCompleter(completer)
        db = self.open_connection()
        cursor = db.cursor()
        cursor.execute(f"""SELECT * FROM HeureNormales ORDER BY Annee DESC ,mois DESC ;""")
        result = cursor.fetchone()
        print(result)
        db.close()
        self.resultt = result[2]
        self.show_Employees()
        print(self.list_emp)
        self.checknormal()
        
    def modiferJoursP(self):
        self.Aujourdhuit = str(self.lineEdit.text())
        dob = datetime.datetime.strptime(self.Aujourdhuit, '%Y-%m-%d')
        print('type de dob.strftime(Y) est ',type(dob.strftime('%Y')))
        self.modiferAnneeMois(dob.strftime('%Y'),dob.strftime('%m'))

    def open_connection(self):
        return sqlite3.connect("appp.db")

    def modiferAnneeMois(self,Anne,Mois):
        #· il faut vérifier mn la base de données pour eviter les conyraintes
        print('Annee = ',Anne,' Mois = ',Mois)
        pr = Mois[:1]
        if pr == '0':
            Mois = Mois[1:] 
        db = self.open_connection()
        cursor = db.cursor()
        cursor.execute("SELECT Mat_Emp,Nom FROM Employees;")

        tousLesMatricules = []
        for v in cursor.fetchall():
            tousLesMatricules.append(str(v[0]))
        print('tous les matricules = ',tousLesMatricules)
        cursor.execute(f"""SELECT mois,Annee FROM Absence ORDER BY Id DESC;""")
        var = cursor.fetchone()
        print('Mois = ',Mois,' and var[0] = ',var[0])
        if str(Anne) == str(var[1]):
            print('vous etes dans meme annee ...')
            if str(Mois) == str(var[0]):
                print('vous etes dans meme mois')
            else:
                self.moiss = Mois
                if int(Mois) > int(var[0]):
                    print('Nouveau mois ...')
                    for v in tousLesMatricules:
                        requete = f"""INSERT INTO Absence(fgroupbox.,mois,Annee) VALUES ({v},{self.moiss},{self.year})"""
                        print(requete)
                        cursor.execute(str(requete))
                        cursor.execute(f"""INSERT INTO HeureNormales(mat_emp,mois,Annee) VALUES ({v},{self.moiss},{self.year})""")
                        cursor.execute(f"""INSERT INTO HeureSupplémentaires(mat_emp,mois,Annee) VALUES ({v},{self.moiss},{self.year})""")
                    db.commit()
        else:
            self.year = str(Anne)
            self.moiss = 1
            for v in tousLesMatricules:
                requete = f"""INSERT INTO Absence(mat_emp,mois,Annee) VALUES ({v},{self.moiss},{self.year})"""
                print(requete)
                cursor.execute(str(requete))
                cursor.execute(f"""INSERT INTO HeureNormales(mat_emp,mois,Annee) VALUES ({v},{self.moiss},{self.year})""")
                cursor.execute(f"""INSERT INTO HeureSupplémentaires(mat_emp,mois,Annee) VALUES ({v},{self.moiss},{self.year})""")
            db.commit()
        db.close()
        

    def getListNoms(self):
        db = self.open_connection()
        cursor = db.cursor()
        cursor.execute("SELECT concat(Nom,' ',Prenom),Mat_Emp FROM Employees;")
        v = cursor.fetchall()
        db.close()
        list_nom = []
        for a in v:
            list_nom.append(str(a[0]))
        return list_nom
    def changeEmployees(self):
        self.id_emp = int(self.getId(str(self.lineEdit_13.text())))
        print('date == ',self.Aujourdhuit)
        print('idemp = ',self.id_emp)
        if self.checkConge(self.id_emp):
            self.groupBox.setEnabled(False)
            self.msg = QtWidgets.QMessageBox()
            self.msg.setWindowTitle('Remarque')
            self.msg.setText(f""" {self.lineEdit_13.text()} est en congé maintenant !! """ )
            self.msg.show()
        else:
            self.groupBox.setEnabled(True)

    def checkConge(self,id_emp):
        try:
            db = self.open_connection()
            cursor = db.cursor()
            cursor.execute(f"""SELECT DateDebut,DateFin FROM Conge WHERE Mat_Emp = {id_emp} AND Validation = 'V' ORDER BY DateDebut DESC;""")
            var = cursor.fetchone()
            self.date_debut = var[0]
            self.date_fin = var[1]
            print('debut ',self.date_debut,' date fin = ',self.date_fin,' and ',self.Aujourdhuit, ' ',id_emp)
            cursor.execute(f"""SELECT NbrJours,Type_de_Conge from Conge WHERE Mat_Emp = {id_emp} and '{self.Aujourdhuit}' BETWEEN '{self.date_debut}' and '{self.date_fin}' GROUP BY NbrJours;""")
            print('execute deux hhh wi')
            vv = cursor.fetchone()
            len(vv)
            #cursor.execute(f"""INSERT INTO Pointage (id_emp,Date_Jour,estCongé) VALUES({id_emp},'{self.Aujourdhuit}',1);""")
            db.commit()
            db.close()
            return True
        except (dbs.Error , TypeError):
            print('hhhh')
            return False

    def getId(self,nomcomplet):
        db = self.open_connection()
        cursor = db.cursor()
        cursor.execute(f"""SELECT Mat_Emp,Nom FROM Employees WHERE concat(Nom,' ',Prenom) = "{nomcomplet}";""")
        result = cursor.fetchone()
        db.close()
        return result[0]




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

    def getJoursRecup(self):
        db = self.open_connection()
        cursor = db.cursor()
        cursor.execute(f"""SELECT * FROM CongeRecupere WHERE id_emp = {self.id_emp}""")
        rs = cursor.fetchone()
        db.close()
        return float(rs[2])


    def valider(self):
        try:
            self.id_emp = int(self.getId(str(self.lineEdit_13.text())))
            if self.checkBox_5.isChecked():
                tt = float(self.getTotalSupp('Absence'))
                db = self.open_connection()
                db.cursor().execute(f"""INSERT INTO Pointage(id_emp,Date_Jour,Temps_de_travail) VALUES ({self.id_emp},'{self.lineEdit.text()}','Mi-Temps');""")
                print('hhhh')
                if self.checkBox_4.isChecked():
                    print('walo')
                    cursor = db.cursor().execute(f"""SELECT * FROM Pointage WHERE id_emp = {self.id_emp} ORDER by Date_Jour DESC;""")
                    id_pointage = cursor.fetchone()
                    requete1 = f"""UPDATE Pointage SET Absence = 1 WHERE id_emp = {self.id_emp} AND id = {id_pointage[0]};"""
                    print(requete1)
                    db.cursor().execute(requete1)
                    db.cursor().execute(f"""UPDATE Absence SET Total = {tt + float(str(self.lineEdit_9.text()))} WHERE mat_emp = {self.id_emp} AND mois = {self.moiss} AND Annee = {self.year};""")
                db.commit()
                db.close()
            elif self.checkBox_4.isChecked():
                self.lineEdit_9.setReadOnly(False)
                self.groupBox.setEnabled(False)
                tt = float(self.getTotalSupp('Absence'))
                if self.lineEdit_9.text() == '':
                    self.lineEdit_9.setText('0')
                print('totzl = ',tt)
                db = self.open_connection()
                db.cursor().execute(f"""INSERT INTO Pointage(id_emp,Date_Jour,Absence,Temps_de_travail) VALUES ({self.id_emp},'{self.lineEdit.text()}',1,'{str(self.comboBox.currentText())}');""")
                print('hhhh')
                db.cursor().execute(f"""UPDATE Absence SET Total = {tt + float(str(self.lineEdit_9.text()))} WHERE mat_emp = {self.id_emp} AND mois = {self.moiss} AND Annee = {self.year};""")
                db.commit()
                db.close()
            else:
                self.HeuresDeTravail = float(str(self.lineEdit_10.text()))
                print('heures de travail = ',self.HeuresDeTravail)
                if self.lineEdit_11.text() == '':
                    self.lineEdit_11.setText('0.0')
                if self.lineEdit_12.text() == '':
                    self.lineEdit_12.setText('0.0')
                self.joursrecup = self.getJoursRecup()
                self.joursrecup = self.joursrecup + float(str(self.lineEdit_12.text()))
                print('jour recup = ',self.joursrecup)
                self.sommesHeuresSupp = float(str(self.lineEdit_11.text()))
                self.sommesSupp()
                print('somme sup mzyana')
                self.InsertDonnees()
            self.msg = save_pointage()
            self.msg.show()
        except :
            self.msg = erreur_pointage()
            self.msg.show()


    def sommesSupp(self):
        self.sommesHeuresSupp = 0
        self.supp_1 = self.supp_2 = self.supp_3 = 0
        if self.lineEdit_6.text() != '':
            self.supp_1 = self.supp_1 + float(str(self.lineEdit_6.text()))
            self.sommesHeuresSupp = self.sommesHeuresSupp + float(str(self.lineEdit_6.text()))
        if self.lineEdit_7.text() != '':
            self.supp_2 = self.supp_2 + float(str(self.lineEdit_7.text()))
            self.sommesHeuresSupp = self.sommesHeuresSupp + float(str(self.lineEdit_7.text()))
        if self.lineEdit_8.text() != '':
            self.supp_3 = self.supp_3 + float(str(self.lineEdit_8.text()))
            self.sommesHeuresSupp = self.sommesHeuresSupp + float(str(self.lineEdit_8.text()))
        self.lineEdit_11.setText(str(self.sommesHeuresSupp))
    def getYears_mois(self,table):
        db = self.open_connection()
        cursor = db.cursor()
        cursor.execute(f"""SELECT * FROM {table} WHERE mat_emp = {self.id_emp} ORDER BY Annee DESC ,mois DESC ;""")
        result = cursor.fetchone()
        print(result)
        db.close()
        return result[3],self.resultt,result[4]
    def checknormal(self):
        pass


    def getTroisSupp(self):
        db = self.open_connection()
        cursor = db.cursor()
        cursor.execute(f"""SELECT Vingt_cinq,cinquante,cent FROM HeureSupplémentaires WHERE mat_emp = {self.id_emp};""")
        test = cursor.fetchone()
        db.close()
        return test[0],test[1],test[2]


    def updateTableHeures(self,table,heures):
        #sup1,sup2,sup3 = self.getTroisSupp()
        db = self.open_connection()
        cursor = db.cursor()
        cursor.execute(f"""SELECT Id,mat_emp FROM {table} WHERE mois = {self.moiss} AND Annee = {self.year} AND mat_emp = {self.id_emp};""")
        self.id_table = cursor.fetchone()[0]
        cursor.execute(f"""UPDATE {table} SET Total = {heures} WHERE Id = {self.id_table};""")
        if table == "HeureSupplémentaires":
            print('sup2 = ',self.supp_2)
            cursor.execute(f""" UPDATE {table} SET Vingt_cinq = {self.supp_1},cinquante ={self.supp_2},cent ={self.supp_3} WHERE mat_emp = {self.id_emp} and mois = {self.mois} and Annee = {self.year};""")
     
        db.commit()
        db.close()


    def getTotalSupp(self,table):
        try:
            db = self.open_connection()
            cursor = db.cursor()
            cursor.execute(f"""SELECT Total,mat_emp FROM {table} WHERE mois = {self.moiss} AND Annee = {self.year} AND mat_emp = {self.id_emp};""")
            db.close()
            return cursor.fetchone()[0]
        except :
            pass

    def InsertDonnees(self):
        self.years,self.mois,Total = self.getYears_mois('HeureNormales')
        print('years now = ',self.year)
        print('years normal ',self.years)
        print('mois = ',self.mois)
        print('somme ',self.sommesHeuresSupp)
        self.total = self.HeuresDeTravail + float(Total)
        print('pointage dans meme mois ',self.total)
        self.updateTableHeures("HeureNormales",self.total)
        print('somme ',self.sommesHeuresSupp)
        print('pointage dans meme mois ')
        if self.sommesHeuresSupp != 0:
            print('supp detecterrr')
            self.total_supp = self.getTotalSupp("HeureSupplémentaires")
            print('total supp ',self.total_supp)
            print('supp detecter ',self.sommesHeuresSupp)
            self.total = self.sommesHeuresSupp + float(self.total_supp)
            self.updateTableHeures("HeureSupplémentaires",self.total)
        self.InsertPointage()
            
    def nouveauTable(self,table,heures,mois,annee):
        db = self.open_connection()
        cursor = db.cursor()
        cursor.execute(f""" INSERT INTO {table}(mat_emp,mois,Annee,Total) VALUES({self.id_emp},{mois},{annee},{heures});""")
        if table == "HeureSupplémentaires":
            print('sup2 = ',self.supp_2)
            cursor.execute(f""" UPDATE {table} SET Vingt_cinq = {self.supp_1},cinquante ={self.supp_2},cent ={self.supp_3} WHERE mat_emp = {self.id_emp} and mois = {mois} and Annee = {annee};""")
        db.commit()
        db.close()
        #self.id_emp self.heureTravail self.HeureEntrer self.HeureSortir les trois heures supp 
        

    def show_Employees(self):
        db = self.open_connection()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Employees;")
        self.list_emp = cursor.fetchall()
        db.close()
        
    def Absence(self):
        if self.checkBox_4.isChecked():
            self.lineEdit_9.setReadOnly(False)
            self.groupBox.setEnabled(False)
            for label in self.groupBox.findChildren(QtWidgets.QLineEdit):
                label.setText(' ')
            
        else:
            self.groupBox.setEnabled(True)

    def changeTimer(self):
        if self.comboBox.currentText() == 'Aucun':
            self.groupBox.setEnabled(False)
            for label in self.groupBox.findChildren(QtWidgets.QLineEdit):
                label.setText(' ')
        else:
            self.groupBox.setEnabled(True)
            self.mise_consideration = True
            self.lineEdit_2.setText(str(HeureEntrer[self.comboBox.currentText()][0]))
            self.lineEdit_3.setText(str(HeureEntrer[self.comboBox.currentText()][1]))
            self.lineEdit_5.setText(str(HeureSortir[self.comboBox.currentText()][0]))
            self.lineEdit_4.setText(str(HeureSortir[self.comboBox.currentText()][1]))
            self.TempsTravail = self.comboBox.currentText()
            self.HeureEntrer = f"""{(HeureEntrer[self.comboBox.currentText()][0])}:{(HeureEntrer[self.comboBox.currentText()][1])}"""
            self.HeureSortir = f"""{(HeureSortir[self.comboBox.currentText()][0])}:{(HeureSortir[self.comboBox.currentText()][1])}"""
            print('heures entre = ',self.HeureEntrer,' and heures sortir = ',self.HeureSortir)
            self.ChangeHeureTravail()
    
    def ActualiserHeureNormal(self):
        self.AncienTemp = self.HeureEntrer
        self.HeureEntrer = f"""{self.lineEdit_2.text()}:{self.lineEdit_3.text()}"""
        self.HeureSortir = f"""{self.lineEdit_5.text()}:{self.lineEdit_4.text()}"""
        print('heures entre = ',self.HeureEntrer,' and heures sortir = ',self.HeureSortir)
        self.ChangeHeureTravail()
        

    def ChangeHeureTravail(self):
        self.HeuresDeTravail = str(self.get_Heures(self.HeureEntrer,self.HeureSortir))
        self.HeuresDeTravail = self.HeuresDeTravail.replace(':','.')
        last_char = self.HeuresDeTravail[-3:]
        print(last_char)
        self.HeuresDeTravail = self.HeuresDeTravail.replace(last_char,'')
        print(self.HeuresDeTravail)
        print(self.HeuresDeTravail.find('.'))
        if self.HeuresDeTravail.find('.') <0:
            self.lineEdit_10.setText(self.HeuresDeTravail + '.00')
        else:
            self.lineEdit_10.setText(self.HeuresDeTravail)
        if self.mise_consideration:
            self.mise_consideration = False
            self.mise_consideration_value = float(str(self.lineEdit_10.text()))

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

    def NuitJourRepos(self):
        if self.checkBox_3.isChecked():
            self.lineEdit_8.setReadOnly(False)
        else:
            self.lineEdit_8.setText('')
            self.lineEdit_8.setReadOnly(True)

    def Mi_Temps(self):
        if self.checkBox_5.isChecked():
            self.groupBox.setEnabled(False)
        else:
            self.groupBox.setEnabled(True)

    def NuitJourOuvrable(self):
        if self.checkBox_2.isChecked():
            self.lineEdit_7.setReadOnly(False)
        
        else:
            self.lineEdit_7.setText('')
            self.lineEdit_7.setReadOnly(True)



    def InsertPointage(self):
        print('insert pointage')
        if self.groupBox.isEnabled():
            print("groupbox enabled")
            self.Retard()
            if self.lineEdit_10.text() == '':
                self.lineEdit_10.setText('0.00')
            print(float(self.lineEdit_10.text()),'      ',self.lineEdit_11.text())
            db = self.open_connection()
            print(f"""INSERT INTO Pointage(id_emp,Temps_de_travail,Date_Jour,Heure_Entrer,Heure_Sortir,NbrHeures,HeuresSupp,heures_récupération,Retard,vintCinq,cinquante,cent,Heure_mise_en_consideration) VALUES ({self.id_emp},'{str(self.comboBox.currentText())}','{self.lineEdit.text()}','{self.lineEdit_2.text()}:{self.lineEdit_3.text()}','{self.lineEdit_5.text()}:{self.lineEdit_4.text()}',{self.mise_consideration_value},{float(self.lineEdit_11.text())},{float(str(self.lineEdit_12.text()))},{self.retard},{self.supp_1},{self.supp_2},{self.supp_3},{float(self.lineEdit_10.text())});""")
            db.cursor().execute(f"""INSERT INTO Pointage(id_emp,Temps_de_travail,Date_Jour,Heure_Entrer,Heure_Sortir,NbrHeures,HeuresSupp,heures_récupération,Retard,vintCinq,cinquante,cent,Heure_mise_en_consideration) VALUES ({self.id_emp},'{str(self.comboBox.currentText())}','{self.lineEdit.text()}','{self.lineEdit_2.text()}:{self.lineEdit_3.text()}','{self.lineEdit_5.text()}:{self.lineEdit_4.text()}',{self.mise_consideration_value},{float(self.lineEdit_11.text())},{float(str(self.lineEdit_12.text()))},{self.retard},{self.supp_1},{self.supp_2},{self.supp_3},{float(self.lineEdit_10.text())});""")
            if self.lineEdit_12.text() != '0.0':
                db.cursor().execute(f"""UPDATE CongeRecupere SET heures_récupération = {self.joursrecup} WHERE id_emp = {self.id_emp};""")
            db.commit()
            db.close()



    def Ouvrable(self):
        if self.checkBox.isChecked():
            self.lineEdit_6.setReadOnly(False)
        else:
            self.lineEdit_6.setText('')
            self.lineEdit_6.setReadOnly(True)

    def close_app(self):
        self.close()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = msg_modification()
    ui.show()
    sys.exit(app.exec_())