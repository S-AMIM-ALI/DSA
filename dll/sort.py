#sort a dll
def sort(mylist):
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

mylist=dll()
mylist.insert_at_first(20)
mylist.insert_after(mylist.search(20),10)
mylist.insert_after(mylist.search(10),30)
mylist.insert_at_last(50)
mylist.print_list()
print("\n")
sort(mylist)
mylist.print_list()