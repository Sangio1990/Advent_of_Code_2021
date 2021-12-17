# Solutions do Day14 puzzle at https://adventofcode.com/2021

class Day14:
    def __init__(self):
        with open("puzzle_input/input_day14.txt") as file:
            self.lines = [x for x in file.read().split("\n") if x != ""]
        file.close()
        self.parse_input()
        for x in range(10):
            self.pairs = self.dict_step()
        print("Part 1:\n"
              "Result: ", self.max_less_min())

        for x in range(30):
            self.pairs = self.dict_step()
        print("Part 2:\n"
              "Result: ", self.max_less_min())

    def parse_input(self):
        self.pair_insertion_list = dict()
        for line in self.lines:
            try:
                pair = line.split(" -> ")[0]
                insertion = line.split(" -> ")[1]
                self.pair_insertion_list[pair] = insertion
            except IndexError:
                self.recurrency = dict()
                self.pairs = dict()
                for x in range(len(line)):
                    try:
                        self.recurrency[line[x]] += 1
                    except KeyError:
                        self.recurrency[line[x]] = 1
                    try:
                        self.pairs[line[x]+line[x+1]] += 1
                    except KeyError:
                        self.pairs[line[x] + line[x + 1]] = 1
                    except IndexError:
                        pass

    def dict_step(self) -> dict:
        temp_dict = dict()
        for pair in self.pairs:
            if pair in self.pair_insertion_list:
                new_letter = self.pair_insertion_list[pair]
                try:
                    self.recurrency[new_letter] += self.pairs[pair]
                except KeyError:
                    self.recurrency[new_letter] = self.pairs[pair]
                new_pair_1 = pair[0] + new_letter
                new_pair_2 = new_letter + pair[1]
                try:
                    temp_dict[new_pair_1] += self.pairs[pair]
                except KeyError:
                    temp_dict[new_pair_1] = self.pairs[pair]
                try:
                    temp_dict[new_pair_2] += self.pairs[pair]
                except KeyError:
                    temp_dict[new_pair_2] = self.pairs[pair]
            else:
                temp_dict[pair] = self.pairs[pair]
        return temp_dict

    def max_less_min(self) -> int:
        min = list(self.recurrency.keys())[0]
        max = list(self.recurrency.keys())[0]
        for letter in self.recurrency:
            if self.recurrency[letter] > self.recurrency[max]:
                max = letter
            elif self.recurrency[letter] < self.recurrency[min]:
                min = letter
        return self.recurrency[max]-self.recurrency[min]
