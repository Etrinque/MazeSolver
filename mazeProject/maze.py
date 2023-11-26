
import time
from cell import Cell
import random

class Maze():
    def __init__(
            self, x1, y1, num_rows, num_cols,
            cellSize_X, cellSize_Y, win=None, seed=None
        ):
        self._cells = []
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cellSize_X = cellSize_X
        self.cellSize_Y = cellSize_Y
        self.win = win
        
        if seed:
            random.seed(seed)

        self.createCells()
        self.break_start_end()
        self.break_walls_rec(0,0)
        self.reset_visited()


    def createCells(self):
    
        #Append Cell to Column
        for i in range(self.num_cols):
            cols = []
            for j in range(self.num_rows):
                cols.append(Cell(self.win))
            self._cells.append(cols)
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self.drawCell(i,j)

        # #Append list of columns to list of cells
        # if cols not in self._cells:
        #     self._cells.append(cols)

        # if len(self._cells) == self.num_cols:
        #     self.drawCell(i, j)

    def drawCell(self, i, j):
        if self.win is None:
            return
        x1 = self.x1 + i * self.cellSize_X
        y1 = self.y1 + j * self.cellSize_Y
        x2 = x1 + self.cellSize_X
        y2 = y1 + self.cellSize_Y
        self._cells[i][j].drawCell(x1, y1, x2, y2)
        self.animate()


    def animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.01)

    def break_start_end(self):
        self._cells[0][0].has_top_wall = False
        self.drawCell(0,0)
        self._cells[self.num_cols-1][self.num_rows-1].has_bottom_wall = False
        self.drawCell(self.num_cols - 1, self.num_rows -1)

    #Break path 
    def break_walls_rec(self, i, j):
        self._cells[i][j].visited = True

        while True:
            next_index = []
        
            #Left?
            if i > 0 and not self._cells[i-1][j].visited:
                next_index.append((i-1,j))
            #Right?
            if i < self.num_cols - 1 and not self._cells[i+1][j].visited:
                next_index.append((i+1,j))
            #Up?
            if j > 0 and not self._cells[i][j-1].visited:
                next_index.append((i, j-1))
            #Down?
            if j < self.num_rows -1 and not self._cells[i][j+1].visited:
                next_index.append((i, j+1))
            
            if len(next_index) == 0:
                self.drawCell(i,j)
                return
            
            randIndex = random.randrange(len(next_index))
            next_index = next_index[randIndex]
            
            #Right break
            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
            #Left Break
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False
            #Down Break
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j+1].has_top_wall = False
            #Up Break
            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j-1].has_bottom_wall = False
            
            self.break_walls_rec(next_index[0], next_index[1])

    def reset_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False
    

    def solvR(self, i, j):

        self.animate()
        self._cells[i][j].visited = True

    # Reached End
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True
    # Left    
        if (
            i > 0
            and not self._cells[i][j].has_left_wall
            and not self._cells[i-1][j].visited
        ):
            self._cells[i][j].drawMove(self._cells[i - 1][j])
            if self.solvR(i - 1, j):
                return True
            else:
                self._cells[i][j].drawMove(self._cells[i - 1][j], True)
        
    # Right    
        if (
            i < self.num_cols - 1
            and not self._cells[i][j].has_right_wall
            and not self._cells[i+1][j].visited
        ):
            self._cells[i][j].drawMove(self._cells[i + 1][j])
            if self.solvR(i + 1, j):
                return True
            else:
                self._cells[i][j].drawMove(self._cells[i + 1][j], True)

    # Upward    
        if (
            j > 0
            and not self._cells[i][j].has_top_wall
            and not self._cells[i][j - 1].visited
        ):
            self._cells[i][j].drawMove(self._cells[i][j - 1])
            if self.solvR(i, j - 1):
                return True
            else:
                self._cells[i][j].drawMove(self._cells[i][j - 1], True)        

    # Down
        if (
            j < self.num_rows - 1
            and not self._cells[i][j].has_bottom_wall
            and not self._cells[i][j + 1].visited
        ):
            self._cells[i][j].drawMove(self._cells[i][j + 1])
            if self.solvR(i, j + 1):
                return True
            else:
                self._cells[i][j].drawMove(self._cells[i][j + 1], True)
        
        return False
    
    def solv(self):
        return self.solvR(0,0)