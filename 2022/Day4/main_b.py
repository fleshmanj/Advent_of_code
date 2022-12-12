class Member:
    numbers: list

    def __init__(self, member):
        self.high = 0
        self.low = 0
        self.numbers = []
        self.member = member
        self.find_range()

    def find_range(self):
        numbers = self.member.split("-")
        self.low = int(numbers[0])
        self.high = int(numbers[1])
        for i in range(self.low, self.high + 1):
            self.numbers.append(i)


class InputHandler:
    input: str

    def __init__(self, input):
        self.count = 0
        self.input = input
        self.teams = []
        self.prepare_data()
        self.find_overlaps()
        print(self.count)

    def prepare_data(self):
        for line in self.input.splitlines():
            self.teams.append(line)

    def find_overlaps(self):
        for team in self.teams:
            self.analyze_team(team)

    def analyze_team(self, team: str):
        team = team.split(",")
        # print(team[0], team[1])
        member1 = Member(team[0])
        member2 = Member(team[1])

        for i in member1.numbers:
            if i in member2.numbers:
                self.count += 1
                break
