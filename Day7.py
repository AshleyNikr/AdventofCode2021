def part1():
    with open("inputs/Day7.txt") as file:
        crabs = next(file).split(',')
    highest_pos = 0
    for value in crabs:
        if int(value) > highest_pos:
            highest_pos = int(value)
    
    lowest_fuel = 100000000000000000000000000000000000000000000000000
    for i in range(0, highest_pos + 1):
        fuel = 0
        for value in crabs:
            distance = abs(int(value)-i)
            sum = 0
            for k in range(0, distance + 1):
                sum += k
                fuel += k
        if fuel < lowest_fuel:
            lowest_fuel = fuel
    print(lowest_fuel)
    
if __name__ == "__main__":
    part1()