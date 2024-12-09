with open('input.txt', 'r') as reading_file:
    string = reading_file.read()

def part_1():
    with open('input.txt', 'r') as reading_file:
        disk = reading_file.read().strip()


    layout = []

    for idx in range(len(disk)):
        ch = idx // 2 if idx % 2 == 0 else "."
        layout.extend([ch] * int(disk[idx]))

    while layout.count("."):
        pos = layout.index(".")
        n = layout.pop()
        layout[pos] = n

        while layout[-1] == ".":
            layout.pop()

    print(sum(c*i for i, c in enumerate(layout)))

part_1()