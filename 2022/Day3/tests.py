import pytest
from main_a import InputHandler
from main_b import InputHandler as IB

from data import test_input


def test_data_prep():
    i = InputHandler(test_input)
    print(i.score)

def test_main_b():
    i = IB(test_input)
    print(i.common_items)
    print(i.score)