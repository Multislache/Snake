#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#from microbit import *
import Cellule as fl
import Serpent as sp
import random
class Pomme:
    def __ini__(self):
        self.coordonnees = (random.randint(0,4),random.randint(0,4))
        while sp.corps.appartient(self.coordonnees):
            self.coordonnees = (random.randint(0,4),random.randint(0,4))
        
#class Amanger:
#    def __init__(self):
#        self.amanger = 
        
    