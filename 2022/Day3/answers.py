from main_a import InputHandler as InputHandler_a
from main_b import InputHandler as InputHandler_b
from data import raw_input

def main_a():
    i = InputHandler_a(raw_input)
    print(i.score)

def main_b():
    i = InputHandler_b(raw_input)
    print(i.score)

if __name__ == "__main__":
    main_a()
    main_b()