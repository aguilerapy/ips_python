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

#Recorremos los archivos de la carpeta /temp
for dir, archivos in os.walk('/tmp'): 
	for name in archivos: 
		directorio = os.path.join(dir, name);

		ext_peligrosas = ['.sh','.exe','.bash','.zsh', '.py', '.csh', '.pl','.bat', '.ksh', '.rb','.java'];
		
		#Verificamos que el archivo no sea potencialmente peligroso
		for ext in ext_peligrosas: 
			if(directorio.endswith(ext)): 
				os.remove(directorio)

				mensaje = 'extension_peligrosa_tmp_archivo:' + directorio;
				tipo_alarma = 'tmp_ext'
				cmd = './generar_alarma.py ' + tipo_alarma + ' ' + mensaje
                		os.system(cmd)

		#Es posibole que el archivo no pueda ser abierto por estar bloqueado
		try:
			archivo = file(directorio, 'r'); 
		except IOError:
			sys.exc_clear(); 
			continue;

		linea = archivo.readline(); 
		if('#!' in linea): 
			os.remove(directorio)

			#Generamos la alarma de deteccion
			mensaje = 'archivo:' + directorio + '_podria_ser_un_script_peligroso';
			tipo_alarma = 'tmp_script'
			cmd = './generar_alarma.py ' + tipo_alarma + ' ' + mensaje
                	os.system(cmd)

		archivo.close();




