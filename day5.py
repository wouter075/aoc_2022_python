import copy

with open('day5.txt') as f:
    lines = f.read()

crates_raw, movements_raw = lines.split("\n\n")
crates_raw = crates_raw.split("\n")
max_crates = int(crates_raw[-1:][0].strip().split("   ")[-1:][0])
max_lines = len(crates_raw) - 1

part1 = ""
part2 = ""

crates = []
for x in range(max_crates):
    crates.append([])

for row in range(max_lines - 1, -1, -1):
    col_counter = 0
    for col in range(1, len(crates_raw[row]), 4):
        letter = crates_raw[row][col]
        if letter != ' ':
            crates[col_counter].append(letter)

        col_counter += 1

crates2 = copy.deepcopy(crates)

movements = []
for m in movements_raw.split("\n"):
    m = m.replace("move ", "").replace(" from ", ";").replace(" to ", ";")
    movements.append(list(map(int, m.split(";"))))

movements2 = movements.copy()

for move in movements:
    a, f, t = move

    # part 1
    for _ in range(a):
        letter = crates[f - 1][-1:][0]
        crates[t - 1].append(letter)
        crates[f - 1].pop()

    # part 2
    p = []
    for _ in range(a):
        letter = crates2[f - 1][-1:][0]
        p.append(letter)
        crates2[f - 1].pop()
    p.reverse()
    crates2[t - 1].extend(p)

for x in crates:
    part1 += x[-1:][0]

for x in crates2:
    part2 += x[-1:][0]

print(part1)
print(part2)
