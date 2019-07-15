#!/usr/bin/python
# -*- coding: utf-8 -*-

import string;
import sys;
import commands
import re;
import datetime;
import os

cmd = 'crontab -l'
entrada, salida = os.popen4(cmd)
salida = salida.read()

if  salida :
        if not (('hids_ips_main.py' in salida) and ('ips' in salida)):
                mensaje= 'archivo_ejecutandose_como_cron:' + salida
                tipo_alarma = 'cron_root'
                cmd = './generar_alarma.py ' + tipo_alarma + ' ' + mensaje
                os.system(cmd)

cmd= 'ls /var/spool/cron'
entrada, salida = os.popen4(cmd);
salida = salida.read();
usuario = salida.split()
for i in range(0,len(usuario)):
        if not ('root' in usuario[i]):
                mensaje= 'usuario:'+ usuario[i]+'_posee_crontab'
                tipo_alarma = 'cron_usuarios'
                cmd = './generar_alarma.py ' + tipo_alarma + ' ' + mensaje
                os.system(cmd)