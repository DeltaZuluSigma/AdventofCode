paper = [] ; folds = []
for i in range(895):
    paper.append(['.']*1311)
with open("Inputs/pinput13.txt") as f:
    sep = False
    for line in f:
        if line == '\n' and not sep:
            sep = True
            continue
        if sep:
            folds.append([line[line.find('=')-1],int(line[line.find('=')+1:-1])])
        else:
            paper[int(line[line.find(',')+1:-1])][int(line[:line.find(',')])] = '#'
for fold in folds:
    if fold[0] == 'x':
        l = len(paper[0])-1
        for i in range(len(paper)):
            for j in range(fold[1]):
                if paper[i][l-j] == '#':
                    paper[i][j] = '#'
            paper[i] = paper[i][:fold[1]]
    else:
        l = len(paper)-1
        for i in range(len(paper[0])):
            for j in range(fold[1]):
                if paper[l-j][i] == '#':
                    paper[j][i] = '#'
        paper = paper[:fold[1]]
for line in paper:
    print(''.join(line))



#     for line in f:
#         if line == '\n':
#             break
#         paper[int(line[line.find(',')+1:-1])][int(line[:line.find(',')])] = '#'
# for i in range(895):
#     for j in range(655):
#         if paper[i][1310-j] == '#':
#             paper[i][j] = '#'
#     paper[i] = paper[i][:655]
# dots = 0
# for i in range(895):
#     dots += paper[i].count('#')
# print(dots)