import sys
import pygame

from Game import Game
from Colors import Colors

pygame.init()
resolutionScreen = (500, 620)           # display resolution
fpsScreen = (60)                        # display FPS
titleFront = pygame.font.Font(None, 40) # font and size for title
        

scoreSurface = titleFront.render("Score", True, Colors.white)       # interface score
scoreRect = pygame.Rect(320, 55, 170, 60)

nextSurface = titleFront.render("Next", True, Colors.white)         # interface next blocks
nextRect = pygame.Rect(320, 215, 170, 180)

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
    screen.blit(scoreSurface, (365, 20, 50, 50))
    screen.blit(nextSurface, (375, 180, 50, 50))
    pygame.draw.rect(screen, Colors.lightBlue, scoreRect, 0, 10)
    pygame.draw.rect(screen, Colors.lightBlue, nextRect, 0, 10)
    Game.draw(screen)

    pygame.display.update()
    clock.tick(fpsScreen)