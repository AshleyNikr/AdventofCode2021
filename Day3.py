def part1():
    with open("inputs/Day3.txt") as file:
        gamma_rate = ""
        epsilon_rate = ""
        for i in range(12):
            zero_bit = 0
            one_bit = 0
            file.seek(0, 0)
            for line in file:
                if line[i] == '0':
                    zero_bit += 1
                if line[i] == '1':
                    one_bit += 1
            if one_bit > zero_bit:
                gamma_rate += '1'
                epsilon_rate += '0'
            else:
                gamma_rate += '0'
                epsilon_rate += '1'
        int_gamma = int(gamma_rate, 2)
        int_epsilon = int(epsilon_rate, 2)
        print(int_gamma * int_epsilon)

def purge(chosen_bit, index, list):
    for el in list:
        if el[index] != chosen_bit:
            list.remove(el)
            purge(chosen_bit, index, list)

def part2():
    with open("inputs/Day3.txt") as file:
        o_candidates = []
        for line in file:
            o_candidates.append((line.strip()))
    i = 0
    while True:
        i = i % 12
        for _ in range(len(o_candidates)):
            chosen_bit = 0
            zero_bit = 0
            one_bit = 0
            for line in o_candidates:
                if line[i] == '0':
                    zero_bit += 1
                if line[i] == '1':
                    one_bit += 1
            if zero_bit > one_bit:
                chosen_bit = '0'
            else:
                chosen_bit = '1'
        purge(chosen_bit, i, o_candidates)
        i += 1
        if len(o_candidates) == 1:
            break
                
    with open("inputs/Day3.txt") as file:
        c_candidates = []
        for line in file:
            c_candidates.append((line.strip()))
    i = 0
    while True:
        i = i % 12
        for _ in range(len(c_candidates)):
            chosen_bit = 0
            zero_bit = 0
            one_bit = 0
            for line in c_candidates:
                if line[i] == '0':
                    zero_bit += 1
                if line[i] == '1':
                    one_bit += 1
            if one_bit < zero_bit:
                chosen_bit = '1'
            else:
                chosen_bit = '0'
        purge(chosen_bit, i, c_candidates)
        i += 1
        if len(c_candidates) == 1:
            break
    
    print(c_candidates, o_candidates)
    c = int(c_candidates[0], 2)
    o = int(o_candidates[0], 2)
    print(c * o)
    
    

if __name__ == "__main__":
    part2()
            