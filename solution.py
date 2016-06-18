

def getClique(U, arr):
    masterArr = []
    if(len(U) == 0):
        masterArr.append(arr)
        #return arr
    while (len(U) != 0):
   	v = min(U)
    	arr.append(v)
    	U.remove(v)
    	return getClique(list(set(U) & set(getAdjacent(v))), arr)
    return masterArr

#def getClique(U, arr):
#    masterArr = []
#    for v in U:
#        V = U
#        arr.append(v)
#        V.remove(v)
#        if (len(V) == 0):
#            return arr
#        masterArr.append(getClique(list(set(V) & set(getAdjacent(v), arr))
#        return getClique(list(set(V) & set(getAdjacent(v))), arr)
#    return masterArr
	
def getAdjacent(v):
    adjacent = []
    edges = open("edges_world_1.clq","r")
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

#def solution():
#    U = 
#    for v in U:
#        getClique(getNodes(fileName, option), 

#print getNodes("nodes_world_1.txt","r")
arr = []
print getClique(getNodes("nodes_world_1.txt","r"), arr)

#a = ['1','2','3','4','5']
#a.remove('1')
#print a
#print getAdjacent("1");


#print int('1')







#def createEdges(fileName, option

#createNodes("nodes_world_1.txt", "r");

#nodes = openFile("nodes_world_1.txt", "r")
#edges = openFile("edges_world_1.clq", "r")

#openFile("edges_world_1.clq", "r");
