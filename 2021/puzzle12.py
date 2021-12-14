pathlist = {}

def totalPaths(node,dst,visited,path,map,exempt,times):
    if node == exempt and times < 1:
        times += 1
    elif node.islower():
        visited[node] = True
    path.append(node)
    global pathlist
    if node == dst:
        #print(path)
        temp = ''.join(path)
        pathlist[temp] = 1
    else:
        for s in map[node]:
            if visited[s] == False:
                totalPaths(s,dst,visited,path,map,exempt,times)
    path.pop()
    visited[node] = False

with open("Inputs/pinput12.txt") as f:
    cxns = []
    for line in f:
        cxns.append([line[:line.find('-')],line[line.find('-')+1:-1]])
map = {}
visited = {}
twice = []
for cxn in cxns:
    for i in range(2):
        map[cxn[i]] = []
        visited[cxn[i]] = False
for attr,value in map.items():
    if attr.islower() and attr != "start" and attr != "end":
        twice.append(attr)
for cxn in cxns:
    map[cxn[0]].append(cxn[1])
    map[cxn[1]].append(cxn[0])
for str in twice:
    totalPaths("start","end",visited,[],map,str,0)
#print(pathlist)
print(len(pathlist))


# def totalPaths(node,dst,visited,path,map):
#     if node.islower():
#         visited[node] = True
#     path.append(node)
#     cum = 0
#     if node == dst:
#         #print(path)
#         cum = 1
#     else:
#         for s in map[node]:
#             if visited[s] == False:
#                 cum += totalPaths(s,dst,visited,path,map)
#     path.pop()
#     visited[node] = False
#     return cum

# with open("Inputs/pinput12.txt") as f:
#     cxns = []
#     for line in f:
#         cxns.append([line[:line.find('-')],line[line.find('-')+1:-1]])
# map = {}
# visited = {}
# for cxn in cxns:
#     for i in range(2):
#         map[cxn[i]] = []
#         visited[cxn[i]] = False
# for cxn in cxns:
#     map[cxn[0]].append(cxn[1])
#     map[cxn[1]].append(cxn[0])
# print(totalPaths("start","end",visited,[],map))