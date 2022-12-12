import pytest

from main_a import Inputhandler as IHa
from data import test_input

def test_data_parse():
    i = IHa(test_input)
    print(i.instructions)

def test_move_containers():
    i = IHa(test_input)
    for k, stack in i.stacks.items():
        print(stack.stack)

def test_find_top_containers():
    i = IHa(test_input)
    result = i.find_top_containers()
    assert result == "CMZ"