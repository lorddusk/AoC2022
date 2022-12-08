import json

from utils.read import read_file


def get_inputs():
    return read_file(8, "string")


def check_visible(data, row, column):
    if all(data[row][column] > data[_row][column] for _row in range(row)):
        return True
    if all(data[row][column] > data[row][_column] for _column in range(column)):
        return True
    if all(data[row][column] > data[_row][column] for _row in range(row + 1, len(data))):
        return True
    if all(data[row][column] > data[row][_column] for _column in range(column + 1, len(data))):
        return True
    return False


def part_one():
    data = get_inputs()
    total_trees = sum([check_visible(data, row, column) for row in range(len(data)) for column in range(len(data))])
    print(f"There are **{total_trees}** trees visible from outside the grid")


def part_two():
    pass
