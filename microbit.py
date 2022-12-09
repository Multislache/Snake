#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from threading import Thread


class matrice_led:
    """Méthodes pour l'affichage sur la matrice de leds."""

    def __init__(self):
        """
        Matrice de leds 5*5.

        Attribut matrice de type list.
        Chaque élément est une ligne de la matrice.

        """
        self.matrice = [[0 for _ in range(5)] for _ in range(5)]

    def __repr__(self):
        char = '#'*7 + '\n'
        for i in range(5):
            char += '#'
            for j in range(5):
                char += str(self.matrice[i][j])
            char += '#\n'
        char += '#' * 7
        return char

    def set_pixel(self, x, y, intensite):
        if intensite > 10 or intensite < 0:
            raise ValueError('intensite entre 0 et 10.')
        if x > 4 or x < 0:
            raise ValueError('x doit être compris entre 0 et 4.')
        if y > 4 or y < 0:
            raise ValueError('y doit être compris entre 0 et 4.')
        if intensite == 10:
            self.matrice[y][x] = 9
        else:
            self.matrice[y][x] = intensite

    def clear(self):
        self.matrice = [[0 for _ in range(5)] for _ in range(5)]

    def scroll(self, text):
        print(text)


class accelero:
    """Methode pour l'acquisition des paramètres de l'accéléromètre."""

    def __init__(self):
        self.x = 0
        self.y = 0

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y



def lancement():
    pygame.init()
    SCREEN = pygame.display.set_mode((300, 280))
    pygame.display.set_caption("Microbit")
    fond = pygame.image.load("microbit.jpg")
    SCREEN.fill((255, 255, 255))
    SCREEN.blit(fond, (0, 0))

    FPS = 10

    run = True

    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for i in range(5):
            for j in range(5):
                pygame.draw.rect(SCREEN, (display.matrice[i][j]*25, 0, 0),
                                  (100+23*j, 110+22*i, 5, 10))

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            accelerometer.x = 100
            accelerometer.y = 0
        elif keys_pressed[pygame.K_LEFT]:
            accelerometer.x = -100
            accelerometer.y = 0
        elif keys_pressed[pygame.K_UP]:
            accelerometer.x = 0
            accelerometer.y = -100
        elif keys_pressed[pygame.K_DOWN]:
            accelerometer.x = 0
            accelerometer.y = 100

        pygame.display.update()


    pygame.quit()


display = matrice_led()
accelerometer = accelero()
fenetre = Thread(target=lancement)
fenetre.start()