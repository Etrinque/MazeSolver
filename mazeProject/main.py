from mazeSolver import Window
from maze import Maze

    
def Main():
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 600
    screen_y = 400
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    print("Maze Created")
    resolvd = maze.solv()
    if not resolvd:
        print("UnSolvdAble")
    else:
        print("SolvDeD")

    win.waitForClose()

Main()