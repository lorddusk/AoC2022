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
    manhattan_values, nw, sw, ne, se = [], [], [], [], []
    for sensor, beacon in data:
        manhattan_values.append((manhattan := sum(abs(a - b) for a, b in zip(sensor, beacon))))
        nw.append(((w := (sensor[0] - manhattan - 1, sensor[1])), (n := (sensor[0], sensor[1] - manhattan - 1))))
        sw.append((w, (s := (sensor[0], sensor[1] + manhattan + 1))))
        ne.append((n, (e := (sensor[0] + manhattan + 1, sensor[1]))))
        se.append((s, e))
        if (man_y := abs(sensor[1] - set_y)) <= manhattan:
            x_ranges.add((sensor[0] - (man_x := manhattan - man_y), sensor[0] + man_x))
    start, end = min(x[0] for x in x_ranges), max(x[1] for x in x_ranges)
    return manhattan_values, nw, sw, ne, se, abs(start - end) + 1 - sum(x[1] == set_y for x in beacons)


def part_one():
    global data
    data = [((z := [int(x.split(" ")[y].split("=")[1].strip(",").strip(":")) for y in [2, 3, -2, -1]])[:2], z[2:]) for x in data]
    beacons = set(tuple(x[1]) for x in data)
    *_, positions = find(beacons)
    print(f"There are **{positions}** positions where there cannot be a beacon")


def part_two():
    global data
    beacons = set(tuple(x[1]) for x in data)
    manhattan_values, nw, sw, ne, se, _ = find(beacons)
    frequency = None
    while not frequency:
        for a, b in nw + se:
            for c, d in sw + ne:
                if (hit := line_intersection(*a, *b, *c, *d)) and 0 <= min(hit) and max(hit) <= 4000000:
                    for e, (sensor, beacon) in enumerate(data):
                        if sum(abs(a - b) for a, b in zip(sensor, hit)) <= manhattan_values[e]:
                            break
                    else:
                        frequency = hit[0] * 4000000 + hit[1]
    print(f"The tuning frequency is **{frequency}**")


if __name__ == "__main__":
    part_one()
    part_two()
