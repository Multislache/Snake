#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Cellule:
    def __init__(self, v, s=None):
        self.valeur = v
        self.suivante = s

    def __str__(self):
        if self.suivante is None:
            return 'Cellule(' + str(self.valeur) + ')'
        return 'Cellule(' + str(self.valeur) + ', ' + str(self.suivante) + ')'

    def __len__(self):
        if self.suivante is None:
            return 1
        return 1 + len(self.suivante)
    def appartient(self, x):
        if self.suivante is None:
            return self.valeur == x
        else:
            if self.valeur == x:
                return True
            else:
                return self.suivante.appartient(x)
    def get_valeur(self):
        return self.valeur
    def get_suivante(self):
        return self.suivante
    def set_valeur(self, val):
        self.valeur = val
    def set_suivante(self, cel):
        self.suivante = cel
class File:
    def __init__(self):
        self.dernier = None
        self.premier = None
        self.longueur = 0
    def __str__(self):
        return str(self.premier)
    def est_vide(self):
        if self.longueur == 0:
            return True
        else:
            return False
    def enfile(self, element):
        if self.dernier == None:
            self.dernier= Cellule(element)
            self.premier= self.dernier
            self.longueur +=1
        else:
            self.dernier = self.dernier.set_suivante(Cellule(element))
            self.longueur +=1
    def defile(self):
        if self.premier == None:
            return('La file est vide')
        else:
            self.premier = self.premier.get_suivante()
            self.longueur -= 1
    def __len__(self):
        return self.longueur
