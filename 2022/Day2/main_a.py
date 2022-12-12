from data import test_input


class InputHandler:

    def __init__(self, data):
        self.rounds = self.prepare_data(data)
        self.add_scores()

    def prepare_data(self, data):
        raw_data = data.split("\n")
        rounds = []
        for line in raw_data:
            if len(line) == 3:
                opponent, player = line[0], line[2]
                rounds.append((opponent, player))

        return rounds

    def validate(self, round):
        opponent = False
        tie = False
        player = False
        score = 0
        if round[0] == "A" and round[1] == "X" or round[0] == "B" and round[1] == "Y" or round[0] == "C" and round[
            1] == "Z":
            tie = True


        if round[0] == "A" and round[1] == "Z" or round[0] == "B" and round[1] == "X" or round[0] == "C" and round[
            1] == "Y":
            opponent = True


        if round[0] == "A" and round[1] == "Y" or round[0] == "B" and round[1] == "Z" or round[0] == "C" and round[
            1] == "X":
            player = True


        if tie:
            if round[1] == "X":
                score = 1 + 3
            elif round[1] == "Y":
                score = 2 + 3
            elif round[1] == "Z":
                score = 3 + 3

        if opponent:
            if round[1] == "X":
                score = 1
            elif round[1] == "Y":
                score = 2
            elif round[1] == "Z":
                score = 3

        elif player:
            if round[1] == "X":
                player_score = 1
            elif round[1] == "Y":
                player_score = 2
            elif round[1] == "Z":
                player_score = 3
            else:
                player_score = 0
            # print(f"{6} {player_score}")
            score = 6 + player_score

        return score

    def add_scores(self):
        score = 0
        for round in self.rounds:
            score += self.new_validate(round)
        print(score)

    def new_validate(self, round):
        opponent = False
        tie = False
        player = False
        score = 0

        if round[1] == "X":
            if round[0] == "A":
                score = 3
            if round[0] == "B":
                score = 1
            if round[0] == "C":
                score = 2
        if round[1] == "Y":
            if round[0] == "A":
                score = 4
            if round[0] == "B":
                score = 5
            if round[0] == "C":
                score = 6
        if round[1] == "Z":
            if round[0] == "A":
                score = 8
            if round[0] == "B":
                score = 9
            if round[0] == "C":
                score = 7
        return score