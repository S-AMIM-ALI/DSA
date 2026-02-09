from sll import sll,Node

def Rotate(mylist,k):
    curr=mylist.start
    item_count=0
    while curr.next:
        curr=curr.next
        item_count+=1
   

    length=item_count+1
    tail=curr
    
    k=k%length
    if k==0:
        return mylist
    
    tail.next=mylist.start
    curr=mylist.start
    for i in range(length-k-1):
        curr=curr.next

    mylist.start=curr.next
    curr.next=None
    return mylist
mylist = sll()

mylist.insert_at_first(10)
mylist.insert_last(20)
mylist.insert_after(mylist.search(20), 40)

mylist.print_list()      # 10 20 40

mylist.insert_after(mylist.search(40),50)      # 10 20
mylist.insert_after(mylist.search(50),60)

mylist.print_list() 
Rotate(mylist,2)
mylist.print_list() 


