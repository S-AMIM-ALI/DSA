class Queue:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def enqueue(self,data):
        self.items.append(data)
    def dequeue(self):
        if not self.is_empty():
             self.items.pop(0)
        else:
            raise IndexError("underflow")
    def get_front(self):
        if not self.is_empty():
            return  self.items[0]
        else:
            raise IndexError("underflow")
    def get_rear(self):
        if not self.is_empty():
            return  self.items[-1]
        else:
            raise IndexError("underflow")
    def size(self):
        return len(self.items)
q1=Queue()
try:
    print(q1.get_front())
except IndexError as e:
    print(e.args[0])
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(33)
q1.enqueue(34)
print(f"top element is {q1.get_front()} and last elementts is {q1.get_rear()}")
try:
    print(f"after deleting no of elements in queue is {q1.size()}")
except IndexError as e :
    print(e.args[0])