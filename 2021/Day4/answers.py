from main_a import InputHandler, OutputHandler
from main_b import InputHandler as IH, OutputHandler as OH
from data import raw_input


def main_a():
    i = InputHandler(raw_input)
    o = OutputHandler(i)
    o.make_output()

def main_b():
    i = IH(raw_input)
    o = OH(i)
    o.make_output()


if __name__ == "__main__":
    main_b()
