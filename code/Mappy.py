#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 21:57:31 2023

@author: si-thami
"""

import pygame as pg
#GAME WORLD

_ = False



#ICI LES 1 SONT LES MURS ET LES UNDERSCRORE LES VIDES
mini_map = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 2],
        [1, _, _, 3, 3, 3, 3, _, _, _, 2, 2, 2, _, _, 2],
        [1, _, _, _, _, _, 4, _, _, _, _, _, 2, _, _, 2],
        [1, _, _, _, _, _, 4, _, _, _, _, _, 2, _, _, 2],
        [1, _, _, 3, 3, 3, 3, _, _, _, _, _, _, _, _, 2],
        [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 2],
        [1, _, _, 4, _, _, _, 4, _, _, _, _, _, _, _, 2],
        [1, 1, 1, 1, 1, _, _, _, _, _, _, _, _, 1, 1, 1],
        [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 2],
        [1, _, _, 3, 3, 3, 3, _, _, _, 4, 4, 4, _, _, 2],
        [1, _, _, _, _, _, 4, _, _, _, _, _, 4, _, _, 2],
        [1, _, _, _, _, _, 4, _, _, _, _, _, 4, _, _, 2],
        [1, _, _, 3, 3, 3, 3, _, _, _, _, _, _, _, _, 2],
        [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 2],
        [1, _, _, 4, _, _, _, 5, _, _, _, _, _, _, _, 2],
        [1, 1, 1, 1, 1, _, _, _, _, _, _, _, _, 1, 1, 1],
        [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 2],
        [1, _, _, 3, 3, 3, 3, _, _, _, 2, 2, 2, _, _, 2],
        [1, _, _, _, _, _, 4, _, _, _, _, _, 2, _, _, 2],
        [1, _, _, _, _, _, 4, _, _, _, _, _, 2, _, _, 2],
        [1, _, _, 3, 3, 3, 3, _, _, _, _, _, _, _, _, 2],
        [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 2],
        [1, _, _, 4, _, _, _, 4, _, _, _, _, _, _, _, 2],
        [1, _, _, 4, _, _, _, 4, _, _, _, _, _, _, _, 2],
        [1, _, _, 4, _, _, _, 4, _, _, _, _, _, _, _, 2],
        [1, _, _, 4, _, _, _, 4, _, _, _, _, _, _, _, 2],
        [1, _, _, 4, _, _, _, 4, _, _, _, _, _, _, _, 2],
        [1, _, _, 4, _, _, _, 4, _, _, _, _, _, _, _, 2],
        [1, _, _, 4, _, _, _, 4, _, _, _, _, _, _, _, 2],
        [1, 1, 1, 3, 1, 1, 1, 3, 3, 3, 3, 3, 3, 1, 1, 1],
    ]


class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()
        
        
    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value
                    
                    
    
    def draw(self):
        [pg.draw.rect(self.game.screen, 'darkgray', (pos[0]*100, pos[1]*100, 100, 100), 2)
         for pos in self.world_map]
        
        
"""
La classe Map a trois méthodes :

__init__ : Cette méthode initialise la carte avec la matrice mini_map et la crée sous forme d'un dictionnaire nommé world_map qui contient les coordonnées des murs de la carte.
get_map : Cette méthode parcourt la matrice mini_map et ajoute les coordonnées des murs dans le dictionnaire world_map.
draw : Cette méthode dessine chaque mur de la carte à l'écran en utilisant la méthode draw.rect de Pygame.
La matrice mini_map est définie en haut du fichier, elle contient des 1 qui représentent les murs et des _ qui représentent les espaces vides.


"""