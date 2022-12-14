from utils.read import read_file
import networkx as nx

day = 12


def get_inputs():
    return read_file(day, "string")


def get_example():
    return read_file(day, "string", True)


def create_matrix(data):
    matrix = {}

    for x, row in enumerate(data):
        for y, character in enumerate(row):
            matrix[(x, y)] = character

    end = [key for key in matrix.keys() if matrix[key] == "E"][0]
    start = [key for key in matrix.keys() if matrix[key] == "S"][0]
    matrix[end] = "z"
    matrix[start] = "s"
    return matrix, start, end

def create_grid(matrix):
    grid = nx.DiGraph()

    for (x, y) in matrix.keys():
        adjacent = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        adjacent = [pos for pos in adjacent if pos in matrix.keys()]
        adjacent = [pos for pos in adjacent if (ord(matrix[pos]) - ord(matrix[(x,y)])) <= 1]
        for adj in adjacent:
            grid.add_edge((x, y), adj)

    return grid


def part_one():
    data = get_inputs()
    matrix, start, end = create_matrix(data)
    grid = create_grid(matrix)
    shortest_route = nx.shortest_path(grid, start, end)
    shortest_length = len(shortest_route)-1
    print(f"The shortest route to the endpoint is {shortest_length} steps")


def part_two():
    data = get_inputs()
    matrix, _, end = create_matrix(data)
    grid = create_grid(matrix)
    possible_candidates = [key for key in matrix.keys() if matrix[key] == "a"]
    paths = []
    for candidate in possible_candidates:
        if nx.has_path(grid, candidate, end):
            result = nx.shortest_path(grid, candidate, end)
            paths.append(len(result)-1)
    print(f"The shortest scenic route to the endpoint is {min(paths)} steps")


if __name__ == "__main__":
    part_one()
    part_two()
