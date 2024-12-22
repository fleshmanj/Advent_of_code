from main_a import InputHandler as IH1
from main_b import InputHandler as IH2
from data import raw_input

def run_main_a():
    i = IH1(raw_input)
    answer = i.answer
    print("Answer_A: ", answer)
def run_main_b():
    i = IH2(raw_input)
    answer = i.answer
    print("Answer_B: ", answer)


if __name__ == '__main__':
    run_main_a()
    run_main_b()