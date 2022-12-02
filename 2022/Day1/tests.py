import pytest
from main_a import InputHandler

from data import test_input as tst, raw_input


def test_input():
    i = InputHandler(raw_input)
