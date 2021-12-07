import math

with open("Inputs/pinput5.txt") as f:
    seats = []
    for line in f:
        row = [0,127]
        col = [0,7]
        for i in range(6):
            if line[i] == 'F':
                row[1] = math.floor(row[0]+(row[1]-row[0])/2)
            else:
                row[0] = math.ceil(row[0]+(row[1]-row[0])/2)
        for j in range(7,9):
            if line[j] == 'L':
                col[1] = math.floor(col[0]+(col[1]-col[0])/2)
            else:
                col[0] = math.ceil(col[0]+(col[1]-col[0])/2)
        sltrow = row[0] if line[6] == 'F' else row[1]
        sltcol = col[0] if line[9] == 'L' else col[1]
        seats.append(sltrow*8+sltcol)
    empty = []
    for i in range(len(seats)):
        if seats[i]+1 not in seats and seats[i]+2 in seats:
            empty.append(seats[i]+1)
        elif seats[i]-1 not in seats and seats[i]-2 in seats:
            empty.append(seats[i]-1)
    print(*empty)