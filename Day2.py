def part1():
    horizontal = 0
    depth = 0
    with open("inputs/Day2.txt") as file:
        for line in file:
            line = line.split()
            command = line[0]
            amount = int(line[1])
            if command == 'forward':
                horizontal += amount
            if command == 'down':
                depth += amount
            if command == 'up':
                depth -= amount
                
    print(horizontal * depth)
    
def part2():
    horizontal = 0
    depth = 0
    aim = 0
    with open("inputs/Day2.txt") as file:
        for line in file:
            line = line.split()
            command = line[0]
            amount = int(line[1])
            if command == 'down':
                aim += amount
            if command == 'up':
                aim -= amount
            if command == 'forward':
                horizontal += amount
                depth += aim * amount
            
    print(horizontal * depth)

if __name__ == "__main__":
    part2()