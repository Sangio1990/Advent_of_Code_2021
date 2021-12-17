# Solutions do Day11 puzzle at https://adventofcode.com/2021

import numpy as np

class Day11:
    def __init__(self) -> None:
        with open("puzzle_input/input_day11.txt") as file:
            lines = file.read().split("\n")
        file.close()
        self.matrix = np.ndarray((len(lines[0]), len(lines)), dtype=int)
        for x in range(len(lines)):
            for y in range(len(lines[0])):
                self.matrix[x][y] = lines[x][y]
        total = 0
        for x in range(100):
            total += self.step()
        print("Total:", total)

        x = 100
        while True:
            x += 1
            if self.step() == self.matrix.size:
                break
        print("First global flash at step", x)

    def step(self):
        counter = 0
        self.matrix_energy_increase()
        cells = []
        while True:
            result = np.where(self.matrix == 10)
            cells = np.dstack((result[0], result[1]))
            for cell in cells[0]:
                counter += 1
                self.adjacent_cell_increase(cell)
            if len(cells[0]) == 0:
                break
        result = np.where(self.matrix == 11)
        cells = np.dstack((result[0], result[1]))
        for cell in cells[0]:
            self.matrix[cell[0]][cell[1]] = 0
        return counter

    def adjacent_cell_increase(self, cell):
        for x in range(cell[0]-1, cell[0]+2):
            for y in range(cell[1]-1, cell[1]+2):
                if x >= 0 and y >= 0:
                    try:
                        if self.matrix[x][y] < 10:
                            self.matrix[x][y] += 1
                    except IndexError:
                        pass
        self.matrix[cell[0]][cell[1]] = 11


    def matrix_energy_increase(self):
        self.matrix = self.matrix + 1



if __name__ == "__main__":
    Day11()