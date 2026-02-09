#sorting the sll 
from sll import sll,Node
def sort(mylist):
    if mylist.start is None or mylist.start.next is None:
        return mylist

    swapped=True
    while swapped:
        swapped=False
        current=mylist.start
        while current.next:
            if current.item>current.next.item:
                current.item,current.next.item=current.next.item,current.item
                swapped=True
            current=current.next
    return mylist
mylist=sll()
mylist.insert_at_first(10)
mylist.insert_last(20)
mylist.insert_after(mylist.search(20), 40)
mylist.insert_last(15)
mylist.insert_after(mylist.search(10),5)
mylist.print_list()
sort(mylist)
mylist.print_list()

        


    






