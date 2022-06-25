from fpdf import FPDF
from docx2pdf import __convert
class PDF(FPDF):
    def header(self):
        # Logo
        self.image('logo.png', 70, 8, 80)
        self.ln(30)
        # font
        self.set_font('helvetica', 'B', 30)
        # Padding
        self.cell(80)
        # Title
        self.cell(30, 10, 'Attestation de congé ',ln=1, align='C')
        # Line break
        self.ln(20)
        self.set_font('helvetica', 'I', 18)
        pdf.cell(100, 20, 'Nom complet : ',ln=1)
        pdf.cell(100, 20, 'Responsable : ',ln=1)
        pdf.cell(100, 20, 'Jours : ',ln=1)
    # Page footer

# Create a PDF object
pdf = PDF('P', 'mm', 'Letter')
#Add Page
pdf.add_page()
# specify font
pdf.set_font('helvetica', 'BIU', 16)

pdf.set_font('times', '', 12)


pdf.output("C:\\Users\\ayoub\\Desktop\\Stages_SFE\\file.pdf")
