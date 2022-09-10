import time

input_string = "vzbxxyzz"
test_string = "ghijklmn"
not_allowed = [ord("i"), ord("o"), ord("l")]


def roll_digit(number):
    rolled = False
    if number < 122:
        number += 1
    else:
        number = 97
        rolled = True
    return rolled, number


def find_pairs(data: str):
    pairs = []
    for i in range(len(data)):
        # print(i)
        if i < len(data) - 1 and data[i] not in pairs:
            if data[i] == data[i + 1]:
                pairs.append(data[i])
    if len(pairs) > 1:
        return True
    return False


def make_string(numbers: list) -> str:
    outputstring = ""
    for number in numbers:
        outputstring = outputstring + chr(number)
    return outputstring


def find_not_allowed(numbers: list) -> bool:
    not_allowed = [ord("i"), ord("o"), ord("l")]
    # print(not_allowed)
    # print(numbers)
    for letter in not_allowed:
        if letter in numbers:
            return True
    return False


def find_straight(numbers: list) -> bool:
    for i, number in enumerate(numbers):
        if i < len(numbers) - 2:
            if numbers[i + 1] == number + 1 and numbers[i + 2] == number + 2:
                return True
    return False


def roll_password(password: str) -> str:
    full_revolution = [False, False, False, False, False, False, False, True]
    characters = []
    for letter in password:
        characters.append(ord(letter))
    # for _ in range(26):
    #     for i, number in enumerate(characters):
    #         if full_revolution[i]:
    #             rolled, characters[i] = roll_digit(number)
    #             if rolled:
    #                 full_revolution[i-1] = True
    found = False

    while True:
        rolled, characters[7] = roll_digit(characters[7])
        if rolled:
            rolled, characters[6] = roll_digit(characters[6])
            if rolled:
                rolled, characters[5] = roll_digit(characters[5])
                if rolled:
                    rolled, characters[4] = roll_digit(characters[4])
                    if rolled:
                        rolled, characters[3] = roll_digit(characters[3])
                        if rolled:
                            rolled, characters[2] = roll_digit(characters[2])
                            if rolled:
                                rolled, characters[1] = roll_digit(characters[1])
                                if rolled:
                                    rolled, characters[0] = roll_digit(characters[0])

        if not find_not_allowed(characters):
            if find_straight(characters):
                # print(make_string(characters))
                output = make_string(characters)
                if find_pairs(output):
                    return output
                # if output == input_string:
                #     found = True


# for i in input_string:
#     print(chr(roll_digit(ord(i))))

print(roll_password(input_string))

# print(find_pairs("ghjaabcc"))
