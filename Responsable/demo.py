from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5 import QtGui
import mysql.connector as db

class InsertDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(InsertDialog, self).__init__(*args, **kwargs)
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        #self.setStyleSheet("background-color: white;")
        self.QBtn = QPushButton()
        self.QBtn.setText("Enregister")
        #Θself.setWindowIcon(QIcon('add1.jpg')) 

        self.setWindowTitle("Add Student")
        self.setFixedWidth(400)
        self.setFixedHeight(400)

        self.setWindowTitle("Insert Client")
        self.setFixedWidth(626)
        self.setFixedHeight(300)

        #self.QBtn.clicked.connect(self.addclient)

        layout = QVBoxLayout()
        layout1 = QHBoxLayout()



        #elf.nameinput = QLineEdit()
        #self.nameinput.setPlaceholderText("Name")
        self.mouad0 = QLineEdit(self)
        self.mouad0.setGeometry(220,50,400,35)
        self.mouad0.setPlaceholderText("Nom......")
        self.mouad0.setStyleSheet("QLineEdit"" {"
	        "box-shadow:inset 0px 1px 0px 0px #276873;"
	        "background:linear-gradient(to bottom, #C4F21A 5%, #DCFF9B   100%);"
	        "background-color:#C4F21A;"
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
	        "background:linear-gradient(to bottom, #8CD800 5%, #DCFF9B   100%);"
	        "background-color:#DCFF9B;"
            "}"
            ".QLineEdit:active {"
	        "position:relative;"
	        "top:1px;"
            "}")


        #layout.addWidget(self.nameinput)
        #Nom,Téléphone,Catégorie,Email

        self.mouadlabels=QLabel(self)
        self.mouadlabels.setGeometry(120+50-20-10,40+55+10-10,400,35)
        self.mouadlabels.setText("Catégorie:")
        self.mouadlabels.setStyleSheet("""font: bold 15pt 'Comic Sans MS""")
        self.mouadlabels.setFont(QFont('Times', 11))
        
        self.mouadlabels1=QLabel(self)
        self.mouadlabels1.setGeometry(120+20-8,40+55+50,400,35)
        self.mouadlabels1.setText("Téléphone:")
        self.mouadlabels1.setStyleSheet("""font: bold 15pt 'Comic Sans MS""")
        self.mouadlabels1.setFont(QFont('Times', 11))

        self.mouadlabels2=QLabel(self)
        self.mouadlabels2.setGeometry(120+50-20-10+10,40+55+50+50-10+10,400,35)
        self.mouadlabels2.setText("Email:")
        self.mouadlabels2.setStyleSheet("""font: bold 15pt 'Comic Sans MS""")
        self.mouadlabels2.setFont(QFont('Times', 11))

        self.mouadlabels3=QLabel(self)
        self.mouadlabels3.setGeometry(120+50-20+10,40+10+5,100,35)
        self.mouadlabels3.setText("Nom:")
        self.mouadlabels3.setStyleSheet("""font: bold 15pt 'Comic Sans MS""")
        self.mouadlabels3.setFont(QFont('Times', 11))




        self.mouad1 = QLineEdit(self)
        self.mouad1.setGeometry(220,40+55+50,400,35)
        self.mouad1.setPlaceholderText("Téléphone.....")
        self.mouad1.setStyleSheet("QLineEdit"" {"
	        "box-shadow:inset 0px 1px 0px 0px #276873;"
	        "background:linear-gradient(to bottom, #C4F21A 5%, #DCFF9B  100%);"
	        "background-color:#C4F21A;"
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
            "}")
        self.mouad2 = QLineEdit(self)
        self.mouad2.setGeometry(220,40+55+50+50,400,35)
        self.mouad2.setPlaceholderText("Email.........")
        self.mouad2.setStyleSheet("QLineEdit"" {"
	        "box-shadow:inset 0px 1px 0px 0px #276873;"
	        "background:linear-gradient(to bottom, #C4F21A 5%, #DCFF9B  100%);"
	        "background-color:#C4F21A;"
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


        self.buthonAdd=QPushButton(self)
        #self.buthonAdd.setText("Add")
        self.buthonAdd.setGeometry(QtCore.QRect(10,10,120,300-30+10))
        self.buthonAdd.setStyleSheet("QPushButton {"
	        "box-shadow:inset 0px 1px 0px 0px #276873;"
	        "background:linear-gradient(to bottom, #C4F21A 5%, #DCFF9B  100%);"
	        "background-color:#C9FF65 ;"
	        "border:1px solid #29668f;"
	        "display:inline-block;"
            "qproperty-icon:url(add_sell.png);"
            "qproperty-iconSize: 200px 200px;"
	        "cursor:pointer;"
	        "color:#000000 ;"
	        "font-family:Arial;"
	        "font-size:15px;"
	        
	        "padding:6px 12px;"
	        "text-decoration:none;"
            "}"
            ".QPushButton:hover {"
	        "background:linear-gradient(to bottom, #DCFF9B  5%, #DCFF9B  100%);"
	        "background-color:#DCFF9B ;"
            "}"
            ".QPushButton:active {"
	        "position:relative;"
	        "top:1px;"
            "}"
            )

        self.buthonAdd1=QPushButton(self)
        self.buthonAdd1.setText("  Suprimer")
        self.buthonAdd1.setIconSize(QtCore.QSize(25,40))
        self.buthonAdd1.setGeometry(QtCore.QRect(120+40+30+50-20,300-30-20,100,30))
        self.buthonAdd1.setIcon(QtGui.QIcon("19N.png"))
        self.buthonAdd1.setToolTip("&lt;h1&gt;This Is Click Button&lt;h1&gt;")
        self.buthonAdd1.setStyleSheet("""QPushButton {


	        font-family:Arial;
            text-align: left;
	        font-size:14px;

qproperty-icon:url(19N.png);
qproperty-iconSize: 20px 20px;
}
            .QPushButton:hover {
	        background:linear-gradient(to bottom, #DCFF9B  5%, #DCFF9B  100%);
	        background-color:#DCFF9B ;"
            }
QPushButton:pressed {
background-color:#B1BAA2  ;
}""")
        self.buthonAdd1.clicked.connect(self.supprimer)
        self.buthonAdd2=QPushButton(self)
        self.buthonAdd2.setText(" Enregister")
        self.buthonAdd2.setIconSize(QtCore.QSize(25,40))
        self.buthonAdd2.setGeometry(QtCore.QRect(120+40+110+30+50+8,300-30-20,100,30))
        self.buthonAdd2.setIcon(QtGui.QIcon("19N.png"))
        self.buthonAdd2.setToolTip("&lt;h1&gt;This Is Click Button&lt;h1&gt;")
        self.buthonAdd2.setStyleSheet("""QPushButton {


	        font-family:Arial;
            text-align: left;
	        font-size:14px;

qproperty-icon:url(save.png);
qproperty-iconSize: 20px 20px;
}
            .QPushButton:hover {
	        background:linear-gradient(to bottom, #DCFF9B  5%, #DCFF9B  100%);
	        background-color:#DCFF9B ;"
            }
QPushButton:pressed {
background-color:#B1BAA2  ;
}""")
        self.buthonAdd2.clicked.connect(self.addclient)
        

        self.buthonAdd3=QPushButton(self)
        self.buthonAdd3.setText("  Exit")
        self.buthonAdd3.setIconSize(QtCore.QSize(25,40))
        self.buthonAdd3.setGeometry(QtCore.QRect(120+40+110+110+30+50+30,300-30-20,100,30))
        self.buthonAdd3.setIcon(QtGui.QIcon("19N.png"))
        self.buthonAdd3.setToolTip("&lt;h1&gt;This Is Click Button&lt;h1&gt;")
        self.buthonAdd3.setStyleSheet("""QPushButton {


	        font-family:Arial;
            text-align: left;
	        font-size:14px;

qproperty-icon:url(close.png);
qproperty-iconSize: 20px 20px;
}
            .QPushButton:hover {
	        background:linear-gradient(to bottom, #DCFF9B  5%, #DCFF9B  100%);
	        background-color:#DCFF9B ;"
            }
QPushButton:pressed {
background-color:#B1BAA2  ;
}""")
        self.buthonAdd3.clicked.connect(self.reject)




       
        self.mouad = db.connect(
        host="bgoayczsbsi8nmqt38xq-mysql.services.clever-cloud.com",
        user="udaetm9z9ar5dp5i",
        password="llulr86Scgsop7VNYjbZ",
        database="bgoayczsbsi8nmqt38xq"
        )
        mycursor = self.mouad.cursor()
        #mycursor.execute()
        #query = "SELECT * FROM Client"
        mycursor.execute("SELECT Catégoriee FROM Catégorie group by Catégoriee")
        result=mycursor.fetchall()
        print("###",result) 
        #mouad=tuple(result[0])
        #print(mouad[0])




        self.Catégorie = QComboBox(self)
        #self.seminput.addItem("1")
        for var in result:
            self.Catégorie.addItem(str(var[0]))

        self.Catégorie.setGeometry(220,40+55,400,35)
        
        #layout.addWidget(self.mobileinput)

        self.addressinput = QLineEdit()
        self.addressinput.setPlaceholderText("Address Email")
        self.addressinput.setGeometry(100,10+35+35,400,35)
        
        mycursor.close()

    def reject(self):
        QDialog.reject(self)

    def supprimer(self):
        self.mouad0.setText("")
        #self.Catégorie.itemText(self.Catégorie.currentIndex())
        self.mouad1.setText("")
        self.mouad2.setText("")
        

    def addclient(self):

        name = ""
        Catégorie=""
        mobile = ""
        address = ""

        name = self.mouad0.text()
        #branch = self.branchinput.itemText(self.branchinput.currentIndex())
        Catégorie = self.Catégorie.itemText(self.Catégorie.currentIndex())
        mobile = self.mouad1.text()
        address = self.mouad2.text()

        try:
            if name==""  or mobile=="" or address=="":
                QMessageBox.warning(QMessageBox(), 'Error', 'Could not add Client to the database remplire les cases correctement.')
               
                 
            else:
                self.mouad = db.connect(
                host="bgoayczsbsi8nmqt38xq-mysql.services.clever-cloud.com",
                user="udaetm9z9ar5dp5i",
                password="llulr86Scgsop7VNYjbZ",
                database="bgoayczsbsi8nmqt38xq"
                )
                mycursor = self.mouad.cursor()
                #mycursor.execute()
                query = "SELECT * FROM Client"
                #mycursor.execute("SELECT Catégorie FROM Client group by Catégorie")
                #result=mycursor.fetchall()
                sql="INSERT INTO Client (Nom,Téléphone,Catégorie,Email) VALUES (%s, %s,%s, %s)"
                val = (name, mobile,Catégorie,address)
                print("##############",val)
                mycursor.execute(sql, val)
                self.mouad.commit()
                mycursor.close()
            
                QMessageBox.information(QMessageBox(),'Successful','Student is added successfully to the database.')
            
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not add student to the database.')
            #msg = QtWidgets.QMessageBox.show(self,'CHAMP INVALID ! ','Vous été oublié des champs Vides !',QtWidgets.QMessageBox.Ok)
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = InsertDialog()
    ui.show()
    sys.exit(app.exec_())