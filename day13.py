from functools import cmp_to_key
from itertools import zip_longest

from utils.read import read_file
from utils.chunks import chunks

day = 13
pair_output = []


def get_inputs():
    return read_file(day, "array")


def get_example():
    return read_file(f"{day}e", "array")


def compare(left, right):
    for result in compare_lists(left, right):
        if result == "good":
            return 1
        elif result == "bad":
            return -1
        elif result == "ok":
            continue
    return 0


def compare_ints(left, right):
    if left < right:
        return "good"
    elif left == right:
        return "ok"
    else:
        return "bad"


def compare_none(left, right):
    if left is None and right is None:
        return "ok"
    elif left is None:
        return "good"
    elif right is None:
        return "bad"


def compare_lists(left, right):
    for x, y in zip_longest(left, right):
        if isinstance(x, int) and isinstance(y, int):
            yield compare_ints(x, y)
        elif isinstance(x, list) and isinstance(y, list):
            yield from compare_lists(x, y)
        elif isinstance(x, int) and isinstance(y, list):
            yield from compare_lists([x], y)
        elif isinstance(x, list) and isinstance(y, int):
            yield from compare_lists(x, [y])
        else:
            yield compare_none(x, y)


def part_one():
    data = get_inputs()
    pair = 1
    chunked_list = list(chunks(data, 2))
    for chunk in chunked_list:
        correct = compare(chunk[0], chunk[1])
        if correct == 1:
            correct = True
        elif correct == -1:
            correct = False
        pair_output.append({"pair": pair, "order": correct})
        pair += 1
    correct_pairs = sum([p['pair'] for p in pair_output if p['order']])
    print(f"The sum of all the correct pairs is {correct_pairs}")


def part_two():
    data = get_inputs()
    data.append([[2]])
    data.append([[6]])
    data.sort(key=cmp_to_key(compare), reverse=True)

    key1 = data.index([[2]]) + 1
    key2 = data.index([[6]]) + 1
    decoder_key = key1 * key2
    print(f"The decoder key for the distress signal {decoder_key}")


if __name__ == "__main__":
    part_one()
    part_two()
