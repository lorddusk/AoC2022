import json

from utils.read import read_file


def get_inputs():
    return read_file(8, "string")


def check_visible(data, row, column):
    current_tree = data[row][column]
    if all(current_tree > data[_row][column] for _row in range(row)):
        return True
    if all(current_tree > data[row][_column] for _column in range(column)):
        return True
    if all(current_tree > data[_row][column] for _row in range(row + 1, len(data))):
        return True
    if all(current_tree > data[row][_column] for _column in range(column + 1, len(data))):
        return True
    return False


def find_score(data, row, column):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    answer = 1
    for (direction_row, direction_column) in directions:
        score_row, score_column = row, column
        score = 0
        while True:
            score_row += direction_row
            score_column += direction_column
            if score_row < 0 or score_row >= len(data) or score_column < 0 or score_column >= len(data):
                break
            elif data[score_row][score_column] < data[row][column]:
                score += 1
            else:
                score += 1
                break
        answer *= score
    return answer


def part_one():
    data = get_inputs()
    total_trees = sum([check_visible(data, row, column) for row in range(len(data)) for column in range(len(data))])
    print(f"The total number of visible trees outside the grid is **{total_trees}**")


def part_two():
    data = get_inputs()
    total_trees = max([find_score(data, row, column) for row in range(len(data)) for column in range(len(data))])
    print(f"The highest scenic score for a tree is **{total_trees}**")


if __name__ == "__main__":
    part_one()
    part_two()
