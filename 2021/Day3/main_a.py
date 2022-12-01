class CodedData:
    data: list
    max_bit_length: int
    gamma: str
    epsilon: str

    def __init__(self):
        self.data = []
        self.max_bit_length = 0
        self.gamma = ""
        self.epsilon = ""




class InputHandler:
    data_in: str
    coded_data = CodedData

    def __init__(self, data_in: str) -> None:
        self.data_in = data_in
        self.coded_data = CodedData()
        self.prepare_data()
        self.find_gamma()
        self.find_epsilon()

    def prepare_data(self):
        lines = self.data_in.split("\n")
        self.coded_data.max_bit_length = len(lines[0])
        for line in lines:
            self.coded_data.data.append(line)

    def find_common_bit(self, nth):
        zero = 0
        one = 0
        for binary_number in self.coded_data.data:
            if binary_number[nth] == "0":
                zero += 1
            else:
                one += 1
        if zero > one:
            return "0"
        else:
            return "1"

    def find_gamma(self):
        for digit in range(0, self.coded_data.max_bit_length):
            self.coded_data.gamma = self.coded_data.gamma + self.find_common_bit(digit)

    def find_epsilon(self):
        temp = ""
        for letter in self.coded_data.gamma:
            if letter == "0":
                temp = temp + "1"
            else:
                temp = temp + "0"
        self.coded_data.epsilon = temp





class OutputHandler:
    input_handler = InputHandler

    def __init__(self, input_handler: InputHandler):
        self.input_handler = input_handler

    def make_output(self):
        answer = int(self.input_handler.coded_data.gamma, 2) * int(self.input_handler.coded_data.epsilon, 2)
        print(f"Submarine gamma is {self.input_handler.coded_data.gamma}\nSubmarine epsilon is {self.input_handler.coded_data.epsilon}\nAnswer is {answer}")
