from Grid import Grid
from Blocks import *
import random

class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [IBlocks(), JBlocks(), LBlocks(),
                        OBlocks(), SBlocks(), TBlocks(), ZBlocks()]
        self.currentBlock = self.getRandomBlocks()
        self.nextBlock = self.getRandomBlocks()

    def getRandomBlocks(self):
        if len(self.blocks) == 0:
            self.blocks = [IBlocks(), JBlocks(), LBlocks(),
                            OBlocks(), SBlocks(), TBlocks(), ZBlocks()]
        Block = random.choice(self.blocks)
        self.blocks.remove(Block)
        return Block
        
    def draw(self, screen):
        self.grid.draw(screen)
        self.currentBlock.draw(screen)