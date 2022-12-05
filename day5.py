from utils.read import file


def get_crates():
    string_input = file(5, "string")

    # string_input = ["    [D]    ",
    #          "[N] [C]    ",
    #          "[Z] [M] [P]",
    #          "1   2   3",
    #          "",
    #          "move 1 from 2 to 1",
    #          "move 3 from 1 to 3",
    #          "move 2 from 2 to 1",
    #          "move 1 from 1 to 2"]

    crates = [[] for i in range(9)]
    assignments = [[] for i in range(3)]

    for line in string_input:
        if not line.startswith("move") and not line.startswith(" 1"):
            actual_line = line.replace("    ",".").replace(" ","").replace("[","").replace("]","")
            for i in range(0, len(actual_line)):
                if actual_line[i] != ".":
                    crates[i].append(actual_line[i])
        if line.startswith("move"):
            assignment_line = line.replace("move ", "").replace("from ","").replace("to ","").split(" ")
            assignments[0].append(assignment_line[0])
            assignments[1].append(assignment_line[1])
            assignments[2].append(assignment_line[2])

    return crates, assignments


def part_one():
    crates, assignments = get_crates()
    print(crates)
    for i in range(0, len(assignments) + 1):
        move = int(assignments[0][i])
        _from = int(assignments[1][i]) - 1
        to = int(assignments[2][i]) - 1
        for j in range(move, 0, -1):
            crate = crates[_from][0]
            crates[_from].remove(crate)
            crates[to].insert(0, crate)

    print(crates)
    string = ""
    for x in crates:
        try:
            string += x[0]
        except:
            pass
    print(f"The crate sequence that ends up on top is **{string}**")


def part_two():
    print(f"The crate sequence that ends up on top is  **{0}**")
