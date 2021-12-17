# Solutions do Day17 puzzle at https://adventofcode.com/2021
import time


class Target:
    def __init__(self, x_range, y_range):
        self.max_x = int(max(x_range))
        self.min_x = int(min(x_range))
        self.max_y = int(max(y_range))
        self.min_y = int(min(y_range))

    def is_hit(self, position):
        """Positions must be an array or touple with 2 integer values"""
        if self.min_x <= position[0] <= self.max_x:
            if self.min_y <= position[1] <= self.max_y:
                return True
        return False

    def is_over(self, position):
        """Positions must be an array or touple with 2 integer values"""
        if position[0] > self.max_x:
            return True
        if position[1] < self.min_y:
            return True
        return False


class Day17:
    def __init__(self):
        with open("puzzle_input/input_day17.txt") as file:
            lines = file.readlines()
        file.close()
        x_range, y_range = self.parse_input(lines[0].replace("\n", ""))
        self.target = Target(x_range, y_range)
        self.main()

    def main(self):
        max_y = (0, 0, 0)
        good_shots = []
        for x in range(1, 500):
            for y in range(-110, 500):
                #time.sleep(0.001)
                result = self.shoot_calculation((x, y))
                if result is not False:
                    good_shots.append((x, y, result))
                    max_y = (x, y, result) if result > max_y[2] else max_y
        print("max_y:", max_y)
        print(good_shots)
        print("good shoots:", len(good_shots))

    def shoot_calculation(self, shoot_velocity):
        shoot_velocity, bullet_position = self.shoot_probe(shoot_velocity, (0, 0))
        count = 1
        max_y = 0
        while True:
            if bullet_position[1] > max_y:
                max_y = bullet_position[1]
            if self.target.is_over(bullet_position) is True:
                #print(f"MISS! after {count} step:", bullet_position)
                return False
            elif self.target.is_hit(bullet_position):
                #print(f"HIT! after {count} step:", bullet_position, max_y)
                return max_y
            count += 1
            shoot_velocity, bullet_position = self.shoot_probe(shoot_velocity, bullet_position)

    @staticmethod
    def shoot_probe(velocity, start_position):
        new_position = [start_position[0] + velocity[0], start_position[1] + velocity[1]]
        if velocity[0] < 0:
            new_velocity = (velocity[0] + 1, velocity[1] - 1)
        elif velocity[0] > 0:
            new_velocity = (velocity[0] - 1, velocity[1] - 1)
        else:
            new_velocity = (velocity[0], velocity[1] - 1)
        return new_velocity, new_position

    @staticmethod
    def parse_input(line):
        temp = line.replace("target area: ", "").split(",")
        temp = [x.split("=") for x in temp]
        x_range = temp[0][1].split("..")
        y_range = temp[1][1].split("..")
        return x_range, y_range
