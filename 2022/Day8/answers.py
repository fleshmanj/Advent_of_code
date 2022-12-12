from main_a import InputHandler as IHA
from data import raw_input

def main_a():
    i = IHA(raw_input)
    i.find_hidden_trees()
    count = 0
    for tree in i.trees:
        if tree.visible:
            count += 1
    print(count)

def maion_b():
    i = IHA(raw_input)
    i.find_best_scenic_score()

if __name__ == "__main__":
    maion_b()