import sys
import pygame
# from Grid import Grid
# from Blocks import *
from Game import Game

pygame.init()
colorScreen = (44,44,127)       # darkblue color
resolutionScreen = (300,600)    # display resolution
fpsScreen = (60)                # display FPS

screen = pygame.display.set_mode((resolutionScreen))
pygame.display.set_caption("Game Tetris")
clock = pygame.time.Clock()

Game = Game()
GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

# gameGrid = Grid()
# Test --> gameGrid.grid[0][0] = 1
# Test --> gameGrid.grid[3][5] = 4
# Test --> gameGrid.grid[17][8] = 7
# Test --> gameGrid.printGrid()
# Test --> block = LBlocks()
# Test --> block = JBlocks()
# Test --> block = IBlocks()
# Test --> block = TBlocks()
# Test --> block = ZBlocks()
# Test --> block = SBlocks()
# Test --> block.move(4,3)
# block = OBlocks()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if Game.gameOver() == True:
                Game.gameOver = False
                Game.reset
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
    screen.fill(colorScreen)
    # gameGrid.draw(screen)
    # block.draw(screen)
    Game.draw(screen)

    pygame.display.update()
    clock.tick(fpsScreen)