from utils.read import read_file

day = 14


def get_inputs():
    return read_file(day, "string")


def get_example():
    return read_file(day, "string", True)


def get_rocks(data):
    rocks = {}
    for line in data:
        coords = line.split(" -> ")
        for _from, _to in zip(coords[0::], coords[1::]):
            (fromx, fromy) = (int(n) for n in _from.split(","))
            (tox, toy) = (int(n) for n in _to.split(","))

            for x in range(min(fromx, tox), max(fromx, tox) + 1):
                rocks[x, fromy] = "#"

            for y in range(min(fromy, toy), max(fromy, toy) + 1):
                rocks[fromx, y] = "#"

    return rocks


def bottom(rocks):
    return max(y for (_, y), val in rocks.items() if val == '#')


def sand(rocks):
    x = 500

    for y in range(bottom(rocks)):
        if (x, y + 1) not in rocks:
            pass
        elif (x - 1, y + 1) not in rocks:
            x -= 1
        elif (x + 1, y + 1) not in rocks:
            x += 1
        else:
            rocks[(x, y)] = "o"
            return (x, y) != (500, 0)

    return False


def add_floor(rocks):
    bottom_y = bottom(rocks)
    for x in range(-1000, 1000):
        rocks[x, bottom_y + 2] = "#"


def do_simulation(data, use_bottom):
    rocks = get_rocks(data)

    if not use_bottom:
        add_floor(rocks)

    while sand(rocks):
        pass

    return rocks


def part_one():
    data = get_inputs()
    cave = do_simulation(data, True)
    sand = sum(1 for v in cave.values() if v == 'o')
    print(f"How many units of sand come to rest before sand starts flowing into the abyss below? {sand}")


def part_two():
    data = get_inputs()
    cave = do_simulation(data, False)
    sand = sum(1 for v in cave.values() if v == 'o')
    print(f"How many units of sand come to rest? {sand}")


if __name__ == "__main__":
    part_one()
    part_two()
