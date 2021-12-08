class LanternFish():
    __slots__ = ['__timer']
    def __init__(self, timer=8):
        self.__timer = int(timer)
        
    def check_timer(self):
        if self.__timer == 0:
            self.__timer = 6
            return True
        self.__timer -= 1
        return False

    def __repr__(self):
        return self.__timer

def part1():
    with open("inputs/Day6.txt") as file:
        list_fish = next(file).split(',')
        
    for i in range(len(list_fish)):
        list_fish[i] = LanternFish(list_fish[i])
        
    for i in range(256):
        new_fish = []
        for fish in list_fish:
            if fish.check_timer() == True:
                new_fish.append(LanternFish())
        list_fish.extend(new_fish)
    print(len(list_fish))
    
def part2():
    with open("inputs/Day6.txt") as file:
        list_fish = next(file).split(',')
        
    fish_count = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for value in list_fish:
        fish_count[int(value)] += 1
    print("Initial state:", fish_count)

    for j in range(256):
        new_fish = fish_count[0]
        for i in range(7):
            fish_count[i] = fish_count[i + 1]
        fish_count[6] += new_fish
        fish_count[7] = fish_count[8]
        fish_count[8] = new_fish
        print("After ", j + 1, "day: ", fish_count)
    sum = 0
    for num in fish_count:
        sum += num
    print("Total fish:", sum)
if __name__ == "__main__":
    # part1()
    part2()