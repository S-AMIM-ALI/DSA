#Flatten multiple circular linked lists.
class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class cll:
    def __init__(self,last=None):
        self.last=last
    def isempty(self):
        return self.last is None
    def insert(self,value):
        n=Node(value)
        if self.isempty():
            self.last=n 
            n.next=n 
        
        temp=self.last.next
        while temp.next!=self.last.next:
            temp=temp.next
        n.next=self.last.next
        temp.next=n 
        self.last=n

    def prints(self):
        curr=self.last.next
        while curr.next!=self.last.next:
            print(curr.item,end=' ')
            curr=curr.next
        print()
    def Flatten(l1,l2):
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
        new_head=tail.next
        self.last=new_head
        return new_head
            

    
l1=cll()
n=5
for i in range(1,n+1):
    l1.insert(i)
l1.prints()
l2=cll()
n=8
for i in range(n,1,-1):
    l2.insert(i)
l2.prints()
