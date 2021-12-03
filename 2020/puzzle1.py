arr = []
with open("Inputs/pinput1.txt") as f:
    for line in f:
        arr.append(int(line))

#for val in arr:
#   remain = 2020-val
#       if remain in arr:
#           print

for a in arr:
    for b in arr:
        remain = 2020-a-b
        if remain in arr:
            print(a,",",b,",",remain,";",a*b*remain)
            break