class Monkey:
    id: str
    starting_items: list
    operation: str
    test: int
    do_if_true: str
    do_if_false: str

    def __init__(self, id, starting_items: list, operation, test, do_if_true: str, do_if_false):
        self.id = id
        self.starting_items = starting_items
        self.operation = operation
        self.test = test
        self.do_if_true = do_if_true
        self.do_if_false = do_if_false

    def __str__(self):
        from pprint import pprint
        return str(pprint(vars(self)))


class InputHandler:
    data: str
    monkies: list

    def __init__(self, data):
        self.data = data
        self.monkies = []
        self.parse_data()

    def parse_data(self):
        for monkies in self.data.split("\n\n"):
            monkey = monkies.splitlines()

            id = monkey[0][-2]

            starting_items = monkey[1].replace("Starting items: ", "").replace(",", "").strip()
            starting_items = [int(item) for item in starting_items.split(" ")]

            operation = monkey[2].replace("Operation: new = ", "").strip()

            test_case = monkey[3].replace("Test: divisible by ", "").strip()

            do_if_true = monkey[4][-1]

            do_if_false = monkey[5][-1]
            print(starting_items)
            self.monkies.append(Monkey(id, starting_items, operation, test_case, do_if_true, do_if_false))
