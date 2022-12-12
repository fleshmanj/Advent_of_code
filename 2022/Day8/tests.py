import pytest

from main_a import InputHandler
from data import test_input


def test_forest_height():
    i = InputHandler(test_input)
    assert i.height == 5


def test_forest_width():
    i = InputHandler(test_input)
    assert i.width == 5


def test_tree_coords():
    i = InputHandler(test_input)
    assert i.trees[0].coords == (0, 0)


def test_find_tree_heights():
    i = InputHandler(test_input)
    for tree in i.trees:
        pass
        # print(tree.height)


def test_find_hidden_trees():
    i = InputHandler(test_input)
    count = 0
    for tree in i.trees:
        if tree.visible:
            count += 1
    assert count == 21


def test_find_best_score():
    i = InputHandler(test_input)
    i.find_best_scenic_score()
