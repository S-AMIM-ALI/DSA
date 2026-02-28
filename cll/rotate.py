#Rotate a circular linked list by K nodes.
from cll import *
def Rotate(mylist,k):
    if mylist.last is None or mylist.last==mylist.last.next:
        return mylist
    curr=mylist.last.next
    item_count=0
    while curr.next!=mylist.last.next:
        curr=curr.next
        item_count+=1
    #length=item_count+1
    length=item_count

    if k%length==0:
        return mylist
    temp=mylist.last.next
    for i in range(length-k):
        temp=temp.next
    mylist.last=temp

mylist=cll()
mylist.insert_at_first(10)
mylist.insert_after(10,20)
mylist.insert_after(20,30)
mylist.insert_after(30,40)
mylist.insert_after(40,60)
mylist.insert_at_last(50)
mylist.print_list()
Rotate(mylist,3)
mylist.print_list()

Rotate(mylist,4)
mylist.print_list()

Rotate(mylist,2)
mylist.print_list()

    
