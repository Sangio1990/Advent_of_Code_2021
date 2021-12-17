# Solutions do Day7 puzzle at https://adventofcode.com/2021
import copy


class Day7:
    def __init__(self):
        with open("puzzle_input/input_day7.txt") as file:
            self.crab_starting_positions = [int(x) for x in file.read().split(",")]
        file.close()
        fuel_cost = dict()
        exponential_fuel_cost = dict()
        for x in range(max(self.crab_starting_positions)):
            fuel_cost[x] = 0
            exponential_fuel_cost[x] = 0
        for position in fuel_cost:
            fuel_cost[position] = self.crab_fuel_cost_calculator(position)
        print(fuel_cost)
        print("Best position:", list(fuel_cost.keys())[list(fuel_cost.values()).index(min(fuel_cost.values()))], "cost:", min(fuel_cost.values()))

        print("\nPart 2")
        for position in exponential_fuel_cost:
            exponential_fuel_cost[position] = self.crab_exponential_fuel_cost_calculator(position)
        print(exponential_fuel_cost)
        print("Best position:", list(exponential_fuel_cost.keys())[list(exponential_fuel_cost.values()).index(min(exponential_fuel_cost.values()))],
              "cost:", min(exponential_fuel_cost.values()))

    def crab_fuel_cost_calculator(self, position) -> int:
        fuel_cost = 0
        for crab_position in self.crab_starting_positions:
            fuel_cost += abs(crab_position-position)
        return fuel_cost

    def crab_exponential_fuel_cost_calculator(self, position):
        fuel_cost = 0
        for crab_position in self.crab_starting_positions:
            delta = abs(crab_position - position)
            fuel_cost += self.cost_calculator(delta, delta)
        return fuel_cost

    @staticmethod
    def cost_calculator(start, stop):
        return int(((start*stop)-(stop/2)*(stop+1))+start)
