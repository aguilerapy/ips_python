#!/usr/bin/python
# -*- coding: utf-8 -*-

import os;
import sys;
import re;
import string;
import datetime;
import smtplib;
import socket;

#Recibir parametros y preparar log
tipoadvertencia = sys.argv[1]
mensaje = sys.argv[2]
directorio = '/var/log/hids/alarmas_hids.log'
x = datetime.datetime.now()
s = str(x.day)+'/'+str(x.month)+'/'+str(x.year)+ ' :: ' +tipoadvertencia+  ' :: ' +mensaje+'\n'

#Escribir en archivo log
archivo = open(directorio, 'a')
archivo.write(s)
archivo.close()

#Enviar correo a admin
cmd = './enviar_mail.py ' + mensaje
os.system(cmd)