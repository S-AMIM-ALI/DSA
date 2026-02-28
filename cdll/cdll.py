class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next


class cdll:
    def __init__(self):
        self.start = None

    def isempty(self):
        return self.start is None

    def insert_at_first(self, data):
        if self.start is None:
            n = Node(None, data, None)
            n.next = n.prev = n
            self.start = n
        else:
            last = self.start.prev
            n = Node(last, data, self.start)
            last.next = n
            self.start.prev = n
            self.start = n

    def insert_at_last(self, data):
        if self.start is None:
            self.insert_at_first(data)
        else:
            last = self.start.prev
            n = Node(last, data, self.start)
            last.next = n
            self.start.prev = n

    def search(self, data):
        if self.start is None:
            return None

        temp = self.start
        while True:
            if temp.item == data:
                return temp
            temp = temp.next
            if temp == self.start:
                break
        return None

    def insert_after(self, item, data):
        node = self.search(item)
        if node:
            n = Node(node, data, node.next)
            node.next.prev = n
            node.next = n

    def delete_first(self):
        if self.start is None:
            return
        elif self.start == self.start.next:
            self.start = None
        else:
            last = self.start.prev
            self.start.next.prev = last
            last.next = self.start.next
            self.start = self.start.next

    def delete_last(self):
        if self.start is None:
            return
        elif self.start == self.start.next:
            self.start = None
        else:
            last = self.start.prev
            last.prev.next = self.start
            self.start.prev = last.prev

    def delete_item(self, data):
        node = self.search(data)
        if node is None:
            return

        # single node case
        if node.next == node:
            self.start = None
            return

        # deleting start node
        if node == self.start:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.start = node.next
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

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
mycdll=cdll()
# mycdll.insert_at_first(10)
# mycdll.insert_after(10,20)
# mycdll.insert_after(20,30)
# mycdll.insert_after(30,40)
# mycdll.insert_at_last(50)
# mycdll.display()
# mycdll.delete_first()
# mycdll.delete_last()
# mycdll.delete_item(20)
# print("\n")
# mycdll.display()

    
