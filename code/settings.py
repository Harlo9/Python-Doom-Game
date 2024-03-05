#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 21:56:48 2023

@author: si-thami
"""
import math
#RESOLUTION -> Game settings
RES = WIDTH, HEIGHT = 1600, 900
HALF_WITDH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 0

#Player settings 
PLAYER_POS = 1.5, 5 #position map 
PLAYER_ANGLE = 0   #angle
PLAYER_SPEED = 0.004
PLAYER_ROT_SPEED = 0.002 #rotation speed
PLAYER_SIZE_SCALE = 60
PLAYER_MAX_HEALTH = 100



# MOUSE MOVE 
MOUSE_SENSITIVITY = 0.0003
MOUSE_MAX_REL = 40
MOUSE_BORDER_LEFT = 100
MOUSE_BORDER_RIGHT = 100

FLOOR_COLOR = (30, 30, 30)



#Raycastings settings :
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2 #En nombre entier
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 20

SCREEN_DIST = HALF_WITDH / math.tan(HALF_FOV)
SCALE = WIDTH // NUM_RAYS

TEXTURE_SIZE = 256
HALF_TEXTURE_SIZE = TEXTURE_SIZE // 2