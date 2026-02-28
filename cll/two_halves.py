#Split a circular linked list into two halves.
import sys
sys.path.append(r"D://pythoncodes//dsa") 
from sll.sll import Node,sll
def convert(mylist):
    first=mylist.start
    if first is None:
        return None
    while first.next is not None:
        first=first.next
    first.next=mylist.start
    return mylist.start
def print_cll(head):
    temp=head
    if temp is None:
        return None
    while True:
        print(temp.item,end="->")
        temp=temp.next
        if temp==head:
            break
    print("traversal completed")

def halves(mylist):
    if mylist.start is None:
        return None,None
    fast=mylist.start
    slow=mylist.start
    while fast.next!=mylist.start  and fast.next.next!=mylist.start:
        slow=slow.next
        fast=fast.next.next
    if fast.next.next==mylist.start:
        fast=fast.next
    head1=mylist.start
    head2=slow.next
    fast.next=head2
    slow.next=head1
    return head1,head2







mylist=sll()
mylist.insert_at_first(10)
mylist.insert_after(mylist.search(10),20)
mylist.insert_after(mylist.search(20),25)
mylist.insert_after(mylist.search(25),30)
mylist.insert_after(mylist.search(30),35)
mylist.insert_last(40)
mylist.print_list()
convert(mylist)

h1,h2=halves(mylist)
print_cll(h1)
print_cll(h2)

