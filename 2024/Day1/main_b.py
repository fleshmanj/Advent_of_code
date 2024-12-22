class InputHandler:

    def __init__(self, input: str):
        self.input = input
        self.data = self.prepare_data()
        self.simularity_scores = []
        self.get_simularity_scores()
        self.answer = sum(self.simularity_scores)

    def prepare_data(self):
        list_of_rows = self.input.split('\n')
        list_a = []
        list_b = []
        for row in list_of_rows:
            d1, d2 = row.split('  ')
            list_a.append(d1.strip(" "))
            list_b.append(d2.strip(" "))
        dict_to_return = {"data_a": list_a, "data_b": list_b}
        return dict_to_return

    def get_simularity_scores(self):
        for number in self.data['data_a']:
            score = int(number) * int(self.data['data_b'].count(number))
            self.simularity_scores.append(score)