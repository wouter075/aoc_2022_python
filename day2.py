with open('day2.txt') as f:
    lines = [line.rstrip() for line in f]

part1 = 0
part2 = 0

for line in lines:
    o, m = line.split(" ")

    if o == "A" and m == "X":
        part1 += (3 + 1)
        part2 += 3
    if o == "B" and m == "Y":
        part1 += (3 + 2)
        part2 += (3 + 2)
    if o == "C" and m == "Z":
        part1 += (3 + 3)
        part2 += (6 + 1)

    if o == "A" and m == "Y":
        part1 += (6 + 2)
        part2 += (3 + 1)
    if o == "B" and m == "Z":
        part1 += (6 + 3)
        part2 += (6 + 3)
    if o == "C" and m == "X":
        part1 += (6 + 1)
        part2 += (0 + 2)

    if o == "A" and m == "Z":
        part1 += 3
        part2 += (6 + 2)
    if o == "B" and m == "X":
        part1 += 1
        part2 += (0 + 1)
    if o == "C" and m == "Y":
        part1 += 2
        part2 += (3 + 3)

print(part1)
print(part2)
