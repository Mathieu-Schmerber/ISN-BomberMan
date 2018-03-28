import pygame
from pygame.locals import * # import pygame constantes (KEYDOWN name)
from Objects import *
# from Player import *
from BuildLevel import *
gameLoop = False

def launchGame():
    print("START THE GAME")
    gameLoop = True
    BuildLevel() # on BuildLevel.py
    while gameLoop:
        for event in pygame.event.get():   # Get all events
            if event.type == QUIT:  # if quit event, stop the main loop and quit
                gameLoop = False
                pygame.quit()



