import pytest
from main_a import InputHandler, OutputHandler
from data import test_input_1


def test_input():
    i = InputHandler(test_input_1)


def test_bingo_board():
    i = InputHandler(test_input_1)
    i.boards[0].print_board()


def test_draw_number():
    i = InputHandler(test_input_1)
    for number in i.numbers:
        i.boards[2].draw_number(number)
    # i.boards[0].draw_number(i.numbers[0][0])
    # for cell in i.boards[2].board:
    #     print(cell.called)
    i.boards[2].print_board()
    print(i.boards[2].bingo)
