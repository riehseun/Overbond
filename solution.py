import random
masterArr = []
arr = []
def getClique(U, arr, m):
    
    print len(U)
    if(len(U) == 0):
        masterArr.append(arr);
        return
            
    while (len(U) != 0):
        if (len(U)+len(arr) <= m):
            print "returned early"
            return
    	#v = max(U)
        v = random.choice(U)
    	arr.append(v)
    	U.remove(v)
    	return getClique(list(set(U) & set(getAdjacent(v))), arr, m)
    #return masterArr

def getAdjacent(v):
    adjacent = []
    edges = open("edges_world_2a.clq","r")
    edges.readline()
    for line in edges:
        tempArr = line.split(" ")
        if (int(tempArr[1]) == v and not(int(tempArr[2]) in adjacent)):
            adjacent.append(int(tempArr[2]))
    return adjacent

def getNodes(fileName, option):
    arr = []
    file = open(fileName)

    for line in file:
        tempArr = line.split(" ")
        arr.append(int(tempArr[0]))
     
    file.close
    return arr

getClique(getNodes("nodes_world_2a.txt","r"), arr, 0)
print masterArr

