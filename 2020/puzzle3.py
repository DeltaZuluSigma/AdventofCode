trees = pos = lnum = 0
with open("Inputs/pinput3.txt") as f:
    for line in f:
        lnum += 1
        if lnum%2 == 1:
            if pos > 30:
                pos -= 31
            print(lnum,";",pos,"|",line[pos])
            if line[pos] == '#':
                trees += 1
            pos += 1
print(trees)