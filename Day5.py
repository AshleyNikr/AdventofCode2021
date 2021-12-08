import re

def calculate(map):
    sum = 0
    for row in map:
        for point in row:
            try:
                if point > 1:
                    sum += 1
            except:
                pass
    return sum

def subtract(a, b):
    return a - b

def add(a, b):
    return a + b

def part1():
    with open("inputs/Day5.txt") as file:
        lines = []
        highest_x = 0
        highest_y = 0
        for line in file:
            line = re.findall(r'[0-9]+', line)
            if (line[0] == line[2] or line[1] == line[3]) or abs(int(line[0]) - int(line[2])) == abs(int(line[1]) - int(line[3])):
                lines.append(line)
            # find highest x
            for el in line[::2]:
                if int(el) > highest_x:
                    highest_x = int(el)
            # find highest y
            for el in line[1::2]:
                if int(el) > highest_y:
                    highest_y = int(el)
    map = [['.' for _ in range(highest_x + 1)] for _ in range(highest_y + 1)]
    print(lines)
    for line in lines:
        x1 = int(line[0])
        y1 = int(line[1])
        x2 = int(line[2])
        y2 = int(line[3])
        bound = 0
        if x1 == x2:
            if y1 < y2:
                bound = range(y1, y2 + 1)
            else:
                bound = range(y2, y1 + 1)
            for k in bound:
                if map[k][x1] == '.':
                    map[k][x1] = 1
                else:
                    map[k][x1] += 1         
        elif y1 == y2:
            if x1 < x2:
                bound = range(x1, x2 + 1)
            else:
                bound = range(x2, x1 + 1)
            for k in bound:
                if map[y1][k] == '.':
                    map[y1][k] = 1
                else:
                    map[y1][k] += 1
        else:
            if x1 < x2:
                start_x = x1
                x_operator = add
            else:
                start_x = x1
                x_operator = subtract
            
            if y1 < y2:
                start_y = y1
                y_operator = add
            else:
                start_y = y1
                y_operator = subtract
            for k in range(abs(x1 - x2) + 1):
                x = x_operator(start_x, k)
                y = y_operator(start_y, k)
                if map[y][x] == '.':
                    map[y][x] = 1
                else:
                    map[y][x] += 1
    for row in map:
        print(row)
    print(calculate(map))
    
if __name__ == "__main__":
    part1()