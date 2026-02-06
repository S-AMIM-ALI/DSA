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
    def insert_first(self,data):
        n=Node(data)
        if self.isempty():
            n.next=n.prev=n
            self.start=n 
        else:
            n.next=self.start
            n.prev=self.start.prev
            self.start.prev.next=n
            self.start.prev=n
            self.start=n
            return 
    def insert_after(self,data):
        n=Node(data)            
        if self.isempty():
            n.next=n.prev=n
            self.start=n
        n.next=self.start
        n.prev=self.start.prev
        self.start.prev.next=n
        self.start.prev=n
    def insert_item(self,temp,data):
        if temp is None:
            pass
        else:
            n=Node(data)
            n.next=temp.next
            n.prev=temp
            temp.next.prev=n
            temp.next=n
    def delete_first(self):
        if self.isempty():
            return 
        elif self.start.next==self.start:
             self.start=None
        else:
             self.start.prev.next=self.start.next
             self.start.next.prev=self.start.prev
             self.start=self.start.next
    def delete_last(self):
        if self.isempty():
            return
        elif self.start.next==self.start:
            self.start =None
        else:
            last=self.start.prev
            before_last=self.start.prev.prev
            before_last.next=self.start
            self.start.prev=before_last
    def delete_item(self,data):
        if data is None:
            return
        temp=self.start
        while True:
            if temp.item==data:
                if temp.next==temp:
                    self.start=None
                if temp==self.start:
                    self.delete_first()
                    return
                temp.prev.next=temp.next
                temp.next.prev=temp.prev
                return
            temp=temp.next
            if temp==self.start:
                print("element not found")
    def display(self):
        if self.isempty():
            print("list is empty")
        temp=self.start
        
        while True:
            print(temp.item,end=' ')
            temp=temp.next
            if temp==self.start:
                break
mycdll = cdll()
mycdll.insert_start(10)
mycdll.insert_start(19)
mycdll.insert_last(1999)

mycdll.display()

# Deletions
mycdll.delete_first()
mycdll.display()

mycdll.delete_last()
mycdll.display()

mycdll.insert_last(100)
mycdll.insert_item(mycdll.start, 55)
mycdll.display()
             

    