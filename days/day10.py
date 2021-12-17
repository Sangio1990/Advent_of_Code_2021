# Solutions do Day10 puzzle at https://adventofcode.com/2021

class Day10:
    def __init__(self):
        with open("puzzle_input/input_day10.txt") as file:
                lines = file.read().split("\n")
        file.close()
        errors_values = {
            ")": 3,
            "]": 57,
            "}": 1197,
            ">": 25137
        }
        repair_values = {
            ")": 1,
            "]": 2,
            "}": 3,
            ">": 4
        }
        errors_points = []
        repair_points = []
        print("Part 1:")
        for line in lines:
            result, string = self.find_syntax_error(line)
            print(line, "-", string)
            if type(result) is str:
                errors_points.append(errors_values[result])
            else:
                total = 0
                for symbol in self.repair_incomplete_line(line):
                    total = total*5 + repair_values[symbol]
                repair_points.append(total)
        print("Sum of errors points:", sum(errors_points))

        print("\nPart 2:")
        repair_points.sort()
        print("Solution:", repair_points[len(repair_points)//2])

    @staticmethod
    def find_syntax_error(line):
        chunk_delimiter = {
            "(": ")",
            "[": "]",
            "{": "}",
            "<": ">"
        }
        counter_list = []
        for symbol in line:
            if symbol in chunk_delimiter:
                counter_list.append(chunk_delimiter[symbol])
            else:
                if counter_list[-1] == symbol:
                    counter_list.pop()
                else:
                    return symbol, f"Syntax Error: Expected {counter_list[-1]}, Found {symbol}"
        return False, f"No syntax error found"

    @staticmethod
    def repair_incomplete_line(line):
        chunk_delimiter = {
            "(": ")",
            "[": "]",
            "{": "}",
            "<": ">"
        }
        counter_list = []
        for symbol in line:
            if symbol in chunk_delimiter:
                counter_list.append(chunk_delimiter[symbol])
            else:
                counter_list.pop()
        counter_list.reverse()
        return counter_list



