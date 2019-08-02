if root == None: return
        
    # tuple (pos, lvl, node.info)
    tupleList = [(0,0,root.info)]
    tupleAppend(tupleList, root.left, 0, 0, 'L')
    tupleAppend(tupleList, root.right, 0, 0, 'R')

    # select tuples with lowest lvl for each pos
    tupleList.sort(key = lambda tup: (tup[0], tup[1]))
    i = 0
    while i < len(tupleList) - 1:
        while tupleList[i][0] == tupleList[i + 1][0]:
            tupleList.pop(i + 1)
            if (i + 1) > len(tupleList) - 1: break
        i += 1
    
    for _, _, data in tupleList: print(data, end = " ")

def tupleAppend(ls, node, pos, lvl, direction):
    if node:
        if direction == 'L': pos = pos - 1
        elif direction == 'R': pos = pos + 1
        lvl = lvl + 1
        ls.append((pos, lvl, node.info))
        tupleAppend(ls, node.left, pos, lvl, 'L')
        tupleAppend(ls, node.right, pos, lvl, 'R')