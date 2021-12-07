with open("inputs/Day1") as file:
    count = 0
    prev_depth = int(next(file))
    for line in file:
        curr_depth = int(line)
        if curr_depth > prev_depth:
            count += 1
        prev_depth = curr_depth
    print(count)