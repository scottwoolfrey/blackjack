import pygame
from main import User, Card, Main

bg = pygame.image.load("Blackjack map.png")
cardload = pygame.image.load("card.png")
card = pygame.transform.scale(cardload, (100,150))

white = (255, 255, 255)
hitWhite = (242, 242, 242)
black = (0, 0, 0)
hitBlack = (128, 128, 128)
pygame.font.init()
font = pygame.font.SysFont("ariel", 20)
text = font.render(f'', True, black)

while True:
    screen = pygame.display.set_mode((916,512))
    screen_w = screen.get_width()
    screen_h = screen.get_height()
    screen.blit(bg, (0,0))
    screen.blit(card, (100, 50))
    screen.blit(text, (100, 50))
    pygame.display.update()
# card = Card()
# player = User("Player")
# dealer = User("Dealer")
# m = Main()
# m.loop()




