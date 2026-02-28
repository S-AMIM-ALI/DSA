from q import dll,Node 
# Merge two sorted DLLs
def merge(l1,l2):
    dummy=Node(None,0,None)
    tail=dummy
    p1=l1.start
    p2=l2.start
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
        p1=p1.next
    if p2:
        tail.next=p2
        p2.prev=tail
        p2=p2.next
        
    merge_list=dll()
    merge_list.start=dummy.next
    if merge_list.start:
        merge_list.start.prev=None
    return merge_list
l1=dll()
l2=dll()

l1.insert_at_first(10)
l1.insert_after(l1.search(10),30)
l1.insert_after(l1.search(30),50)
l1.insert_after(l1.search(50),70)
l1.print_list()
print("\n")
l2.insert_at_first(20)
l2.insert_after(l2.search(20),40)
l2.insert_after(l2.search(40),60)
l2.insert_after(l2.search(60),80)
l2.print_list()
print("\n")

merged=merge(l1,l2)
merged.print_list()




    
        

