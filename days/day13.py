# Solutions do Day13 puzzle at https://adventofcode.com/2021

class Day13:
    def __init__(self):
        with open("puzzle_input/input_day13_test.txt") as file:
            lines = [x for x in file.read().split("\n") if x != ""]
        file.close()
        self.parse_input(lines)
        print(self.dots_ccordinates)
        print(self.folds)

    def parse_input(self, lines):
        self.dots_ccordinates = []
        self.folds = []
        for line in lines:
            try:
                x, y = line.split(",")
                self.dots_ccordinates.append((x, y))
            except ValueError:
                self.folds.append(line.split(" ")[2])
