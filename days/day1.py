# Code done in less than 1h in live with others people, so something shitty
def day1():
    print("Day 1 Puzzles: ")
    file = open("puzzle_input/input_day1.txt")
    deep_list = file.readlines()
    deep_counter = 0

    old_deep = int(deep_list[0].rstrip())
    temp_list = []
    for deep in deep_list:
      temp_list.append(int(deep.rstrip()))
    deep_list = temp_list

    for deep in deep_list:
      if deep > old_deep:
        deep_counter +=1
      old_deep = deep
    print("First deep:", deep_counter)

    sum_A = 0
    sum_B = 0
    sum_C = 0
    sum_D = 0
    counter = 0
    deep_counter = -1

    for x in range(len(deep_list)):
      try:
        temp_sum = deep_list[x] + deep_list[x+1] + deep_list[x+2]
        counter += 1
        if counter % 4 == 0:
          sum_A = temp_sum
          if sum_A > sum_D:
            deep_counter += 1
        elif counter % 4 == 1:
          sum_B = temp_sum
          if sum_B > sum_A:
            deep_counter += 1
        elif counter % 4 == 2:
          sum_C = temp_sum
          if sum_C > sum_B:
            deep_counter += 1
        else:
          sum_D = temp_sum
          if sum_D > sum_C:
            deep_counter += 1
      except IndexError:
        break

    print("Second deep:", deep_counter)
