from utils.read import file


def part_one():
    input = file(1, "string")
    elves = []
    elf = []
    for line in input:
        if line != "":
            elf.append(int(line))
        else:
            elves.append(sum(elf))
            elf = []
    print(f"Elf with the largest amount of calories, is carrying **{max(elves)}** calories")
