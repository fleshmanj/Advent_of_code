import pytest
from main_a import InputHandler
from data import test_input


def test_parse_data():
    i = InputHandler(test_input)
    assert len(i.monkies) == 4

def test_one_round():
    i = InputHandler(test_input)
    i.make_one_round()
    assert len(i.monkies) == 4
    for _, monkey in i.monkies.items():
        print(monkey.starting_items)
