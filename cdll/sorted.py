class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next


class SortedCLL:
    def __init__(self):
        self.start = None

    def insert(self, value):
        new_node = Node(item=value)

        # Case 1: Empty list
        if self.start is None:
            new_node.next = new_node
            new_node.prev = new_node
            self.start = new_node
            return

        current = self.start

        # Case 2: Insert before start (smallest element)
        if value <= self.start.item:
            last = self.start.prev

            new_node.next = self.start
            new_node.prev = last

            last.next = new_node
            self.start.prev = new_node

            self.start = new_node
            return

        # Case 3: Insert in middle or end
        while current.next != self.start and current.next.item < value:
            current = current.next

        new_node.next = current.next
        new_node.prev = current

        current.next.prev = new_node
        current.next = new_node

    def display(self):
        if self.start is None:
            print("List is empty")
            return

        temp = self.start
        while True:
            print(temp.item, end=" ")
            temp = temp.next
            if temp == self.start:
                break
        print()
mylist=SortedCLL()
mylist.insert(10)
mylist.insert(2)
mylist.insert(123)
mylist.insert(20)
mylist.insert(50)
mylist.insert(100)
mylist.display()