class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class CLL:
    def __init__(self):
        self.last = None

    def isempty(self):
        return self.last is None

    # Insert at the beginning
    def insert_start(self, data):
        n = Node(data)
        if self.isempty():
            self.last = n
            self.last.next = self.last
        else:
            n.next = self.last.next
            self.last.next = n

    # Insert at the end
    def insert_last(self, data):
        n = Node(data)
        if self.isempty():
            self.last = n
            self.last.next = self.last
        else:
            n.next = self.last.next
            self.last.next = n
            self.last = n

    # Insert after a specific item
    def insert_item(self, item, data):
        if self.isempty():
            print("List is empty!")
            return

        temp = self.last.next
        while temp != self.last:
            if temp.item == item:
                n = Node(data)
                n.next = temp.next
                temp.next = n
                if temp == self.last:
                    self.last = n
                return
            temp = temp.next

        # Check last node
        if self.last.item == data:
            n = Node(data)
            n.next = self.last.next
            self.last.next = n
            self.last = n
        else:
            print(f"Item {item} not found!")

    # Delete first node
    def delete_first(self):
        if self.isempty():
            print("List is empty!")
            return

        temp = self.last.next
        if temp == self.last:  # only one node
            self.last = None
        else:
            self.last.next = temp.next
        print(f"Deleted first node ({temp.item})")

    # Delete last node
    def delete_last(self):
        if self.isempty():
            print("List is empty!")
            return

        temp = self.last.next
        if temp == self.last:
            print(f"Deleted last node ({temp.item})")
            self.last = None
        else:
            while temp.next != self.last:
                temp = temp.next
            temp.next = self.last.next
            print(f"Deleted last node ({self.last.item})")
            self.last = temp

    # Delete specific item
    def delete_item(self, data):
        if self.isempty():
            print("List is empty!")
            return

        temp = self.last.next
        prev = self.last

        while temp != self.last:
            if temp.item == data:
                prev.next = temp.next
                print(f"Deleted {data}")
                return
            prev = temp
            temp = temp.next

        if self.last.item == data:
            prev.next = self.last.next
            self.last = prev
            print(f"Deleted {data}")
        else:
            print(f"Item {data} not found!")

    # Display all elements
    def display(self):
        if self.isempty():
            print("List is empty!")
            return

        temp = self.last.next
        print("Circular Linked List:", end=" ")
        while temp != self.last:
            print(temp.item, end=" ")
            temp = temp.next
        print(temp.item)  # print last node


# -------------------------
# Test the implementation
# -------------------------
mylist = CLL()
mylist.insert_start(5)
mylist.insert_start(10)
mylist.insert_last(20)
mylist.insert_item(10, 15)
mylist.display()         # 10 15 5 20
mylist.delete_first()    
mylist.display()         # 15 5 20
mylist.delete_last()     
mylist.display()         # 15 5
mylist.delete_item(5)
mylist.display()         # 15
