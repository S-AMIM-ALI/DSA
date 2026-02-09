# Search an element in a DLL
from q import dll
def search(mylist,element):
    current=mylist.start
    while current:
        if current.item==element:
            print("element found ",element)
        current=current.next
    
mylist=dll()
mylist.insert_at_first(10)
mylist.insert_at_last(20)
mylist.insert_at_last(30)
mylist.insert_after(mylist.search(20),25)

#mylist.delete_first()
mylist.insert_at_first(21)

mylist.insert_after(mylist.search(21),22)


print("\n elements",mylist.print_list())
search(mylist,22)