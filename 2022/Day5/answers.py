from main_a import Inputhandler as Handler_a
from main_b import Inputhandler as Handler_b
from data import raw_input

def main_a():
    i = Handler_a(raw_input)
    print(i.find_top_containers())

def main_b():
    i = Handler_b(raw_input)
    print(i.find_top_containers())

if __name__ == "__main__":
    main_a()
    main_b()