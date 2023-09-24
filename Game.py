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
        self.gameOver = False

    def getRandomBlocks(self):
        if len(self.blocks) == 0:
            self.blocks = [IBlocks(), JBlocks(), LBlocks(),
                            OBlocks(), SBlocks(), TBlocks(), ZBlocks()]
        Block = random.choice(self.blocks)
        self.blocks.remove(Block)
        return Block
        
    def moveLeft(self):
        self.currentBlock.move(0, -1)
        if self.blockInside() == False or self.blockFits() == False:
            self.currentBlock.move(0,1)

    def moveRight(self):
        self.currentBlock.move(0, 1)
        if self.blockInside() == False or self.blockFits() == False:
            self.currentBlock.move(0, -1)

    def moveDown(self):
        self.currentBlock.move(1, 0)
        if self.blockInside() == False or self.blockFits() == False:
            self.currentBlock.move(-1, 0)
            self.lockBlock()
    
    def lockBlock(self):
        tiles = self.currentBlock.getCellPosition()
        for position in tiles:
            self.grid.grid[position.row][position.col] = self.currentBlock.id
        self.currentBlock = self.nextBlock
        self.nextBlock = self.getRandomBlocks()
        self.grid.clearFullRow()
        if self.blockFits() == False:
            self.gameOver = True

    def reset(self):
        self.grid.reset()

    def blockInside(self):
        tile = self.currentBlock.getCellPosition()
        for tile in tile:
                if self.grid.isInside(tile.row, tile.col) == False:
                    return False
        return True

    def blockFits(self):
        tiles = self.currentBlock.getCellPosition()
        for tile in tiles:
            if self.grid.isEmpty(tile.row, tile.col) == False:
                return False
        return True

    def rotate(self):
        self.currentBlock.rotate()
        if self.blockInside() == False or self.blockFits() == False:
            self.currentBlock.undoRotation()

    def draw(self, screen):
        self.grid.draw(screen)
        self.currentBlock.draw(screen)