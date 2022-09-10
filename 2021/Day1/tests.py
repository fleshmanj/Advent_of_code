import pytest
from main_a import InputHandler, OutputHandler, DepthFinder
from data import test_input_1


def test_input_length():
    d = DepthFinder()
    i = InputHandler(test_input_1, d)
    assert len(i.data_out) == 10


def test_depth_increased_or_decreased():
    d = DepthFinder()
    i = InputHandler(test_input_1, d)
    o = OutputHandler(d, i.data_out)
    o.read_measurements()
    o.show_results()
    assert d.recorded_increase == 7
