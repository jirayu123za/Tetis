import sys
import pygame
from Grid import Grid
from Blocks import *

pygame.init()
colorScreen = (44,44,127)       # darkblue color
resolutionScreen = (300,600)    # display resolution
fpsScreen = (60)                # display FPS

screen = pygame.display.set_mode((resolutionScreen))
pygame.display.set_caption("Game Tetris")
clock = pygame.time.Clock()

gameGrid = Grid()
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
block = OBlocks()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Drawing
    screen.fill(colorScreen)
    gameGrid.draw(screen)
    block.draw(screen)

    pygame.display.update()
    clock.tick(fpsScreen)