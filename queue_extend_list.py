class Queue(list):
    def is_empty(self):
        return len(self)==0
    def enqueue(self,data):
        self.append(data)
    def dequeue(self):
        if not self.is_empty():
            return self.pop(0)
        else:
            raise IndexError("list is empty")
    def get_front(self):
        if not self.is_empty():
            return self[0]
        else:
            raise IndexError("undeflow") 
    def get_rear(self):
        if not self.is_empty():

           return self[-1]
        else:
            raise IndexError("underflow")
    def size(self):
        return len(self)
q1=Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(202)
q1.enqueue(22)
print(f"front{q1.get_front()} and last element is {q1.get_rear()}")
q1.dequeue()
print(f"front{q1.get_front()} and last element is {q1.get_rear()}")
print(f"no of elemenets in {q1.size()}")
