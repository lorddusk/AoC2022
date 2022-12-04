from utils.read import file


def get_assignments():
    assignments = file(4, "string")

    # assignments = [
    #     "2-4,6-8",
    #     "2-3,4-5",
    #     "5-7,7-9",
    #     "2-8,3-7",
    #     "6-6,4-6",
    #     "2-6,4-8"
    # ]

    return assignments


def part_one():
    assignments = get_assignments()
    assignments_one = []
    assignments_two = []
    for assignment in assignments:
        assignment = assignment.split(",")
        assignment_one_range = assignment[0].split("-")
        temp_list_one = []
        for i in range(int(assignment_one_range[0]), int(assignment_one_range[1])+1):
            temp_list_one.append(i)
        assignments_one.append(temp_list_one)

        assignment_two_range = assignment[1].split("-")
        temp_list_two = []
        for i in range(int(assignment_two_range[0]), int(assignment_two_range[1])+1):
            temp_list_two.append(i)
        assignments_two.append(temp_list_two)

    intersections = 0

    for i in range(len(assignments_one)):
        if set((assignments_one[i])).issubset(assignments_two[i]) or set((assignments_two[i])).issubset(assignments_one[i]):
            intersections += 1

    print(f"The amount of assignment pairs that does contain the other fully is **{intersections}**")


def part_two():
    print(f"The amount of assignment pairs that does contain the other fully is **{0}**")
