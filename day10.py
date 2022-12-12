with open('day10.txt') as f:
    lines = [line.rstrip() for line in f]

part1 = 0

x = 1
cycle = 0
cycles = []

screen = []
for _ in range(6):
    row = []
    for _ in range(40):
        row.append(".")
    screen.append(row)

doubler = []
for d in range(20, 221, 40):
    doubler.append(d)

for line in lines:
    if line == "noop":
        cycle += 1
        if cycle in doubler:
            cycles.append(x * cycle)
    else:
        cycle += 1
        if cycle in doubler:
            cycles.append(x * cycle)

        cycle += 1
        if cycle in doubler:
            cycles.append(x * cycle)

        x += int(line.split(" ")[1])

part1 = sum(cycles)

print(part1)

for row in screen:
    print("".join(row))


