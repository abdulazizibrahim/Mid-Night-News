from typing import Tuple
from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # logo
        self.image('news.jpg',10,8, 25)
        #font
        self.set_font('helvetica', 'B', 20)
        # padding
        #self.cell(80)
        # title
        self.cell(0,10, "The Midnight News", border=0, ln=True, align='C')
        # line break
        self.ln(20)

    def footer(self):
        #set position of the footer
        self.set_y(-15)
        #set font
        self.set_font('helvetica', 'I', 10)
        #page number
        self.cell(0, 10, f'Page {self.page_no()}/nb', align='C')










# create FPDF object
# Layout(P,L)
# Unit('mm', 'cm','in') 
# format('A3', 'A4'(default), 'A5', 'Letter', 'Legal', (100,150))
pdf = PDF('P', 'mm','Letter')

# get total page numbers
pdf.alias_nb_pages(alias='nb')

# Add a page
pdf.add_page()

# set page break
pdf.set_auto_page_break(auto=True, margin=15)

# specify font
# fonts ('times', 'couries', 'helvetica','symbol','zpfdingbats')
# 'B' (bold), 'U' (underline), 'I' (italics), '' (regular), combination ('BU')

pdf.set_font('helvetica', '', 16)


# Add text
# w = width
# h = height
# ln(0 False; 1 True - move curson to the next line)
# border (0 False ; 1 True - add border around cell)
#pdf.cell(40,10, "hello world", ln=True, border=False)


for i in range(0, 40):
    pdf.cell(0,10, f'This is line {i}', ln=True)


pdf.output('pdf_1.pdf')

