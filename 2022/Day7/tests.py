import pytest
from main_a import InputHandler as IHa, Directory
from data import raw_input, test_input


def test_directory():
    directory = Directory()
    i = IHa(test_input)
    i.build_dir()
    i.directory.show_dir()
