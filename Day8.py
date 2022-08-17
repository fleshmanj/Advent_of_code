import requests
import mine
import re

headers = mine.cookies

response = requests.get("https://adventofcode.com/2015/day/8/input", cookies=headers)

new_string = ""
for i, character in enumerate(response.content):
    new_string = new_string + chr(character)

new_string = new_string.split("\n")

total_of_string_code = 0
viewable = 0
for i, line in enumerate(new_string):
    if line != "":
        string = eval(line)
        viewable += len(string)

        total_of_string_code += len(line)
# print(total_of_string_code)
# print(viewable)
print(total_of_string_code-viewable)


for i, line in enumerate(new_string):
    if line != "":
        string = '""'
        for character in line:
            if character == '"':
                string = string[:-1] + r'\"'
            if ord(character) == '"':
                print("these are equal----------------------------------")
            else:
                string = string + character
        print(new_string[i])
        print(string)
