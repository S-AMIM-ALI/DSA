
# Detect a loop (cycle) in a linked list
# 👉 Floyd’s Cycle Detection Algorithm
# Remove a loop from a linked list

from sll import sll,Node
def findloop(self):
    slow=self.start
    fast=self.start
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            break
    else:
        print("no loop detected")
    
    ## Find the starting point of a loop
    slow=self.start
    while slow!=fast:
        slow=slow.next
        fast=fast.next
    print("loop start here",slow.item)
    return slow
mylist=sll()
mylist.findloop()




# Find the Nth node from the end

def Nth(self,n):
    fast=self.start
    slow=self.start
    for i in range(n):
        fast=fast.next
    while fast:
        fast=fast.next
        slow=slow.next
    return slow.item
    
# Find the Nth node from the start
def nth(self,n):
    slow=self.start
    for i in range(n):
       slow=slow.next
    return slow.item



# Check if a linked list is a palindrome
def palindrome(self):
    #first is to calculate middle of list
    slow=self.start
    fast=self.start
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    #now reverse list from middle
    current=slow
    prev=None
    while current:
        nxt=current.next
        current.next=prev
        prev=current
        current=nxt
    first=self.start
    second=prev
    while second:
        if first.item != second.item:
            return False:
        first=first.next
        second=second.next
    return True


# Merge two sorted singly linked lists
def merge(l1,l2):
    dummy=Node(0)
    tail=dummy
    p1=l1.start
    p2=l2.start
    while p1 and p2:
        if p1.item <= p2.item:
            tail.next=p1
            p1=p1.next
        else:
            tail.next=p2
            p2=p2.next
        tail=tail.next
    if p1:
        tail.next=p1
        p1=p1.next
    if p2:
        tail.next=p2
        p2=p2.next
    
    merge.start=dummy.next
    return merge



# Delete the middle node
def  delete_middle(self):
    if self.start is None or self.start.next is None:
        self.start=None
        return 
    slow=self.start
    fast=self.start
    prev=None
    while fast and fast.next:
        prev=slow
        slow=slow.next
        fast=fast.next.next
    prev.next=slow.next
    
    

# Count occurrences of a given element
def count(self,element):
    if self.start is None:
        return False
       
    slow=self.start
    count=0
    while slow :
        if slow.item==element:
            count+=1
        slow=slow.next
    return count

# 🔹 Advanced (Product-Based Companies)

# Asked by Amazon, Microsoft, Google, Flipkart, Uber, etc.

# Reverse nodes in groups of K

# Add two numbers represented by linked lists
def add_sll(self,l1,l2):
        dummy=Node(0)
        curr=dummy
        carry=0
    while l1 or l2 or carry:
        v1=l1.item if l1 else 0
        v2=l2.item if l2 else 0
        total=v1+v2+carry
        carry=total//10
        curr.next=Node(total %10)
        curr=curr.next
        l1=l1.next if l1 else 0
        l2=l2.next if l2 else 0
    return dummy.next
# Flatten a linked list (child pointers / multilevel lists)

# Clone a linked list with random pointer

# Rotate a linked list by K positions

# Segregate even and odd nodes

# Intersection point of two linked lists

# Sort a linked list using Merge Sort

# Delete nodes having greater value on right side

# Convert a linked list to a balanced BST
