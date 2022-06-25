from datetime import date,datetime,timedelta
import sqlite3
now = date.today()
class ClassGeneral:
    def open_connection(self):
        return sqlite3.connect("appp.db")
    def get_id_employe(self,id_conge):
        db = self.open_connection()
        cursor = db.cursor()
        cursor.execute(f'''SELECT Mat_Emp,Validation FROM Conge WHERE Id = {id_conge};''')
        id_conge_nv = cursor.fetchone()
        db.close()
        return id_conge_nv[0]
    def get_nbr_samediFromTable(self,id_emp):
        #╘id_cg = get_id_conge(id_emp,date_debut)
        db = self.open_connection()
        cursor = db.cursor()
        cursor.execute(f'''SELECT nbr_Samedi,Nom FROM Employees WHERE Mat_Emp = {id_emp};''')
        nbr_ss = cursor.fetchone()
        db.close()
        return nbr_ss[0]
    def Get_Date_Fin(self,var,nbr):
        Begindate = datetime.strptime(var, "%Y-%m-%d")
        Enddate = Begindate + timedelta(days=nbr)
        return Enddate.strftime("%Y-%m-%d")


class Calendrier_class(ClassGeneral):
    def open_connection(self):
        return sqlite3.connect("appp.db")
    def Calculer_Anciennete_Days(self,var):
        experience = date(int(var[0]), int(var[1]), int(var[2]))
        experience_in_days = now - experience
        datetime.today().strftime('%Y-%m-%d')
        return experience_in_days

        return rdelta.years,rdelta.months,rdelta.days
    def Get_Date_Fin_encien(self,var,nbr):
        specific_date = date(int(var[0]), int(var[1]), int(var[2]))
        new_date = specific_date + timedelta(nbr)
        return new_date
    
    def perdelta(self,start, end):
        curr = start
        delta = timedelta(days=1)
        while curr <= end:
            yield curr
            curr += delta

    def GetNbrDimanche(self,start,end):
        var = 0
        for result in self.perdelta(date(start.year,start.month,start.day), date(end.year, end.month, end.day)):
                if result.strftime("%A") == 'Sunday':
                    var = var +1
        return var
    def get_nbr_samedi(self,start,end):
        var = 0
        for result in self.perdelta(date(start.year,start.month,start.day), date(end.year, end.month, end.day)):
                if result.strftime("%A") == 'Saturday':
                    var = var +1
        return var
    def get_nbr_vendredi(self,start,end):
        var = 0
        for result in self.perdelta(date(start.year,start.month,start.day), date(end.year, end.month, end.day)):
                if result.strftime("%A") == 'Friday':
                    var = var +1
        return var
    


    def get_id_conge(self,id_emp,date_debut):
        db = self.open_connection()
        cursor = db.cursor()
        print(date_debut)
        cursor.execute(f'''SELECT Id,Validation FROM Conge WHERE Mat_Emp = {id_emp} AND DateDebut = '{date_debut}';''')
        id_conge = cursor.fetchone()
        db.close()
        return id_conge[0]
    

    def get_id_responsable(self,id):
        db = self.open_connection()
        cursor = db.cursor()
        cursor.execute(f"""SELECT Mat_Responsable,Nom FROM Employees WHERE Mat_Emp = {id};""")
        ff = cursor.fetchone()
        return ff[0]

    
    def get_nom_prenom(self,idemp):
        db = self.open_connection()
        cursor = db.cursor()
        ids = idemp
        cursor.execute(f""" SELECT Nom,Prenom FROM Employees WHERE Mat_Emp = {ids};""")
        idd = cursor.fetchone()
        db.close()
        return f'''{idd[0]}  {idd[1]}'''


    def GetFonction(self,id_admin):
        db = self.open_connection()
        cursor = db.cursor()
        cursor.execute(f"""SELECT Fonction,Cin FROM Employees WHERE Mat_Emp = {id_admin};""")
        result = cursor.fetchone()
        db.close()
        return result[0]

    def verifier_Samedi(self,id_emp,temp_travail,nbr_samedi):
        nbr_samedi_rest = super().get_nbr_samediFromTable(id_emp)
        if temp_travail ==True:   #normal et 22->6
            if nbr_samedi <= nbr_samedi_rest:
                #autorisation de demande  calcul samedi
                return nbr_samedi
            else :
                return nbr_samedi_rest # n'est pas calucle samedi
        else :
            return nbr_samedi



class Conge(ClassGeneral):

    def __init__(self,id_conge,nbrJoursDemander,nbrSamediDemander,typeShift,secondtypeshift,tempsTravail):
        self.tempsTravail = tempsTravail
        self.id_conge = id_conge
        self.nbrJoursDemander = nbrJoursDemander
        self.nbrSamediDemander = nbrSamediDemander
        self.typeShift = typeShift
        self.testv = True
        self.secondtypeShift = secondtypeshift
        self.id_emp = super().get_id_employe(self.id_conge)
        self.samediDeEmployer = super().get_nbr_samediFromTable(self.id_emp)
        self.rest_samedi = self.samediDeEmployer - self.nbrSamediDemander
        self.traiter = False
        self.verfier = False
        self.nbrsamedi = 0
        self.nbrVendredi = 0
        self.nbrDimanche = 0
        self.touverJourFin = ' '
        
    def choisirTypeConge(self,typeConge):
        print('choisir type de conge ...')
        db = self.open_connection()
        cursor = db.cursor()
        if typeConge == 'CongeDeRecuperation':
            cursor.execute(f'''SELECT mat_emp,Id,sum(Heures) FROM {typeConge} WHERE mat_emp = {self.id_emp};''')
        else:
            cursor.execute(f'''SELECT * FROM {typeConge} WHERE id_emp = {self.id_emp};''')
        self.type_Conge = cursor.fetchone()
        db.close()
        #transferer heures recup
        if self.tempsTravail == 'Normal':
            print('type choisir est normal',float(self.type_Conge[2]))
            totalHeures = float(float(self.type_Conge[2]) / 9)
        else:
            totalHeures = float(float(self.type_Conge[2]) / 8)
        self.Rest = totalHeures - self.nbrJoursDemander
        print('self.Rest = totalHeures - self.nbrJoursDemander == ',self.Rest,' = ',totalHeures,' - ',self.nbrJoursDemander)
        if self.secondtypeShift == True and self.typeShift == True:
            print('second shift,shift are  true ... with rest samedi = ',self.rest_samedi)
        elif self.secondtypeShift == False and self.typeShift == False:
            pass

        elif self.secondtypeShift == False or self.typeShift == False:
            if self.samediDeEmployer != 0:
                self.rest_samedi = self.rest_samedi + 1
            print('second shift false or shift false ... with rest samedi = ',self.rest_samedi)

    def miseAjourConge(self,nbrDeSamediCalculer):    
        print('mise a jour ...')      
        db = self.open_connection()
        cursor = db.cursor()
        cursor.execute(f'''UPDATE Conge SET nbr_Samedi = {nbrDeSamediCalculer} WHERE Id = {self.id_conge};''')
                #cursor.execute(f'''UPDATE Conge SET DateFin = {nbr_samedi_rest} WHERE Id = {id_conge};''')     
        db.commit()
        db.close()

    def touverDateFin(self):
        db = self.open_connection()
        cursor = db.cursor()
        cursor.execute(f'''SELECT DateFin,DateDebut FROM Conge WHERE Id = {self.id_conge};''')
        Df = cursor.fetchone()
        db.close()
        return Df[0]



    def DeleteConge(self):
        print('deletting conge ....')
        db = self.open_connection()
        cursor = db.cursor()
        requ = f"""DELETE FROM Conge WHERE Id = {self.id_conge};"""
        print(requ)
        cursor.execute(requ)
        db.commit()
        db.close()


    def get_Jours(self,date_fin):
        day_dimanche = datetime.strptime(str(date_fin),"%Y-%m-%d")
        return day_dimanche.strftime("%A")


    def troisSamedi(self,Rest):
        print('analiqing three saturday ...')
        if Rest >=0:
            self.miseAjourConge(Rest)
            print('calculer le samedi')
        else:
            Rest = -Rest
            if self.verfier == True:
                Rest = 0
            db = self.open_connection()
            cursor = db.cursor()
            cursor.execute(f'''SELECT DateFin,DateDebut FROM Conge WHERE Id = {self.id_conge};''')
            dateFin =cursor.fetchone()
            dateFin_changer = super().Get_Date_Fin(str(dateFin[0]),Rest)
            cursor.execute(f'''UPDATE Conge SET DateFin = '{dateFin_changer}' WHERE Id = {self.id_conge};''')
            print('date fin aprés changement = ',dateFin_changer)
            
            db.commit()
            db.close()
            self.miseAjourConge(0)
                    #calculer le samedi
            print('rest = ',Rest)
            #calculer samedi et le rest sans samedi
            print('calculer samedi et le rest sans samedi')


    def CongePaye(self):
        self.choisirTypeConge('CongePaye')
        if self.Rest >= 0:
            self.traiter = True
            #vérifier droit de samedi            
            db = self.open_connection()
            cursor = db.cursor()
            #cursor.execute(f'''UPDATE CongePaye SET nbr_jours = {self.Rest} WHERE Id = {self.type_Conge[0]};''')
            cursor.execute(f'''UPDATE Conge SET nbr_Samedi_Consommer = {self.nbrSamediDemander} WHERE Id = {self.id_conge};''')
            db.commit()
            db.close()
            #nomer cette partie comme fonction de troisSamedi(self,id_conge,Rest,nbrDeSamediCalculer)
            #ghda andir typeshift treur bohdha olakhra bohda onkhdm 3la date fin si vendredi ajouter 0 avec condition de rest négative
            if self.GetNbrDimanche == 0:                
                #if self.typeShift == True or self.secondtypeShift == True:
                if self.typeShift == True:
                    if self.get_Jours(self.touverDateFin()) == 'Friday' and self.rest_samedi < 0:
                        print('date fin est vendredi sans calculer samedi')
                        self.verfier = True
                    self.troisSamedi(self.rest_samedi)
           # elif self.touverDateFin == 'Friday' and self.rest_samedi < 0:
            elif self.typeShift == True or self.secondtypeShift == True:
                self.troisSamedi(self.rest_samedi)
                
        else:
            self.DeleteConge()
            print('vous etes dépasser le nbr autoriser')


    def AjouterJours(self,nbr):
        db = self.open_connection()
        cursor = db.cursor()
        cursor.execute(f'''SELECT DateFin,DateDebut FROM Conge WHERE Id = {self.id_conge};''')
        dateFin =cursor.fetchone()
        dateFin_changer = super().Get_Date_Fin(str(dateFin[0]),nbr)
        cursor.execute(f'''UPDATE Conge SET DateFin = '{dateFin_changer}' WHERE Id = {self.id_conge};''')
        print('date fin aprés changement = ',dateFin_changer)
            
        db.commit()
        db.close()

    def CongeEvenement(self):
        self.choisirTypeConge('CongeEvenement')#Zajouter le shift et nbr samedidemander pour comparer samedirest vec samedidemander
        if self.Rest >= 0:
            self.traiter = True
            print('nbr samedi consommer ',self.nbrSamediDemander)
            db = self.open_connection()
            cursor = db.cursor()
            cursor.execute(f'''UPDATE Conge SET nbr_Samedi_Consommer = {self.nbrSamediDemander} WHERE Id = {self.id_conge};''')
            db.commit()
            db.close()
        else:
            self.DeleteConge()
            self.traiter = False
    def CongeRecuperer(self):
        self.choisirTypeConge('CongeDeRecuperation')
        if self.Rest >= 0:
            self.traiter = True
            print('nbr samedi consommer ',self.nbrSamediDemander)
            db = self.open_connection()
            cursor = db.cursor()
            cursor.execute(f'''UPDATE Conge SET nbr_Samedi_Consommer = {self.nbrSamediDemander} WHERE Id = {self.id_conge};''')
            db.commit()
            db.close()
        else:
            self.DeleteConge()
            print('vous etes dépasser le nbr autoriser')
    def makeTrue(self):
        self.traiter = True

#instance_conge = Conge(298,1,2,True,False)
#ùprint(instance_conge.get_Jours(instance_conge.touverDateFin()))
#del instance_conge




