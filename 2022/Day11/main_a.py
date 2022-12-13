import math
from tqdm import tqdm
import logging
from data import test_input, raw_input

logging.basicConfig(filename="testing.txt", level=logging.DEBUG)


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
        self.items_inspected = 0

    def __str__(self):
        from pprint import pprint
        return str(pprint(vars(self)))

    def inspect_item(self, item):
        operation = self.operation.replace("old", str(item))
        strings = self.operation.split(" ")
        operand = strings[1]

        if operand == "*":
            operand = "multiplied"
        if operand == "/":
            operand = "divided"
        if operand == "+":
            operand = "increased"
        if operand == "-":
            operand = "decreased"

        logging.debug(f"  Monkey inspects an item with a worry level of {item}.")
        item = eval(operation)
        logging.debug(f"    Worry level is {operand} by {strings[2]} to {item}.")
        item = item%9699690
        # logging.debug(f"    Monkey gets bored with item. Worry level is divided by 3 to {item}.")
        return item

    def test_item(self, item):
        self.starting_items.pop(0)
        logging.debug(f"    {item} divided by {int(self.test)} = {math.floor(item // int(self.test))}")
        x = item / int(self.test)
        if x.is_integer():
            logging.debug(f"    Current worry level is divisible by {self.test}.")
            return self.do_if_true, item
        else:
            logging.debug(f"    Current worry level is not divisible by {self.test}.")
            return self.do_if_false, item

    def evaluate_item(self, item):
        item = self.inspect_item(item)
        result = self.test_item(item)
        self.items_inspected += 1
        logging.debug(f"    Item with worry level {result[1]} is thrown to monkey {result[0]}.")
        return result


class InputHandler:
    data: str
    monkies: dict

    def __init__(self, data):
        self.data = data
        self.monkies = {}
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
            self.monkies[id] = (Monkey(id, starting_items, operation, test_case, do_if_true, do_if_false))

    def make_one_round(self):
        for k, monkey in self.monkies.items():
            logging.debug(f"Monkey {k}:")
            newlist = self.monkies[k].starting_items
            for item in list(newlist):
                result = monkey.evaluate_item(item)
                self.monkies[result[0]].starting_items.append(result[1])
                newlist = monkey.starting_items
            # for k, monkey in self.monkies.items():
            #     print(monkey.starting_items)


if __name__ == "__main__":
    i = InputHandler(raw_input)
    for _ in tqdm(range(0, 10000)):
        i.make_one_round()
    inspected = []
    for k, monkey in i.monkies.items():
        inspected.append(monkey.items_inspected)
        print(f"Monkey {k} inspected items {monkey.items_inspected} times.")

    inspected.sort()
    level_of_monkey_business = inspected[-1] * inspected[-2]
    print(f"Level of shenanigans is {level_of_monkey_business}")
