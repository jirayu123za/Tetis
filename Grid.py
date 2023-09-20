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

    def getCellColor(self):

        darkGray = (26, 31, 40)
        green = (47, 230, 23)
        red = (232, 18, 18)
        orange = (226, 116, 17)
        yellow = (237, 234, 4)
        purple = (166, 0, 247)
        cyan = (21, 204, 209)
        blue = (13, 64, 216)

        return [darkGray, green, red, orange, yellow, purple, cyan, blue]
    
    def draw(self, screen):
        for row in range(self.numRows):
            for col in range(self.numCols):
                cellValue = self.grid[row][col]
                cellRect = pygame.Rect(col * self.cellSize + 1, row * self.cellSize + 1,
                                        self.cellSize - 1, self.cellSize - 1)
                pygame.draw.rect(screen, self.colors[cellValue], cellRect)
