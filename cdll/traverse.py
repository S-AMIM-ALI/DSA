#Traverse forward and backward.
from cdll import *
def Traverse(mycdll):
    if mycdll.start is None:
        return None
    temp=mycdll.start
    while temp:
        print(temp.item,end=" ")
        temp=temp.next
        if temp==mycdll.start:
            break
def Traverse_backward(mycdll):
    if mycdll.start is None:
        return None
    temp=mycdll.start.prev
    while temp:
        print(temp.item,end=" ")
        temp=temp.prev
        if temp==mycdll.start.prev:
            break
mycdll=cdll()
mycdll.insert_at_first(10)
mycdll.insert_after(10,20)
mycdll.insert_after(20,30)
mycdll.insert_at_last(40)
Traverse(mycdll)
print("\n")
Traverse_backward(mycdll)
    
       

