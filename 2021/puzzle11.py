grid = []
gsize = 10
with open("Inputs/pinput11.txt") as f:
    for line in f:
        grid.append([int(val) for val in line[:-1]])
# flashes = 0
for step in range(10000):
    for i in range(gsize):
        for j in range(gsize):
            grid[i][j] += 1
    while any(x > 9 for x in grid[0]) or any(x > 9 for x in grid[1]) or any(x > 9 for x in grid[2]) or any(x > 9 for x in grid[3]) or any(x > 9 for x in grid[4]) or any(x > 9 for x in grid[5]) or any(x > 9 for x in grid[6]) or any(x > 9 for x in grid[7]) or any(x > 9 for x in grid[8]) or any(x > 9 for x in grid[9]):
        for i in range(gsize):
            for j in range(gsize):
                if grid[i][j] > 9:
                    grid[i][j] = -100
                    if i-1 >= 0:
                        grid[i-1][j] += 1
                    if i-1 >= 0 and j+1 < gsize:
                        grid[i-1][j+1] += 1
                    if j+1 < gsize:
                        grid[i][j+1] += 1
                    if i+1 < gsize and j+1 < gsize:
                        grid[i+1][j+1] += 1
                    if i+1 < gsize:
                        grid[i+1][j] += 1
                    if i+1 < gsize and j-1 >= 0:
                        grid[i+1][j-1] += 1
                    if j-1 >= 0:
                        grid[i][j-1] += 1
                    if i-1 >= 0 and j-1 >= 0:
                        grid[i-1][j-1] += 1
    for i in range(gsize):
        for j in range(gsize):
            if grid[i][j] < 0:
                # flashes += 1
                grid[i][j] = 0
    if all(x == 0 for x in grid[0]) and all(x == 0 for x in grid[1]) and all(x == 0 for x in grid[2]) and all(x == 0 for x in grid[3]) and all(x == 0 for x in grid[4]) and all(x == 0 for x in grid[5]) and all(x == 0 for x in grid[6]) and all(x == 0 for x in grid[7]) and all(x == 0 for x in grid[8]) and all(x == 0 for x in grid[9]):
        print(step)
        break
# print(flashes)
# print(*grid)