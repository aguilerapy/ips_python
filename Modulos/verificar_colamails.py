#!/usr/bin/python
# -*- coding: utf-8 -*-

import string;
import sys;
import commands
import re;
import datetime;
import os

def tam_colamail():
        cmd = 'mailq | tail -n1'
        entrada, salida = os.popen4(cmd)
        salida = salida.read()
        salida = salida.split(" ")
        tam = salida[2]
        tam = int(tam)
        return tam

def ver_colamail():
        tam_colamax = 100

        tam_cola = tam_colamail()
        if(tam_cola < 0):
                return -1;

        if(tam_cola > tam_colamax):
                print tam_colamax
                print tam_cola

		#Alarma de deteccion
                mensaje = 'Tamaño_cola_superado_es_de_' + str(tam_cola)
                tipo_alarma = 'cola_mail';
                cmd = './generar_alarma.py ' + tipo_alarma + ' ' + mensaje
                os.system(cmd)
		
		#Ver quien esta validando para enviar correo
		cmd = 'tail -f /usr/local/psa/var/log/maillog | grep LOGIN'
        	entrada, salida = os.popen4(cmd)
        	salida = salida.read()
        	usuario = salida.split(" ")

		#Verificar si es usuario local o no
		conn = psycopg2.connect("dbname=ips_db user=ips_user password=12345 host=localhost")
		cur = conn.cursor()
		cur.execute("SELECT origen FROM verificar_acceso WHERE usuario_ips LIKE  %s", (datos[0],) )
       		resultados = cur.fetchall()
		if usuario[0] != resultados[0]:
			#Usuario extraño
			#Bloqueo en /etc/mail/access
			nueva_linea = usuario[0] + '         	REJECT'
			directorio = '/var/log/hids/prevencion_hids.log'
			archivo = open(directorio, 'a')
			archivo.write(nueva_linea)
			archivo.close()

			#Alarma de prevencion
                	mensaje = 'usuario:' + usuario[0] + '_bloqueado_por_spam' 
                	tipo_alarma = 'usuario_bloqueado'
                	cmd = './generar_prevencion.py ' + tipo_alarma + ' ' + mensaje
                	os.system(cmd)

		else:
			#Usuario local
			#Generar contraseña aleatoria
			cmd = 'date +%s | sha256sum | base64 | head -c 32'
			entrada, salida = os.popen4(cmd)
			salida = salida.read()
        		pass = salida.split(" ")
			cmd = 'date +%s | sha256sum | base64 | head -c 32'
			os.system(cmd)
			cmd = 'sudo passwd ' + usuario[0]'
			os.system(cmd)
			os.system(pass)
			os.system(pass)
			
			#Alarma de prevencion
                	mensaje = 'usuario:' + usuario[0] + '_contraseña_cambiada' 
                	tipo_alarma = 'usuario_cambiado'
               	 	cmd = './generar_prevencion.py ' + tipo_alarma + ' ' + mensaje
               	 	os.system(cmd)
			

ver_colamail()
