arr = []
with open("Inputs/pinput1.txt") as f:
    # cuminc = 0
    # pre = 99999
    # for val in f:
    #     cur = int(val)
    #     if cur > pre:
    #         cuminc += 1
    #     pre = cur
    # print(cuminc)
    for val in f:
        arr.append(int(val))
cuminc = 0
for i in range(1,len(arr)-2):
    windowa = arr[i-1]+arr[i]+arr[i+1]
    windowb = arr[i]+arr[i+1]+arr[i+2]
    if windowb > windowa:
        print(i,"|",windowa,":",windowb," yes")
        cuminc += 1
    else:
        print(i,"|",windowa,":",windowb," no")
print(cuminc)