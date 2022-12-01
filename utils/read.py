def file(dayNumber, type="string"):
    input = []
    f = open(f'inputs/day{dayNumber}.txt', 'r')
    if type == "string":
        for x in f:
            input.append(x.rstrip())
    if type == "int":
        for x in f:
            input.append(int(x.rstrip()))
    return input