class Deque:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def insert_front(self,data):
        self.items.insert(0,data)
    def insert_rear(self,data):
        self.items.append(data)
    def delete_front(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("underflow")
    def delete_rear(self):
        if not self.is_empty():
            return self.items.pop(-1)
        else:
            raise IndexError("underflow")
    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("underflow")
    def get_rear(self):
        if not self.is_empty():
            return self.items[-1] 
        else:
         raise IndexError("underflow") 
    def size(self):
        return len(self.items)
dq=Deque()
dq.insert_front(10)
dq.insert_front(20)
dq.insert_front(30)
dq.insert_rear(22)
dq.insert_rear(25)
dq.insert_rear(29)
print(f"top element is {dq.get_front()} and last elements is {dq.get_rear()}")
dq.delete_front()
dq.delete_rear()
print(f"top element is {dq.get_front()} and last elements is {dq.get_rear()}") 
 
