import pytest
from main_a import InputHandler
from data import test_input

def test_parse_data():
    i = InputHandler(test_input)
    assert len(i.monkies) == 4
    for monkey in i.monkies:
        print(monkey)