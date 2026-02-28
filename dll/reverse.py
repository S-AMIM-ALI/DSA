# Reverse a doubly linked list
from q import dll

def reverse(mylist):
    current=mylist.start
    temp=None
    while current:
        temp=current.prev
        current.prev=current.next
        current.next=temp
        current=current.prev
    if temp:
        mylist.start=temp.prev





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
print("\nrevrse doubly linked list")
reverse(mylist)
print("\n elements",mylist.print_list())
