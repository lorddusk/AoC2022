from utils.read import read_file


def get_inputs():
    return read_file(9, "string")


class Knot:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0

    def position(self):
        return self.x, self.y


class Rope:
    def __init__(self, n_knots: int):
        self.segments = [Knot() for _ in range(n_knots)]
        self.head = self.segments[0]
        self.tail = self.segments[-1]

    def move_head(self, x, y):
        step(self.head, x, y)
        for s in range(1, len(self.segments)):
            follow(self.segments[s - 1], self.segments[s])


def knots_touching(x, y):
    return abs(x) <= 1 and abs(y) <= 1


def step(knot, x, y):
    knot.x += x
    knot.y += y


def follow(lead, knot):
    diff_x = lead.x - knot.x
    diff_y = lead.y - knot.y
    if knots_touching(diff_x, diff_y):
        pass
    elif diff_x == 0:
        step(knot, 0, diff_y // abs(diff_y))
    elif diff_y == 0:
        step(knot, diff_x // abs(diff_x), 0)
    else:
        step(knot, diff_x // abs(diff_x), diff_y // abs(diff_y))


def solve(data, rope):
    move = {'R': (1, 0),
            'L': (-1, 0),
            'U': (0, 1),
            'D': (0, -1)}
    unique_tail_pos = set()
    for line in data:
        direction, steps = line.split()
        for _ in range(int(steps)):
            rope.move_head(*move[direction])
            unique_tail_pos.add(rope.tail.position())
    return len(unique_tail_pos)


def part_one():
    data = get_inputs()
    rope = Rope(2)
    tail_pos = solve(data, rope)
    print(f"The number of unique positions the tail has visited is **{tail_pos}**")


def part_two():
    data = get_inputs()
    rope = Rope(10)
    tail_pos = solve(data, rope)
    print(f"The number of unique positions the tail has visited is **{tail_pos}**")
