with open('day4.txt') as f:
    lines = [line.rstrip() for line in f]

part1 = 0
part2 = 0

for line in lines:
    a1, a2 = line.split(",")
    s1b, s1e = a1.split("-")
    s2b, s2e = a2.split("-")

    r1 = range(int(s1b), int(s1e) + 1)
    r2 = range(int(s2b), int(s2e) + 1)

    if set(r1).issubset(r2) or set(r2).issubset(r1):
        part1 += 1

    for x in r1:
        if x in r2:
            part2 += 1
            break

print(part1)
print(part2)
