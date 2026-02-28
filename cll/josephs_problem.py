class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class cll:
    def __init__(self,last=None):
        self.last=last
    def isempty(self):
        return self.last is None
    def insert(self,value):
        n=Node(value)
        if self.isempty():
            self.last=n 
            n.next=n 
        temp=self.last.next
        while temp.next!=self.last.next:
            temp=temp.next

        n.next=self.last.next 
        temp.next=n
        self.last=n 
    
    def josephs(mylist,k):
        if mylist.last is None:
            return None
        current=mylist.last.next
        prev=mylist.last
        while current.next!=current:
            for i in range(k-1):
                prev=current
                current=current.next
            print("element deleted is",current.item)
            prev.next=current.next
            current=current.next
        return current.item
mylist=cll()
n,k=7,3
for i in range(1,n+1):
    mylist.insert(i)
print("survivor",mylist.josephs(k))        
    