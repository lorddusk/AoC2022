from utils.read import read_file


def get_inputs():
    return read_file(7, "string")


class Directory:
    def __init__(self, parent=None):
        self.parent = self if parent is None else parent
        self.directories = {}
        self.files = []
        self.size = 0

    def calculate_sizes(self):
        self.size = sum(file for file in self.files) + sum(directory.calculate_sizes() for directory in self.directories.values())
        return self.size

    def get_size(self):
        self.calculate_sizes()
        sizes = [self.size]
        for d in self.directories.values():
            sizes += d.get_size()
        return sizes


def create_file_system():
    root = Directory()
    current_dir = root

    for line in get_inputs():
        command = line.split()
        if command[1] == "cd":
            if command[2] == "/":
                current_dir = root
            elif command[2] == "..":
                current_dir = current_dir.parent
            else:
                current_dir = current_dir.directories[command[2]]
        elif command[1] != "ls":
            if command[0] == "dir":
                current_dir.directories[command[1]] = Directory(current_dir)
            else:
                current_dir.files.append(int(command[0]))
    return root


def part_one():
    root = create_file_system()
    sizes = root.get_size()
    total_sum = sum([size for size in sorted(sizes) if size <= 100000])
    print(f"The sum of all the directories < 100kb is: **{total_sum}**")


def part_two():
    root = create_file_system()
    sizes = root.get_size()
    total_sum = next(size for size in sorted(sizes) if size >= sizes[0] - 40000000)
    print(f"The smallest directory size to delete that frees up at least 40000kb is: **{total_sum}**")
