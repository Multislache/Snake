#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 17:23:14 2022

@author: atsankova
"""
from microbit import *
from File import *
from SNAKE import *
import random
class Pomme:
    def __init__(self, serpent):
        self.coordonnees = (random.randint(0,4),random.randint(0,4))
        while serpent.corps.appartient(self.coordonnees):
            self.coordonnees = (random.randint(0,4),random.randint(0,4))
        
class Amanger(File):
    def affichage(self):
        for i in range(len(self)):
            set_pixel(Pomme.coordonnes[0], Pomme.coordonnes[1], intensite)
        
class Digestion(File):
    def enfiler_1(c):
        p=Cellule(c)
        p.premier.suivante = serpent.premier