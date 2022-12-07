with open('day7.txt') as f:
    lines = [line.rstrip() for line in f]

path = ['/']
fs = {"/": 0}
part1 = 0
part2 = 0
used_space = 0

for line in lines:
    if line.startswith("$ cd "):
        d = line[5:]

        if d == '/':
            path = ['/']
        elif d == '..':
            path.pop()
        else:
            path.append(d)
            fs["/".join(path)] = 0

    # if it starts with a number, it is a file
    # ignore filenames, for now
    if line.split(" ")[0].isnumeric():
        f = int(line.split(" ")[0])
        fs["/".join(path)] += f

        # needed for part 2
        used_space += f

        # also add to parent
        if len(path) == 1:
            fs['/'] += f
        else:
            for x in range(len(path) - 1, 0, -1):
                fs["/".join(path[:x])] += f

# part 1
for s in fs.values():
    if s <= 100000:
        part1 += s

# part 2
unused_space = 70000000 - used_space
fs_tmp = []
for s in fs.values():
    if unused_space + s >= 30000000:
        fs_tmp.append(s)
part2 = min(fs_tmp)

print(part1)
print(part2)
