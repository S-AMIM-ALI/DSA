#Delete every K-th node.
from cll import *
def item(mylist):
    temp=mylist.last.next
    item_count=0
    while True:
        temp=temp.next
        item_count+=1
        if temp==mylist.last.next:
            break
    print("no of element", item_count)
def kth_delete(mylist,pos):
    count=0
    temp=mylist.last.next
    while temp!=mylist.last:
          count+=1
          temp=temp.next
    
    first=mylist.last.next
    prev=mylist.last
    if pos<1 and pos>count:
        print("invalid")
    
    else:

        if pos==1:
            if count==1:
                mylist.last=None
            else:
                prev.next=first.next
        else:
            for i in range(1,pos):
                prev=first
                first=first.next
            if first==mylist.last:
                prev.next=mylist.last.next
                mylist.last=prev
            else:
                prev.next=first.next
mylist=cll()
mylist.insert_at_first(10)
mylist.insert_after(10,20)
mylist.insert_after(20,30)
mylist.insert_after(30,40)
mylist.insert_after(40,60)
mylist.insert_at_last(50)
mylist.print_list()
item(mylist)
kth_delete(mylist,4)
mylist.print_list()