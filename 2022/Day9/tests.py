import pytest

from data import test_input , test_input_2
from main_a import Inputhandler

def test_find_past_tail_visited():
    i = Inputhandler(test_input)
    i.traverse()
    print(set(i.past_positions))

def test_find_past_tail_visited_longer_version():
    i = Inputhandler(test_input_2)
    i.traverse()
    print(len(set(i.past_positions)))

def test_print_board():
    i = Inputhandler(test_input_2)
    i.traverse()
    print(len(set(i.past_positions)))
    i.print_board()

