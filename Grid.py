import pygame

class Grid:
    def __init__(self):
        self.numRows = 20
        self.numCols = 10
        self.cellSize = 30
        self.grid = [[0 for i in range(self.numCols)] for j in range(self.numRows)]
        self.colors = self.getCellColor()

    def printGrid(self):
        for row in range(self.numRows):
            for col in range(self.numCols):
                print(self.grid[row][col], end = " ")
            print()
    
    def draw(self, screen):
        for row in range(self.numRows):
            for col in range(self.numCols):
                cellValue = self.grid[row][col]
                cellRect = pygame.Rect(col * self.cellSize + 1, row * self.cellSize + 1,
                                        self.cellSize - 1, self.cellSize - 1)
                pygame.draw.rect(screen, self.colors[cellValue], cellRect)