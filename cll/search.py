from cll import Node,cll
# Count nodes in CLL.
# Search an element in CLL.
mylist=cll()
mylist.insert_at_first(10)
mylist.insert_after(15,10)
mylist.insert_after(25,15)
mylist.insert_at_last(40)
mylist.print_list()
result=mylist.search(15)
if result:
    print(f"element exist {result.item}")
else:
    print(f"element doesnt exist")
result=mylist.search(11)
if result:
    print(f"element exist {result.item}")
else:
    print(f"element doesnt exist")
print(len(mylist))

#Detect if a linked list is circular.
import sys
sys.path.append(r"D://pythoncodes//dsa") 
from sll.sll import Node,sll
def check_circular(mylist):
    first=mylist.last.next
    last=mylist.last
    if last.next==first:
        print("list is circular")
    else:
        print("not circular")
mylist=sll()
mylist.insert_at_first(10)
mylist.insert_after(mylist.search(10),12)
mylist.insert_after(mylist.search(12),13)
mylist.insert_last(15)
mylist.print_list()
check_circular(mylist)
