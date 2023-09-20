import sys
import pygame
from Grid import Grid

pygame.init()
colorScreen = (44,44,127)   # darkblue color

screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Game Tetris")
clock = pygame.time.Clock()

gameGrid = Grid()
# Test --> gameGrid.grid[0][0] = 1
# Test --> gameGrid.grid[3][5] = 4
# Test --> gameGrid.grid[17][8] = 7
gameGrid.printGrid()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Drawing
    screen.fill(colorScreen)
    gameGrid.draw(screen)

    pygame.display.update()
    clock.tick(60)