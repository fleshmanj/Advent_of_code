class Member:

    def __init__(self, member):
        self.high = 0
        self.low = 0
        self.member = member
        self.find_range()

    def find_range(self):
        numbers = self.member.split("-")
        self.low = int(numbers[0])
        self.high = int(numbers[1])


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
        member1 = Member(team[0])
        member2 = Member(team[1])
        if member1.low >= member2.low and member1.high <= member2.high or member2.low >= member1.low and member2.high <= member1.high:
            self.count += 1
