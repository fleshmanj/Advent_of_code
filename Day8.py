import requests
import mine
import re

headers = mine.cookies

response = requests.get("https://adventofcode.com/2015/day/8/input", cookies=headers)


def convert_byte_string_to_string(input_string):
    string_to_return = ""
    for i, character in enumerate(input_string):
        string_to_return = string_to_return + chr(character)
    string_to_return = string_to_return.split("\n")
    return string_to_return


def show_length_of_strings(string):
    total_of_string_code = 0
    viewable = 0
    for i, line in enumerate(string):
        if line != "":
            string = eval(line)
            viewable += len(string)

            total_of_string_code += len(line)
    return total_of_string_code, viewable


def show_string_length_and_print_string_length(new_string):
    total = 0
    for i, line in enumerate(new_string):
        if line != "":
            string = ''
            for character in line:
                if character == '"':
                    string = string[:-1] + r'\"'
                if character[:2] == '\"':
                    pass
                    # print("these are equal----------------------------------")
                else:
                    string = string + character
            string = '"' + string + '"'
            # print(len(new_string[i].encode()))
            print(string, string.encode())
            total += len(string.encode())
    return total

def part2():
    fin = open('day8.txt', 'rb')
    after = 0
    before = 0
    while True:
        line = fin.readline()
        if line == b"":
            break
        before += len(line[:-2].decode())
        new = b''
        for i in range(0,len(line[:-2])):
            if chr(line[i]) == '"':
                new += b'\\' + b'"'
            elif chr(line[i]) == '\\':
                new += b'\\' + b'\\'
            else:
                new += chr(line[1]).encode()
        new = b'"' + new + b'"'
        after += len(new.decode())
    return after - before

if __name__ == "__main__":
    print(part2())

    # new_string = convert_byte_string_to_string(response.content)
    # print(new_string)
    # total_of_string_code, viewable = show_length_of_strings(new_string)
    # # print(total_of_string_code)
    # # print(viewable)
    # print(total_of_string_code - viewable)
    # show_string_length_and_print_string_length(new_string[:10])
    # print(viewable)
