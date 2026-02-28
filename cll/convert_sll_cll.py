#Convert a normal singly list into circular list.
import sys
sys.path.append(r"D://pythoncodes//dsa") 
from sll.sll import Node,sll
def convert(mylist):
    first=mylist.start
    if first is None:
            return None
        
    while first.next is not None:
            first=first.next
    first.next=mylist.start
    
    return mylist.start
def prints(mylist):
    first=mylist.start
    if first is None:
        return None
    temp=first
    while True:
        print(temp.item,end="->")
        temp=temp.next
        if temp==first:
            break
    print("\n")
    print("back to start")


mylist=sll()
mylist.insert_at_first(10)
mylist.insert_after(mylist.search(10),20)
mylist.insert_after(mylist.search(20),30)
mylist.insert_after(mylist.search(30),40)
mylist.insert_last(50)
mylist.print_list()
convert(mylist)
print("after sll to cll")
prints(mylist)


