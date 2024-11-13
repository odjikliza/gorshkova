import json

INPUT_FILE = 'input.json'


def task(filename):
    with open(filename) as file:
        json_data = json.load(file)

    total = sum(item['score'] * item['weight'] for item in json_data)

    return round(total, 3)


print(task(INPUT_FILE))
