class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class sll:
    def __init__(self):
        self.start = None
        self.item_count = 0

    def isempty(self):
        return self.item_count == 0

    def insert_at_first(self, data):
        self.start = Node(data, self.start)
        print("element inserted at first position:", data)
        self.item_count += 1

    def insert_at_last(self, data):
        if self.start is None:
            self.insert_at_first(data)
            return
        temp = self.start
        while temp.next:
            temp = temp.next
        temp.next = Node(data)
        print("element inserted at last position:", data)
        self.item_count += 1

    def insert_at(self, temp, data):
        if temp is None:
            print("given node not found")
            return
        temp.next = Node(data, temp.next)
        print("element inserted after node:", temp.item)
        self.item_count += 1

    def search(self, data):
        temp = self.start
        while temp:
            if temp.item == data:
                return temp
            temp = temp.next
        return None

    def deletefirst(self):
        if self.start is None:
            print("list is empty")
            return
        deleted = self.start.item
        self.start = self.start.next
        print("element deleted at first position:", deleted)
        self.item_count -= 1

    def deletelast(self):
        if self.start is None:
            print("list is empty")
            return
        if self.start.next is None:
            deleted = self.start.item
            self.start = None
        else:
            temp = self.start
            while temp.next.next:
                temp = temp.next
            deleted = temp.next.item
            temp.next = None
        print("element deleted at last position:", deleted)
        self.item_count -= 1

    def deleteitem(self, data):
        if self.start is None:
            print("list is empty")
            return
        if self.start.item == data:
            deleted = self.start.item
            self.start = self.start.next
            print("element deleted:", deleted)
            self.item_count -= 1
            return
        temp = self.start
        while temp.next:
            if temp.next.item == data:
                deleted = temp.next.item
                temp.next = temp.next.next
                print("element deleted:", deleted)
                self.item_count -= 1
                return
            temp = temp.next
        print("element not found")

    def printlist(self):
        temp = self.start
        if temp is None:
            print("list is empty")
            return
        while temp:
            print(temp.item, end=" ")
            temp = temp.next
        print()

    def reverse(self):
        prev = None
        current = self.start
        while current:
            new_node = current.next
            current.next = prev
            prev = current
            current = new_node
        self.start = prev

    def recursive_reverse(self, current, prev=None):
        if current is None:
            self.start = prev
            return
        new_node = current.next
        current.next = prev
        self.recursive_reverse(new_node, current)

    # ✅ Middle element method
    def middle(self):
        if self.start is None:
            print("list is empty")
            return None
        slow = self.start
        fast = self.start
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print("middle element is", slow.item)
        return slow.item

    # Iterator
    def __iter__(self):
        return slliterator(self.start)


class slliterator:
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


# ---------------- TESTING ----------------

mylist = sll()
mylist.insert_at_first(10)
mylist.insert_at(mylist.search(10), 20)
mylist.insert_at(mylist.search(20), 30)
mylist.insert_at_last(40)
mylist.insert_at_last(50)

mylist.printlist()         # 10 20 30 40
mylist.reverse()
mylist.printlist()         # 40 30 20 10
mylist.recursive_reverse(mylist.start)
mylist.printlist()         # 10 20 30 40

for val in mylist:
    print(val, end=" ")
print()

print(f"no of elements in list is {mylist.item_count}")

mylist.middle()            # Middle element

mylist.deletefirst()
mylist.deletelast()
mylist.deleteitem(20)

mylist.printlist()
