import pygame
from Colors import Colors

class Grid:
    def __init__(self):
        self.numRows = 20
        self.numCols = 10
        self.cellSize = 30
        self.grid = [[0 for i in range(self.numCols)] for j in range(self.numRows)]
        self.colors = Colors.getCellColors()

    def printGrid(self):
        for row in range(self.numRows):
            for col in range(self.numCols):
                print(self.grid[row][col], end = " ")
            print()

    def isInside(self, row, col):
        if row >= 0 and row < self.numRows and col >= 0 and col < self.numCols:
            return True
        return False
    
    def isEmpty(self, row, col):
        if self.grid[row][col] == 0:
            return True
        return False
    
    def isRowFull(self, row):
        for col in range(self.numCols):
            if self.grid[row][col] == 0:
                return False
        return True
    
    def clearRow(self, row):
        for col in range(self.numCols):
            self.grid[row][col] = 0

    def draw(self, screen):
        for row in range(self.numRows):
            for col in range(self.numCols):
                cellValue = self.grid[row][col]
                cellRect = pygame.Rect(col * self.cellSize + 1, row * self.cellSize + 1,
                                        self.cellSize - 1, self.cellSize - 1)
                pygame.draw.rect(screen, self.colors[cellValue], cellRect)