import time

# input_string = "vzbxkghb"
input_string = "aaaaaaaa"
not_allowed = [ord("i"),ord("o"),ord("l")]
print(not_allowed)
def roll_digit(number):
    rolled = False
    if number < 122:
        number += 1
    else:
        number = 97
        rolled = True
    return number

def make_string(numbers:list)->str:
    outputstring = ""
    for number in numbers:
        outputstring = outputstring + chr(number)
    return outputstring

def find_not_allowed(numbers:list)->bool:
    not_allowed = [ord("i"), ord("o"), ord("l")]
    # print(not_allowed)
    # print(numbers)
    for letter in not_allowed:
        print(letter)
        if letter in numbers:
            return True
        else:
            return False
def find_straight(numbers:list)->bool:
    for i, number in enumerate(numbers):
        if i < len(number)-2:
            if number[i+1] == number + 1 and  number[i+2] == number + 2:
                return False
            else:
                return True


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

    for _ in range(26):
        for _ in range(26):
            for _ in range(26):
                for _ in range(26):
                    for _ in range(26):
                        for _ in range(26):
                            for _ in range(26):
                                for _ in range(26):
                                    characters[7] = roll_digit(characters[7])
                                    if not find_not_allowed(characters):
                                        output = make_string(characters)
                                        print(output)
                                    time.sleep(.25)
                                characters[6] = roll_digit(characters[6])
                            characters[5] = roll_digit(characters[5])
                        characters[4] = roll_digit(characters[4])
                    characters[3] = roll_digit(characters[3])
                characters[2] = roll_digit(characters[2])
            characters[2] = roll_digit(characters[2])
        characters[1] = roll_digit(characters[1])
    characters[0] = roll_digit(characters[0])


# for i in input_string:
#     print(chr(roll_digit(ord(i))))

roll_password(input_string)
