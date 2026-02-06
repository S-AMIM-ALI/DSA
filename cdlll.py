class Node:
    def __init__(self, item=None, prev=None, next=None):
        self.item = item
        self.prev = prev
        self.next = next


class CDLL:
    def __init__(self, start=None):
        self.start = start

    def isempty(self):
        return self.start is None

    def insert_start(self, data):
        n = Node(data)
        if self.isempty():
            n.next = n.prev = n
            self.start = n
        else:
            n.next = self.start
            n.prev = self.start.prev
            self.start.prev.next = n
            self.start.prev = n
            self.start = n

    def insert_last(self, data):
        n = Node(data)
        if self.isempty():
            n.next = n.prev = n
            self.start = n
        else:
            n.next = self.start
            n.prev = self.start.prev
            self.start.prev.next = n
            self.start.prev = n

    def insert_item(self, temp, data):
        if temp is None:
            return None
        n = Node(data)
        n.next = temp.next
        n.prev = temp
        temp.next.prev = n
        temp.next = n

    def delete_first(self):
        if self.isempty():
            return
        if self.start.next == self.start:  # only one node
            self.start = None
        else:
            self.start.prev.next = self.start.next
            self.start.next.prev = self.start.prev
            self.start = self.start.next

    def delete_last(self):
        if self.isempty():
            return
        if self.start.next == self.start:
            self.start = None
        else:
            last = self.start.prev
            before_last = last.prev
            before_last.next = self.start
            self.start.prev = before_last

    def delete_item(self, data):
        if self.isempty():
            return
        temp = self.start
        while True:
            if temp.item == data:
                # If it's the only node
                if temp.next == temp:
                    self.start = None
                    return
                # If deleting start node
                if temp == self.start:
                    self.delete_first()
                    return
                # Otherwise
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                return
            temp = temp.next
            if temp == self.start:
                print("Item not found!")
                return

    def display(self):
        if self.isempty():
            print("List is empty!")
            return
        temp = self.start
        print("Circular Doubly Linked List:", end=" ")
        while True:
            print(temp.item, end=" <=> ")
            temp = temp.next
            if temp == self.start:
                break
        print("(back to start)")


# 🧪 Example usage
mycdll = CDLL()
mycdll.insert_start(10)
mycdll.insert_start(19)
mycdll.insert_last(1999)

mycdll.display()

# Deletions
mycdll.delete_first()
mycdll.display()

mycdll.delete_last()
mycdll.display()

mycdll.insert_last(100)
mycdll.insert_item(mycdll.start, 55)
mycdll.display()
