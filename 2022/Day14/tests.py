import pytest
from main_a import InputHandler
from data import test_data, raw_data

def test_get_walls():
    i = InputHandler(test_data)
    i.find_walls()
    # i.build_map()
    i.spawn_sand_and_fall()