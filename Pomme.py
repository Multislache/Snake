#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from moicrobit import *
import File as f1
import Serpent as sp
import random
class Pomme:
    def __ini__(self):
        self.coordonnées = (None,None)
    def aleatoire(self):
        list1 = [0, 1 ,2 ,3 ,4]
        self.coordonnées = random.choice(list1)