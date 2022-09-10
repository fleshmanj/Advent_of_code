import pytest
from main_a import Map, Inputhandler, Seafloor_placeholder
# from data import test_input

test_input = """v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>"""



def test_map_height():
    i = Inputhandler()
    m = Map(i.generate_map_floor(test_input))
    height = m.get_height()
    assert height == 9

def test_map_width():
    i = Inputhandler()
    m = Map(i.generate_map_floor(test_input))
    width = m.get_width()
    assert width == 10

def test_move_east_cucs():
    i = Inputhandler
    m = Map(i.generate_map_floor(test_input))
    m.print_grid()
    m.move_east_cucs()
    print("-------------------------")
    m.print_grid()

def test_move_south_cucs():
    i = Inputhandler
    m = Map(i.generate_map_floor(test_input))
    m.print_grid()
    m.move_south_cucs()
    print("-------------------------")
    m.print_grid()

def test_move_east_then_south_cucs():
    i = Inputhandler
    m = Map(i.generate_map_floor(test_input))
    m.print_grid()
    for i in range(58):
        m.move_east_cucs()
        m.move_south_cucs()
    m.print_grid()


