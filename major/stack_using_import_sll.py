from sll import *
class stack:
    def __init__(self):
        self.mylists=sll()
        self.item_count=0
    def is_empty(self):
        return self.mylists.isempty()
    def push(self,data):
        self.mylists.insert_at_first(data)
        self.item_count+=1
    def pop(self):
        if self.mylists.isempty():
            print("list is empty")
            pass
        else:
            self.mylists.delete_first()
            self.item_count-=1
    def peek(self):
        if not self.mylists.isempty():
            return self.mylists.start.item
    def size(self):
        return self.item_count
s=stack()
s.push(10)
s.push(11)
s.push(12)
print(s.peek())