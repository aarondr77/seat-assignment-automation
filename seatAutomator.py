import copy;
import queue;

class Theatre:
    
    def __init__(self, left_row_size, right_row_size, number_of_rows):
        self.leftRows = []
        self.rightRows = []

        leftRow = []
        rightRow = []
        for i in range(left_row_size):
            leftRow.append("_")
        for i in range(right_row_size):
            rightRow.append("_")
        
        for i in range(number_of_rows):
            self.leftRows.append((copy.deepcopy(leftRow)))
            self.rightRows.append((copy.deepcopy(rightRow)))

class Group: 
    
    def __init__(self, group_info):
        (self.name, self.size, self.priority) = group_info

    def __lt__(self, other):

        if self.priority == other.priority:
            return self.size > other.size  
        return self.priority < other.priority

def make_group_queue(groups):
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

group_obj_list = []
for g in sampleGroups:
    groupObj = Group(g)
    group_obj_list.append(groupObj)
q = make_group_queue(group_obj_list)
while not q.empty():
    o = q.get(0)
    print ("Name: " + o.name)


