class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next
class Deque:
    def __init__(self):
        self.front=None
        self.rear=None
        self.item_count=0
    def is_empty(self):
        return self.item_count==0
    def insert_front(self,data):
        n=Node(None,data,self.front)
        if self.is_empty():
            self.rear=n
        else:
            self.front.prev=n
        self.front=n
        self.item_count+=1
    def insert_rear(self,data):
        n=Node(self.rear,data,None)
        if self.is_empty():
            self.front=n
        else:
            self.rear.next=n
        self.rear=n
        self.item_count+=1
    def delete_front(self):
        if self.is_empty():
            raise IndexError("underflow")
        elif self.front==self.rear:
            self.front=self.rear=None
        else:
            self.front=self.front.next
            self.front.prev=None
        self.item_count-=1
    def delete_rear(self):
        if self.is_empty():
            raise IndexError("underflow")
        elif self.front==self.rear:
            self.front=self.rear=None
        else:
            self.rear=self.rear.prev
            self.rear.next=None
        self.item_count-=1
    def get_front(self):
        if self.is_empty():
            raise IndexError("underflow")
        else:
            return self.front.item
    def get_rear(self):
        if self.is_empty():
            raise IndexError("underflow")
        else:
            return self.rear.item
    def size(self):
        return self.item_count
dql=Deque()
dql.insert_front(10)
dql.insert_front(20)
dql.insert_front(30)
dql.insert_front(40)
dql.insert_front(50)
dql.insert_rear(60)
dql.insert_rear(70)
dql.insert_rear(80)
print(f"top elements is {dql.size()}")
print(f'top and last elemets is {dql.get_front()},{dql.get_rear()}')
dql.delete_front()
dql.delete_rear()
print(f"top elements is {dql.size()}")
print(f'top and last elemets is {dql.get_front()},{dql.get_rear()}')      