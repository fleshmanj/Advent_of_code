test_input = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

raw_input = """Monkey 0:
  Starting items: 98, 70, 75, 80, 84, 89, 55, 98
  Operation: new = old * 2
  Test: divisible by 11
    If true: throw to monkey 1
    If false: throw to monkey 4

Monkey 1:
  Starting items: 59
  Operation: new = old * old
  Test: divisible by 19
    If true: throw to monkey 7
    If false: throw to monkey 3

Monkey 2:
  Starting items: 77, 95, 54, 65, 89
  Operation: new = old + 6
  Test: divisible by 7
    If true: throw to monkey 0
    If false: throw to monkey 5

Monkey 3:
  Starting items: 71, 64, 75
  Operation: new = old + 2
  Test: divisible by 17
    If true: throw to monkey 6
    If false: throw to monkey 2

Monkey 4:
  Starting items: 74, 55, 87, 98
  Operation: new = old * 11
  Test: divisible by 3
    If true: throw to monkey 1
    If false: throw to monkey 7

Monkey 5:
  Starting items: 90, 98, 85, 52, 91, 60
  Operation: new = old + 7
  Test: divisible by 5
    If true: throw to monkey 0
    If false: throw to monkey 4

Monkey 6:
  Starting items: 99, 51
  Operation: new = old + 1
  Test: divisible by 13
    If true: throw to monkey 5
    If false: throw to monkey 2

Monkey 7:
  Starting items: 98, 94, 59, 76, 51, 65, 75
  Operation: new = old + 5
  Test: divisible by 2
    If true: throw to monkey 3
    If false: throw to monkey 6
"""