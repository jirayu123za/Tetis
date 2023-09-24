from Colors import Colors
from Position import Position
import pygame

class Block:
    def __init__(self,id):
        self.id = id
        self.cells = {}
        self.cellSize = 30
        self.rowOffset = 0
        self.colOffset = 0
        self.rotationState = 0
        self.colors = Colors.getCellColors()

    def move(self, row, col):
        self.rowOffset += row
        self.colOffset += col

    def getCellPosition(self):
        tiles = self.cells[self.rotationState]
        moveTiles = []
        for position in tiles:
            position = Position(position.row + self.rowOffset,
                                position.col  + self.colOffset)
            moveTiles.append(position)
        return moveTiles

    def rotate(self):
        self.rotationState += 1
        if self.rotationState == len(self.cells):
            self.rotationState = 0

    def undoRotation(self):
        self.rotationState -= 1
        if self.rotationState == 0:
            self.rotationState = len(self.cells) - 1

    def draw(self, screen, offsetX, offsetY):
        tiles = self.getCellPosition()
        for tile in tiles:
            tile_rect = pygame.Rect(offsetX + tile.col * self.cellSize, offsetY + tile.row * self.cellSize,
                                    self.cellSize - 1, self.cellSize - 1)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)