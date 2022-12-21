with open('day14.txt') as f:
    lines = [line.rstrip() for line in f]

low_col = 1000
high_col = 0
max_row = 0
grid = []
draw = []

for line in lines:
    parts = line.split(" -> ")
    for part in range(len(parts[:-1])):
        col, row = parts[part].split(",")
        col = int(col)
        row = int(row)

        if col >= high_col:
            high_col = col

        if col <= low_col:
            low_col = col

        if row >= max_row:
            max_row = row

        next_col = int(parts[part + 1].split(",")[0])
        next_row = int(parts[part + 1].split(",")[1])

        if col == next_col:
            # same column
            if row < next_row:
                start = row
                stop = next_row
            else:
                start = next_row
                stop = row

            for i in range(start, stop + 1):
                draw.append([col, i])

        if row == next_row:
            #     # same row
            if col < next_col:
                start = col
                stop = next_col
            else:
                start = next_col
                stop = col

            for i in range(start, stop + 1):
                draw.append([i, row])

    last_col, last_row = parts[-1:][0].split(",")

    if int(last_col) >= high_col:
        high_col = int(last_col)

    if int(last_col) <= low_col:
        low_col = int(last_col)

for r in range(max_row + 1):
    row = []
    for c in range(low_col, high_col + 1):
        row.append(".")
    grid.append(row)

sand = abs(low_col - 500)
grid[0][sand] = "+"
for d in draw:
    col, row = d
    grid[row][col - low_col] = "#"

# sand dropper:
for x in range(1, len(grid) - 1):
    next_row = grid[x + 1][sand]
    if next_row == "#":
        # update current:
        grid[x][sand] = "o"
    if next_row == "o":
        pass
        
for g in grid:
    print("".join(g))


