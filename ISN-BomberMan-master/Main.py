import pygame
from pygame.locals import * # import pygame constantes (KEYDOWN name)
from Game import *

menuLoop = True
inMenu = True
inRules = False
inInputs = False
inGame = False

pygame.init() # Initialise Pygame
window = pygame.display.set_mode((1080, 720))

menuBackground = pygame.image.load("Menus/MenuBackground.png")
rulesMenu = pygame.image.load("Menus/RulesMenu.png")
inputsMenu = pygame.image.load("Menus/InputsMenu.png")
Cursor = pygame.image.load("Menus/cursor.png").convert_alpha()
Cursor = pygame.transform.scale(Cursor, (50, 50))
cursorPos = Cursor.get_rect()
cursorPos = cursorPos.move(470,310)

buttonNumber = 1 # button number where the cursor is pointing at (1 = Start; 3 = Quit)
buttonDistance = 80 # y distance between buttons

def DrawMenu():
    if menuLoop:
        window.blit(menuBackground, (0,0))
        window.blit(Cursor, cursorPos)
        if inRules:
            window.blit(rulesMenu, (165 ,135))
        elif inInputs:
            window.blit(inputsMenu, (165 ,135))
        else:
            window.blit(rulesMenu, (-500 ,-500))
            window.blit(inputsMenu, (-500 ,-500))
        pygame.display.flip()

while menuLoop:
    for event in pygame.event.get():   # Get all events
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                buttonNumber += 1
                if buttonNumber > 3:
                    buttonNumber = 1
                    cursorPos = cursorPos.move(0,-buttonDistance*2)
                else:
                    cursorPos = cursorPos.move(0,buttonDistance)
            elif event.key == K_UP:
                buttonNumber -= 1
                if buttonNumber < 1:
                    buttonNumber = 3
                    cursorPos = cursorPos.move(0,buttonDistance*2)
                else:
                    cursorPos = cursorPos.move(0,-buttonDistance)

            elif event.key == K_SPACE: # in rules or inputs
                if inRules:
                    inInputs = True
                    inRules = False
                elif inInputs:
                    inInputs = False

            elif event.key == K_RETURN:
                if inRules == False and inInputs == False:
                    if buttonNumber == 1: # Start
                        menuLoop = False
                        launchGame(window) # Function on Game.py
                    elif buttonNumber == 2: # Rules
                        inRules = True
                    elif buttonNumber == 3: # Quit
                        menuLoop = False
                        pygame.quit()

            elif event.type == QUIT:  # if quit event, stop the main loop and quit
                menuLoop = False
                pygame.quit()

    DrawMenu() # Refresh screen

