from time import time

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
