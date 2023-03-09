#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 17:15:54 2022

@author: atsankova
"""

from SNAKE import *
from File import *
from microbit import *
from Pomme import *
from time import *

while True:
    game = True
    sp = Serpent()
    ma = Amanger()
    di = Digestion()
    ma.enfile(Pomme(sp))
    for i in range(len(sp.corps)):#Affichage des points
        v = sp.corps.defile()
        print(type(v))
        display.set_pixel(v[0],v[1],9)
        sp.corps.enfile(v)
    ma.enfile(Pomme(sp))
    x = ma.defile()
    display.set_pixel(x.coordonnees[0],x.coordonnees[1],5)
    ma.enfile(x)
    while game is True:
        sleep(500)
        tourne()
        avance()
        if colisions() == False:
            game = False
            display.scroll('score',len(sp))
            break
        elif sp.corps.dernier == ma.dernier.coordonnees:
            di.enfile(ma.defile())
            ma.enfile(Pomme(sp))
            if ma.dernier.coordonnees == sp.corps.premier:
                tourne()
                sp.avance()
                sp.enfile(di.defile())
                