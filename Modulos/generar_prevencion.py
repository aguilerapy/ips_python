#!/usr/bin/python
# -*- coding: utf-8 -*-

import os;
import sys;
import re;
import string;
import datetime;
import smtplib;
import socket;

tipoadvertencia = sys.argv[1]
mensaje = sys.argv[2]
directorio = '/var/log/hids/prevencion_hids.log'
x = datetime.datetime.now()
s = str(x.day)+'/'+str(x.month)+'/'+str(x.year)+ ' :: ' +tipoadvertencia+  ' :: ' +mensaje+'\n'
archivo = open(directorio, 'a')
archivo.write(s)
archivo.close()