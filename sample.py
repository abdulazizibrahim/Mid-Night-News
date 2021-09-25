from newsapi import NewsApiClient, const
from fpdf import FPDF
from PIL import Image
import requests

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
 

title = "The Midnight News"

class PDF(FPDF):
    def header(self):
        # logo
        self.image('news.jpg',10,8, 25)
        #font
        self.set_font('helvetica', 'B', 20)
        
        doc_w = self.w
        
        self.set_x((doc_w-self.get_string_width(title)+6)/2)
        # padding
        self.set_draw_color(0,80,180) # border = blue
        self.set_fill_color(230,230,0) #background ==> yellow
        self.set_text_color(220,50,50) # text ==> red

        #Thickness of frame
        self.set_line_width(1)

        # title
        self.cell(self.get_string_width(title)+6,10,title, border=1, ln=True, align='C', fill=1)
        # line break
        self.ln(30)

    def footer(self):
        #set position of the footer
        self.set_y(-15)
        #set font
        self.set_font('helvetica', 'I', 10)
        #page number
        self.cell(0, 10, f'Page {self.page_no()} / nb', align='C')
    
    def article_title(self, name):
        self.set_font('helvetica','BI',18)

        self.set_fill_color(200,220,255)

        self.multi_cell(0,8, name, ln=1, fill=1,align='C')

        self.ln(10)




class news:
    def __init__(self) -> None:
        pass

    def get_news(self):
        # Init
        newsapi = NewsApiClient(api_key='key')

        #sources = newsapi.get_sourcesa)llklkjjliljsjlssadkisaiioaj
        top_headlines = newsapi.get_everything(sources='bbc-news')
        articles = top_headlines['articles']

        return articles

        
    def get_content(self, articles):
        contents = []
        for stuff in articles:
            conts = stuff['content']
            contents.append(conts[:190])
        return contents

    def get_titles(self, articles):
        titles = []
        for stuff in articles:
            conts = stuff['title']
            titles.append(conts)
        return titles
    
    def get_description(self, articles):
        desc = []
        for stuff in articles:
            conts = stuff['description']
            desc.append(conts)
        return desc

    def get_image(self,articles):
        images = []
        for stuff in articles:
            conts = stuff['urlToImage']
            images.append(conts)
        return images

    def get_date(self,articles):
        date = []
        for stuff in articles:
            conts = stuff['publishedAt']
            date.append(conts)
        return date
    
    def get_source(self,articles):
        source = []
        for stuff in articles:
            const = stuff['source']
            source.append(const['name'])
        return source

    def send_news(self,recv, file):
        body = 'Dear Subscriber,\n\nPlease find your daily dose of mid-night news. \n\nRegards,\n The Midnight News'
        # put your email here
        sender = 'news@gmail.com'
        # get the password in the gmail (manage your google account, click on the avatar on the right)
        # then go to security (right) and app password (center)
        # insert the password and then choose mail and this computer and then generate
        # copy the password generated here
        password = '--'
        # put the email of the receiver here
        receiver = recv

        #Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender
        message['To'] = receiver
        message['Subject'] = 'The Midnight News'

        message.attach(MIMEText(body, 'plain'))

        pdfname = file

        # open the file in bynary
        binary_pdf = open(pdfname, 'rb')

        payload = MIMEBase('application', 'octate-stream', Name=pdfname)
        # payload = MIMEBase('application', 'pdf', Name=pdfname)
        payload.set_payload((binary_pdf).read())

        # enconding the binary into base64
        encoders.encode_base64(payload)

        # add header with pdf name
        payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
        message.attach(payload)

        #use gmail with port
        session = smtplib.SMTP('smtp.gmail.com', 587)

        #enable security
        session.starttls()

        #login with mail_id and password
        session.login(sender, password)

        text = message.as_string()
        session.sendmail(sender, receiver, text)
        session.quit()
        print('Mail Sent')
        
    def generate_PDF(self, contents):

        pdf = PDF('P', 'mm', 'Letter')
        pdf.alias_nb_pages(alias='nb')
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)
        

        articles = self.get_news()
        images = self.get_image(articles)
        date = self.get_date(articles)
        desc = self.get_description(articles)
        title = self.get_titles(articles)
        contents = self.get_content(articles)
        source = self.get_source(articles)

        for a in desc:
            print(a, "\n")
        for i in range(len(articles)):
            #pdf.set_font('helvetica', 'BI', 18)
            #pdf.multi_cell(0,10, title[i], ln=True, align='C')
            #pdf.ln(10)
            pdf.article_title(title[i])
            pdf.set_font('times', '', 14)
            pdf.cell(0,0, f'Source : {source[i]}', ln=True)
            pdf.ln(5)
            pdf.cell(0,0, f'Dated : {date[i][:10]}', ln=True)
            pdf.ln(5)
            im = Image.open(requests.get(images[i], stream=True).raw)
            #im.resize((10,10))
            x = pdf.get_x()
            y = pdf.get_y()
            pdf.image(im,8,y+5,200)
            pdf.set_y(y+100)
            pdf.ln(30)
            pdf.multi_cell(0,5, str(desc[i]))
            pdf.ln(5)
            pdf.multi_cell(0,5, contents[i] +"...",ln=1)
            y = pdf.get_y()
            brk = 270 - y
            pdf.ln(brk)
            


        pdf.output('sample.pdf')
        
if __name__ =="__main__":
    obj = news()
   # obj.generate_PDF(None)
    obj.send_news('p176143@nu.edu.pk','sample.pdf')
