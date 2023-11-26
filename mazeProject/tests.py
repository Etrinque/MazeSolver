import unittest
from maze import *
from cell import *

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):

        num_rows = 12
        num_cols = 10
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(maze._cells),
            num_cols,
        )
        self.assertEqual(
            len(maze._cells[0]),
            num_rows,
        )

    def test_maze_break_start_end(self):

        num_rows = 12
        num_cols = 10
        maze = Maze(0,0,num_rows, num_cols, 10,10)
        self.assertEqual(
            maze._cells[0][0].has_top_wall, 
            False,
        )
        self.assertEqual(
            maze._cells[num_cols -1][num_rows -1].has_bottom_wall,
            False,
        )

    def test_reset_maze(self):

        num_rows = 12
        num_cols = 10
        maze = Maze(0,0,num_rows, num_cols, 10,10)
        for col in maze._cells:
            for i in col:
                self.assertEqual(
                    i.visited,
                    False
                )

if __name__ == "__main__":
    unittest.main()