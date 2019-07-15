#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2;
import string;
import sys;
import commands
import re;
import datetime;
import md5;
import os;
from os import listdir


#Nos conectamos a la base de datos
conn = psycopg2.connect("dbname=ips_db user=ips_user password=12345 host=localhost")
cur = conn.cursor()

#Verificamos binarios
directorio_binarios = ['/bin','/sbin','/usr/bin','/usr/sbin']
for directorio in directorio_binarios:
        for archivo in listdir(directorio):
                dir = directorio+'/'+archivo
                cod = hashlib.md5(open(dir).read()).hexdigest()
                sum = str(cod)
		
		#Seleccionamos de la base de datos el codigo correspondiente
                cur.execute("SELECT checksum FROM archivo WHERE directorio like %s", (dir,) )
                check = cur.fetchone()

                if (sum != check[0]):
                        mensaje= 'archivo_'+ dir + '_fue_modificado'
                        tipo_alarma ='binario_modificado'
                        cmd = './generar_alarma.py ' + tipo_alarma + ' ' + mensaje
                        os.system(cmd)

#Verificamos passwd y shadow
archivos_etc = ['/etc/passwd','/etc/shadow']
for archivo in archivos_etc:
        cod = hashlib.md5(open(archivo).read()).hexdigest()
        sum = str(cod)

	#Seleccionamos de la base de datos el codigo correspondiente
        cur.execute("SELECT checksum FROM archivo WHERE  directorio like %s", (archivo,) )
        check = cur.fetchone()

	#Si el numero guardado no coincide, genera la alarma
        if (sum != check[0]):
                mensaje = 'archivo_'+ archivo + '_fue_modificado'
                tipo_alarma ='archivo_etc_modificado'
                cmd = './generar_alarma.py ' + tipo_alarma + ' ' + mensaje
                os.system(cmd)

#Desconectamos de la base de datos
conn.commit()
cur.close()
conn.close()