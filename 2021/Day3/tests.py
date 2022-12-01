import pytest
from main_b import InputHandler, OutputHandler
from data import test_input_1


def test_find_gamma_and_epsilon():
    i = InputHandler(test_input_1)
    o = OutputHandler(i)
    o.make_output()


def test_oxygen_gen():
    i = InputHandler(test_input_1)
    assert i.coded_data.oxygen_gen_rating == "23"


def test_co2_gen():
    i = InputHandler(test_input_1)
    assert i.coded_data.co2_scrub_rating == "10"


def test_life_support_rating():
    i = InputHandler(test_input_1)
    assert i.coded_data.life_support_rating == "230"
