#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2;
import string;
import sys;
import commands
import re;
import datetime;
import md5;
import smtplib;
import socket;
import hashlib;
from os import listdir

#Nos conectamos a la base de datos
conn = psycopg2.connect("dbname=ips_db user=ips_user password=12345 host=localhost")

cur = conn.cursor()

for i in range(1, 11):
        bandera = 1
        #Seleccionamos la bandera de la base de datos
	cur.execute("SELECT bandera FROM banderas WHERE id_bandera = %s", (i,))
        resultados = cur.fetchall()
        for n in resultados:
                if n == 1 or n == 0:
                        bandera = n
	
	#Verificamos si la bandera esta activada y ejecutamos su sensor
        if bandera == 1:
                if(i==1):
                        os.system('./verificar_accesos.py')

                elif(i==2):
                        os.system('./verificar_binarios.py')

                elif(i==3):
                        os.system('./verificar_colamails.py')

                elif(i==4):
                        os.system('./verificar_cron.py')

                elif(i==5):
                        os.system('./verificar_ddos.py')

                elif(i==6):
                        os.system('./verificar_logs.py')

                elif(i==7):
                        os.system('./verificar_procesos.py')

                elif(i==8):
                        os.system('./verificar_sniffers.py')

                elif(i==9):
                        os.system('./verificar_tmp.py')

                elif(i==10):
                        os.system('./verificar_usuarios_conectados.py')

#Mover al servidor web las alarmas
os.system('unalias cp')
cmd = 'cp /var/log/hids/alarmas_hids.log /var/www/html/alarmas_hids.log')
os.system(cmd)
cmd = 'cp /var/log/hids/alarmas_hids.log /var/www/html/prevencion_hids.log')
os.system(cmd)


conn.commit()
cur.close()
conn.close()