# import pygame
# screen_w = 1025
# screen_h = 512
# screen = screen_w, screen_h
# map = pygame.image.load("Blackjack map.png")
# while True:
#     pygame.init()
#     myDisplay = pygame.display.set_mode(screen)
#     empty_surface = pygame.Surface(screen)
#     pygame.display.update()

import pygame
bg = pygame.image.load("Blackjack map.png")
pygame.transform.smoothscale(bg, (916,512))
while True:
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((916,512))
    screen.blit(bg, (0,0))
    pygame.transform.scale(bg, (916,512))
    pygame.display.update()




