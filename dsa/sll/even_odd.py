#Segregate even and odd nodes
from sll import sll,Node

def Segregate(mylist):
    if mylist.start is None:
        return mylist
    even_start=even_end=None
    odd_start=odd_end=None
    curr=mylist.start
    while curr:
        new_node=curr.next
        curr.next=None

        if curr.item % 2==0:
            if even_start is None:
                even_start=even_end=curr
            else:
                even_end.next=curr
                even_end=curr


        else:
            if odd_start is None:
                odd_start=odd_end=curr
            else:
                odd_end.next=curr
                odd_end=curr
        
        curr=new_node
    if even_start is None:
        mylist.start=odd_start
        return mylist
    even_end.next=odd_start
    mylist.start=even_start
    return mylist
mylist=sll()
mylist.insert_at_first(10)
mylist.insert_last(60)
mylist.insert_after(mylist.search(10),15)
mylist.insert_after(mylist.search(15),17)
mylist.insert_after(mylist.search(17),20)
mylist.print_list()
Segregate(mylist)
mylist.print_list()

        


