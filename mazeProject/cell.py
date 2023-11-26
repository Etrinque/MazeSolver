from mazeSolver import Line, Point

class Cell():
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self.x1 = None
        self.y1 = None
        self.x2 = None
        self.y2 = None
        self.win = win


    def drawCell(self, x1, y1, x2, y2):
        if self.win is None:
            return

        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self.win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self.win.draw_line(line, "white")
        
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self.win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self.win.draw_line(line, "white")
        
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self.win.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self.win.draw_line(line, "white")

        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self.win.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self.win.draw_line(line, "white")

    def drawMove(self, to_cell, undo=False):

        if self.win is None:
            return
        
#Mid points for cells
        firstX = (self.x1 + self.x2) / 2
        firstY = (self.y1 + self.y2) / 2
        
        toSecondX = (to_cell.x1 + to_cell.x2) / 2
        toSecondY = (to_cell.y1 + to_cell.y2) / 2

        fill_color = "red"
        if undo is True:
            fill_color = "grey"
        
#LEFT
        if self.x1 > to_cell.x1:
            line = Line(Point(self.x1,firstY), Point(firstX, firstY))
            self.win.draw_line(line, fill_color)
            line = Line(Point(toSecondX, toSecondY), Point(to_cell.x2 ,toSecondY))
            self.win.draw_line(line, fill_color)
#RIGHT
        elif self.x1 < to_cell.x1:
            line = Line(Point(firstX,firstY), Point(self.x2, firstY))
            self.win.draw_line(line, fill_color)
            line = Line(Point(to_cell.x1, toSecondY), Point(toSecondX ,toSecondY))
            self.win.draw_line(line, fill_color)
#UP
        elif self.y1 > to_cell.y1:
            line = Line(Point(firstX, firstY), Point(firstX, self.y1))
            self.win.draw_line(line, fill_color)
            line = Line(Point(toSecondX, to_cell.y2), Point(toSecondX ,toSecondY))
            self.win.draw_line(line, fill_color)
#DOWN
        elif self.y1 < to_cell.y1:
            line = Line(Point(firstX, firstY), Point(firstX, self.y2))
            self.win.draw_line(line, fill_color)
            line = Line(Point(toSecondX, toSecondY), Point(toSecondX ,to_cell.y1))
            self.win.draw_line(line, fill_color)


#Helper func:
    # def isLeaf(self):
        
    #     if self.current is None:
    #         return True
        
    #     elif self.next == self.next.left and self.next not in self.visited:
    #         self.current = self.next.left
            

    #     elif self.next == self.next.right and self.next not in self.visited:
    #         self.current = self.next.right
            

    #     elif self.next == self.next.down and self.next not in self.visited:
    #         self.current = self.next.down
            

    #     elif self. next == self.next.up and self.next not in self.visited:
    #         self.current = self.next.up
        

    #     self.visited.append(self.next)
        


    # recursively create a path by breaking walls in a DFS traversal
        