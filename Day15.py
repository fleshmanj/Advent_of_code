import itertools

input_string = """Sugar,3,0,0,-3,2
Sprinkles,-3,3,0,0,9
Candy,-1,0,4,0,1
Chocolate,0,0,-2,2,8"""

test_string = """Butterscotch,-1,-2,6,3,8
Cinnamon,2,3,-2,-1,3"""


class Ingredient:
    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name = name
        self.capacity = int(capacity)
        self.durability = int(durability)
        self.flavor = int(flavor)
        self.texture = int(texture)
        self.calories = int(calories)


def get_score(ingredients: tuple, ingredient_list: list) -> int:
    sugar = ingredients.count("Sugar")
    sprinkles = ingredients.count("Sprinkles")
    candy = ingredients.count("Candy")
    chocolate = ingredients.count("Chocolate")
    # butterscotch = ingredients.count("Butterscotch")
    # cinnamon = ingredients.count("Cinnamon")
    # print(butterscotch,cinnamon)
    #
    # capacity = butterscotch * ingredient_list[0].capacity + cinnamon * ingredient_list[1].capacity
    # durability = butterscotch * ingredient_list[0].durability + cinnamon * ingredient_list[1].durability
    # flavor = butterscotch * ingredient_list[0].flavor + cinnamon * ingredient_list[1].flavor
    # print(f"{butterscotch}* {ingredient_list[0].flavor} + {cinnamon} * {ingredient_list[1].flavor}")
    # texture = butterscotch * ingredient_list[0].texture + cinnamon * ingredient_list[1].texture

    capacity = sugar * ingredient_list[0].capacity + sprinkles * ingredient_list[1].capacity + candy * ingredient_list[
        2].capacity + chocolate * ingredient_list[3].capacity
    durability = sugar * ingredient_list[0].durability + sprinkles * ingredient_list[1].durability + candy * \
                 ingredient_list[2].durability + chocolate * ingredient_list[3].durability
    flavor = sugar * ingredient_list[0].flavor + sprinkles * ingredient_list[1].flavor + candy * ingredient_list[
        2].flavor + chocolate * ingredient_list[3].flavor
    texture = sugar * ingredient_list[0].texture + sprinkles * ingredient_list[1].texture + candy * ingredient_list[
        2].texture + chocolate * ingredient_list[3].texture
    calories = sugar * ingredient_list[0].calories + sprinkles * ingredient_list[1].calories + candy * ingredient_list[
        2].calories + chocolate * ingredient_list[3].calories

    # print(capacity, durability, flavor, texture, calories)

    if capacity <= 0 or durability <= 0 or flavor <= 0 or texture <= 0:
        return 0
    else:
        if calories == 500:
            return capacity * durability * flavor * texture
        else:
            return 0


if __name__ == "__main__":
    lines = input_string.split("\n")
    ingredient_list = []
    possible_ingredients = ["Sugar", "Sprinkles", "Candy", "Chocolate"]
    test_ingredients = ["Butterscotch", "Cinnamon"]
    highscore = 0

    for line in lines:
        line = line.split(",")
        ingredient_list.append(
            Ingredient(name=line[0], capacity=line[1], durability=line[2], flavor=line[3], texture=line[4],
                       calories=line[5]))

    for v in itertools.combinations_with_replacement(possible_ingredients, 100):
        current_score = get_score(v, ingredient_list)
        if current_score > highscore:
            highscore = current_score
    print(highscore)
