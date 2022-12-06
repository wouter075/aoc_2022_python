with open('day6.txt') as f:
    line = f.read().strip()

# part 1
for x in range(3, len(line)):
    if len(set(line[x - 4:x])) == 4:
        print(x)
        break

# part 2
for x in range(13, len(line)):
    if len(set(line[x - 14:x])) == 14:
        print(x)
        break
