import pygame
import sys
import random

pygame.init()

WINDOW = pygame.display.set_mode((1024,720))

image = pygame.image.load("goku.png")

while True:

    WINDOW.fill("White")
    WINDOW.blit(image,(10,10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Xử lý sự kiện bàn phím
    

    pygame.display.update()
