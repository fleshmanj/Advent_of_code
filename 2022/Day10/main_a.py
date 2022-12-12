import logging

logging.basicConfig(filename="testing_log.txt", level=logging.DEBUG)


class Clock:

    def __init__(self):
        self.cycles = 1
        self.state = "tock"

    def cycle(self):
        self.cycles += 1
        if self.state == "tick":
            self.state = "tock"
        else:
            self.state = "tick"


class CPU:
    clock: Clock

    def __init__(self):
        self.clock = Clock()
        self.value = 1
        self.signals = [1]

    def addx(self, V):
        self.clock.cycle()
        self.clock.cycle()
        self.signals.append(self.value)
        self.value += V
        self.signals.append(self.value)

    def noop(self):
        self.clock.cycle()
        self.signals.append(self.value)


class CRT:

    def __init__(self):
        self.screen_width = 40

    def draw_screen(self, signal, commands: list):
        string_to_print = "\n"
        for i, value in enumerate(signal):
            cycle = (i + 1) % 40
            pixel = cycle-1

            if pixel == -1:
                pixel = 39

            print(pixel, [value - 1, value, value + 1])
            if pixel in [value - 1, value, value + 1]:
                # print(f"cycle {cycle} pixel is {pixel}, values {[value - 1, value, value + 1]}")
                string_to_print = string_to_print + "#"
            else:
                string_to_print = string_to_print + "."
            # else:
            #     print("not printing",pixel, [value - 1, value, value + 1])
            #     string_to_print = string_to_print + "."
            if cycle % 40 == 0:
                string_to_print = string_to_print + "\n"
        print(string_to_print)
###...###...###...###...###...###...###.

class InputHandler:
    data: str
    crt = CRT()

    def __init__(self, data, cycles_to_record: list):
        self.cycles_to_record = cycles_to_record
        self.cpu = CPU()
        self.crt = CRT()
        self.data = data
        self.instructions = []
        self.cpu_instructions = ["not noop"]
        self.parse_data()
        self.signal_strengths = []
        self.run_cpu()
        self.crt.draw_screen(self.cpu.signals, self.cpu_instructions)

    def parse_data(self):
        for line in self.data.splitlines():
            if line.startswith("noop"):
                self.instructions.append(line)
            else:
                _, number = line.split(" ")
                self.instructions.append(int(number))

    def execute_instruction(self):
        instruction = self.instructions.pop(0)
        if instruction != "noop":
            self.cpu.addx(instruction)
            self.cpu_instructions.append("not noop")
            self.cpu_instructions.append("not noop")
        else:
            self.cpu.noop()
            self.cpu_instructions.append("noop")

    def find_signal_strengths(self):
        sum_of_signals = 0
        for cycle in self.cycles_to_record:
            print(f"adding {self.cpu.signals[cycle]}")
            sum_of_signals += self.cpu.signals[cycle] * cycle
        print(sum_of_signals)

    def run_cpu(self):
        running = True
        while running:
            self.execute_instruction()
            if len(self.instructions) == 0:
                running = False
