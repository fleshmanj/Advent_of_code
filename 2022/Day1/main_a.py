class InputHandler:

    def __init__(self, input: str):
        self.input = input
        self.elves = []
        self.prepare_data()
        self.find_highest(self.elves)
        self.find_top_three(self.elves)

    def prepare_data(self):
        temp = []
        elf = []
        elf_count = 0

        for line in self.input.split("\n"):
            if line == "":
                elf.append(temp)
                elf_count += 1
                temp = []
            else:
                temp.append(int(line))
        self.elves = elf

    def find_highest(self, elves):
        highest = 0
        for elf in elves:
            if sum(elf) > highest:
                highest = sum(elf)
        print(highest)
        return highest

    def find_top_three(self, elves):
        scores = []
        for elf in elves:
            scores.append(sum(elf))
        scores.sort()
        top_three_total = scores[-1] + scores[-2] + scores[-3]
        print(top_three_total)
