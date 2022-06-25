import os
import smtplib
import imghdr
from email.message import EmailMessage
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

class Emails:
    def __init__(self,email,motDePasse,Recepteur,text):
        i = 1
        j = 0
        m = []
        try:
            m.append(Recepteur)
            print('email envoyer to : ',m)
            for mail in m:
                msg = MIMEMultipart()
                msg['Subject'] = 'Demande de congé'
                msg['From'] = email
                msg['To'] = mail
                msg.attach(MIMEText(text))
                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                    smtp.login(email,motDePasse)
                    smtp.send_message(msg)
                    print('smtp envoye')
                    print('Email successfilly sent to :  ', mail)
                    j += 1
                    print('j = ',j)
            print('Emails : successfilly sent !!')
        except:
            print('Failed to sent email !!')
