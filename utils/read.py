import ast


def read_file(day_number, list_type="string", example=False):
    input_list = []
    if example:
        f = open(f'inputs/examples/day{day_number}.txt', 'r')
    else:
        f = open(f'inputs/day{day_number}.txt', 'r')
    if list_type == "string":
        for x in f:
            input_list.append(x.rstrip())
    elif list_type == "int":
        for x in f:
            input_list.append(int(x.rstrip()))
    elif list_type == "array":
        for x in f:
            if x.rstrip() != "":
                string = ast.literal_eval(x.rstrip())
                input_list.append(string)
    return input_list
