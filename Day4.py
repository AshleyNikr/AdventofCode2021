class Board():
    __slots__ = ['__win', '__spaces']
    def __init__(self, spaces):
        self.__spaces = spaces
        self.__win = False
        
    def check_win(self):
        # horizontal    
        for i in range(len(self.__spaces)):
            for k in range(len(self.__spaces)):
                win = True
                if self.__spaces[i][k].check_marked() == False:
                    win = False
                    break
            if win == True:
                return True
        # vertical
        for i in range(len(self.__spaces)):
            for k in range(len(self.__spaces)):
                win = True
                if self.__spaces[k][i].check_marked() == False:
                    win = False
                    break
            if win == True:
                return True

    def get_spaces(self):
        return self.__spaces
    
    def set_win(self):
        self.__win = True
        
    def get_win(self):
        return self.__win
    
    def __repr__(self):
        rows = ""
        for row in self.__spaces:
            rows += "\n" + str(row)
        return rows

    
class Space():
    __slots__ = ['__value', '__marked']
    def __init__(self, value):
        self.__value = value
        self.__marked = False
        
    def check_value(self, called_num):
        if self.__value == int(called_num):
            self.__marked = True
            
    def check_marked(self):
        return self.__marked
    
    def get_value(self):
        return self.__value

    def __repr__(self):
        return str(self.__value)

def calculate_score(board):
    sum = 0
    for row in board.get_spaces():
        for space in row:
            if space.check_marked() == False:
                sum += space.get_value()
    return sum

def part1():
    with open("inputs/Day4.txt") as file:
        bingo_nums = next(file).split(",")
        board = []
        bingo_boards = []
        for line in file:
            line = line.strip()
            if len(line) > 0:
                line = line.split()
                for i in range(len(line)):
                    line[i] = Space(int(line[i]))
                board.append(line)
                if len(board) == 5:
                    bingo_boards.append(Board(board))
                    board = []

    for num in bingo_nums:
        for bingo_board in bingo_boards:
            for row in bingo_board.get_spaces():
                for space in row:
                    space.check_value(num)
            if bingo_board.check_win() == True:
                return bingo_board, num
            
def part2():
    with open("inputs/Day4.txt") as file:
        bingo_nums = next(file).split(",")
        board = []
        bingo_boards = []
        for line in file:
            line = line.strip()
            if len(line) > 0:
                line = line.split()
                for i in range(len(line)):
                    line[i] = Space(int(line[i]))
                board.append(line)
                if len(board) == 5:
                    bingo_boards.append(Board(board))
                    board = []

    winless_board = Board([])
    for num in bingo_nums:
        for bingo_board in bingo_boards:
            for row in bingo_board.get_spaces():
                for space in row:
                    space.check_value(num)
            if bingo_board.check_win() == True:
                bingo_board.set_win()
            res = check_last(bingo_boards)
            if res != None:
                winless_board = res
            if winless_board.get_win() == True:
                return winless_board, num
            
def check_last(boards):
    count = 0
    winless = None
    for board in boards:
        if board.get_win() == False:
            winless = board
            count += 1
    if count == 1:
        return winless
                   
if __name__ == "__main__":
    # winning_board, winning_num = part1()
    # print(winning_board)
    # sum = calculate_score(winning_board)
    # print(sum)
    # print(int(winning_num) * sum)
    winning_board, num = part2()
    print(winning_board)
    res = calculate_score(winning_board)
    print(res * int(num))