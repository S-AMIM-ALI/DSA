#Insert a node before / after a given node
from q import dll,Node
def insert_before(mylist,before,val):
    if before:
        n=Node(before.prev,val,before)
        if before.prev is None:
            mylist.start=n 
        else:
            before.prev.next=n
        before.prev=n

mylist=dll()
mylist.insert_at_first(10)
mylist.insert_at_last(20)
mylist.insert_at_last(30)
mylist.insert_after(mylist.search(20),25)

#mylist.delete_first()
mylist.insert_at_first(21)
mylist.print_list()
print('\n')
mylist.insert_after(mylist.search(21),22)
mylist.print_list()
print('\n')
insert_before(mylist,mylist.search(25),23)
mylist.print_list()
    
        



