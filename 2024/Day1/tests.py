import pytest
from main_a import InputHandler as IH1
from main_b import InputHandler as IH2

from data import test_input as tst, raw_input


def test_input():
    i = IH1(tst)

def test_compare_line_1():
    i = IH1(tst)
    number = i.compare_numbers(i.data["data_a"][0], i.data["data_b"][0])
    assert number == 2
def test_compare_lists():
    i = IH1(tst)
    list = i.differences
    assert list == [2,1,0,1,2,5]

def test_check_sum():
    i = IH1(tst)
    assert i.add_differences() == 11

def test_add_scores():
    i = IH2(tst)
    assert i.simularity_scores == [9,4,0,0,9,9]

def run_main_a():
    i = IH1(raw_input)
    answer = i.answer
    print("Answer_A: ", answer)
def run_main_b():
    i = IH2(raw_input)
    answer = i.answer
    print("Answer_B: ", answer)