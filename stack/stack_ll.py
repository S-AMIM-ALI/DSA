class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class stack:
    def __init__(self,start=None):
        self.start=start
        self.item_count=0
    def is_empty(self):
        return self.start is None
    def push(self,data):
        n=Node(item=data)
        if self.is_empty():
            self.start=n
        n.next=self.start
        self.start=n 
        self.item_count+=1
        print("element insert",data)
    def pop(self):
        if self.is_empty():
            raise IndexError("underflow")
        data=self.start.item
        self.start=self.start.next
        self.item_count-=1
        print("element is deleted is ",data)
    def peek(self):
        if self.is_empty():
            raise IndexError("Underflow")
        return self.start.item
    def size(self):
        return self.item_count
mylist=stack()
mylist.push(10)
mylist.push(20)
mylist.push(30)
mylist.push(40)
mylist.push(50)
mylist.pop()
mylist.peek()
print(mylist.size())

