# Count nodes in a DLL
from q import dll
def count(mylist):
    item_count=0
    current=mylist.start
    while current:
        current=current.next
        item_count+=1
    print("no of elements in dll is",item_count)
mylist=dll()
mylist.insert_at_first(10)
mylist.insert_at_last(20)
mylist.insert_at_last(30)
mylist.insert_after(mylist.search(20),25)

#mylist.delete_first()
mylist.insert_at_first(21)

mylist.insert_after(mylist.search(21),22)


print("\n elements",mylist.print_list())
#mylist.delete_item(21)
count(mylist)
