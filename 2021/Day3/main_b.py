class CodedData:
    data: list
    max_bit_length: int
    gamma: str
    epsilon: str
    oxygen_gen_rating: str
    co2_scrub_rating: str
    life_support_rating: str

    def __init__(self):
        self.data = []
        self.max_bit_length = 0
        self.gamma = ""
        self.epsilon = ""
        self.oxygen_gen_rating = ""
        self.co2_scrub_rating = ""
        self.life_support_rating = ""


def find_most_common_bit(list_of_binary_numbers, nth):
    zero = 0
    one = 0
    for binary_number in list_of_binary_numbers:
        if binary_number[nth] == "0":
            zero += 1
        else:
            one += 1
    if zero > one:
        return "0"
    elif zero == one:
        return "1"
    else:
        return "1"

def find_least_common_bit(list_of_binary_numbers, nth):
    zero = 0
    one = 0
    for binary_number in list_of_binary_numbers:
        if binary_number[nth] == "0":
            zero += 1
        else:
            one += 1
    if zero < one:
        return "0"
    elif zero == one:
        return "0"
    else:
        return "1"


class InputHandler:
    data_in: str
    coded_data = CodedData

    def __init__(self, data_in: str) -> None:
        self.data_in = data_in
        self.coded_data = CodedData()
        self.prepare_data()
        self.find_gamma()
        self.find_epsilon()
        self.find_oxygen_gen_rating(self.coded_data.data)
        self.find_co2_scrub_rating(self.coded_data.data)
        self.find_life_support_rating()

    def prepare_data(self):
        lines = self.data_in.split("\n")
        self.coded_data.max_bit_length = len(lines[0])
        for line in lines:
            self.coded_data.data.append(line)

    def find_gamma(self):
        for digit in range(0, self.coded_data.max_bit_length):
            self.coded_data.gamma = self.coded_data.gamma + find_most_common_bit(self.coded_data.data, digit)

    def find_epsilon(self):
        temp = ""
        for letter in self.coded_data.gamma:
            if letter == "0":
                temp = temp + "1"
            else:
                temp = temp + "0"
        self.coded_data.epsilon = temp

    def find_oxygen_gen_rating(self, possibles: list, bit=0):
        if len(possibles) == 1:
            self.coded_data.oxygen_gen_rating = str(int(possibles[0], 2))
        else:
            new_possibles = []
            common = find_most_common_bit(possibles, bit)
            for possible in possibles:
                if possible[bit] == common:
                    new_possibles.append(possible)
            self.find_oxygen_gen_rating(new_possibles, bit + 1)

    def find_co2_scrub_rating(self, possibles: list, bit=0):
        if len(possibles) == 1:
            self.coded_data.co2_scrub_rating = str(int(possibles[0], 2))
        else:
            new_possibles = []
            common = find_least_common_bit(possibles, bit)
            for possible in possibles:
                if possible[bit] == common:
                    new_possibles.append(possible)
            self.find_co2_scrub_rating(new_possibles, bit + 1)

    def find_life_support_rating(self):
        self.coded_data.life_support_rating = str(int(self.coded_data.oxygen_gen_rating) * int(self.coded_data.co2_scrub_rating))


class OutputHandler:
    input_handler = InputHandler

    def __init__(self, input_handler: InputHandler):
        self.input_handler = input_handler

    def make_output(self):
        print(
            f"Submarine life support rating is {self.input_handler.coded_data.life_support_rating}")
