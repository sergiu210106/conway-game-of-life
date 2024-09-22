from grid import Grid

class Simulation:
    def __init__(self, width, height, cellSize):
        self.grid = Grid(width, height, cellSize)
        self.tempGrid = Grid(width, height, cellSize)
        
        self.rows = self.grid.rows
        self.cols = self.grid.cols
        
        self.grid.fillRandom()
        self.run = False
    def draw(self, window):
        self.grid.draw(window)
        
    def countLiveNeighbours(self, row, col):
        liveNeighbours = 0
        offsets = [[-1,-1], [-1,0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        
        for offset in offsets:
            newRow = (row + offset[0]) % self.rows
            newCol = (col + offset[1]) % self.cols
            
            if self.grid.cells[newRow][newCol] == 1:
                liveNeighbours += 1
        return liveNeighbours
    
    def update(self):
        if self.isRunning():
            for row in range(self.rows):
                for col in range(self.cols):
                    liveNeighbours = self.countLiveNeighbours(row, col)
                    cellValue = self.grid.cells[row][col]
                    
                    if cellValue == 1:
                        if liveNeighbours < 2 or liveNeighbours > 3:
                            self.tempGrid.cells[row][col] = 0
                        else:
                            self.tempGrid.cells[row][col] = 1
                    elif cellValue == 0:
                        if liveNeighbours == 3:
                            self.tempGrid.cells[row][col] = 1
                        else:
                            self.tempGrid.cells[row][col] = 0
            
            for row in range(self.rows):
                for col in range(self.cols):        
                    self.grid.cells[row][col] = self.tempGrid.cells[row][col]
    def isRunning(self):
        return self.run
    def start(self):
        self.run = True
    def stop(self):
        self.run = False
    
    
    def clear(self):
        if not self.isRunning():
            self.grid.clear()
    
    def createRandomState(self):
        if not self.isRunning():
            self.grid.fillRandom()
    
    def toggleCell(self, row, col):
        if not self.isRunning():
            self.grid.toggleCellValue(row, col)