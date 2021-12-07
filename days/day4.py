# Solutions do Day4 puzzle at https://adventofcode.com/2021

class Day4():
    def __init__(self) -> None:
        print("\nDay4")
        print("Part 1:")
        self.tables = []
        self.extraction_list = ""
        self.extracted_numbers = []
        self.winning_table = []
        self.num_sum = 0
        self.table_creation()
        self.start_extraction()
        self.sum_of_number_in_a_table(self.winning_table)
        w_n = self.extracted_numbers[-1]
        print("Winning number:", w_n)
        print("Sum of not winning numbers:", self.num_sum)
        print("Product:", w_n*self.num_sum)
        
        # Part 2 calculations:
        print("\nPart: 2")
        self.num_sum = 0
        self.extracted_numbers = []
        self.last_winner()
        print(self.winning_table)
        w_n = self.extracted_numbers[-1]
        self.sum_of_number_in_a_table(self.winning_table)
        print("Winning number:", w_n)
        print("Sum of not winning numbers:", self.num_sum)
        print("Product:", w_n*self.num_sum)

    def last_winner(self):
        for num in self.extraction_list:
            self.extracted_numbers.append(num)
            while True:
                if self.check_winner():
                    self.tables.remove(self.winning_table)
                else:
                    break
            if len(self.tables) == 0:
                break

    def start_extraction(self) -> None:
        check = False
        for num in self.extraction_list:
            self.extracted_numbers.append(num)
            if self.check_winner():
                check = True
                break
        if not check:
            print("No winner!")

    def check_winner(self):
        for table in self.tables:
            if self.table_is_winning(table):
                self.winning_table = table
                return True
        return False

    def table_creation(self):
        with open("puzzle_input/input_day4.txt") as file:
            self.extraction_list = [int(x) for x in file.readline().split(",")]
            temp_list = [x for x in file.read().split("\n") if x != ""]
            self.tables = []
            table = []
            for line in range(len(temp_list)):
                temp_row = [int(x) for x in temp_list[line].split(" ") if x != ""]
                table.append(temp_row) 
                if len(table) == 5:
                    self.tables.append(table)
                    table = []
    
    def table_is_winning(self, table) -> bool:
        for row in table:
            if self.rowiswinning(row):
                return True
        for colum_position in range(len(table[0])):
            temp_row = []
            for row_position in range(len(table)):
                temp_row.append(table[row_position][colum_position])
            if self.rowiswinning(temp_row):
                return True
        return False

    def rowiswinning(self, row) -> bool:
        for number in row:
            if number not in self.extracted_numbers:
                return False
        return True
        
    def sum_of_number_in_a_table(self, table) -> None:
        for row in table:
            for num in row:
                if num not in self.extracted_numbers:
                    self.num_sum += num


if __name__ == "__main__":
    print("Start")
    Day4()
    print("End")