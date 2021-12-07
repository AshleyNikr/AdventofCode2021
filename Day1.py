def part1():
    with open("inputs/Day1") as file:
        count = 0
        prev_depth = int(next(file))
        for line in file:
            curr_depth = int(line)
            if curr_depth > prev_depth:
                count += 1
            prev_depth = curr_depth
        print(count)
        
def compare_sum(a, b):
    sum_a = 0
    sum_b = 0
    for el in a:        
        sum_a += el
        
    for el in b:
        sum_b += el
        
    return sum_b > sum_a

def part2():
    with open("inputs/Day1") as file:
        count = 0
        prev_depth = []
        curr_depth = []
        for _ in range(3):
            prev_depth.append(int(next(file)))
        for line in file:
            curr_depth = prev_depth[1:]
            curr_depth.append(int(line))
            if compare_sum(prev_depth, curr_depth):
                count += 1
            prev_depth = curr_depth
        print(count)

if __name__ == "__main__":
    part2()