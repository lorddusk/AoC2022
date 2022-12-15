from utils.read import read_file

day = 15
data = read_file(day, "string")


def line_intersection(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    if d := (by2 - by1) * (ax2 - ax1) - (bx2 - bx1) * (ay2 - ay1):
        if 0 <= (ua := ((bx2 - bx1) * (ay1 - by1) - (by2 - by1) * (ax1 - bx1)) / d) <= 1 and 0 <= (ub := ((ax2 - ax1) * (ay1 - by1) - (ay2 - ay1) * (ax1 - bx1)) / d) <= 1:
            return int(ax1 + ua * (ax2 - ax1)), int(ay1 + ua * (ay2 - ay1))


def find(beacons):
    set_y = 2000000
    x_ranges = set()
    manhattan_values = []
    for sensor, beacon in data:
        manhattan_values.append((manhattan := sum(abs(a - b) for a, b in zip(sensor, beacon))))
        if (man_y := abs(sensor[1] - set_y)) <= manhattan:
            x_ranges.add((sensor[0] - (man_x := manhattan - man_y), sensor[0] + man_x))
    start, end = min(x[0] for x in x_ranges), max(x[1] for x in x_ranges)
    return abs(start - end) + 1 - sum(x[1] == set_y for x in beacons)


def part_one():
    global data
    data = [((z := [int(x.split(" ")[y].split("=")[1].strip(",").strip(":")) for y in [2, 3, -2, -1]])[:2], z[2:]) for x in data]
    beacons = set(tuple(x[1]) for x in data)
    positions = find(beacons)
    print(f"There are **{positions}** positions where there cannot be a beacon")


def part_two():
    global data
    data = [((z := [int(x.split(" ")[y].split("=")[1].strip(",").strip(":")) for y in [2, 3, -2, -1]])[:2], z[2:]) for x in data]
    beacons = set(tuple(x[1]) for x in data)
    positions = find(beacons)
    frequency = 0
    print(f"The tuning frequency is **{frequency}**")


if __name__ == "__main__":
    part_one()
    part_two()
