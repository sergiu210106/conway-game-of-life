import pygame
import random
class Grid:
    def __init__(self, width, height, cellSize):
        self.rows = height // cellSize
        self.cols = width // cellSize
        self.cellSize = cellSize
        self.cells = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        
    def draw(self, screen):
        for row in range(self.rows):
            for col in range(self.cols):
                color = (0, 255, 0) if self.cells[row][col] else (55, 55, 55)
                pygame.draw.rect(screen, color, (col * self.cellSize, row * self.cellSize, self.cellSize - 1, self.cellSize - 1))
    
    def fillRandom(self):
        for row in range(self.rows):
            for col in range(self.cols):
                self.cells[row][col] = random.choice([0, 0, 0, 1])
                
    def clear(self):
        self.cells = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
    
    def toggleCellValue(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.cells[row][col] = not self.cells[row][col]