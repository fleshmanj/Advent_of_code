import requests

url = "https://adventofcode.com/2015/day/2/input"

cookies = {"_ga": "GA1.2.1248021130.1660347335",
           "_gid": "GA1.2.207307331.1660347335",
           "session": "53616c7465645f5f28ed115d40ff354e9b1526b666d199539096604c83746d5f3319c326c38d33e4400cf026f5ea4b590449f2bfdb83bb25905b5498a1c1897c"
           }
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