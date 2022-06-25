#import mysql.connector as db
import sqlite3 as db
try:
    mydb = db.connect("appp.db")
    print('database connect ')
except:
    print('database not connected')
#db.connect(
        #host="bldqvvs4xvzxvsrelzxn-mysql.services.clever-cloud.com",
       # user="uziulijiyownhgls",
      #  password="KYiEApuZMfyt3pXidUbF",
     #   database="bldqvvs4xvzxvsrelzxn"
    #     )
#mydb.cursor().execute("INSERT INTO Employees VALUES(1,'N443311','EL BAHTI','Ayoub','2000-08-11','2021-05-03',12)")
#mydb.cursor().execute("CREATE TABLE Conge (Id INT(4),Mat_Emp INT(4),Type_de_Conge VARCHAR(25),DateDebut DATE,NbrJours DECIMAL (3,1),Validation CHAR(1),PRIMARY KEY(Id),FOREIGN KEY (Mat_Emp) REFERENCES Employees(Mat_Emp),FOREIGN KEY (Type_de_Conge) REFERENCES TypeConge(Code))")
#mydb.commit()
#mydb.close()
#mydb.cursor().execute("CREATE TABLE Employees(Mat_Emp INT(4),Cin VARCHAR (12),Nom VARCHAR(25),Prenom VARCHAR(25),DateDeNaissance DATE,DateEntree DATE,Anciennete DECIMAL(12,6),PRIMARY KEY (Mat_Emp),UNIQUE(Cin))")