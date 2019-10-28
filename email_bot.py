#In cmd line run python emailmeme.py
import os, sys, mimetypes, time, random

from smtplib import SMTP as SMTP
from argparse import ArgumentParser

from email.message import Message
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# msg['Subject'] = 'F' #put subject inside quote

#ankleman1999@gmail.com



class Email():
    def __init__(self, sender, reciever, subject, body, img, iterations):
        self.sender = sender
        self.msg = MIMEMultipart()
        self.msg['From'] = sender #put your email inside quote (you have to authorize python gmail api and allow less secure apps to access your data)
        self.msg['To'] = reciever #put recipient's email inside quote
        self.msg['Subject'] = subject
        if body != '':
            self.msg.attach(MIMEText(body))
        if img != '':
            with open(img, 'rb') as fp: #put image file inside the quotes: image must be in the folder where this file is
                attatchment = MIMEImage(fp.read())
                self.msg.attach(attatchment)
        self.iterations = iterations

    def send(self):
        for x in range(self.iterations): #put number of emails to send inside parens
            server = SMTP(host= 'smtp.gmail.com', port = 587)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(self.sender,'yeeterson') #put your email in first quote and password inside other
            server.send_message(self.msg)
            print("send " + str(x))
        server.close()
        return "Email sent " + str(self.iterations)
