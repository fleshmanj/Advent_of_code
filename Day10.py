input_string = "1321131112"


def make_list_numbers_from_string(input_string: str) -> list:
    list_for_strings = []
    current = -1
    for i, number in enumerate(input_string):
        if i < len(input_string):
            if number != input_string[i - 1]:
                list_for_strings.append(number)
                current += 1
            if number == input_string[i - 1]:
                list_for_strings[current] = list_for_strings[current] + number
        else:
            if number != input_string[i - 1]:
                list_for_strings.append(number)
                current += 1
            if number == input_string[i - 1]:
                list_for_strings[current] = list_for_strings[current] + number
    return list_for_strings


def make_string_of_numbers(numbers: list) -> str:
    string_to_return = ""
    for i in numbers:
        string_to_return += str(len(i))
        string_to_return += i[0]
    return string_to_return


for i in range(50):
    numbers = make_list_numbers_from_string(input_string)
    input_string = make_string_of_numbers(numbers)
print(len(input_string))
