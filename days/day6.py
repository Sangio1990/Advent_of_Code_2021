# Solutions do Day6 puzzle at https://adventofcode.com/2021
import numpy as np
import copy

class Day6:
    def __init__(self) -> None:
        print("\nDay6")
        #with open("puzzle_input/input_day6_test.txt") as file:
        with open("puzzle_input/input_day6.txt") as file:
            fish_timers = np.array([int(timer) for timer in file.read().split(",")])
        file.close()
        self.fish_number = fish_timers.size
        fish_dict = {
            0: 0,
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0
                      }
        for fish in fish_timers:
            fish_dict[fish] += 1
        for x in range(80):
            fish_dict = self.the_day_after_dict(fish_dict)
        total_fish = 0
        for x in fish_dict:
            total_fish += fish_dict[x]
        print("Fish counter after 80 days", total_fish)
        for x in range(176):
            fish_dict = self.the_day_after_dict(fish_dict)
        total_fish = 0
        for x in fish_dict:
            total_fish += fish_dict[x]
        print("Fish counter after 256 days", total_fish)

    @staticmethod
    def the_day_after(fish_timers) -> np.array:
        # old method with list
        for x in range(fish_timers.size):
            if fish_timers[x] == 0:
                fish_timers[x] = 6
                fish_timers = np.append(fish_timers, 8)
            else:
                fish_timers[x] -= 1
        return fish_timers

    @staticmethod
    def the_day_after_dict(fish_dict: dict) -> dict:
        # new and faster version with dictionaries
        new_dict = {}
        for fish_timer in sorted(fish_dict, reverse=True):
            if fish_timer == 0:
                new_dict[8] = fish_dict[fish_timer]
                new_dict[6] += fish_dict[fish_timer]
            else:
                new_dict[fish_timer - 1] = fish_dict[fish_timer]
        return new_dict


if __name__ == "__main__":
    Day6()
