# Check if CDLL is palindrom
from cdll import *
class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next
class cdll:
    def __init__(self,start=None):
        self.start=start
    def isempty(self):
        return self.start is None
    def insert(self,value):
        if self.start is None:
            n=Node(item=value)
            self.start=n 
            n.next=n.prev=n 
        else:
            n=Node(item=value)
            current=self.start
            while current.next!=self.start :
                current=current.next
            n.next=current.next
            self.start.prev=n 
            current.next=n 
            n.prev=current
    def display(self):
        temp=self.start
        while True:
            print(temp.item,end=" ")
            temp=temp.next
            if temp==self.start:
                break

        print()
    def is_palindrome(self):
        if mycdll.start is None:
            return True

        left = mycdll.start
        right = mycdll.start.prev  # last node

        while True:
            if left.item != right.item:
                return False

            # If pointers meet or cross, stop
            if left == right or left.next == right:
                break

            left = left.next
            right = right.prev

        return True
       
mycdll=cdll()
# n=5
# for _ in range(5):
#     num = int(input("Enter a number: "))
#     mycdll.insert(num)
# mycdll.display()
# print(mycdll.is_palindrome())


