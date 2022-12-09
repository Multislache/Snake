#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#from microbit import *
import Cellule as fl
class Serpent():
    def __init__(self):
        self.corps = fl.File()
        self.corps.enfile((0,0))
        self.corps.enfile((0,1))
        self.direction = (1,0)
    """
    def get_tete(self):
        return
    def get_queue(self):
        return
    def set_tete(self):
        return
    def set_queue(self):
        return
    """
        
    def __str__(self):
        return str(self.corps)
    def avance(self):
        self.corps.fl.enfile(1)
        self.corps.fl.defile()

    def tourne(self, ancienx, ancieny):
        differencex = accelerometer.get_x() - ancienx
        differencey = accelerometer.get_y() - ancieny
        self.direction = (differencex, differencey)
        ancienx = accelerometer.get_x()
        ancieny = accelerometer.get_y()

#    def grandit(self):
#        if self.avance() ==