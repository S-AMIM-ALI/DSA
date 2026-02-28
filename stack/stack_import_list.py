class stack(list):
    def is_empty(self):
        return len(self)==0
    def push(self,value):
        self.append(value)
        print("elements inserted",value)
    def pop(self):
        if self.is_empty():
            raise IndexError("underflow")
        super().pop()
    def peek(self):
        if self.is_empty():
            raise IndexError("Underflow situation")
        return self[-1]
    def size(self):
        return len(self)
    def insert(self, index, data):
        raise AttributeError(" no attribute insert is allowed")
mylist=stack()
mylist.push(10)
mylist.push(20)
mylist.push(30)
mylist.push(40)
mylist.pop()
mylist.peek()
print(mylist.size())
