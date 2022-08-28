import itertools

input_string = """Sugar,3,0,0,3,2
Sprinkles,3,3,0,0,9
Candy,1,0,4,0,1
Chocolate,0,0,2,2,8"""

test_string = """Butterscotch,-1,-2,6,3,8
Cinnamon,2,3,2,1,3"""


class Ingredient:
    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name = name
        self.capacity = int(capacity)
        self.durability = int(durability)
        self.flavor = int(flavor)
        self.texture = int(texture)
        self.calories = int(calories)


if __name__ == "__main__":
    lines = input_string.split("\n")
    ingredients = []
    possible_ingredients = ["Sugar", "Sprinkles", "Candy", "Chocolate"]
    for line in lines:
        line = line.split(",")
        ingredients.append(Ingredient(line[0], line[1], line[2], line[3], line[4], line[5]))
    test_list = []
    for v in itertools.product(range(5), repeat=100):
        test_list.append(v)
    print(test_list)