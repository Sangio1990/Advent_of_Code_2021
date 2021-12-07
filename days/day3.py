# Solutions do Day3 puzzle at https://adventofcode.com/2021
import copy

class Day3:
    def __init__(self) -> None:
        print("\nDay3")
        self.gamma = ""
        self.epsylon = ""
        #with open("puzzle_input/input_day3_test.txt") as file:
        with open("puzzle_input/input_day3.txt") as file:
            self.lines = [line for line in file.read().split("\n") if line != ""]
        file.close()
        self.recursions = {}
        vertical_lines = self.vertical_lines_creator(self.lines)
        for x in range(len(vertical_lines)):
            self.recursions[str(x)+"0"] = vertical_lines[x].count("0")
            self.recursions[str(x)+"1"] = vertical_lines[x].count("1")
        print(self.recursions)
        self.gamma_and_epsylon()
        print("Gamma:", self.gamma, int(self.gamma, 2), "\nEpsylon:", self.epsylon, int(self.epsylon, 2))
        print("GxE =", int(self.gamma, 2)*int(self.epsylon, 2))

        self.oxygen = copy.deepcopy(self.lines)
        self.co2 = copy.deepcopy(self.lines)
        self.oxygen_and_co2()
        print("O2:", self.oxygen, int(self.oxygen[0], 2), "\nCo2:", self.co2, int(self.co2[0], 2))
        print("O2 x Co2:" , int(self.oxygen[0], 2)*int(self.co2[0], 2))

    @staticmethod
    def vertical_lines_creator(lines) -> list:
        vertical_lines = []
        for x in range(len(lines[0])):
            vertical_line = ""
            for line in lines:
                vertical_line += line[x]
            vertical_lines.append(vertical_line)
        return vertical_lines

    
    def gamma_and_epsylon(self):
        for x in range(len(self.lines[0])):
            if self.recursions[str(x)+"0"] > self.recursions[str(x)+"1"]:
                self.gamma += "0"
                self.epsylon += "1"
            else:
                self.gamma += "1"
                self.epsylon += "0"

    def oxygen_and_co2(self):
        for x in range(len(self.oxygen[0])):
            if len(self.oxygen) > 1:
                verticals = self.vertical_lines_creator(self.oxygen)
                times_0 = verticals[x].count("0")
                times_1 = verticals[x].count("1")
                if times_0 > times_1:
                    self.oxygen = [line for line in self.oxygen if line[x] == "0"]
                else:
                    self.oxygen = [line for line in self.oxygen if line[x] == "1"]
            else:
                break

        for x in range(len(self.co2[0])):
            if len(self.co2) > 1:
                verticals = self.vertical_lines_creator(self.co2)
                times_0 = verticals[x].count("0")
                times_1 = verticals[x].count("1")
                if times_0 > times_1:
                    self.co2 = [line for line in self.co2 if line[x] == "1"]
                else:
                    self.co2 = [line for line in self.co2 if line[x] == "0"]
            else:
                break


if __name__=="__main__":
    Day3()