class InputHandler:

    def __init__(self, input: str):
        self.input = input
        self.data = self.prepare_data()
        self.differences = []
        self.compare_lists()
        self.answer = self.add_differences()

    def prepare_data(self):
        list_of_rows = self.input.split('\n')
        list_a = []
        list_b = []
        for row in list_of_rows:
            d1, d2 = row.split('  ')
            list_a.append(d1)
            list_b.append(d2)
        list_a.sort()
        list_b.sort()
        dict_to_return = {"data_a": list_a, "data_b": list_b}
        return dict_to_return

    def compare_numbers(self, number1, number2):
        difference = abs(int(number1) - int(number2))
        return difference

    def compare_lists(self):
        list_1 = self.data["data_a"]
        list_2 = self.data["data_b"]
        for i in range(0, len(list_1)):
            self.differences.append(self.compare_numbers(list_1[i], list_2[i]))

    def add_differences(self):
        return sum(self.differences)