with open("Inputs/pinput8.txt") as f:
    total = 0
    for line in f:
        keys = ['','','','','','','','','','','abcdefg']
        nums = line[:line.find('|')-1].split(' ')
        out = line[line.find('|')+2:-1].split(' ')
        output = ''
        for num in nums:
            l = len(num)
            if l == 2:
                keys[1] = num
            elif l == 4:
                keys[4] = num
            elif l == 3:
                keys[7] = num
            elif l == 7:
                keys[8] = num
        for j in range(7):
            c = ' '.join(nums).count(keys[10][j])
            if c == 4:
                keys[0] += keys[10][j]
                keys[6] += keys[10][j]
                keys[2] += keys[10][j]
            elif c == 6 and keys[10][j] in keys[4]: #0 4
                keys[0] += keys[10][j]
                keys[6] += keys[10][j]
                keys[5] += keys[10][j]
                keys[9] += keys[10][j]
            elif c == 6 and keys[10][j] not in keys[4]: #0
                keys[0] += keys[10][j]
                keys[6] += keys[10][j]
                keys[2] += keys[10][j]
                keys[3] += keys[10][j]
                keys[5] += keys[10][j]
            elif c == 7:
                keys[6] += keys[10][j]
                keys[2] += keys[10][j]
                keys[3] += keys[10][j]
                keys[5] += keys[10][j]
                keys[9] += keys[10][j]
            elif c == 8 and keys[10][j] in keys[1]: #0 1,2
                keys[0] += keys[10][j]
                keys[2] += keys[10][j]
                keys[3] += keys[10][j]
                keys[9] += keys[10][j]
            elif c == 8 and keys[10][j] not in keys[1]:
                keys[0] += keys[10][j]
                keys[6] += keys[10][j]
                keys[2] += keys[10][j]
                keys[3] += keys[10][j]
                keys[5] += keys[10][j]
                keys[9] += keys[10][j]
            elif c == 9:
                keys[0] += keys[10][j]
                keys[6] += keys[10][j]
                keys[3] += keys[10][j]
                keys[5] += keys[10][j]
                keys[9] += keys[10][j]
        for num in nums:
            if all(d in num for d in keys[0]) and len(num) == 6:
                keys[0] = num
        for od in out:
            for i in range(10):
                if all(v in od for v in keys[i]) and len(od) == len(keys[i]):
                    output += str(i)
        total += int(output)
    print(total)

            

    # num = [2,4,3,7]
    # for line in f:
    #     arr = line[line.find('|')+2:].split(' ')
    #     arr[3] = arr[3][:-1]
    #     for comb in arr:
    #         if len(comb) in num:
    #             total += 1
    # print(total)