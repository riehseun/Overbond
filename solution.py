#import sys
#sys.setrecursionlimit(15000)
masterArr = []
arr = []
adjacent = []
costTable = []

def getCost(clique):
    cost = 0
    for n in clique:
        for c in costTable:
            if costTable.index(c) == n:
                print c[1]
                if c[1] == 'Email':
                    cost = cost + 0.80
                elif c[1]  == 'Phone':
                    cost = cost + 1
                elif c[1] == 'Overbond':
                    cost = cost + 0.5
            #print cost
    return cost/2

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
        costTable.append([])
        a -= 1
    #print(len(adjacent))


def populateAdjacent():
    for line in edges:
        tempArr = line.split(" ")
        adjacent[int(tempArr[1])].append(int(tempArr[2]))
        adjacent[int(tempArr[2])].append(int(tempArr[1]))

        costTable[int(tempArr[1])].append([tempArr[2],tempArr[3]])
        costTable[int(tempArr[2])].append([tempArr[1],tempArr[3]])
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

fr = open("nodes_world_2b.txt","r");
f = open("result.txt", "w")
for line in fr:
    tempArr = line.split(" ")
    if int(tempArr[0]) in masterArr[0]:
        f.write(line)
fr.close()
f.close()

#print getCost(masterArr[0])
