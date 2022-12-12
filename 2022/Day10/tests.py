import pytest
from data import test_data, test_data_2

from main_a import InputHandler


# def test_parse_data():
#     i = InputHandler(test_data, [])
#     assert i.instructions[0] == "noop"
#     assert i.instructions[1] == 3


def test_cpu_operation():
    i = InputHandler(test_data, [])
    print(i.cpu.value)


def test_cpu_operation_longer():
    i = InputHandler(test_data_2, [20, 60, 100, 140, 180, 220])
    print(len(i.cpu_instructions))
    print(len(i.cpu.signals))



