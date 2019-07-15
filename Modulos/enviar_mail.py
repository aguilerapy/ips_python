#!/usr/bin/python
# -*- coding: utf-8 -*-

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import sys


#Se crea el objeto mensaje
msg = MIMEMultipart()

message = sys.argv[1]

#Configuracion de los parametros del mail
password = "s0cytUca."
msg['From'] = "tp.ips.mail@gmail.com"
msg['To'] = "amaguilera96@gmail.com"
msg['Subject'] = "Alarma IPS!"

#Agregar el mensaje
msg.attach(MIMEText(message, 'plain'))

#Crear el servidor
server = smtplib.SMTP('smtp.gmail.com: 587')

server.starttls()

#Credenciales del correo origen
server.login(msg['From'], password)


#Enviar el mensaje por el servidor creado
server.sendmail(msg['From'], msg['To'], msg.as_string())

server.quit()
