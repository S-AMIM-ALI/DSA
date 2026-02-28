# Find the middle of a DLL
from q import dll
def middle(mylist):
    slow=mylist.start
    fast=mylist.start
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    print("middle elements is ",slow.item)


mylist=dll()
mylist.insert_at_first(10)
mylist.insert_at_last(20)
mylist.insert_at_last(30)
mylist.insert_after(mylist.search(20),25)

#mylist.delete_first()
mylist.insert_at_first(21)

mylist.insert_after(mylist.search(21),22)

mylist.insert_at_last(55)
print("\n elements",mylist.print_list())
#mylist.delete_item(21)
print("no of elements in list is ",mylist.item_count)

middle(mylist)