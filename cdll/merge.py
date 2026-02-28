from palindrom import *
def merge(l1,l2):
    if l1.start is None:
        return l1
    if l2.start is None:
        return l2
    last1=l1.start.prev
    last2=l2.start.prev

    last1.next=None
    last2.next=None

    l1.start.prev=None
    l2.start.prev=None
    
    p1=l1.start
    p2=l2.start

    if p1.item<=p2.item:
        head=p1
        p1=p1.next
    else:
        head=p2
        p2=p2.next
    tail=head
    tail.prev=None
    while p1 and p2:
        if p1.item<=p2.item:
            tail.next=p1
            p1.prev=tail
            p1=p1.next
        else:
            tail.next=p2
            p2.prev=tail
            p2=p2.next
        tail=tail.next
    if p1:
        tail.next=p1
        p1.prev=tail
    if p2:
        tail.next=p2
        p2.prev=tail
    while tail.next:
        tail=tail.next
    head.prev=tail
    tail.next=head
    l1.start=head
    return l1

    

mycdll=cdll()
l1=cdll()
l2=cdll()
n=int(input("enter no of nodes you want to insert"))
for i in range(1,n+1):
    l1.insert(i)
l1.display()
print("\n")
n=int(input("enter no of nodes you want to insert"))
for i in range(n,n+n,1):
    l2.insert(i)
l2.display()
print("\n")
merged = merge(l1, l2)
print("Merged list:")
merged.display()