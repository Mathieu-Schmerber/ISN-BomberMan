import pygame
from pygame.locals import * # import pygame constantes (KEYDOWN name)
from Objects import *
# from Player import *
from BuildLevel import *
gameLoop = False

def launchGame(window):
    print("START THE GAME")
    BuildLevel(window) # on BuildLevel.py
    gameLoop = True
    while gameLoop:
        RefreshWalls(window)
        for event in pygame.event.get():   # Get all events
            if event.type == QUIT:  # if quit event, stop the main loop and quit
                gameLoop = False
                pygame.quit()



