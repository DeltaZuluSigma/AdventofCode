actions = []
with open("Inputs/pinput8.txt") as f:
    for line in f:
        actions.append(line[:-1])
cidx = i = 0
idxs = [val for val in range(len(actions))]
chg = []
while i in idxs:
    idxs[i] = -1
    val = int(actions[i][actions[i].find(' ')+1:])
    if "nop" in actions[i]:
        chg.append(i)
        i += 1
    elif "jmp" in actions[i]:
        chg.append(i)
        i += val
    else:
        i += 1
while cidx < len(chg):
    cum = i = 0
    idxs = [val for val in range(len(actions))]
    while i in idxs:
        idxs[i] = -1
        val = int(actions[i][actions[i].find(' ')+1:])
        if i == chg[cidx]:
            if "nop" in actions[i] and val != 1:
                i += val
            else:
                i += 1
            continue
        if "acc" in actions[i]:
            cum += val
        elif "jmp" in actions[i] and val != 1:
            i += val
            continue
        i += 1
    if i >= 616:
        break
    cidx += 1
print(cum,";",cidx)



# cum = i = 0
# idxs = [val for val in range(len(actions))]
# while i in idxs:
#     idxs[i] = -1
#     print(i)
#     val = int(actions[i][actions[i].find(' ')+1:])
#     if "acc" in actions[i]:
#         cum += val
#     elif "jmp" in actions[i] and val != 1:
#         i += val
#         continue
#     i += 1
# print(cum)