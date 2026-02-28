#Split into even and odd positioned nodes.
import sys
from cll import *
def split_even_odd(mylist):
    if mylist.last is None:
        return None,None
    current=mylist.last.next
    pos=1
    start=current
    odd_head=odd_tail=None
    even_head=even_tail=None
    while True:
        next_node=current.next
        if pos%2==1:
            if odd_head is None:
                odd_head=odd_tail=current
            else:
                odd_tail.next=current
                odd_tail=current
        else:
            if even_head is None:
                even_head=even_tail=current
            else:
                even_tail.next=current
                even_tail=current
        pos+=1
        current=next_node
        if current==start:
            break
    if even_tail:
        even_tail.next=even_head
    if odd_tail:
        odd_tail.next=odd_head
    return odd_head,even_head

def print_list_(head):
        temp=head
        if temp is None:
            return None
        while True:
            print(temp.item,end=' ')
            temp=temp.next
            if temp==head:
                break



mylist=cll()
mylist.insert_at_first(10)
mylist.insert_after(10,20)
mylist.insert_after(20,30)
mylist.insert_after(30,40)
mylist.insert_at_last(50)
mylist.print_list()
print("\n")
h1,h2=split_even_odd(mylist)
print_list_(h1)
print("\n")
print_list_(h2)


