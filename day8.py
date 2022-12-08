from time import time

with open('day8.txt') as f:
    lines = [line.rstrip() for line in f]

start_time = time()

grid = []
for line in lines:
    row = []
    for x in line:
        row.append(int(x))
    grid.append(row)

parse_time = time()

around = (len(lines) * 2) - 2 + (len(lines[0]) * 2) - 2
part1 = around

for row in range(1, len(lines) - 1):
    for col in range(1, len(lines[0]) - 1):
        current = grid[row][col]

        # tree to start
        vis = all(x < current for x in grid[row][:col])
        if vis:
            part1 += 1
            continue

        # tree to end
        vis = all(x < current for x in grid[row][col+1:])
        if vis:
            part1 += 1
            continue

        # tree to top
        vis = True
        for tt in range(row - 1, -1, -1):
            if grid[tt][col] >= current:
                vis = False
                break

        if vis:
            part1 += 1
            continue

        # tree to end
        vis = True
        for te in range(row + 1, len(lines)):
            if grid[te][col] >= current:
                vis = False
                break

        if vis:
            part1 += 1
            continue

part1_time = time()
# part 2
# skip outer row
part2 = 0
for row in range(1, len(lines) - 1):
    for col in range(1, len(lines[0]) - 1):
        current = grid[row][col]

        # up, tree to top
        up = 0
        for tt in range(row - 1, -1, -1):
            if grid[tt][col] < current:
                up += 1
            else:
                up += 1
                break

        # left, tree to start
        left = 0
        for ts in range(col - 1, -1, - 1):
            if grid[row][ts] < current:
                left += 1
            else:
                left += 1
                break

        down = 0
        for te in range(row + 1, len(lines)):
            if grid[te][col] < current:
                down += 1
            else:
                down += 1
                break

        right = 0
        for te in range(col + 1, len(lines[0])):
            if grid[row][te] < current:
                right += 1
            else:
                right += 1
                break
        if part2 < up * left * down * right:
            part2 = up * left * down * right

part2_time = time()

print(part1)
print(part2)

print("-[ stats ]" + "-" * 30)
print("Parse time:\t", (parse_time - start_time) * 10**3, "ms")
print("Part 1:\t\t", (part1_time - start_time) * 10**3, "ms")
print("Part 2:\t\t", (part2_time - start_time) * 10**3, "ms")