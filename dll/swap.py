# Swap two nodes without swapping data
from q import dll,Node
def swap(mylist,a,b):
    if a is None or b is None or a==b:
        return 
    curr=a
    while curr and curr!=b:
        curr=curr.next
    if curr is None:
        a,b=b,a
    a_prev,a_next=a.prev,a.next
    b_prev,b_next=b.prev,b.next

    if a_next==b:
        if a_prev:
            a_prev.next=b
        else:
            mylist.start=b
        if b_next:
            b_next.prev=a
        b.prev=a_prev
        a.next=b_next
        b.next=a
        a.prev=b
    else:
        if a_prev:
            a_prev.next=b
        else:
            mylist.start=b
        if b_prev:
            b_prev.next=a
        else:
            mylist.start=a
        if a_next:
            a_next.prev=b
        if b_next:
            b_next.prev=a
        a.prev,b.prev=b_prev,a_prev
        a.next,b.next=b_next,a_next
mylist=dll()

mylist.insert_at_first(10)
mylist.insert_at_last(20)
mylist.insert_at_last(30)
mylist.insert_after(mylist.search(20),25)

#mylist.delete_first()
mylist.insert_at_first(21)
mylist.print_list()
print('\n')
mylist.insert_after(mylist.search(21),22)

mylist.print_list()
swap(mylist,mylist.search(10),mylist.search(25))
print('\n')
mylist.print_list()
    
        


