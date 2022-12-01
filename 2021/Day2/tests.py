import pytest
from main_b import InputHandler, OutputHandler, Submarine
from data import test_input


def test_horizontal_movement():
    sub = Submarine()
    sub.move_forward(1)
    assert sub.current_x == 1


def test_move_up():
    sub = Submarine()
    sub.move_up(1)
    assert sub.current_y == -1


def test_move_down():
    sub = Submarine()
    sub.move_down(distance=1)
    assert sub.current_y == 1


def test_move_sequence():
    sub = Submarine()
    i = InputHandler(test_input, sub)
    o = OutputHandler(i)
    i.make_move_sequence()
    for instruction in i.move_sequence:
        i.move_direction(instruction[0], instruction[1])
    assert i.submarine.current_y == 60
    assert i.submarine.current_x == 15
    o.get_sub_position()

