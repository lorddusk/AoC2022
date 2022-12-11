from utils.read import read_file


def get_crates():
    string_input = read_file(5, "string")

    # string_input = ["    [D]    ",
    #          "[N] [C]    ",
    #          "[Z] [M] [P]",
    #          " 1   2   3",
    #          "",
    #          "move 1 from 2 to 1",
    #          "move 3 from 1 to 3",
    #          "move 2 from 2 to 1",
    #          "move 1 from 1 to 2"]

    crates = [[] for i in range(9)]
    assignments = [[] for i in range(3)]

    for line in string_input:
        if not line.startswith("move") and not line.startswith(" 1"):
            actual_line = line.replace("    ", ".").replace(" ", "").replace("[", "").replace("]", "")
            for i in range(0, len(actual_line)):
                if actual_line[i] != ".":
                    crates[i].append(actual_line[i])
        elif line.startswith("move"):
            assignment_line = line.replace("move ", "").replace("from ", "").replace("to ", "").split(" ")
            assignments[0].append(assignment_line[0])
            assignments[1].append(assignment_line[1])
            assignments[2].append(assignment_line[2])

    return crates, assignments


def part_one():
    crates, assignments = get_crates()

    for i in range(0, len(assignments[0])):
        move = int(assignments[0][i])
        _from = int(assignments[1][i]) - 1
        to = int(assignments[2][i]) - 1
        while move > 0:
            crates[to].insert(0, crates[_from].pop(0))
            move -= 1

    string = ""
    for x in crates:
        string += x[0]
    print(f"The crate sequence that ends up on top is **{string}**")


def part_two():
    crates, assignments = get_crates()

    for i in range(0, len(assignments[0])):
        move = int(assignments[0][i])
        _from = int(assignments[1][i]) - 1
        to = int(assignments[2][i]) - 1
        to_move = []
        while move > 0:
            to_move.append(crates[_from].pop(0))
            move -= 1
        to_move.reverse()

        for crate_to_move in to_move:
            crates[to].insert(0, crate_to_move)

    string = ""
    for x in crates:
        string += x[0]
    print(f"The crate sequence that ends up on top is **{string}**")


if __name__ == "__main__":
    part_one()
    part_two()
