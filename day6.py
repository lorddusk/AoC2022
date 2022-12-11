from utils.read import read_file


def get_buffer():
    return read_file(6, "string")[0]


def get_marker(marker_num):
    buffer = get_buffer()
    pos = 0
    while True:
        curr = buffer[pos:marker_num + pos]
        if len(set(curr)) == len(curr):
            return marker_num + pos
        pos += 1


def part_one():
    marker = get_marker(4)
    print(f"The amount of characters processed before the marker is **{marker}**")


def part_two():
    marker = get_marker(14)
    print(f"The amount of characters processed before the marker is **{marker}**")


if __name__ == "__main__":
    part_one()
    part_two()
