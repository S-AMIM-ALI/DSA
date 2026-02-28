from sll import *

class Queue:
    def __init__(self):
        self.list = sll()
        self.item_count = 0

    def is_empty(self):
        return self.list.isempty()

    def enqueue(self, data):
        self.list.insert_last(data)
        self.item_count += 1

    def dequeue(self):
        if not self.is_empty():
            data = self.list.start.item
            self.list.delete_first()
            self.item_count -= 1
            return data
        else:
            raise IndexError("underflow")

    def get_front(self):
        if not self.is_empty():
            return self.list.start.item
        else:
            raise IndexError("underflow")

    def get_rear(self):
        if not self.is_empty():
            temp = self.list.start
            while temp.next is not None:
                temp = temp.next
            return temp.item
        else:
            raise IndexError("underflow")

    def size(self):
        return self.item_count
q1=Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(22)
q1.enqueue(30)
print(f"{q1.get_front()} and last element is ,{q1.get_rear()}")

q1.dequeue()
print(f"{q1.get_front()} and last element is ,{q1.get_rear()}")
q1.size()