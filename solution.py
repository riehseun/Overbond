import sys
sys.setrecursionlimit(15000)
masterArr = []
arr = []
adjacent = []


def getClique(U, arr, isFirstCall):
    if(len(U) == 0):
        print "U is equal to 0"
        if arr not in masterArr:
            masterArr.append(arr)
        return
            
    while (len(U) > 0):
        #print U
        if(isFirstCall == True):
            v = getMax(U)
        else:
            v = min(U)
        #print v
    	arr.append(v)
    	U.remove(v)
        return getClique(list(set(U) & set(getAdjacent(v))), arr, False)

def initAdjacent():
    W = getNodes("nodes_world_2b.txt","r")
    a = max(W)
    while (a >= 0): 
        adjacent.append([])
        a -= 1
    #print(len(adjacent))


def populateAdjacent():
    for line in edges:
        tempArr = line.split(" ")
        adjacent[int(tempArr[1])].append(int(tempArr[2]))
        adjacent[int(tempArr[2])].append(int(tempArr[1]))
        #if (not(int(tempArr[2]) in adjacent[int(tempArr[1])])):
        #    adjacent[int(tempArr[1])].append(int(tempArr[2]))
        #elif (not(int(tempArr[1]) in adjacent[int(tempArr[2])])):
        #    adjacent[int(tempArr[2])].append(int(tempArr[1]))
    return adjacent

def getAdjacent(v):
    return adjacent[v]

def getNodes(fileName, option):
    arr = []
    file = open(fileName)

    for line in file:
        tempArr = line.split(" ")
        arr.append(int(tempArr[0]))
     
    return arr

def openFile(f):
    global edges
    edges = []
    #f.readline()
    for e in f:
        edges.append(e)
    return edges
with open("edges_world_2b.clq","r") as f:
    edges = openFile(f)
    #print(edges)

def getMax(I):
    m = -1
    file = open("a.txt","w")
    for ad in adjacent:
        #file.write(str(adjacent.index(ad)))
        #file.write(" ")
        #file.write(str(len(ad)))
        #file.write("\n")
        if (len(ad) > m):
            m = len(ad)
            j = ad
    return adjacent.index(j)




initAdjacent()
populateAdjacent()
V = getNodes("nodes_world_2b.txt","r")
getClique(V, arr, True)
print masterArr
print len(masterArr[0])
#print getMax(V)



#T = [[1,2,3],[4,5,2],[6,5,4,2],[1,2]]
#print getMax(T)
