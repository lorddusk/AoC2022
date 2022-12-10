from utils.read import read_file


def get_inputs():
    return read_file(10, "string")


def get_example():
    return read_file("10e", "string")


def calculate_cycle(cycle, strengths):
    if cycle in [20, 60, 100, 140, 180, 220]:
        cycle_strengths = sum(strengths) * cycle
        return cycle_strengths
    return 0


def determine_pixel(cycle, curr_position):
    lit = "\u2588"
    dark = " "
    if cycle in curr_position:
        pixel = lit
    else:
        pixel = dark
    return pixel


def what_row(cycle, pixel, row1, row2, row3, row4, row5, row6):
    if cycle < 40:
        row1.append(pixel)
    if 40 <= cycle < 80:
        row2.append(pixel)
    if 80 <= cycle < 120:
        row3.append(pixel)
    if 120 <= cycle < 160:
        row4.append(pixel)
    if 160 <= cycle < 200:
        row5.append(pixel)
    if 200 <= cycle < 240:
        row6.append(pixel)
    return row1, row2, row3, row4, row5, row6


def move_curr_position(strength, curr_position):
    middle_pixel = curr_position[1]
    middle_pixel += strength
    curr_position = [middle_pixel-1, middle_pixel, middle_pixel+1]
    return curr_position


def solve_row(data):
    starting_position = [0, 1, 2]
    curr_position = starting_position
    cycle = 0
    strength = 1
    row1, row2, row3, row4, row5, row6 = [], [], [], [], [], []
    for line in data:
        if "noop" in line:
            row1, row2, row3, row4, row5, row6 = what_row(cycle, determine_pixel(cycle % 40, curr_position), row1, row2, row3, row4, row5, row6)
            cycle += 1
        else:
            operation = int(line.split(" ")[1])
            row1, row2, row3, row4, row5, row6 = what_row(cycle, determine_pixel(cycle % 40, curr_position), row1, row2, row3, row4, row5, row6)
            cycle += 1
            row1, row2, row3, row4, row5, row6 = what_row(cycle, determine_pixel(cycle % 40, curr_position), row1, row2, row3, row4, row5, row6)
            curr_position = move_curr_position(operation, curr_position)
            cycle += 1
    return row1, row2, row3, row4, row5, row6


def part_one():
    data = get_inputs()
    cycle = 1
    strengths = [1]
    cycle_strengths = []
    for line in data:
        if "noop" in line:
            cycle += 1
        else:
            operation = int(line.split(" ")[1])
            cycle += 1
            cycle_strengths.append(calculate_cycle(cycle, strengths))
            strengths.append(operation)
            cycle += 1
        cycle_strengths.append(calculate_cycle(cycle, strengths))
    signal_strengths = sum(cycle_strengths)
    print(f"The sum of the six signal strengths is **{signal_strengths}**")


def part_two():
    data = get_inputs()
    row1, row2, row3, row4, row5, row6 = solve_row(data)
    print(f"The rendered image is:")
    print("".join(row1))
    print("".join(row2))
    print("".join(row3))
    print("".join(row4))
    print("".join(row5))
    print("".join(row6))
