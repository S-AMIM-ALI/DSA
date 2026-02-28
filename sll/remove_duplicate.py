from sll import sll,Node
#remove duplicate from sorted sll
def sorted(mylist):
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
def remove_sorted(mylists):
    curr=mylist.start
    while curr.next:
        if curr.item==curr.next.item:
            curr.next=curr.next.next
        curr=curr.next
    return mylist
#remove duplicate from unsorted sll
def remove_unsorted(mylist):
    if mylist.start is None or mylist.start.next is None:
        return mylist
    curr=mylist.start
    while curr.next:
        temp=curr
        while temp.next:
            if temp.next.item==curr.item:
                temp.next=temp.next.next
            else:
                temp=temp.next
        curr=curr.next
    return mylist


mylist=sll()
mylist.insert_at_first(10)
mylist.insert_last(20)
mylist.insert_after(mylist.search(20), 40)
mylist.insert_after(mylist.search(40),10)
mylist.insert_last(15)
mylist.insert_after(mylist.search(10),5)
mylist.print_list()
# sorted(mylist)
# mylist.print_list()
# remove_sorted(sorted(mylist))
remove_unsorted(mylist)
mylist.print_list()

            

