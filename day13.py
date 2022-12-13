import pprint

from utils.read import read_file
from utils.chunks import chunks, grouped

day = 13
pair_output = []


def get_inputs():
    return read_file(day, "array")


def get_example():
    return read_file(f"{day}e", "array")


def compare(x, y, index):
    try:
        if len(x) == 0 and len(y) >= 1:
            print(f"X {x} has no length, and Y {y} has length, return True")
            return True
        elif len(x) >= 1 and len(y) == 0:
            print(f"X {x} has length, and Y {y} has no length, return False")
            return False
        elif isinstance(x[index], int) and isinstance(y[index], int):
            print(f"{x[index]} int {y[index]}")
            return ints(x, y, index)
        elif isinstance(x[index], list) and isinstance(y[index], list):
            print("Both are lists")
            return lists(x, y, index)
        elif (isinstance(x[index], int) and not isinstance(y[index], int)) or (not isinstance(x[index], int) and isinstance(y[index], int)):
            print("X and Y are different types")
            return exactly_one(x[index], y[index], index)
    except IndexError:
        print(f"Found that X {x} and Y {y} have different lengths")
        if len(x) < len(y):
            print(f"X is larger than Y, return True")
            return True
        else:
            print(f"X is smaller than Y, return False")
            return False


def ints(x, y, index):
    if x[index] > y[index]:
        print(f"x {x[index]} is larger than y {y[index]}, return False")
        return False
    elif x[index] == y[index]:
        print(f"x {x[index]} and y {y[index]} are equal, moving to next index")
        compare(x,y,index+1)
    elif x[index] < y[index]:
        print(f"x {x[index]} is smaller than y {y[index]}, return True")
        return True


def lists(x, y, index):
    compare(x[index], y[index], index+1)


def exactly_one(x, y, index):
    if isinstance(x, int):
        x = [x]
    if isinstance(y, int):
        y = [y]
    compare(x, y, index=0)


def part_one():
    data = get_example()
    pair = 1
    for x, y in grouped(data, 2):
        print(f"==Pair {pair}==")
        print(f"Comparing X: {x} and Y: {y}")
        correct = compare(x, y, index=0)
        pair_output.append({"pair": pair, "order": correct})
        pair += 1
    print("--------------------")
    pprint.pprint(pair_output)
    # print(f"The shortest route to the endpoint is {shortest_length} steps")


def part_two():
    data = get_example()
    # print(f"The shortest scenic route to the endpoint is {min(paths)} steps")


if __name__ == "__main__":
    part_one()
    # part_two()
