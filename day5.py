from utils.read import file


def get_crates():
    string_input = file(5, "string")

    string_input = ["    [D]    ",
             "[N] [C]    ",
             "[Z] [M] [P]",
             "1   2   3",
             "",
             "move 1 from 2 to 1",
             "move 3 from 1 to 3",
             "move 2 from 2 to 1",
             "move 1 from 1 to 2"]

    crates = [[] for i in range(3)]
    assignments = [[] for i in range(3)]

    for line in string_input:
        if not line.startswith("move") and not line.startswith("1"):
            actual_line = line.replace("    ","X").replace(" ","").replace("[","").replace("]","")
            for i in range(0, len(actual_line)):
                if actual_line[i] != "X":
                    crates[i].append(actual_line[i])
        if line.startswith("move"):
            assignment_line = line.replace("move ", "").replace("from ","").replace("to ","").split(" ")
            assignments[0].append(assignment_line[0])
            assignments[1].append(assignment_line[1])
            assignments[2].append(assignment_line[2])

        print(crates)
        print(assignments)


    # print(string_input)

    # return crates, assignments


def part_one():
    get_crates()
    print(f"The crate sequence that ends up on top is **{0}**")


def part_two():
    print(f"The crate sequence that ends up on top is  **{0}**")
