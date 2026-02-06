class stack:
    def __init__(self):
        self.item=[]
    def is_empty(self):
        return len(self.item)==0
    def push(self,data):
        self.item.append(data)
    def pop(self):
        if not self.is_empty():
            return self.item.pop()
        else:
            raise IndexError("list is empty")
    def peek(self):
        if not self.is_empty():
            return self.item[-1]
        else:
            raise IndexError("list is empty")
    def size(self):
        return len(self.item)
s1=stack()
s1.push(20)
s1.push(30)
s1.push(10)
print(f"no of elments in list is {s1.size()}")
print(f" top element in list {s1.peek()}")
s1.pop()
print(f" top element in list {s1.peek()}")