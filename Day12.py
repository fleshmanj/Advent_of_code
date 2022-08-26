import json


def iterdict(d, numbers: list) -> None:
    if isinstance(d, int):
        numbers.append(d)
    if isinstance(d, dict):
        if "red" not in d.values():
            for k, v in d.items():
                if isinstance(v, int):
                    numbers.append(v)
                if isinstance(v, dict):
                    iterdict(v, numbers)
                if isinstance(v, list):
                    iterdict(v, numbers)
                if type(v) == str:
                    if str(v).isnumeric():
                        numbers.append(int(v))
    if isinstance(d, list):
        for element in d:
            iterdict(element, numbers)


if __name__ == "__main__":
    with open('day12.json') as f:
        data = json.load(f)

    numbers = []
    solution = 0

    for d in data:
        iterdict(d, numbers)

    for number in numbers:
        solution += number

    print(solution)
