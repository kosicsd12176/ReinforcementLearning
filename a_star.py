import numpy as np


class Cell(object):
    def __init__(self, x, y, utility=0):
        self.neighbors = []
        self.x = x
        self.y = y
        self.utility = utility

    def get_neighbors(self):
        return self.neighbors

    def set_neighbors(self, neighbor):
        self.neighbors.append(neighbor)

    def set_utility(self, utility):
        self.utility = utility

    def get_utility(self):
        return  self.utility




class Enviroment_a_star(object):
    def __init__(self, utilities):
        self.cells = []
        self.utilities = utilities
        cell1 = Cell(0, 0)
        cell2 = Cell(0, 1)
        cell3 = Cell(0, 2)
        cell4 = Cell(0, 3)
        cell5 = Cell(1, 0)
        cell6 = Cell(1, 1)
        cell7 = Cell(1, 2)
        cell8 = Cell(1, 3)
        cell9 = Cell(2, 0)
        cell10 = Cell(2, 1)
        cell11 = Cell(2, 2)
        cell12 = Cell(2, 3)
        self.terminal_state = cell9.utility
        self.start_cell = cell9

        cell1.neighbors.append(cell2)
        cell1.neighbors.append(cell5)
        cell2.neighbors.append(cell1)
        cell2.neighbors.append(cell6)
        cell2.neighbors.append(cell3)
        cell3.neighbors.append(cell2)
        cell3.neighbors.append(cell7)
        cell3.neighbors.append(cell4)
        cell4.neighbors.append(cell3)
        cell4.neighbors.append(cell8)
        cell5.neighbors.append(cell6)
        cell5.neighbors.append(cell1)
        cell5.neighbors.append(cell9)
        cell6.neighbors.append(cell5)
        cell6.neighbors.append(cell7)
        cell6.neighbors.append(cell2)
        cell6.neighbors.append(cell10)
        cell7.neighbors.append(cell6)
        cell7.neighbors.append(cell8)
        cell7.neighbors.append(cell3)
        cell7.neighbors.append(cell11)
        cell8.neighbors.append(cell4)
        cell8.neighbors.append(cell7)
        cell8.neighbors.append(cell12)
        cell9.neighbors.append(cell5)
        cell9.neighbors.append(cell10)
        cell10.neighbors.append(cell9)
        cell10.neighbors.append(cell11)
        cell10.neighbors.append(cell6)
        cell11.neighbors.append(cell10)
        cell11.neighbors.append(cell12)
        cell11.neighbors.append(cell7)
        cell12.neighbors.append(cell8)
        cell12.neighbors.append(cell11)

        self.cells.append(cell1)
        self.cells.append(cell2)
        self.cells.append(cell3)
        self.cells.append(cell4)
        self.cells.append(cell5)
        self.cells.append(cell6)
        self.cells.append(cell7)
        self.cells.append(cell8)
        self.cells.append(cell9)
        self.cells.append(cell10)
        self.cells.append(cell11)
        self.cells.append(cell12)

        for cell in self.cells:
            cell.set_utility(utilities[self.cells.index(cell)])




    def set_cells(self, cell: Cell):
        self.cells.append(cell)

    def get_cells(self):
        return  self.cells

    def compute_a_star(self):
        path = []
        path.append(self.start_cell.utility)


        while self.start_cell.utility != 1:
            for cell in np.array(self.start_cell.get_neighbors()):
                if cell.get_utility() >= self.start_cell.utility:
                    self.start_cell = cell
                    self.start_cell.utility = cell.get_utility()

            path.append(self.start_cell.utility)

        return path
