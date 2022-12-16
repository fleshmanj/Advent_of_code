from tqdm import tqdm

from main_a import InputHandler
from data import test_data, raw_data

def test_parse_data():
    i = InputHandler(test_data)
    assert len(i.map_cells) == 40

def test_move_player():
    i = InputHandler(test_data)
    for line in i.maze:
        print(line)


