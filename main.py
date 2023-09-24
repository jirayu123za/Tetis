import sys
import pygame

from Game import Game
from Colors import Colors

pygame.init()
resolutionScreen = (500, 620)    # display resolution
fpsScreen = (60)                # display FPS

screen = pygame.display.set_mode((resolutionScreen))
pygame.display.set_caption("Game Tetris")
clock = pygame.time.Clock()

Game = Game()
GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if Game.gameOver == True:
                Game.gameOver = False
                Game.reset()
            if event.key == pygame.K_LEFT and Game.gameOver == False:
                Game.moveLeft()
            if event.key == pygame.K_RIGHT and Game.gameOver == False:
                Game.moveRight()
            if event.key == pygame.K_DOWN and Game.gameOver == False:
                Game.moveDown()
            if event.key == pygame.K_UP and Game.gameOver == False:
                Game.rotate()
        if event.type == GAME_UPDATE and Game.gameOver == False:
            Game.moveDown()

    # Drawing
    screen.fill(Colors.colorScreen)
    Game.draw(screen)

    pygame.display.update()
    clock.tick(fpsScreen)