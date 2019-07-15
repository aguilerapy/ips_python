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

#bloqueo
iptables -A INPUT -s IP-ADDRESS -j DROP

#desbloqueo
iptables -D INPUT -s 10.10.10.10 -j DROP