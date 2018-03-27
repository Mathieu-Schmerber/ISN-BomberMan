import pygame
from pygame.locals import *

pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((640, 480))

#Chargement et collage du fond

#Chargement et collage du personnage
Cursor = pygame.image.load("cursor.png").convert_alpha()
Cursor = pygame.transform.scale(Cursor, (50, 50))
fenetre.blit(Cursor, ((300, 300)))
cursorPos = Cursor.get_rect()

#Rafraîchissement de l'écran
pygame.display.flip()

#BOUCLE INFINIE
continuer = 1
while continuer:
	continuer = int(input())
