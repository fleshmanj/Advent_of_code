import random
class Person:

    def __init__(self, name):
        self.name = name
        self.happiness = 0


input_string = """Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 81 happiness units by sitting next to Carol.
Alice would lose 42 happiness units by sitting next to David.
Alice would gain 89 happiness units by sitting next to Eric.
Alice would lose 89 happiness units by sitting next to Frank.
Alice would gain 97 happiness units by sitting next to George.
Alice would lose 94 happiness units by sitting next to Mallory.
Alice would gain 0 happiness units by sitting next to Joshua.
Bob would gain 3 happiness units by sitting next to Alice.
Bob would lose 70 happiness units by sitting next to Carol.
Bob would lose 31 happiness units by sitting next to David.
Bob would gain 72 happiness units by sitting next to Eric.
Bob would lose 25 happiness units by sitting next to Frank.
Bob would lose 95 happiness units by sitting next to George.
Bob would gain 11 happiness units by sitting next to Mallory.
Bob would gain 0 happiness units by sitting next to Joshua.
Carol would lose 83 happiness units by sitting next to Alice.
Carol would gain 8 happiness units by sitting next to Bob.
Carol would gain 35 happiness units by sitting next to David.
Carol would gain 10 happiness units by sitting next to Eric.
Carol would gain 61 happiness units by sitting next to Frank.
Carol would gain 10 happiness units by sitting next to George.
Carol would gain 29 happiness units by sitting next to Mallory.
Carol would gain 0 happiness units by sitting next to Joshua.
David would gain 67 happiness units by sitting next to Alice.
David would gain 25 happiness units by sitting next to Bob.
David would gain 48 happiness units by sitting next to Carol.
David would lose 65 happiness units by sitting next to Eric.
David would gain 8 happiness units by sitting next to Frank.
David would gain 84 happiness units by sitting next to George.
David would gain 9 happiness units by sitting next to Mallory.
David would gain 0 happiness units by sitting next to Joshua.
Eric would lose 51 happiness units by sitting next to Alice.
Eric would lose 39 happiness units by sitting next to Bob.
Eric would gain 84 happiness units by sitting next to Carol.
Eric would lose 98 happiness units by sitting next to David.
Eric would lose 20 happiness units by sitting next to Frank.
Eric would lose 6 happiness units by sitting next to George.
Eric would gain 60 happiness units by sitting next to Mallory.
Eric would gain 0 happiness units by sitting next to Joshua.
Frank would gain 51 happiness units by sitting next to Alice.
Frank would gain 79 happiness units by sitting next to Bob.
Frank would gain 88 happiness units by sitting next to Carol.
Frank would gain 33 happiness units by sitting next to David.
Frank would gain 43 happiness units by sitting next to Eric.
Frank would gain 77 happiness units by sitting next to George.
Frank would lose 3 happiness units by sitting next to Mallory.
Frank would gain 0 happiness units by sitting next to Joshua.
George would lose 14 happiness units by sitting next to Alice.
George would lose 12 happiness units by sitting next to Bob.
George would lose 52 happiness units by sitting next to Carol.
George would gain 14 happiness units by sitting next to David.
George would lose 62 happiness units by sitting next to Eric.
George would lose 18 happiness units by sitting next to Frank.
George would lose 17 happiness units by sitting next to Mallory.
George would gain 0 happiness units by sitting next to Joshua.
Mallory would lose 36 happiness units by sitting next to Alice.
Mallory would gain 76 happiness units by sitting next to Bob.
Mallory would lose 34 happiness units by sitting next to Carol.
Mallory would gain 37 happiness units by sitting next to David.
Mallory would gain 40 happiness units by sitting next to Eric.
Mallory would gain 18 happiness units by sitting next to Frank.
Mallory would gain 7 happiness units by sitting next to George.
Mallory would gain 0 happiness units by sitting next to Joshua.
Joshua would lose 0 happiness units by sitting next to Alice.
Joshua would gain 0 happiness units by sitting next to Bob.
Joshua would lose 0 happiness units by sitting next to Carol.
Joshua would gain 0 happiness units by sitting next to David.
Joshua would gain 0 happiness units by sitting next to Eric.
Joshua would gain 0 happiness units by sitting next to Frank.
Joshua would gain 0 happiness units by sitting next to George.
Joshua would gain 0 happiness units by sitting next to Mallory."""

traits = input_string.split("\n")

people = []

for line in traits:
    line = line.split(" ")
    if line[0] not in people:
        people.append(line[0])

for i, person in enumerate(people):
    people[i] = Person(person)

for line in traits:
    line = line.split(" ")
    for person in people:
        if line[0] == person.name:
            if line[2] == "gain":
                person.__setattr__(line[10][:-1], int(line[3]))
            else:
                person.__setattr__(line[10][:-1], int(line[3]) - int(line[3]) * 2)


runs = 100000
highscore = 0
for _ in range(runs):
    random.shuffle(people)
    score = 0
    for i, person in enumerate(people):
        if i < len(people) - 1:
            # print(person.__dict__)
            # print(person.__getattribute__(people[i - 1].name), person.name, person.__getattribute__(people[i + 1].name))
            # print(person.name, person.__getattribute__(people[i - 1].name) + person.__getattribute__(people[i + 1].name))
            score += person.__getattribute__(people[i - 1].name) + person.__getattribute__(people[i + 1].name)
        else:
            # print(people[i - 1].name, person.name, people[0].name)
            # print(person.name, person.__getattribute__(people[i - 1].name) + person.__getattribute__(people[i + 1].name))
            score += person.__getattribute__(people[i - 1].name) + person.__getattribute__(people[0].name)
    if score > highscore:
        highscore = score

print(highscore)

# for person in people:
#     print(person.__dict__)


