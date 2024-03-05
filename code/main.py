#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 21:46:56 2023

@author: si-thami
"""
import pygame as pg
import sys 
from settings import *
from Mappy import *
from player import * 
from raycasting import *
from object_renderer import *
from sprite_object import *
from object_handler import *
from weapon import *
from sound import *
from pathfinding import *

class Game:
    
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.global_trigger = False
        self.global_event = pg.USEREVENT + 0
        pg.time.set_timer(self.global_event, 40)
        self.new_game()
        
    
    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = Raycasting(self)
        self.object_handler = ObjectHandler(self)
        self.weapon = Weapon(self)
        self.sound = Sound(self)
        self.pathfinding = PathFinding(self)
        pg.mixer.music.play(-1)
    
    def update(self):
        self.player.update()
        #self.sound.theme.play()
        self.raycasting.update()
        self.object_handler.update()
        self.weapon.update()
        pg.display.flip()
        self.delta_time = self.clock.tick() #NUMBER OF FRAME PER SECONDS
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')
        
    #Fenetre fill in black
    def draw(self):
        self.screen.fill('black')
        #self.object_renderer.draw()
        #self.weapon.draw()
        self.map.draw() #On draw la map defini dans l'autre classe 
        self.player.draw()
        
    def check_events(self):
        #Event listener qui quitte lors des appuie sur les touches 
        self.global_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == self.global_event:
                self.global_trigger = True
            self.player.single_fire_event(event)
    
    #Main loop
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

#On run on creer une instance de la classe game 
if __name__ == "__main__":
    game = Game() #Création d'une instance 
    game.run()