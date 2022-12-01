class BingoBoard:
    rows: int
    cols: int

    def __init__(self, board: list[list]):
        self.board = self.make_board(board)
        self.make_board(board)
        self.rows = 5
        self.cols = 5
        self.bingo = False

    def make_board(self, board: list) -> list:
        temp = []
        for row in range(0, len(board)):
            numbers = board[row].split(" ")
            for i in numbers:
                if i == "":
                    numbers.remove("")
            for number in range(0, len(numbers)):
                temp.append(Cell(numbers[number], number, row))
        return temp

    def print_board(self):
        printed_board = "\n"
        for cell in self.board:
            if len(cell.value) == 1:
                if cell.cords[0] == 4:
                    printed_board = printed_board + cell.value + "\n"
                else:
                    printed_board = printed_board + " " + cell.value + " "
            else:
                if cell.cords[0] == 4:
                    printed_board = printed_board + cell.value + "\n"
                else:
                    printed_board = printed_board + cell.value + " "
        print(printed_board)

    def draw_number(self, number: str):
        for cell in self.board:
            # print(cell.value, number)
            if cell.value == str(number):
                cell.called = True
                # print("found it")
                if self.validate_board():
                    self.bingo = True
                    break

    def validate_board(self):
        bingo = False

        for i in range(0, self.cols):
            count = 0
            for col in range(0, self.rows):
                for cell in self.board:
                    if cell.cords[0] == i:
                        if cell.called == True:
                            count += 1
                        if count == 5:
                            bingo = True
                            return bingo
        for i in range(0, self.rows):
            count = 0
            for row in range(0, self.cols):
                for cell in self.board:
                    if cell.cords[1] == i:
                        if cell.called == True:
                            count += 1
                        if count == 5:
                            bingo = True
                            return bingo
        return bingo


class Cell:

    def __init__(self, value: int, x, y):
        self.value = value
        self.called = False
        self.cords = (x, y)


class InputHandler:
    data_in: str
    numbers: list
    raw_boards: list
    boards: list[BingoBoard]


    def __init__(self, data_in: str) -> None:
        self.data_in = data_in
        self.numbers = []
        self.raw_boards = []
        self.boards = []
        self.prepare_data()

    def prepare_data(self):
        data = self.data_in.split("\n")
        numbers = data[0].split(" ")
        print(type(numbers))
        self.numbers = numbers[0].split(",")

        data.pop(0)
        data.pop(0)

        temp = []
        for line in data:
            if line != "":
                temp.append(line)
            else:
                self.raw_boards.append(temp)
                temp = []
        self.raw_boards.append(temp)

        for board in self.raw_boards:
            self.boards.append(BingoBoard(board))




class OutputHandler:
    input_handler = InputHandler

    def __init__(self, input_handler: InputHandler):
        self.input_handler = input_handler

    def make_output(self):
        answer = ""
        print(f"Submarine gamma is {answer}")
