import requests
from mine import cookies

url = "https://adventofcode.com/2015/day/2/input"


response = requests.get(url=url, cookies=cookies)

raw = response.content

list_of_boxes = list(raw.decode().split("\n"))


def wrap_presents(boxes):
    total_boxes = 0
    for box in boxes:
        if box != "":
            measurements = box.split("x")
            l, w, h = float(measurements[0]), float(measurements[1]), float(measurements[2])
            sides = [l * w, w * h, h * l]
            sides.sort()
            lowest = sides[0]
            total = 0
            for side in sides:
                total += side * 2
            total += lowest

            total_boxes += total
    return total_boxes


# print(wrap_presents(list_of_boxes))


def cut_ribbon(boxes):
    total_length_of_ribbon = 0
    for box in boxes:
        if box != "":
            measurements = box.split("x")
            l, w, h = float(measurements[0]), float(measurements[1]), float(measurements[2])
            measurements = [l, w, h]
            measurements.sort()
            length_of_ribbon = (measurements[0] * 2) + (measurements[1] * 2)
            length_of_ribbon += l * w * h
            total_length_of_ribbon += length_of_ribbon
    return total_length_of_ribbon

print(cut_ribbon(list_of_boxes))