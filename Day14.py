import threading

input_string = """Rudolph 22 8 165
Cupid 8 17 114
Prancer 18 6 103
Donner 25 6 145
Dasher 11 12 125
Comet 21 6 121
Blitzen 18 3 50
Vixen 20 4 75
Dancer 7 20 119"""

test_string = """Comet 14 10 127
Dancer 16 11 162"""


def racer_with_threads(reindeer, duration: int) -> None:
    start = 0
    dist = 0
    while start < duration:
        for _ in range(int(reindeer.endurance)):
            if start < duration:
                start += 1
                dist += int(reindeer.speed)
            else:
                break
        for _ in range(int(reindeer.rest)):
            if start < duration:
                start += 1
            else:
                break
    print(f"{reindeer.name} total distance is {dist}\n")


def race_with_threads(duration: int, contestants: list) -> None:
    for i in range(len(contestants)):
        print(i)
        print(contestants[i].name)
        t = threading.Thread(target=racer_with_threads, args=[contestants[i], duration])
        t.start()


def race(duration: int, contestants: list):
    start = 0
    while start < duration:
        leader = None
        current_standings = {}
        standings = []
        if start < duration:
            for i, contestant in enumerate(contestants):
                contestant.tick_racer()
            for i, contestant in enumerate(contestants):
                current_standings[i] = contestant.dist
            farthest = sorted(current_standings.items(), key=lambda x: x[1], reverse=True)
            leader = farthest[0][1]
            for i in farthest:
                distance = i[1]
                if distance == leader:
                    contestants[i[0]].points += 1
                    standings.append(contestants[i[0]].name)
            print(leader)

            # leader = leader[0]
            # contestants[leader].points += 1
            # print(sorted(current_standings.items(), key=lambda x: x[1], reverse=True))
            print("_________________________________________")
        start += 1
    for i in range(len(contestants)):
        print(contestants[i].points, contestants[i].name, contestants[i].dist)


class Reindeer:
    def __init__(self, name, speed, endurance, rest):
        self.name = name
        self.speed = int(speed)
        self.endurance = int(endurance)
        self.rest = int(rest)
        self.dist = 0
        self.current_endurance = 0
        self.current_rest = 0
        self.running = True
        self.points = 0

    def tick_racer(self):
        if self.running:
            if self.current_endurance < self.endurance:
                self.current_endurance += 1
                self.dist += self.speed
            else:
                self.current_endurance = 0
                self.running = False
        if not self.running:
            if self.current_rest < self.rest:
                self.current_rest += 1
            else:
                self.current_rest = 0
                self.current_endurance += 1
                self.dist += self.speed
                self.running = True


if __name__ == "__main__":
    lines = input_string.split("\n")

    lines = [line.split(" ") for line in lines]
    reindeers = []
    for line in lines:
        reindeer = Reindeer(line[0], line[1], line[2], line[3])
        reindeers.append(reindeer)

    print(race(2503, reindeers))
    # racer()
