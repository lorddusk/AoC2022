from utils.read import read_file
import networkx as nx

day = 12


def get_inputs():
    return read_file(day, "string")


def get_example():
    return read_file(f"{day}e", "string")


def create_grid(data):
    matrix = {}
    grid = nx.DiGraph()

    for x, row in enumerate(data):
        for y, character in enumerate(row):
            matrix[(x, y)] = character

    end = [key for key in matrix.keys() if matrix[key] == "E"][0]
    start = [key for key in matrix.keys() if matrix[key] == "S"][0]
    matrix[end] = "z"
    matrix[start] = "s"

    for (x, y) in matrix.keys():
        adjacent = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        adjacent = [pos for pos in adjacent if pos in matrix.keys()]
        adjacent = [pos for pos in adjacent if (ord(matrix[pos]) - ord(matrix[(x,y)])) <= 1]
        for adj in adjacent:
            grid.add_edge((x, y), adj)
    return grid, start, end


def part_one():
    data = get_inputs()
    grid, start, end = create_grid(data)
    shortest_route = nx.shortest_path(grid, start, end)
    shortest_length = len(shortest_route)-1
    print(f"The shortest route to the endpoint is {shortest_length} steps")


def part_two():
    pass


if __name__ == "__main__":
    part_one()
    part_two()
