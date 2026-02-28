# Create a circular singly linked list.
# Insert at:Beginning,End,Given position,Delete:Head,Tail
# Given value
# Count nodes in CLL.
# Search an element in CLL.

class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class cll:
    def __init__(self,last=None):
        self.last=last
    def isempty(self):
        return self.last is None
    def insert_at_first(self,value):
        n=Node(value)
        if self.last is None:
           self.last=n
           n.next=n 
        else:
            n.next=self.last.next
            self.last.next=n
    def insert_at_last(self,value):
        n=Node(value)
        if self.last is None:
            self.last=n 
            n.next=n 
        else:
            n.next=self.last.next
            self.last.next=n 
            self.last=n 

    def search(self,value):
        temp=self.last.next
        while True:
            if temp.item==value:
                return temp
            temp=temp.next
            if temp==self.last.next:
                break

    def insert_after(self,data,value):
        node=self.search(data)
        if node:
            if node==self.last:
                self.insert_at_last(value)
                return
            else:
                n=Node(value,node.next)
                node.next=n 
    def delete_first(self):
        if self.last is None:
            return None
        elif self.last==self.last.next:
            self.last=None
        else:
            first=self.last.next
            self.last.next=first.next
    def delete_last(self):
        if self.last is None:
            return None
        elif self.last==self.last.next:
            self.last=None
        else:
            temp=self.last.next
            while temp.next!=self.last:
                temp=temp.next
            temp.next=self.last.next
            self.last=temp
    def delete_item(self,data):
        if self.last is None:
            return None
        temp=self.last.next
        prev=self.last
        while True:
            if temp.item==data:
                if temp==self.last and temp.next==self.last:
                    self.last=None
                elif temp==self.last:
                    prev.next=self.last.next
                    self.last=prev
                    return
                elif temp==self.last.next:
                    self.last.next=temp.next
                    
                else:
                    prev.next=temp.next
                return 

                prev=temp
                temp=temp.next
                if temp==self.last.next:
                    break
    def print_list(self):
        if self.last is None:
            return None

        temp=self.last.next
        while True:
            print(temp.item,end=' ')
            temp=temp.next
            if temp==self.last.next:
                break
mylist = cll()

mylist.insert_at_first(5)
mylist.insert_after(5, 10)
mylist.insert_at_last(20)
mylist.insert_after(10, 15)

mylist.print_list()      # 10 15 5 20

mylist.delete_first()
mylist.print_list()      # 15 5 20

mylist.delete_last()
mylist.print_list()      # 15 5

mylist.delete_item(5)
mylist.print_list()





            




# Detect if a linked list is circular.
# Convert a normal singly list into circular list.
# Display CLL without infinite loop.
