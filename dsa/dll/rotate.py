# Rotate a DLL by k nodes
from q import dll,Node
def rotate(mylist,k):
    if mylist.start is None or k==0:
        return mylist
    item_count=0
    curr=mylist.start
    while curr.next:
        curr=curr.next
        item_count+=1

    length=item_count+1
    tail=curr
    tail.next=mylist.start
    mylist.prev=curr

    k=k%length
    curr=mylist.start

    for i in range(length-k-1):
        curr=curr.next
    mylist.start=curr.next
    curr.next.prev=None
    curr.next=None
    return mylist
mylist=dll()
mylist.insert_at_first(10)
mylist.insert_at_last(20)
mylist.insert_at_last(30)
mylist.insert_after(mylist.search(20),25)

#mylist.delete_first()
mylist.insert_at_first(21)

mylist.insert_after(mylist.search(21),22)


print("\n elements",mylist.print_list())
rotate(mylist,2)
print(mylist.print_list())


