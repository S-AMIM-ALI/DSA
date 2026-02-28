class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next
class cdll:
    def __init__(self,start=None):
        self.start=start
    def isempty(self):
        return self.start is None
    def insert(self,value):
        if self.isempty():
            n=Node(item=value)
            n.next=n.prev=n 
            self.start=n 
        else:
            current=self.start
            n=Node(item=value)
            while current.next!=self.start:
                current=current.next
            
            n.next=current.next
            self.start.prev=n 
            current.next=n 
            n.prev=current
    def display(self):
        count=0
        current=self.start
        while True:
            print(current.item,end=" ")
            count+=1
            current=current.next
            if current==self.start:
                break
        print()
        print(f"no of nodes in list",count)
    def remove_duplicate(self):
        if self.start is None or self.start.next ==self.start:
            return 
        current=self.start
        while True:
            temp=current.next
            while temp!=self.start:
                if temp.item==current.item:
                    print("deleted element is",temp.item)
                    temp.prev.next=temp.next
                    temp.next.prev=temp.prev
                    temp=temp.next
                else:
                    temp=temp.next
            current=current.next
            if current==self.start:
                break


mycdll=cdll()
n=int(input("no of node you want"))
for i in range(n):
    mycdll.insert(int(input(f"enter at pos {i} ")))
mycdll.display()
mycdll.remove_duplicate()
mycdll.display()