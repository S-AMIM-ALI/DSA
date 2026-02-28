#Merge two circular linked lists.
from cll import *

def merge_cll(l1,l2):
    head1=l1.last.next
    head2=l2.last.next

    l1.last.next=None
    l2.last.next=None

    dummy=Node(0)
    tail=dummy

    while head1 and head2:
        if head1.item<=head2.item:
            tail.next=head1
            head1=head1.next
        else:
            tail.next=head2
            head2=head2.next
        tail=tail.next
    if head1:
        tail.next=head1
    if head2:
        tail.next=head2

    new_head=dummy.next
    temp=new_head
    while temp.next:
        temp=temp.next
    temp.next=new_head
    l1.last=temp
    return l1




l1=cll()
print("l1 list elements")
l1.insert_at_first(10)
l1.insert_after(10,30)
l1.insert_after(30,50)
l1.insert_after(50,70)
l1.print_list()


l2=cll()
print("l2 list elements")
l2.insert_at_first(20)
l2.insert_after(20,40)
l2.insert_after(40,60)
l2.insert_after(60,80)
l2.print_list()

print("\n")
merge=merge_cll(l1,l2)
merge.print_list()