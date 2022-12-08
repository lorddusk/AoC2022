import json

from utils.read import read_file


def get_inputs():
    return read_file(8, "string")


class Forest:
    def __init__(self, lines):
        self.lines = lines
        self.trees = []

    def to_dict(self):
        return {"trees": [tree.to_dict() for tree in self.trees]}

    def visible(self):
        int = 0
        string = ""
        for tree in self.trees:
            if int == self.lines:
                int = 0
                string += "\n"
            if tree.visible:
                string += "O"
            else:
                string += "X"
            int += 1

        return string


class Tree:
    def __init__(self, x, y, height, visible=False):
        self.height = height
        self.x = x
        self.y = y
        self.visible = visible

    def to_dict(self):
        return {"pos": f"{self.x}, {self.y}", "height": self.height, "visible": self.visible}


def get_example():
    return ["30373",
            "25512",
            "65332",
            "33549",
            "35390"]


def create_tree_grid(input):
    forest = Forest(len(input))
    for x in range(len(input)):
        for y in range(len(input[x])):
            if x == 0 or y == 0 or x == len(input) - 1 or y == len(input) - 1:
                forest.trees.append(Tree(x, y, input[x][y], True))
            else:
                forest.trees.append(Tree(x, y, input[x][y]))
    return forest


def part_one():
    # input = get_example()
    input = get_inputs()
    print(create_tree_grid(input).visible())
    total_trees = 0
    print(f"There are **{total_trees}** trees visible from outside the grid")


def part_two():
    pass
