#Find the middle node of CLL
from cll import *

def middle(mylist):
    slow=first=mylist.last.next
    while first.next!=mylist.last.next and first.next.next!=mylist.last.next:
        slow=slow.next
        first=first.next.next
    print("middle elemenet is ",slow.item)
    t1=t2=mylist.last.next
   



mylist=cll()
mylist.insert_at_first(10)
mylist.insert_after(10,20)
mylist.insert_after(20,30)
mylist.insert_after(30,40)
mylist.insert_after(40,60)
mylist.insert_at_last(50)
mylist.print_list()
middle(mylist)