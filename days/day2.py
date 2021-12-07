def day2():
    print("\nDay 2 puzzles:")
    print("Part 1:")
    with open("puzzle_input/input_day2.txt") as file:
        list_of_input = file.read().split("\n")
        horizontal = 0
        depth = 0
        for move_input in list_of_input:
            direction, value = move_input.split(" ")
            value = int(value)
            if direction == "forward":
                horizontal += value
            elif direction == "up":
                depth -= value
            elif direction == "down":
                depth += value
        print("Forward:", horizontal)
        print("Depth:", depth)
        print("Values:", depth * horizontal)
        print("\nPart 2:")
        horizontal = 0
        depth = 0
        aim = 0
        for move_input in list_of_input:
            direction, value = move_input.split(" ")
            value = int(value)
            if direction == "forward":
                horizontal += value
                depth += value * aim
            elif direction == "up":
                aim -= value
            elif direction == "down":
                aim += value
        print("Forward:", horizontal)
        print("Aim:", aim)
        print("Depth:", depth)
        print("Values:", depth * horizontal)
