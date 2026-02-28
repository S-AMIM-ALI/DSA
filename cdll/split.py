#Split CDLL into two halves.
from cdll import *
def halves(mycdll):
    head1=mycdll.start
    slow=mycdll.start
    fast=mycdll.start
    while fast.next!=mycdll.start and fast.next.next!=mycdll.start:
        slow=slow.next
        fast=fast.next.next
    head2=slow.next
    if fast.next.next==mycdll.start:
        fast=fast.next
    slow.next=head1
    head1.prev=slow

    fast.next=head2
    head2.prev=fast

    return head1,head2



mycdll=cdll()
mycdll.insert_at_first(10)
mycdll.insert_after(10,20)
mycdll.insert_after(20,30)
mycdll.insert_at_last(40)
mycdll.display()
print("\n")
h1,h2=halves(mycdll)
print("First half:")
mycdll.start = h1
mycdll.display()
print("\n")
print("Second half:")
mycdll.start = h2
mycdll.display()



    
