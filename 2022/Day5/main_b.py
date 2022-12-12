class Stack:

    def __init__(self, id: str, index_location: str):
        self.id = id
        self.index_location = index_location
        self.stack = []

    def remove_top_container(self):
        container = self.stack.pop()
        return container

    def add_container(self, container_id):
        self.stack.append(container_id)


class Crane:

    def __init__(self):
        self.bucket = ""

    def transfer_containers(self, containers, target: Stack, source: Stack):
        temp = []
        for i in range(0, containers):
            temp.append(source.remove_top_container())
        for i in range(0, len(temp)):
            target.add_container(temp.pop())


class Inputhandler:
    stacks: dict
    instructions: list[tuple]
    crane: Crane

    def __init__(self, data: str):
        self.crane = Crane()
        self.data = data
        self.clean_data = []
        self.stacks = {}
        self.instructions = []
        self.parse_data()
        self.execute_instructions()

    def parse_data(self):

        # Split the starting state from the instructions into 2 separate strings
        temp = ""
        for line in self.data.splitlines():
            temp = temp + line + "\n"
            if line == "":
                self.clean_data.append(temp)
                temp = ""

        # strip the last line of the starting state to find how many stacks we have
        lines = self.clean_data[0].splitlines()
        for line in lines:
            if line == "":
                lines.pop()
        numbers = lines[-1]

        # Found how many stacks we need and create an instance for each stack and store them in a dictionary as well as
        # keep a record of the string index to locate the correct container above
        for i in range(0, len(numbers)):
            if numbers[i].isnumeric():
                temp = Stack(numbers[i], str(i))
                self.stacks[numbers[i]] = temp

        # Build a list of instructions as a tuple
        for line in self.clean_data[1].splitlines():
            temp = ""
            if line != "":
                elements = line.split(" ")
                temp = (elements[1], elements[3], elements[5])
                self.instructions.append(temp)

        # Poplulate stacks with containers from input
        for i in range(0, len(lines) - 1):
            for k, v in self.stacks.items():
                if lines[-i - 2][int(v.index_location)].isalpha():
                    v.add_container(lines[-i - 2][int(v.index_location)])


    def execute_instructions(self):
        for instruction in self.instructions:
            target = self.stacks[instruction[2]]
            source = self.stacks[instruction[1]]
            self.crane.transfer_containers(int(instruction[0]), target, source)

    def find_top_containers(self):
        result = ""
        for _, stack in self.stacks.items():
            result = result + stack.stack[-1]
        return result
