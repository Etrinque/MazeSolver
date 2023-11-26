from maze import *
from cell import *
from main import *

# Depth First Search Solver

root = Maze._cells[0][0]
end = Maze._cells[num_cols - 1][num_rows - 1]
nextCell = []

def solver():
    if Maze._cells.visited == end:
        return True

    for ind in Maze._cells[i][j]:
        if ind not in nextCell and not Maze._cells[-1][j]:
            nextCell.append(ind)
            ind += 1


