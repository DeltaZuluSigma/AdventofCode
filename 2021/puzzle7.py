import math

with open("Inputs/pinput7.txt") as f:
    arr = [int(val) for val in f.read().split(',')]
    arr.sort()
    # average
    total = [0,0,0]
    for val in arr:
        stepsum = [abs(val-473),abs(val-474),abs(val-475)]
        for i in range(3):
            if stepsum[i]%2 == 0:
                total[i] += (stepsum[i]+1)*(stepsum[i]/2)
            else:
                total[i] += (stepsum[i]+1)*math.floor(stepsum[i]/2)+stepsum[i]-math.floor(stepsum[i]/2)
    print(*total)
    # median
    # minval = 400000
    # total = 0
    # for i in range(500):
    #     for val in arr:
    #         total += abs(val-arr[i])
    #     minval = min(minval,total)
    #     total = 0
    # print(minval)