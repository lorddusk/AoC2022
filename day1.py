from utils.read import read_file


def combine_calories():
    stringInput = read_file(1, "string")
    elves = []
    elf = []
    for line in stringInput:
        if line != "":
            elf.append(int(line))
        else:
            elves.append(sum(elf))
            elf = []
    return elves


def part_one():
    elves = combine_calories()
    amount = max(elves)
    print(f"Elf with the largest amount of calories, is carrying **{amount}** calories")


def part_two():
    elves = combine_calories()
    amount = sum(sorted(elves, reverse=True)[:3])
    print(f"The 3 elves who are carrying the largest amount of calories, have a combined amount of **{amount}** calories")
