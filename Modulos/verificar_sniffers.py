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

cmd = 'ifconfig -a'
entrada, salida = os.popen4(cmd);
salida = salida.read();
if 'PROMISC' in salida:
        mensaje= 'interfaz_en_modo_promiscuo'
        tipo_alarma = 'sniffers'
        cmd = './generar_alarma.py ' + tipo_alarma + ' ' + mensaje
        os.system(cmd)

nombres_procesos = ['tcpdump', 'nload', 'iftop', 'iptraf', 'ethereal', 'wireshark']
for proceso in nombres_procesos:
        cmd = 'ps -e | grep '+ proceso
        entrada, salida = os.popen4(cmd)
        salida = salida.read()
        if salida:
                n = salida.split()
                pid = int(n[0])
                os.kill(pid, signal.SIGTERM)

                mensaje = 'proceso_activo:' + proceso
                tipo_alarma = 'sniffers'
                cmd = './generar_alarma.py ' + tipo_alarma + ' ' + mensaje
                os.system(cmd)

archivo.close()
