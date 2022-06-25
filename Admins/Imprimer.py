from PyQt5.uic import loadUi
from PyQt5 import QtWidgets,QtCore,QtGui
import Resources_rc
from C_Pdf import create_pdf
from tkinter import filedialog
from tkinter import *
from datetime import datetime
class Imprimer_class(QtWidgets.QDialog):
    def __init__(self,List_data):
        Begindate = datetime.today()
        cc = Begindate.strftime("%Y-%m-%d")
        self.name_dossier = cc
        super().__init__()
        loadUi("Imprimer.ui",self)
        self.pushButton_2.setIcon(QtGui.QIcon(":/Icons/Icons/word_icon.png"))
        self.pushButton_2.setStyleSheet("QPushButton {"
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

                             "background-color : #EFF7BE ;"
                             "}"
                             )
        self.pushButton.setIcon(QtGui.QIcon(":/Icons/Icons/pdf_icon.png"))
        self.pushButton.setStyleSheet("QPushButton {"
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

                             "background-color : #EFF7BE ;"
                             "}"
                             )
        self.List_Info = List_data
        self.pushButton.clicked.connect(self.Ouvrir_Pdf)
        self.pushButton_2.clicked.connect(self.Ouvrir_Word)
        self.show()
    def Ouvrir_Pdf(self):
        self.chemain = self.SaveDialog()
        print('chemain = ',self.chemain)
        print('pdf creating ...')
        self.pdf_doc = create_pdf('P', 'mm', 'Letter')
        print('la taille = ',len(self.List_Info))
        if len(self.List_Info) == 7:
            self.pdf_doc.create_instance(self.List_Info)
            chemain_kaml = f"""{self.chemain}/demande_De_Congé_{self.List_Info[0]}_{self.name_dossier}.pdf"""
        else:
            self.pdf_doc.create_instance_pointage(self.List_Info)
            chemain_kaml = f"""{self.chemain}/Bilan de Travail_{self.List_Info[0]}_{self.name_dossier}.pdf"""
        print(chemain_kaml)
        self.pdf_doc.output(str(chemain_kaml))
        if self.pushButton_2.isChecked():
            print('word button selected')
        else:
            self.close()
    def Ouvrir_Word(self):
        import os
        self.Ouvrir_Pdf()
        if len(self.List_Info) == 7:
            self.pdf_doc.convertToDocx(f"""{self.chemain}/demande_De_Congé_{self.List_Info[0]}_{self.name_dossier}""")
            os.remove(f"""{self.chemain}/demande_De_Congé_{self.List_Info[0]}_{self.name_dossier}.pdf""")
        else:
            self.pdf_doc.convertToDocx(f"""{self.chemain}/Bilan de Travail_{self.List_Info[0]}_{self.name_dossier}""")
            os.remove(f"""{self.chemain}/Bilan de Travail_{self.List_Info[0]}_{self.name_dossier}.pdf""")
        self.close()
    def SaveDialog(self):
        Tk().withdraw()
        return (str(filedialog.askdirectory()))
