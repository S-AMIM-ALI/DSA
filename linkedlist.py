class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class sll:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start is None

    def insert_at_first(self, data):
        n = Node(data, self.start)
        self.start = n

    def insert_at_last(self, data):
        n = Node(data)
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
        else:
            self.start = n

    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None

    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(data, temp.next)
            temp.next = n

    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next

    def delete_last(self):
        if self.start is None:
            return
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None

    def delete_item(self, data):
        if self.start is None:
            return
        if self.start.item == data:
            self.start = self.start.next
            return
        temp = self.start
        while temp.next is not None:
            if temp.next.item == data:
                temp.next = temp.next.next
                return
            temp = temp.next

    def __iter__(self):
        return SLLiterator(self.start)


class SLLiterator:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data


# Test
mylist = sll()
mylist.insert_at_first(20)
mylist.insert_at_first(10)
mylist.insert_at_last(30)
mylist.delete_first()

for item in mylist:
    print(item)
