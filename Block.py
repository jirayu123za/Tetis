from Colors import Colors
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

    def draw(self, screen):
        tiles = self.cells[self.rotationState]
        for tile in tiles:
            tile_rect = pygame.Rect(tile.col * self.cellSize + 1, tile.row * self.cellSize + 1,
                                    self.cellSize - 1, self.cellSize - 1)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)