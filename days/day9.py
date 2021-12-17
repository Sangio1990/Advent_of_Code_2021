# Solutions do Day9 puzzle at https://adventofcode.com/2021
import numpy as np


class Day9:
    def __init__(self):
        with open("puzzle_input/input_day9.txt") as file:
                lines = file.read().split("\n")
        file.close()
        self.matrix = self.matrix_creation(lines)
        self.length -= 1
        self.height -= 1
        low_points = self.find_low_points()
        low_point_risk_sum = 0
        for point in low_points:
            low_point_risk_sum += 1 + self.matrix[point[0]][point[1]]
        print("Total risk =", low_point_risk_sum)


    def matrix_creation(self, lines):
        self.length = len(lines[0])
        self.height = len(lines)
        matrix = np.ndarray(shape=(self.height, self.length), dtype=int, order='C')
        for x in range(len(lines)):
            for y in range(len(lines[x])):
                number = int(lines[x][y])
                matrix[x][y] = number
        return matrix

    def find_low_points(self) -> list:
        list_op_lowpoints = []
        for x in range(len(self.matrix)):
            for y in range(len(self.matrix[x])):
                try:
                    if self.matrix[abs(x - 1)][y] > self.matrix[x][y] \
                            and self.matrix[abs(x + 1)][y] > self.matrix[x][y] \
                            and self.matrix[x][abs(y - 1)] > self.matrix[x][y] \
                            and self.matrix[x][abs(y + 1)] > self.matrix[x][y]:
                        list_op_lowpoints.append([x, y])
                except IndexError:
                    if x == self.height and y == self.length:
                        if self.matrix[abs(x - 1)][y] > self.matrix[x][y] \
                                and self.matrix[1][abs(y-1)] > self.matrix[x][y]:
                            list_op_lowpoints.append([x, y])
                    elif x == self.height:
                        if self.matrix[abs(x - 1)][y] > self.matrix[x][y] \
                                and self.matrix[x][abs(y - 1)] > self.matrix[x][y] \
                                and self.matrix[x][abs(y + 1)] > self.matrix[x][y]:
                            list_op_lowpoints.append([x, y])
                    elif y == self.length:
                        if self.matrix[abs(x - 1)][y] > self.matrix[x][y] \
                                and self.matrix[abs(x + 1)][y] > self.matrix[x][y] \
                                and self.matrix[x][abs(y - 1)] > self.matrix[x][y]:
                            list_op_lowpoints.append([x, y])
        return list_op_lowpoints
