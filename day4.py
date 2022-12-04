from utils.read import file


def get_assignments():
    assignments = file(4, "string")

    assignments_one = []
    assignments_two = []
    for assignment in assignments:
        assignment = assignment.split(",")
        assignment_one_range = assignment[0].split("-")
        temp_list_one = []
        for i in range(int(assignment_one_range[0]), int(assignment_one_range[1]) + 1):
            temp_list_one.append(i)
        assignments_one.append(temp_list_one)

        assignment_two_range = assignment[1].split("-")
        temp_list_two = []
        for i in range(int(assignment_two_range[0]), int(assignment_two_range[1]) + 1):
            temp_list_two.append(i)
        assignments_two.append(temp_list_two)

    return assignments_one, assignments_two


def part_one():
    one, two = get_assignments()
    intersections = 0

    for i in range(len(one)):
        if set((one[i])).issubset(two[i]) or set((two[i])).issubset(one[i]):
            intersections += 1

    print(f"The amount of assignment pairs that does contain the other fully is **{intersections}**")


def part_two():
    one, two = get_assignments()
    overlap = 0

    for i in range(len(one)):
        if set(one[i]).intersection(set(two[i])) or set(two[i]).intersection(set(one[i])):
            overlap += 1

    print(f"The amount of assignment pairs that have overlap are **{overlap}**")
