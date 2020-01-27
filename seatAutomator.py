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


    def seat(self, groups):

class Group: 
    
    def __init__(self, groupInfo):
        (self.name, self.size, self.priority) = groupInfo

    def getName(self):
        return self.name

    def getSize(self):
        return self.size

    def getPriority(self):
        return self.priority

def makeGroupQueue():
    q = queue.PriorityQueue()






t = Theatre(3, 4, 5)
sampleGroups = [
    ("A", 4, 1),
    ("B", 2, 3)
    ("C", 2, 1)
    ("D", 3, 2)
    ("E", 4, 3)
    ("F", 1, 2)
    ("G", 1, 2)
    ("H", 3, 1) ]
print(t.leftRows)
print(t.rightRows)

