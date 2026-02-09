class node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next

class dll:
    def __init__(self, start=None):
        self.start = start

    def isempty(self):
        return self.start is None

    def insertstart(self, data):
        n = node(item=data)
        if self.isempty():
            self.start = n
        else:
            n.next = self.start
            self.start.prev = n
            self.start = n

    def insertlast(self, data):
        n = node(item=data)
        if self.isempty():
            self.start = n
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
            n.prev = temp

    def insertitem(self, temp, data):
        n = node(prev=temp, item=data, next=temp.next)
        if temp.next is not None:
            temp.next.prev = n
        temp.next = n

    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                print("Found:", temp.item)
                return temp
            temp = temp.next
        print("Not found")
        return None

    def printlist(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=" ")
            temp = temp.next
        print()

    def deletefirst(self):
        if self.isempty():
            return None
        else:
            self.start = self.start.next
            if self.start is not None:
                self.start.prev = None

    def deletelast(self):
        if self.isempty():
            return None
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.prev.next = None

    def deleteitem(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    self.start = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                return
            temp = temp.next
        print("Element not found.")

    def __iter__(self):
        return dlliterator(self.start)

class dlliterator:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data
# Create the doubly linked list
d = dll()

# Insert some nodes
d.insertlast(10)
d.insertlast(20)
d.insertlast(30)

print("Before insertion:")
d.printlist()   # Output: 10 20 30

# Search for node 20 and insert 35 after it
found_node = d.search(20)
if found_node:
    d.insertitem(found_node, 35)

print("After insertion:")
d.printlist()   # Output: 10 20 35 30


d.deleteitem(20)
print("After deleting 20:")
d.printlist()   # 5 10 30

print("Iterating using for loop:")
for x in d:
    print(x)

