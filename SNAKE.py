import File as fl
import microbit as micro
class Serpent:
    def __init__(self):
        self.corps = fl.File()
        self.corps.enfile((0,0))
        self.corps.enfile((0,1))
        self.direction = (1,0)

    def get_tete(self):
        return self.corps.dernier
    def get_queue(self):
        return self.corps.premier
    def set_tete(self, x):
        self.corps.dernier = x
    def set_queue(self,x ):
        self.corps.premier = x

    def avance(self):
        self.corps.fl.enfile(1)
        self.corps.fl.defile()

    def tourne(self, ancienx, ancieny):
        differencex = micro.accelerometer.get_x() - ancienx
        differencey = micro.accelerometer.get_y() - ancieny
        self.direction = (differencex, differencey)
        ancienx = micro.accelerometer.get_x()
        ancieny = micro.accelerometer.get_y()

    def colisions(self):
        if self.corps.dernier.valeur[0] > 4 or self.corps.dernier.valeur[0] < 0:
            return False
        elif self.corps.dernier.valeur[1] > 4 or self.corps.dernier.valeur[1] < 0:
            return False
        elif self.corps.appartient_spe(self.dernier.valeur):
            return False
        else:
            return True
                


