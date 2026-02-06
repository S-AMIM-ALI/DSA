class Node:
    def __init__(self,item=None,priority=None,next=None):
        self.item=item
        self.priority=priority
        self.next=next
class Priority:
    def __init__(self):
        self.start=None
        self.item_count=0
    def is_empty(self):
        return self.item_count==0
    def push(self,data,priority):
        n=Node(data,priority)
        if self.is_empty() or priority<self.start.priority:
           n.next=self.start
           self.start=n
        else:
            temp=self.start
            while temp.next and temp.next.priority<=priority:
                temp=temp.next
            n.next=temp.next
            temp.next=n
        self.item_count+=1
    def pop(self):
        if self.is_empty():
            raise IndexError("underflow")
        else:
            data=self.start.item
            self.start=self.start.next
            self.item_count-=1
            return data
    def size(self):
        return self.item_count
    def display(self):
        temp=self.start
        while temp is not None:
           print(temp.item)
           temp=temp.next
        
pq=Priority()
pq.push('a',5)
pq.push('b',7)
pq.push('c',2)
pq.push('sd',3)
pq.push('g',4)
print(pq.size())
print(pq.display())
while not pq.is_empty():
     pq.pop()

