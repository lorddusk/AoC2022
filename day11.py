import math
from utils.chunks import chunks
from utils.read import read_file


def get_inputs():
    return read_file(11, "string")


def get_example():
    return read_file(11, "string", True)

def get_modulo(monkeys):
    return math.lcm(*map(lambda m: m['test'], monkeys))


def get_monkeys(data):
    monkeys = list(chunks(data, 7))
    operation_monkeys = []
    for monkey in monkeys:
        operation_monkey = {}
        for line in monkey:
            line = line.strip()
            if line == "":
                pass
            if line.startswith("M"):
                num = line.rstrip(":").split(" ")[1]
                operation_monkey["monkey"] = int(num)
            if line.startswith("S"):
                starting_items = line.split(": ")[1].split(", ")
                operation_monkey["starting_items"] = []
                for x in starting_items:
                    operation_monkey["starting_items"].append(int(x))
            if line.startswith("O"):
                operation = line.split(": new =")[1]
                operation_monkey["operation"] = operation.strip()
            if line.startswith("T"):
                test = line.split("divisible by ")[1]
                operation_monkey["test"] = int(test.strip())
            if "true" in line:
                true = line.split("throw to monkey ")[1]
                operation_monkey["true"] = true.strip()
            if "false" in line:
                false = line.split("throw to monkey ")[1]
                operation_monkey["false"] = false.strip()
        operation_monkey["inspected_items"] = 0
        operation_monkeys.append(operation_monkey)
    return operation_monkeys


def play_rounds(monkeys, amount_of_rounds, worry):
    try:
        modulo = get_modulo(monkeys)
        for round in range(1, amount_of_rounds + 1):
            for monkey in monkeys:
                items = monkey['starting_items']
                length_items = len(items)
                for i in range(length_items):
                    curr_item = items[0]
                    operation = monkey['operation']
                    operation = operation.replace("old", str(curr_item))
                    outcome = eval(operation) // worry
                    test = outcome % monkey["test"]
                    monkey["starting_items"].remove(curr_item)
                    goto = monkey['true'] if test == 0 else monkey['false']
                    goto_monkey = monkeys[[m['monkey'] for m in monkeys if m['monkey'] == int(goto)][0]]
                    goto_monkey['starting_items'].append(outcome if worry != 1 else outcome % modulo)
                    monkey['inspected_items'] += 1
        inspections = []
        for monkey in monkeys:
            inspections.append(int(monkey['inspected_items']))
        inspections = sorted(inspections, reverse=True)[:2]
        return inspections[0] * inspections[1]
    except Exception as e:
        print(f"Crashed on {round}")
        print(e)


def part_one():
    data = get_inputs()
    monkeys = get_monkeys(data)
    monkey_business = play_rounds(monkeys, 20, 3)
    print(f"The level of monkey business is **{monkey_business}**")


def part_two():
    data = get_inputs()
    monkeys = get_monkeys(data)
    monkey_business = play_rounds(monkeys, 10000, 1)
    print(f"The level of monkey business is **{monkey_business}**")


if __name__ == "__main__":
    part_one()
    part_two()
