import json

from utils.read import read_file


def get_inputs():
    # return read_file(7, "string")
    return [
        "$ cd /",
        "$ ls",
        "dir a",
        "14848514 b.txt",
        "8504156 c.dat",
        "dir d",
        "$ cd a",
        "$ ls",
        "dir e",
        "29116 f",
        "2557 g",
        "62596 h.lst",
        "$ cd e",
        "$ ls",
        "584 i",
        "$ cd ..",
        "$ cd ..",
        "$ cd d",
        "$ ls",
        "4060174 j",
        "8033020 d.log",
        "5626152 d.ext",
        "7214296 k",
    ]


def part_one():
    input = get_inputs()
    current_path = ""
    file_system = []

    for line in input:
        if line.startswith("$") and "cd" in line:
            path = line.split(" ")[2]
            if path == "..":
                current_path = current_path.rsplit("/", 1)[0]
                if current_path == "":
                    current_path = "/"
            elif path == "/":
                current_path = "/"
            else:
                if current_path == "/":
                    current_path = f"{current_path}{path}"
                else:
                    current_path = f"{current_path}/{path}"
        elif line == "$ ls":
            pass
        else:
            line_split = line.split(" ")
            if line_split[0] == "dir":
                if f"{current_path}" != "/":
                    file_path = f"{current_path}/{line_split[1]}"
                else:
                    file_path = f"{current_path}{line_split[1]}"
                file = {
                    "root": current_path,
                    "file_path": file_path
                }
            else:
                file = {
                    "root": current_path,
                    "file_size": int(line_split[0]),
                    "file_name": line_split[1]
                }
            file_system.append(file)

    file_size_system = {}
    for file in file_system:
        if file.get("file_size") is not None:
            root = file.get("root")
            if file_size_system.get(root) is not None:
                file_size_system[root] += file.get("file_size")
            else:
                file_size_system[root] = file.get("file_size")
    print(file_size_system)




    # print(f"The amount of characters processed before the marker is **{marker}**")

# def part_two():
#     marker = get_marker(14)
#     print(f"The amount of characters processed before the marker is **{marker}**")
