with open("Inputs/pinput6.txt") as f:
    line = f.read()
    arr = [0,0,0,0,0,0,0,0,0]
    for i in range(1,6):
        arr[i] = line.count(str(i))
    for j in range(256):
        temp = arr[0]
        for k in range(len(arr)-1):
            arr[k] = arr[k+1]
        arr[8] = temp
        arr[6] += temp
    sum = 0
    for val in arr:
        sum += val
    print(sum)
    # arr = [int(d) for d in f.read().split(',')]
    # for i in range(80):
    #     for j in range(len(arr)):
    #         arr[j] -= 1
    #         if arr[j] < 0:
    #             arr[j] = 6
    #             arr.append(8)
    # print(len(arr))