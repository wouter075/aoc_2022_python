with open('day3.txt') as f:
    lines = [line.rstrip() for line in f]

part1 = 0
part2 = 0

# part 1
for line in lines:
    c1, c2 = line[:len(line) // 2], line[len(line) // 2:]
    both = ''
    for c in c1:
        if c in c2:
            both = c
            break

    prio = ord(both) - 96
    if prio < 0:
        prio += 58
    part1 += prio

# part 2
elf_groups = [lines[x:x+3] for x in range(0, len(lines), 3)]
for group in elf_groups:
    both = ''
    for c in group[0]:
        if c in group[1] and c in group[2]:
            both = c
            break

    prio = ord(both) - 96
    if prio < 0:
        prio += 58
    part2 += prio

print(part1)
print(part2)
