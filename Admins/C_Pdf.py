from fpdf import FPDF
import os
from pdf2docx import Converter
from datetime import datetime
class create_pdf(FPDF):
    def create_instance_pointage(self,List_data):
        Begindate = datetime.today()
        cc = Begindate.strftime("%Y-%m-%d")
        self.name_dossier = cc
        print(List_data)
        self.add_page()
        self.image('logo.png', 70, 8, 80)
        self.ln(30)
        self.set_font('helvetica', 'BIU', 25)
        self.cell(0, 10, 'Bilan de Travail ', ln=True,align='C')
        self.set_font('helvetica', '', 12)
        self.ln(25)
        self.cell(80,10,f"""Nom Complet : {List_data[0]}""",ln=1)
        self.cell(80,10,f"""Date : {self.name_dossier}""",ln=1)
        self.cell(80,10,f"""Directeur : {List_data[2]}""",ln=1)
        self.cell(80,10,f"""Heures normales : {List_data[3]} H""",ln=1)
        self.cell(80,10,f"""Heures considérées : {List_data[4]} H""",ln=1)
        self.cell(80,10,f"""Heures de retard  : {List_data[5]} ( calculer par minutes )""",ln=1)
        self.cell(80,10,f"""Heures d'absence  : {List_data[6]} H""",ln=1)
        self.cell(80,10,f"""Heures supplémentaires  : {List_data[7]} H""",ln=1)
    def create_instance(self,List_data):
        Begindate = datetime.today()
        cc = Begindate.strftime("%Y-%m-%d")
        self.name_dossier = cc
        print(List_data)
        self.add_page()
        self.image('logo.png', 70, 8, 80)
        self.ln(30)
        self.set_font('helvetica', 'BIU', 25)
        self.cell(0, 10, 'Attestation de Congé', ln=True,align='C')
        self.set_font('helvetica', '', 12)
        self.ln(25)
        self.cell(80,10,f"""Nom Complet : {List_data[0]}""",ln=1)
        self.cell(80,10,f"""Matricule : {List_data[1]}""",ln=1)
        self.cell(80,10,f"""Date : {self.name_dossier}""",ln=1)
        self.cell(80,10,f"""Responsable RH : {List_data[2]}""",ln=1)
        self.cell(80,10,f"""Responsable Hiérarchique : {List_data[2]}""",ln=1)
        self.cell(80,10,f"""Direction : {List_data[3]}""",ln=1)
        self.cell(80,10,f"""Congé demandé : {List_data[4]}""",ln=1)
        self.cell(80,10,f"""Du : {List_data[5]}""",ln=1)
        self.cell(80,10,f"""Jusqu\'au : {List_data[6]}""",ln=1)
        #self.output('C:/Users/ayoub/Desktop/Stage/tbi.pdf'); 
        #os.remove('ayoub_demander.pdf')
    def convertToDocx(self,directory_file):
        self.output_file_info = directory_file
        pdf_file = f"""{self.output_file_info}.pdf"""
        word_file = f"""{self.output_file_info}.docx"""
        cv = Converter(pdf_file)
        cv.convert(word_file,start=0,end=None)