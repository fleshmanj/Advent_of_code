from main_b import InputHandler, OutputHandler, Submarine

from data import raw_input


def main_a():
    print("running")
    sub = Submarine()
    i = InputHandler(raw_input, sub)
    o = OutputHandler(i)
    i.make_move_sequence()
    i.move_sub()
    o.get_sub_position()
    print(o.output)

def main_b():
    print("running")
    sub = Submarine()
    i = InputHandler(raw_input, sub)
    o = OutputHandler(i)
    i.make_move_sequence()
    i.move_sub()
    o.get_sub_position()
    print(o.output)


if __name__ == "__main__":
    main_b()
