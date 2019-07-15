#!/usr/bin/python
# -*- coding: utf-8 -*-

import string;
import sys;
import commands
import re;
import datetime;
import md5;
import os;
import signal;
from os import listdir

#Comando que nos trae los procesos mas grandes en memoria
cmd = 'ps axo %mem,pid,euser,cmd | sort -nr | head -n 10'; 
entradaStatus, salidaStatus = os.popen4(cmd); 
salidaStatus = salidaStatus.read(); 
procesos=salidaStatus.splitlines()

#Asignamos un max por uso de memoria
consumo_max = 50

#Verificamos cada proceso
for proceso in procesos:
	datosProceso = proceso.split() 
	porcentaje = datosProceso[0].split('.') 
	
	#Si el proceso es mas grande que el establecido, se elimina
	if (int(porcentaje[0]) >= consumo_max):

		pid = int (datosProceso[1])
		os.kill(pid, signal.SIGTERM) 
	
		#Generamos las alarmas de deteccionj y prevencion
		mensaje = 'proceso:'+ datosProceso[3] + '_del_usuario:'+ datosProceso[2]+ '_tiene_consumo_elevado_de_mem:' + datosProceso[0]
		tipo_alarma = 'memoria_elevada'
		cmd = './generar_alarma.py ' + tipo_alarma + ' ' + mensaje
                os.system(cmd)

		mensaje = 'proceso:'+ datosProceso[3] + '_del_usuario:'+ datosProceso[2]+ '_eliminado_por_consumo_elevado_de_mem:' + datosProceso[0]
		tipo_alarma = 'memoria_elevada'
		cmd = './generar_prevencion.py ' + tipo_alarma + ' ' + mensaje
                os.system(cmd)