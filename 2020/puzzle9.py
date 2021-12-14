with open("Inputs/pinput9.txt") as f:
    nums = [int(val) for val in f.read().split('\n')]
for i in range(531,1,-1):
    sum = 0
    dec = 0
    while sum < 50047984:
        sum += nums[i-dec]
        dec += 1
    if sum == 50047984:
        set = []
        for j in range(i-dec+1,i+1):
            set.append(nums[j])
        break
set.sort()
print(set[0]+set[16])



# for i in range(25,len(nums)):
#     preamble = [nums[idx] for idx in range(i-25,i)]
#     prop = False
#     for j in range(len(preamble)-1):
#         if abs(nums[i]-preamble[j]) in preamble:
#             prop = True
#             break
#     if not prop:
#         print(nums[i],";",i)
#         break
