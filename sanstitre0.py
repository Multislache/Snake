#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 13:48:31 2023

@author: jwen
"""

import socket as soc
client = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
client.connect(('192.168.1.1', 50000))
msg = client.recv(1000)
# Création du socket serveur
# Demande de connexion au serveur
# réception de la confirmation de connexion
print(msg.decode())
# Communication
client.send('coucou'.encode())
acc_rcpt = client.recv(1000)
print(acc_rcpt.decode())
# Fermeture
client.close()