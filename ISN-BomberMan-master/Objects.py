from time import time
import pygame

""" Non-Controlable objects (bombs, power ups)
    each object has a collider box             """

class Bomb():

    def __init__(self):
        self.type = "bomb"
        self.tick = 3 # seconds before exploding

        self.lastTime = time() # define variable for timer

        while self.tick >= 0:
            if time() - self.lastTime > 1: # 1 seconds passed
                print(self.tick)
                self.tick -= 1
                self.lastTime = time() # reset timer

        print("BOOOM")

class Wall():
    def __init__(self):
        self.canBreak = False
        self.x = 0
        self.y = 0
        print("wall called")

    def Spawn(self, window):
        print("wall spawned")
        self.wall = pygame.image.load("wall.png")
        self.wall = pygame.transform.scale(self.wall, (55, 55))
