# Solutions do Day12 puzzle at https://adventofcode.com/2021
import copy


class Day12:
    def __init__(self):
        with open("puzzle_input/input_day12.txt") as file:
            self.lines = file.read().split("\n")
        file.close()
        self.joints = dict(self.create_joint())
        self.paths = list()
        self.calculate_path(["start"])
        print("Part 1: ")
        print("Total available paths:", len(self.paths))

        print("Part 2: ")
        self.paths2 = list()
        self.calculate_path_2(["start"])
        print("Total available paths:", len(self.paths2))

    def create_joint(self) -> dict:
        temp_dict = dict()
        for line in self.lines:
            temp = line.split("-")
            start, stop = temp[0], temp[1]
            try:
                temp_dict[start].append(stop)
            except KeyError:
                temp_dict[start] = [stop]
            try:
                temp_dict[stop].append(start)
            except KeyError:
                temp_dict[stop] = [start]
        return temp_dict

    def calculate_path(self, joint_visited):
        for joint in self.joints[joint_visited[-1]]:
            temp = copy.deepcopy(joint_visited)
            if joint == "end":
                temp.append(joint)
                self.paths.append(temp)
            else:
                if joint.islower() and joint in joint_visited:
                    pass
                else:
                    temp.append(joint)
                    self.calculate_path(temp)

    def calculate_path_2(self, joint_visited, double=False):
        for joint in self.joints[joint_visited[-1]]:
            temp = copy.deepcopy(joint_visited)
            if joint == "end":
                temp.append(joint)
                self.paths2.append(temp)
            else:
                if joint.islower() \
                        and joint in joint_visited\
                        and not double\
                        and joint != "start"\
                        and joint != "stop":
                    temp.append(joint)
                    self.calculate_path_2(temp, double=True)
                elif joint.islower() and joint in joint_visited:
                    pass
                else:
                    temp.append(joint)
                    self.calculate_path_2(temp, double)
