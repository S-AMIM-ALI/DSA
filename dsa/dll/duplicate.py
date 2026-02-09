from q import dll,Node
# Remove duplicates from a sorted DLL
def sorted(mylist):
    if mylist.start is None or mylist.start.next is None:
        return mylist
    swapped=True
    while swapped:
        curr=mylist.start
        swapped=False
        while curr.next:
            
            if curr.item>curr.next.item:
                curr.item,curr.next.item=curr.next.item,curr.item
                swapped=True
            curr=curr.next
    return mylist
def remove_duplicate_sorted(mylist):
    curr=mylist.start
    while curr.next:
        if curr.item==curr.next.item:
            curr.next=curr.next.next
        curr=curr.next
    return mylist
#remove duplicates from unsorted dll
def unsorted_remove_duplicate(mylist):
    curr=mylist.start
    while curr.next:
        temp=curr
        while temp.next:
            if curr.item==temp.next.item:
                temp.next=temp.next.next
            temp=temp.next
        curr=curr.next
    return mylist    



mylist=dll()
mylist.insert_at_first(20)
mylist.insert_after(mylist.search(20),10)
mylist.insert_after(mylist.search(10),30)
mylist.insert_at_last(10)
mylist.insert_after(mylist.search(10),15)
mylist.print_list()
print('\n')
sorted(mylist)
mylist.print_list()
remove_duplicate_sorted(sorted(mylist))
print('\n')
mylist.print_list()


