import copy;
import queue;

class Theatre:
    
    def __init__(self, leftRowSize, rightRowSize, numberOfRows):
        self.leftRows = []
        self.rightRows = []

        leftRow = []
        rightRow = []
        for i in range(leftRowSize):
            leftRow.append("_")
        for i in range(rightRowSize):
            rightRow.append("_")
        
        for i in range(numberOfRows):
            self.leftRows.append((copy.deepcopy(leftRow)))
            self.rightRows.append((copy.deepcopy(rightRow)))

class Group: 
    
    def __init__(self, groupInfo):
        (self.name, self.size, self.priority) = groupInfo

    def __lt__(self, other):

        if self.priority == other.priority:
            return self.size > other.size  
        return self.priority < other.priority

    def getName(self):
        return self.name

    def getSize(self):
        return self.size

    def getPriority(self):
        return self.priority

def makeGroupQueue(groups):
    q = queue.PriorityQueue()
    for g in groups:
        q.put(g)
    return q
    

t = Theatre(3, 4, 5)
sampleGroups = [
    ("A", 4, 1),
    ("B", 2, 3),
    ("C", 2, 1),
    ("D", 3, 2),
    ("E", 4, 3),
    ("F", 1, 2),
    ("G", 1, 2),
    ("H", 3, 1) ]

# Expected Ordering: A, H, C, D, F/G, E, B 

groupObjList = []
for g in sampleGroups:
    groupObj = Group(g)
    groupObjList.append(groupObj)
q = makeGroupQueue(groupObjList)
while not q.empty():
    o = q.get(0)
    print ("Name: " + o.getName())


