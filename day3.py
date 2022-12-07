from utils.read import read_file

priority_values = {
    "a": 1, "b": 2, "c": 3, "d": 4,
    "e": 5, "f": 6, "g": 7, "h": 8,
    "i": 9, "j": 10, "k": 11, "l": 12,
    "m": 13, "n": 14, "o": 15, "p": 16,
    "q": 17, "r": 18, "s": 19, "t": 20,
    "u": 21, "v": 22, "w": 23, "x": 24,
    "y": 25, "z": 26, "A": 27, "B": 28,
    "C": 29, "D": 30, "E": 31, "F": 32,
    "G": 33, "H": 34, "I": 35, "J": 36,
    "K": 37, "L": 38, "M": 39, "N": 40,
    "O": 41, "P": 42, "Q": 43, "R": 44,
    "S": 45, "T": 46, "U": 47, "V": 48,
    "W": 49, "X": 50, "Y": 51, "Z": 52
}


def get_rucksacks():
    rucksacks = read_file(3, "string")
    return rucksacks


def part_one():
    rucksacks = get_rucksacks()
    priorities = 0
    for rucksack in rucksacks:
        length = len(rucksack)
        common = list(set.intersection(*map(set, [rucksack[slice(0, length // 2)], rucksack[slice(length // 2, length)]])))[0]
        priorities += priority_values[common]
    print(f"The sum of the priorities is **{priorities}**")


def part_two():
    rucksacks = get_rucksacks()
    priorities = 0
    for group in range(0, len(rucksacks), 3):
        common = list(set.intersection(*map(set, rucksacks[group:group+3])))[0]
        priorities += priority_values[common]
    print(f"The sum of the priorities is **{priorities}**")
