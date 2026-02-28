#Find length of loop in circular list.
from cll import *
def length_of_loop(mylist):
    temp=mylist.last.next
    start=temp
    item_count=1
    while temp.next!=start:
        temp=temp.next
        item_count+=1
    return item_count
mylist=cll()
mylist.insert_at_first(10)
mylist.insert_after(10,20)
mylist.insert_after(20,30)
mylist.insert_after(30,40)
mylist.insert_after(40,60)
mylist.insert_at_last(50)
mylist.print_list()
print("\n")
print(length_of_loop(mylist))

