import pygame
import time
from game import Game

screen_widht = 600
screen_height = 400

pygame.init()

window = pygame.display.set_mode((screen_widht, screen_height))

running = True

game = Game()

while running:
    pygame.draw.rect(window, (200,200,200), pygame.Rect(0,0,screen_widht,screen_height))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game.jump()
            
    game.update()
    game.render(window)
    
    pygame.display.update()
    time.sleep(0.06)