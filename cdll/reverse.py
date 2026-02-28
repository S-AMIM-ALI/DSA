#Reverse a CDLL in-place.
from cdll import *
def Reverse(mycdll):
    if mycdll.start is None:
        return

    left = mycdll.start
    right = mycdll.start.prev

    while left != right and left.prev != right:
        left.item, right.item = right.item, left.item
        left = left.next
        right = right.prev
    
# def reverse(mycdll):
#     if mycdll.start is None:
#         return

#     temp = mycdll.start

#     while True:
#         temp.next, temp.prev = temp.prev, temp.next
#         temp = temp.prev   

#         if temp == mycdll.start:
#             break

   
#     mycdll.start = mycdll.start.next

    
mycdll=cdll()
mycdll.insert_at_first(10)
mycdll.insert_after(10,20)
mycdll.insert_after(20,30)
mycdll.insert_at_last(40)
mycdll.display()
print("\n")
Reverse(mycdll)
mycdll.display()
print("\n")
# reverse(mycdll)

        