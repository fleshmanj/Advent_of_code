import math


class Knot:

    def __init__(self, id):
        self.id = id
        self.current_pos = (0, 0)


class Inputhandler:

    def __init__(self, data):
        self.past_positions = [(0, 0)]
        self.data = data
        self.instructions = []
        self.knots = []
        self.rope = {}
        self.origin = (0, 0)
        self.head = Knot("H")
        self.tail = Knot("9")
        self.build_rope()

        self.parse_data()

    def parse_data(self):
        for line in self.data.splitlines():
            direction = line[0]
            distance = line[2:]
            self.instructions.append((direction, int(distance)))

    def print_board(self):
        width = [0, 0]
        height = [0, 0]
        for k, v in self.rope.items():
            if v.current_pos[0] < width[0]:
                width[0] = v.current_pos[0]
            elif v.current_pos[0] > width[1]:
                width[1] = v.current_pos[0]
            if v.current_pos[1] < height[0]:
                height[0] = v.current_pos[1]
            elif v.current_pos[1] > height[1]:
                height[1] = v.current_pos[1]

        board = ""
        for y in range(height[1], height[0] - 1, -1):
            for x in range(width[0], width[1] + 1):
                # print(x,y)
                found = False
                for k, v in self.rope.items():
                    if v.current_pos[0] == x and v.current_pos[1] == y:
                        # print(v.id, end="")
                        board = board + v.id
                        found = True
                        # print(f"found {v.id} at {x},{y}")
                        break
                if not found:
                    # print(".", end="")
                    board = board + "."
                    # print("added a .")
            # print("\n")
            board = board + "\n"
        print(board)

    def build_rope(self):
        self.knots.append(self.head.id)
        for i in range(1, 10):
            self.knots.append(str(i))
        self.knots.append(self.tail.id)

        self.rope[self.head.id] = self.head
        for i in range(1, 10):
            self.rope[str(i)] = Knot(str(i))
        self.rope[self.tail.id] = self.tail

    def traverse(self):
        for instruction in self.instructions:
            if instruction[0] == "U":
                self.move_up(instruction[1])
                # print(f"moved up {instruction[1]} spaces")
            if instruction[0] == "D":
                self.move_down(instruction[1])
                # print(f"moved down {instruction[1]} spaces")
            if instruction[0] == "L":
                self.move_left(instruction[1])
                # print(f"moved left {instruction[1]} spaces")
            if instruction[0] == "R":
                self.move_right(instruction[1])
                # print(f"moved right {instruction[1]} spaces")
            # print(self.rope["1"].current_pos)
            # self.print_board()

    def move_up(self, distance):
        for _ in range(0, distance):
            self.head.current_pos = (self.head.current_pos[0], self.head.current_pos[1] + 1)
            for index, knot in enumerate(self.knots):
                if index < len(self.knots) - 1:
                    next_knot = self.knots[index + 1]
                    self.find_relative_position("up", self.rope[knot], self.rope[next_knot])
                    # self.print_board()
            self.past_positions.append(self.tail.current_pos)

    def move_down(self, distance):
        for _ in range(0, distance):
            self.head.current_pos = (self.head.current_pos[0], self.head.current_pos[1] - 1)
            for index, knot in enumerate(self.knots):
                if index < len(self.knots) - 1:
                    next_knot = self.knots[index + 1]

                    self.find_relative_position("down", self.rope[knot], self.rope[next_knot])
            self.past_positions.append(self.tail.current_pos)

    def move_left(self, distance):
        for _ in range(0, distance):

            self.head.current_pos = (self.head.current_pos[0] - 1, self.head.current_pos[1])
            for index, knot in enumerate(self.knots):
                if index < len(self.knots) - 1:
                    next_knot = self.knots[index + 1]
                    self.find_relative_position("left", self.rope[knot], self.rope[next_knot])
            self.past_positions.append(self.tail.current_pos)

    def move_right(self, distance):
        for _ in range(0, distance):
            self.head.current_pos = (self.head.current_pos[0] + 1, self.head.current_pos[1])
            for index, knot in enumerate(self.knots):
                if index < len(self.knots) - 1:
                    next_knot = self.knots[index + 1]
                    self.find_relative_position("right", self.rope[knot], self.rope[next_knot])
                    # self.print_board()
            self.past_positions.append(self.tail.current_pos)

    def distance_from_head(self):
        distance = math.sqrt((self.tail.current_pos[0] - self.head.current_pos[0]) ** 2 + (
                self.tail.current_pos[1] - self.head.current_pos[1]) ** 2)
        return distance

    @staticmethod
    def find_relative_position(direction, current_knot: Knot, next_knot):
        distance = math.sqrt((next_knot.current_pos[0] - current_knot.current_pos[0]) ** 2 + (
                next_knot.current_pos[1] - current_knot.current_pos[1]) ** 2)
        if distance > 1.5:
            if current_knot.current_pos[0] == next_knot.current_pos[0] or current_knot.current_pos[1] == next_knot.current_pos[1]:
                if current_knot.current_pos[0] == next_knot.current_pos[0]:
                    if current_knot.current_pos[1] > next_knot.current_pos[1]:
                        next_knot.current_pos = current_knot.current_pos[0], current_knot.current_pos[1]-1
                    if current_knot.current_pos[1] < next_knot.current_pos[1]:
                        next_knot.current_pos = current_knot.current_pos[0], current_knot.current_pos[1]+1
                if current_knot.current_pos[1] == next_knot.current_pos[1]:
                    if current_knot.current_pos[0] > next_knot.current_pos[0]:
                        next_knot.current_pos = current_knot.current_pos[0]-1, current_knot.current_pos[1]
                    if current_knot.current_pos[0] < next_knot.current_pos[0]:
                        next_knot.current_pos = current_knot.current_pos[0]+1, current_knot.current_pos[1]
            else:
                if current_knot.current_pos[0] > next_knot.current_pos[0] and current_knot.current_pos[1] > next_knot.current_pos[1]:
                    next_knot.current_pos = next_knot.current_pos[0] + 1, next_knot.current_pos[1] + 1
                if current_knot.current_pos[0] < next_knot.current_pos[0] and current_knot.current_pos[1] < next_knot.current_pos[1]:
                    next_knot.current_pos = next_knot.current_pos[0] - 1, next_knot.current_pos[1] - 1
                if current_knot.current_pos[0] < next_knot.current_pos[0] and current_knot.current_pos[1] > next_knot.current_pos[1]:
                    next_knot.current_pos = next_knot.current_pos[0] - 1, next_knot.current_pos[1] + 1
                if current_knot.current_pos[0] > next_knot.current_pos[0] and current_knot.current_pos[1] < next_knot.current_pos[1]:
                    next_knot.current_pos = next_knot.current_pos[0] + 1, next_knot.current_pos[1] - 1


    @staticmethod
    def distance_from_next_knot(current_knot: Knot, next_knot: Knot):
        distance = math.sqrt((next_knot.current_pos[0] - current_knot.current_pos[0]) ** 2 + (
                next_knot.current_pos[1] - current_knot.current_pos[1]) ** 2)
        return distance
