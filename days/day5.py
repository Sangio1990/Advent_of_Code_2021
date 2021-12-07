# Solutions do Day5 puzzle at https://adventofcode.com/2021
class Day5:
    def __init__(self) -> None:
        print("\nDay5")
        self.matrix = {}
        self.starts = []
        self.stops = []
        self.crossed_counter = 0
        self.matrix_creation()
        with open("puzzle_input/input_day5.txt") as file:
        #with open("puzzle_input/input_day5_test.txt") as file:
            while True:
                row = file.readline().replace("\n", "")
                if row == "":
                    break
                temp = row.split(" -> ")
                self.starts.append(temp[0])
                self.stops.append(temp[1])
        file.close()

        for index in range(len(self.starts)):
            # print(self.starts[index] + " -> "+ self.stops[index], end=" ")
            result = self.common_coordinate(self.starts[index], self.stops[index])
            if result == "x":
                # print("x")
                self.calculate_horizontal_path(self.starts[index], self.stops[index])
            elif result == "y":
                # print("y")
                self.calculate_vertical_path(self.starts[index], self.stops[index])
            else:
                # print("False")
                self.calculate_diagonal_path(self.starts[index], self.stops[index])
        # print(self.matrix)
        for coordinate in self.matrix:
            if self.matrix[coordinate] > 1:
                self.crossed_counter += 1
        print(self.crossed_counter)

    def calculate_horizontal_path(self, start, stop):
        temp_start = start.split(",")
        temp_stop = stop.split(",")
        delta = int(temp_start[1]) - int(temp_stop[1])
        if delta < 0:
            delta *= -1
        lower =min(int(temp_start[1]), int(temp_stop[1]))
        for num in range(lower, lower+delta+1):
            self.matrix[temp_stop[0]+","+str(num)] += 1

    def calculate_vertical_path(self, start, stop):
        temp_start = start.split(",")
        temp_stop = stop.split(",")
        delta = int(temp_start[0]) - int(temp_stop[0])
        if delta < 0:
            delta *= -1
        lower =min(int(temp_start[0]), int(temp_stop[0]))
        for num in range(lower, lower+delta+1):
            self.matrix[str(num)+","+temp_stop[1]] += 1

    def calculate_diagonal_path(self, start, stop):
        temp_start = start.split(",")
        temp_stop = stop.split(",")
        delta = int(temp_start[0]) - int(temp_stop[0])
        if delta < 0:
            delta = delta*-1
            step_x = 1
        else:
            step_x = -1
        if int(temp_start[1]) > int(temp_stop[1]):
            step_y = -1
        else:
            step_y = 1
        for num in range(0, delta+1):
            # print(str(int(temp_start[0])+(num*step_x))+","+str(int(temp_start[1])+(num*step_y)))
            self.matrix[str(int(temp_start[0])+(num*step_x))+","+str(int(temp_start[1])+(num*step_y))] += 1

    @staticmethod
    def common_coordinate(start, stop):
        temp_start = start.split(",")
        temp_stop = stop.split(",")
        if temp_start[0] == temp_stop[0]:
            return "x"
        elif temp_start[1] == temp_stop[1]:
            return "y"
        else:
            return False

    def matrix_creation(self):
        for x in range(1, 1000):
            for y in range(1, 1000):
                self.matrix[str(x)+","+str(y)] = 0
"""         for x in range(0, 10):
            for y in range(0, 10):
                self.matrix[str(x)+","+str(y)] = 0 """
        
        
if __name__ == "__main__":
    Day5()
