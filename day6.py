from utils.read import file


def get_buffer():
    return file(6, "string")[0]


def part_one():
    buffer = get_buffer()
    i = 0
    while True:
        curr = buffer[i:4 + i]
        if len(set(curr)) == len(curr):
            marker = 4 + i
            break
        i += 1
    print(f"The crate sequence that ends up on top is **{marker}**")


def part_two():
    pass
