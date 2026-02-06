class PriorityQueue:
    def __init__(self):
        self.items=[]
    def push(self,data,priority):
        index=0
        while index <len(self.items) and self.items[index][1]<=priority:
            index+=1
        self.items.insert(index,(data,priority))
    def is_empty(self):
        return len(self.items)==0
    def pop(self):
        if self.is_empty():
            raise IndexError("underflow")
        return self.items.pop(0)[0]
    def size(self):
        return len(self.items)
    def display(self):
        return self.items
p=PriorityQueue()
p.push("a",3)
p.push('v',7)
p.push('b',1)
p.push('e',6)
p.push('d',5)
print(f"size of priorityQueue is {p.size()}")
p.display()
while not p.is_empty():
    p.pop()