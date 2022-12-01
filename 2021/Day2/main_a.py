class Submarine:
    current_y: int
    current_x: int

    def __init__(self):
        self.current_x = 0
        self.current_y = 0

    def move_forward(self, distance: int) -> None:
        self.current_x += distance

    def move_up(self, distance) -> None:
        self.current_y -= distance

    def move_down(self, distance) -> None:
        self.current_y += distance


class InputHandler:
    data_in: str
    submarine: Submarine
    move_sequence: list

    def __init__(self, data_in: str, submarine: Submarine):
        self.data_in = data_in
        self.submarine = submarine
        self.move_sequence = []

    def make_move_sequence(self):
        temp = self.data_in.split("\n")
        for line in temp:
            movement_type, distance = line.split(" ")
            self.move_sequence.append([movement_type, int(distance)])

    def move_sub(self) -> None:
        for instruction in self.move_sequence:
            self.move_direction(instruction[0], instruction[1])

    def move_direction(self, instruction_direction, distance):
        if instruction_direction == "up":
            self.submarine.move_up(distance)
        if instruction_direction == "down":
            self.submarine.move_down(distance)
        if instruction_direction == "forward":
            self.submarine.move_forward(distance)


class OutputHandler:
    input_handler: InputHandler
    output: str

    def __init__(self, input_handler: InputHandler):
        self.input_handler = input_handler
        self.output = ""

    def get_sub_position(self) -> None:
        position = self.input_handler.submarine.current_y * self.input_handler.submarine.current_x
        self.output = f"Submarine depth times Submarine horizontal = {position}"
