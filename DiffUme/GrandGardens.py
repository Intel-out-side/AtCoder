N = int(input())
h = list(map(int, input().split()))

counter = 0

def splitByZero(li):
    returnList = []
    tmpList = []

    for item in li:
        if item > 0:
            tmpList.append(item)

        if item == 0:
            if tmpList:
                returnList.append(tmpList)
            tmpList = []

    if tmpList:
        returnList.append(tmpList)

    return returnList

def dfs(li):
    global counter
    if len(li) == 0:
        return

    li = splitByZero(li)

    for sublist in li:
        minHeight = min(sublist)
        sublist = list(map(lambda x:x-minHeight, sublist))
        counter += minHeight
        dfs(sublist)

dfs(h)

print(counter)
