#Reverse a circular singly linked list.
from cll  import *

def reverse(mylist):
    if mylist.last and mylist.last.next is None:
        return
    prev=mylist.last
    current=mylist.last.next
    start=current
    while True:
        next_node=current.next
        current.next=prev
        prev=current
        current=next_node
        if current==start:
            break
    mylist.last=start




mylist=cll()
mylist.insert_at_first(10)
mylist.insert_after(10,20)
mylist.insert_after(20,30)
mylist.insert_after(30,40)
mylist.insert_after(40,60)
mylist.insert_at_last(50)
mylist.print_list()
reverse(mylist)
mylist.print_list()
