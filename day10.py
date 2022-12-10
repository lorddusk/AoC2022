from utils.read import read_file


def get_inputs():
    return read_file(10, "string")

def get_example():
    return read_file("10e", "string")


def calculate_cycle(cycle, strengths):
    if cycle in [20, 60, 100, 140, 180, 220]:
        print(f"Cycle: {cycle}")
        print(f"Strengths: {sum(strengths)}")
        cycle_strengths = sum(strengths) * cycle
        return cycle_strengths
    return 0


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
    # print(f"The sum of the six signal strengths is **{signal_strengths}**")
