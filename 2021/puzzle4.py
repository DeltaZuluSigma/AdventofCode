with open("Inputs/pinput4.txt") as f:
    arr = []
    idx = -1
    order = f.readline().split(',')
    order[len(order)-1] = str(int(order[len(order)-1]))
    for line in f:
        if len(line) <= 1:
            arr.append([])
            idx += 1
        else:
            arr[idx].append(list(filter(None,line.split(' '))))
    info = [-1,-1]   # 0=index; 1=board
    for b in range(len(arr)):
        bmax = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
        for i in range(5):
            indexes = [[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1]]
            for j in range(5):
                indexes[0][j] = order.index(str(int(arr[b][i][j])))
                indexes[1][j] = order.index(str(int(arr[b][j][i])))
            bmax[i] = max(indexes[0])
            bmax[i+5] = max(indexes[1])
        if min(bmax) > info[0]:
            info[0] = min(bmax)
            info[1] = b
    print(order[85])
    print(*arr[43])
# order = [10,80,6,69,22,99,63,92,30,67,28,93,0,50,65,87,38,7,91,60,57,40,84,51,27,12,44,88,64,35,39,74,61,55,31,48,81,89,62,37,94,43,29,14,95,8,78,49,90,97,66,70,25,68,75,45,42,23,9,96,56,72,59,32,85,3,71,79,18,24,33,19,15,20,82,26,21,13,4,98,83,34,86,5,2,73]
# card = [['11','69','4','6','23'],['38','47','16','99','96'],['7','13','40','41','78'],['12','5','1','18','88'],['20','42','10','82','73']]
# for num in order:
#     for i in range(5):
#         for j in range(5):
#             if card[i][j] == str(num):
#                 card[i][j] = 'X'
# print(*card)


    #print(*arr)
    # brk = False
    # for num in order:
    #     for board in arr:
    #         for i in range(5):
    #             for j in range(5):
    #                 if board[i][j] != 'X' and int(board[i][j]) == int(num):
    #                     board[i][j] = 'X'
    #         for i in range(5):
    #             if board[i].count('X') == 5:
    #                 brk = True
    #             elif board[0][i] == 'X' and board[1][i] == 'X' and board[2][i] == 'X' and board[3][i] == 'X' and board[4][i] == 'X':
    #                 brk = True
    #         if brk:
    #             sum = 0
    #             for i in range(5):
    #                 for j in range(5):
    #                     if board[i][j] != 'X':
    #                         sum += int(board[i][j])
    #             print(sum)
    #             break
    #     if brk:
    #         print(num)
    #         break