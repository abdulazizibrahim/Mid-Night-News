from typing import Tuple
from fpdf import FPDF


title = 'The Midnight News'

class PDF(FPDF):
    def header(self):
        # logo
        self.image('news.jpg',10,8, 25)
        #font
        self.set_font('helvetica', 'B', 20)
       
        title_w = self.get_string_width(title) + 6
        doc_w = self.w
        self.set_x((doc_w-title_w)/2)
        #colors of the frame, background and text.
        self.set_draw_color(0,80,180) # border = blue
        self.set_fill_color(230,230,0) #background ==> yellow
        self.set_text_color(220,50,50) # text ==> red

        #Thickness of frame
        self.set_line_width(1)

        # title
        self.cell(title_w,10, title, border=1, ln=True, align='C', fill=1)
        
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


pdf.output('pdf_3.pdf')

