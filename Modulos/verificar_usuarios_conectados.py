#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2;
import os;
import string;
import sys;
import commands
import re;
import datetime;
import md5;

#Conectamos a la base de datos
conn = psycopg2.connect("dbname=ips_db user=ips_user password=12345 host=localhost")
cur = conn.cursor()

#Comando que nos muestra quienes estan conectados
entrada, salida = os.popen4('who')
salida = salida.read()
usuarios_who =  salida.splitlines()

#Verificamos cada usuario
for usuarios in usuarios_who:
        datos = usuarios.split()
        if (len(datos)== 4):
                datos.append('local')

        cur.execute("SELECT origen FROM verificar_acceso WHERE usuario_ips LIKE  %s", (datos[0],) )
        resultados = cur.fetchall()
        datos[4] = datos[4].replace("(", "")
        datos[4] = datos[4].replace(")", "")

	#Seleccionamos el usuario traido d ela base de datos y comparamos con el conectado
        for item in resultados:
		#Si son diferentes, genera la alarma
                if datos[4] != item[0]:
                        mensaje = 'origen_invalido_' + datos[0] + '_' + datos[4]
                        tipo_alarma = 'usuario_invalido'
                        cmd = './generar_alarma.py ' + tipo_alarma + ' ' + mensaje
                        os.system(cmd)
		#Si no existe, genera la alarma
                if resultados == []:
                        mensaje = 'usuario_' + datos[0] + '_desconocido'
                        tipo_alarma = 'usuario_desconocido'
                        cmd = './generar_alarma.py ' + tipo_alarma + ' ' + mensaje
                        os.system(cmd)

#Cerramos la base de datos
conn.commit()
cur.close()
conn.close()