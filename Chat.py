#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 16:34:58 2023

@author: jwen
"""
from threading import Thread
import socket as soc
    
    
def communication(client,client_info):
    donnees = ''
    while donnees!='fin':
        donnees = client.recv(1000)
        print(client_info, ", message : ", donnees.decode())
        client.send('Reçu. Fin.'.encode())
        # Initialisation
serveur = soc.socket(soc.AF_INET, soc.SOCK_STREAM)  # Création du socket serveur
serveur.bind(('0.0.0.0', 50000)) # Association à une adresse IP et un port
serveur.listen() # Création d'une file d'attente de connexion
while True:
    (client, client_info) = serveur.accept()
    client.send('connecté sur le serveur'.encode())
    t1 = Thread(target = communication, args=[client,client_info])
    t1.start()
    # Fermeture
client.close()