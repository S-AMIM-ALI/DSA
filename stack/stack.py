class stack:
    def __init__(self):
        self.item=[]
    def isempty(self):
        return len(self.item)==0
    def push(self,data):
        self.item.append(data)
        print("elemnt is inserted",data)
    def pop(self):
        if self.isempty():
            raise IndexError("underflow situation")
        print(self.item.pop())
    def peek(self):
        if self.isempty():
            raise IndexError("Underflow situation")
        return self.item[-1]
    def size(self):
        return len(self.item)
mystack=stack()
mystack.push(10)
mystack.push(20)
mystack.push(30)
mystack.push(40)
mystack.push(50)
print(mystack.size())
print(mystack.pop())
print(mystack.peek())

