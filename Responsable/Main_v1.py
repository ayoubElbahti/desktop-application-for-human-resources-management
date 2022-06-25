from PyQt5 import QtCore, QtGui, QtWidgets
from db_connect import mydb as db
from datetime import datetime
from PyQt5.uic import loadUi
from Calendrier import Get_Date_Fin
from Calendrier import GetNbrDimanche
from demandeEnvoyer import Ui_self_1
import Resources_rc
cheking = False
check_grp = False
grp_value_dict = {'normale':1,'équipe':2}
class Ui_Form(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color:#E2E2F4;")
        loadUi("dmd.ui",self)
         #self.Valider.clicked.connect(self.Valider_fct)
        self.radioButton_2.toggled.connect(self.Normal)
        self.radioButton.toggled.connect(self.Equipe)
        self.pushButton.clicked.connect(self.cc)
    def cc(self):
        self.Calendrier_widget.setVisible(True)
    def Calendrier(self):
        print('hhh')
        self.cal = QtWidgets.QCalendarWidget(self)
        self.cal.setGridVisible(True)
        self.cal.move(20, 20)
        self.cal.clicked.connect(self.showDate)
        self.date = self.cal.selectedDate()

    def showDate(self, date):
      self.lineEdit.setText(self.date.toString())
    def Normal(self):
        global check_grp,grp_value_dict
        check_grp = True
        self.grp_value = grp_value_dict[str(self.radioButton_2.text())]
    def Equipe(self):
        global check_grp
        check_grp = True
        self.grp_value = grp_value_dict[str(self.radioButton.text())]

    
    def setup(self):
        self.CSS = QtWidgets.QRadioButton("CSS")
        self.horizontalLayout.addWidget(self.CSS)
        self.CE = QtWidgets.QRadioButton("CE")
        self.horizontalLayout.addWidget(self.CE)
        self.CP = QtWidgets.QRadioButton("CP")
        self.horizontalLayout.addWidget(self.CP)
        self.CR = QtWidgets.QRadioButton("CR")
        self.horizontalLayout.addWidget(self.CR)

    def setup_Details(self):
        self.normal = QtWidgets.QRadioButton("normal")
        self.horizontalLayout_Details.addWidget(self.normal)
        self.equipe = QtWidgets.QRadioButton("équipe")
        self.horizontalLayout_Details.addWidget(self.equipe)
    def Initialiser(self):
        self.Num_Mat.setText('')
        self.Jours.setText('')
        self.setup()
        self.setup_Details()
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Form()
    ui.show()
    sys.exit(app.exec_())
