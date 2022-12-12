class InputHandler:
    data: str
    sacks: list
    common_items: list
    score: int

    def __init__(self, data: str):
        self.data = data
        self.sacks = []
        self.common_items = []
        self.score = 0
        self.prepare_data()
        self.score_items()

    def prepare_data(self):
        data = self.data.splitlines()
        groups = []
        for number in range(0, len(data)):
            if number % 3 == 0:
                if number <= len(data) - 2:
                    groups.append([data[number], data[number + 1], data[number + 2]])
        for group in groups:
            for letter in group[0]:
                if letter in group[1] and letter in group[2]:
                    self.common_items.append(letter)
                    break

    def score_items(self):
        score = 0
        for letter in self.common_items:
            if letter.islower():
                score += ord(letter) - 96
            if letter.isupper():
                score += ord(letter) - 38
        self.score = score
