import re

arr = []
for i in range(990):
    arr.append([0] * 990)
with open("Inputs/pinput5.txt") as f:
    for line in f:
        cords = [int(s) for s in re.findall('([1-9][0-9][0-9]|[1-9][0-9]|[0-9])',line)]
        steps = [0,0]
        steps[0] = 1 if cords[0]-cords[2] < 0 else -1
        steps[1] = 1 if cords[1]-cords[3] < 0 else -1
        if cords[1]-cords[3] != 0:
            slope = abs((cords[0]-cords[2])/(cords[1]-cords[3]))
        if cords[0] == cords[2]:
            for i in range(min(cords[1],cords[3]),max(cords[1],cords[3])+1):
                arr[cords[0]][i] += 1
        elif cords[1] == cords[3]:
            for i in range(min(cords[0],cords[2]),max(cords[0],cords[2])+1):
                arr[i][cords[1]] += 1
        elif slope == 1:
            while cords[0] != cords[2]+steps[0]:
                arr[cords[0]][cords[1]] += 1
                cords[0] += steps[0]
                cords[1] += steps[1]
cum = 0
for i in range(990):
    for j in range(990):
        if arr[i][j] >= 2:
            cum += 1
print(cum)
