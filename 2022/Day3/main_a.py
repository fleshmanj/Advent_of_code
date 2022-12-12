class InputHandler:
    data: str
    sacks: list
    common_items: list
    score: int

    def __init__(self, data:str):
        self.data = data
        self.sacks = []
        self.common_items = []
        self.score = 0
        self.prepare_data()
        self.score_items()

    def prepare_data(self):
        for line in self.data.splitlines():
            slot1 = line[:int(len(line)/2)]
            slot2 = line[int(len(line)/2):]

            for letter in slot1:
                if letter in slot2:
                    self.common_items.append(letter)
                    break

    def score_items(self):
        score = 0
        for letter in self.common_items:
            if letter.islower():
                score += ord(letter)-96
            if letter.isupper():
                score += ord(letter) - 38
        self.score = score

