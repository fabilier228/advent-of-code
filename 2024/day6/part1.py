with open('input.txt', 'r') as reading_file:
    map = reading_file.read().splitlines()

new_map = [list(row) for row in map]
map = new_map


def guard_coordinates(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == '^':
                return [i, j]
    return None


coordinates = guard_coordinates(map)
if coordinates is None:
    print("Guard not found.")
    exit()

guard = {
    "coordinates": coordinates,
    "state": '^'
}

while True:
    y, x = guard['coordinates']

    if not (0 <= y < len(map)) or not (0 <= x < len(map[0])):
        break

    if guard['state'] == '^' and y == 0:
        print("jest na krawedzi u gory")
        break

    if guard['state'] == '>' and x == len(map[0]) - 1:
        print("jest na krawedzi prawo")
        break

    if guard['state'] == 'v' and y == len(map) - 1:
        print("jest na krawedzi na dole")
        break

    if guard['state'] == '<' and x == 0:
        print("jest na krawedzi lewo")
        break

    map[y][x] = "X"
    print(f"Marking position: ({y}, {x})")

    if guard['state'] == '^':
        guard['coordinates'] = [y - 1, x]
        guard['state'] = '>'
    elif guard['state'] == '>':
        guard['coordinates'] = [y, x + 1]
        guard['state'] = 'v'
    elif guard['state'] == 'v':
        guard['coordinates'] = [y + 1, x]
        guard['state'] = '<'
    elif guard['state'] == '<':
        guard['coordinates'] = [y, x - 1]
        guard['state'] = '^'

result = sum(row.count("X") for row in map)
print(f"Total visited cells: {result}")
