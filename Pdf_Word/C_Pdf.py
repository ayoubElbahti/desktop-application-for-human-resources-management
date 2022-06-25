from fpdf import FPDF

# create FPDF object
# Layout ('P','L')
# Unit ('mm', 'cm', 'in')
# format ('A3', 'A4' (default), 'A5', 'Letter', 'Legal', (100,150))
pdf = FPDF('P', 'mm', 'Letter')

# Add a page
pdf.add_page()

# specify font
# fonts ('times', 'courier', 'helvetica', 'symbol', 'zpfdingbats')
# 'B' (bold), 'U' (underline), 'I' (italics), '' (regular), combination (i.e., ('BU'))
pdf.set_font('helvetica', 'BIU', 25)
#pdf.set_text_color(220,50,50)
# Add text
# w = width
# h = height
# txt = your text
# ln (0 False; 1 True - move cursor down to next line)
# border (0 False; 1 True - add border around cell)
pdf.cell(0, 10, 'Attestation de Congé', ln=True,align='C')
pdf.set_font('helvetica', '', 12)
pdf.cell(80, 10, 'Nom complet : ')

pdf.output('pdf_1.pdf')
