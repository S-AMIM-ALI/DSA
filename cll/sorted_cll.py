class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class sorted_cll:
    def __init__(self,last=None):
        self.last=last
    def isempty(self):
        return self.last is None
    def insert(self,value):
        n=Node(value)
        if self.isempty():
            self.last=n 
            n.next=n 
        else:
            first=self.last.next
            if value<=first.item :
                n.next=first
                self.last.next=n 
                return
            current=first
            while current.next!=first and current.next.item<value:
                   current=current.next
            n.next=current.next
            current.next=n 

            if current==self.last:
                self.last=n 
                
    def print_sorted(self):
        temp=self.last.next
        while True:
            print(temp.item,end=' ')
            temp=temp.next
            if temp==self.last.next:
                break
        print()
mylist=sorted_cll()
mylist.insert(10)
mylist.insert(15)
mylist.insert(5)
mylist.insert(3)
mylist.insert(13)
mylist.print_sorted()
            




