from cdll import *
def delete(mycdll,node):
    temp=mycdll.search(node)
    if temp==mycdll.start:
       temp.next.prev=temp.prev
       temp.prev.next=temp.next
       self.start=temp.next
       
    else:
        temp.prev.next=temp.next
        temp.next.prev=temp.prev
mycdll=cdll()
mycdll.insert_at_first(10)
mycdll.insert_after(10,20)
mycdll.insert_after(20,30)
mycdll.insert_after(30,40)
mycdll.insert_at_last(50)
mycdll.display()
delete(mycdll,20)
print("\n")
mycdll.display()