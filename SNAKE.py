from microbit import *
import File as fl
class Serpent():
    def __init__(self):
        self.corps = f1.File()
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
    def avance(self):
        self.corps.fl.enfile(1)
        self.corps.fl.defile()

    def tourne(self, ancienx, ancieny):
        differencex = accelerometer.get_x() - ancienx
        differencey = accelerometer.get_y() - ancieny
        self.direction = (differencex, differencey)
        ancienx = accelerometer.get_x()
        ancieny = accelerometer.get_y()

    def grandit(self):
        if self.avance() ==


