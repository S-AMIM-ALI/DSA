class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class sll:
    def __init__(self):
        self.start = None

    def isempty(self):
        return self.start is None

    def insert_at_first(self, data):
        self.start = Node(data, self.start)

    def insert_last(self, data):
        n = Node(data)
        if self.isempty():
            self.start = n
        else:
            temp = self.start
            while temp.next:
                temp = temp.next
            temp.next = n

    def insert_after(self, temp, data):
        if temp:
            temp.next = Node(data, temp.next)

    def search(self, data):
        temp = self.start
        while temp:
            if temp.item == data:
                return temp
            temp = temp.next
        return None

    def delete_first(self):
        if self.start:
            self.start = self.start.next

    def delete_last(self):
        if self.start is None:
            return
        if self.start.next is None:
            self.start = None
            return

        temp = self.start
        while temp.next.next:
            temp = temp.next
        temp.next = None

    def delete_item(self, data):
        if self.start is None:
            return

        if self.start.item == data:
            self.start = self.start.next
            return

        temp = self.start
        while temp.next:
            if temp.next.item == data:
                temp.next = temp.next.next
                return
            temp = temp.next

    def print_list(self):
        temp = self.start
        while temp:
            print(temp.item, end=" ")
            temp = temp.next
        print()

    def __iter__(self):
        return slliterator(self.start)


class slliterator:
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
    
mylist = sll()

mylist.insert_at_first(10)
mylist.insert_last(20)
mylist.insert_after(mylist.search(20), 40)

mylist.print_list()      # 10 20 40

mylist.delete_item(40)
mylist.print_list()      # 10 20

mylist.delete_last()
mylist.print_list()      # 10

for val in mylist:
    print(val)
