from data import raw_input
from main_a import Inputhandler


def main_a():
    i = Inputhandler(raw_input)
    i.traverse()
    print(len(set(i.past_positions)))

def main_b():
    i = Inputhandler(raw_input)
    i.traverse()
    print(len(set(i.past_positions)))

if __name__ == "__main__":
    main_a()
    main_b()
