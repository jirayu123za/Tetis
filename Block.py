from Colors import Colors
import pygame

class Block:
    def __init__(self,id):
        self.id = id
        self.cells = {}
        self.cellSize = 30
        self.rotationState = 0
        self.colors = Colors.getCellColors()

    def draw(self, screen):
        titles = self.cells[self.rotationState]
        for title in titles:
            title_rect = pygame.Rect(title.cols * self.cellSize + 1, title.rows * self.cellSize + 1,
                                    self.cellSize - 1, self.cellSize - 1)
            pygame.draw.rect(screen, self.colors[self.id], title_rect)