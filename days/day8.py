class Day8:
    def __init__(self) -> None:
        #with open("puzzle_input/input_day8_test.txt") as file:
        with open("puzzle_input/input_day8.txt") as file:
            self.lines = file.read().split("\n")
        file.close()
        self.divide_the_lines()
        print("Part 1:")
        print(self.count_unique_outputs_recurrencies(self.divided_outputs))

        print("\nPart 2:")
        total = 0
        for line in self.lines:
            total += self.decoding_line(line)
        print("Total:", total)

    def divide_the_lines(self):
        self.divided_outputs = []
        self.divided_inputs = []
        input, outputs = [x.split("|")[0] for x in self.lines], [x.split("|")[1] for x in self.lines]
        for line in outputs:
            temp_list = [x for x in line.split(" ") if x != ""]
            self.divided_outputs.append(temp_list)
        for line in input:
            temp_list = [x for x in line.split(" ") if x != ""]
            self.divided_inputs.append(temp_list)

    @staticmethod
    def count_unique_outputs_recurrencies(output_list) -> int:
        counter = 0
        for line in output_list:
            for output in line:
                if len(output) == 2 or len(output) == 4 or len(output) == 3 or len(output) == 7:
                    counter += 1
        return counter
        

    def decoding_line(self, line) -> int:
        self.vocabulary = {
            "T" : "0",
            "TL" : "0",
            "TR" : "0",
            "M" : "0",
            "BL" : "0",
            "BR" : "0",
            "B" : "0",
        }
        self.temp_1 = self.looking_for_1(line)
        #self.vocabulary["TR"], self.vocabulary["BR"] = result[0], result[1]
        self.vocabulary["T"] = "".join([x for x in self.looking_for_top(line) if x not in self.temp_1])
        self.temp_4 = "".join([x for x in self.looking_for_4(line) if x not in self.temp_1])        
        self.vocabulary["B"] = self.looking_for_bottom(line)
        self.vocabulary["M"] = self.looking_for_middle(line)
        self.vocabulary["TL"] = self.temp_4.replace(self.vocabulary["M"], "")
        self.vocabulary["BR"] = self.looking_for_bottom_right(line)
        self.vocabulary["TR"] = self.temp_1.replace(self.vocabulary["BR"], "")
        self.vocabulary["BL"] = self.looking_for_bottom_left(line)
        return int(self.letters_to_number(line))
        

    @staticmethod
    def looking_for_1(line):
        line.replace(" | ", " ")
        numbers = line.split(" ")
        for number in numbers:
            if len(number) == 2:
                return number
        return False
        
    @staticmethod
    def looking_for_top(line):
        line.replace(" | ", " ")
        numbers = line.split(" ")
        for number in numbers:
            if len(number) == 3:
                return number
        return False

    @staticmethod
    def looking_for_4(line):
        line.replace(" | ", " ")
        numbers = line.split(" ")
        for number in numbers:
            if len(number) == 4:
                return number
        return False

    def looking_for_middle(self, line):
        line.replace(" | ", " ")
        numbers = line.split(" ")
        for number in numbers:
            if len(number) == 5:
                temp = self.temp_1 + self.vocabulary["T"] + self.vocabulary["B"]
                for letter in temp:
                    if letter in number:
                        number = number.replace(letter, "")
                if len(number) == 1:
                    return number
        return False     

    def looking_for_bottom(self, line):
        line.replace(" | ", " ")
        numbers = line.split(" ")
        for number in numbers:
            if len(number) == 6:
                temp = self.temp_4 + self.temp_1 + self.vocabulary["T"]
                for letter in temp:
                    if letter in number:
                        number = number.replace(letter, "")
                if len(number) == 1:
                    return number
        return False        

    def looking_for_bottom_right(self, line):
        line.replace(" | ", " ")
        numbers = line.split(" ")
        for number in numbers:
            if len(number) == 5:
                if self.vocabulary["TL"] in number:
                    temp = self.vocabulary["TL"] + self.vocabulary["T"] + self.vocabulary["B"] + self.vocabulary["M"]
                    for letter in temp:
                        if letter in number:
                            number = number.replace(letter, "")
                    if len(number) == 1:
                        return number
        return False        


    def looking_for_bottom_left(self, line):
        line.replace(" | ", " ")
        numbers = line.split(" ")
        for number in numbers:
            if len(number) == 7:
                temp = self.vocabulary["TL"] + self.vocabulary["TR"] + self.vocabulary["T"] + self.vocabulary["B"] + self.vocabulary["BR"] + self.vocabulary["M"]
                for letter in temp:
                    if letter in number:
                        number = number.replace(letter, "")
                if len(number) == 1:
                    return number
        return False    
    
    def letters_to_number(self, line):
        letter_output = line.split("|")[1]
        letter_output = letter_output.strip()
        letter_output = letter_output.split(" ")
        temp = ""
        for number in letter_output:
            if len(number) == 2:
                temp += "1"
            elif len(number) == 3:
                temp += "7"
            elif len(number) == 4:
                temp += "4"
            elif len(number) == 5:
                if self.vocabulary["TR"] in number and self.vocabulary["BR"] in number:
                    temp += "3"
                elif self.vocabulary["TL"] in number and self.vocabulary["BR"] in number:
                    temp += "5"
                else:
                    temp += "2"
            elif len(number) == 6:
                if self.vocabulary["M"] in number:
                    if self.vocabulary["BL"] in number:
                        temp += "6"
                    else:
                        temp += "9"
                else:
                    temp += "0"
            else:
                temp += "8"

        return temp


if __name__ == "__main__":
    Day8()