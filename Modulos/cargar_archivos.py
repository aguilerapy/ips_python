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

#Conectamos a la base de datos
conn = psycopg2.connect("dbname=ips_db user=ips_user password=12345 host=localhost")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS archivo")
cur.execute("CREATE TABLE archivo (id serial PRIMARY KEY, directorio VARCHAR(100), checksum varchar(32)) ")

#Cargamos los binarios
directorio_binarios = ['/bin','/sbin','/usr/bin','/usr/sbin']
for directorio in directorio_binarios:
	for archivo in listdir(directorio):
		dir = directorio+'/'+ archivo
		cod = hashlib.md5(open(dir).read())
		sum = str(cod.hexdigest())
		cur.execute("INSERT INTO archivo (directorio, checksum) VALUES (%s, %s)", (dir, sum))

#Cargamos passwd y shadow
archivos_etc = ['/etc/passwd','/etc/shadow']
for archivo in archivos_etc:
	cod = hashlib.md5(open(directorio).read())
	sum = str(cod.hexdigest())
	cur.execute("INSERT INTO archivo (directorio, checksum) VALUES (%s, %s)", (directorio, sum))	

#Desconectamos de la base de datos
conn.commit()
cur.close()
conn.close()