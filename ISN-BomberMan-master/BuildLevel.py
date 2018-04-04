""" Called by Game.py, to build the level, spawn players and walls at the beginning of the game """
""" Level composed of 71x71 squares, 15 length and 10 height """
import pygame
from Objects import *

squareSize = 60
height = 10
width = 18
beginY = squareSize * 2
beginX = 2
Walls = [] # List of walls

pygame.init() # Initialise Pygame


def BuildLevel(window):
    for y in range(height):
        for x in range(width):
            w = Wall()
            w.x = x * squareSize + beginX
            w.y = y * squareSize + beginY
            w.Spawn(window)
            Walls.append(w)
            window.blit(w.wall, (w.x, w.y))
            pygame.display.flip()

    print("Level build !")

def RefreshWalls(window):
    window.fill((0,0,0))
    for w in Walls:
        window.blit(w.wall, (w.x ,w.y))
    print("number of wall = " + str(len(Walls)))
    pygame.display.flip()