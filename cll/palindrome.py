#Check if CLL is palindrome.
from cll import *
def palindrome(mylist):
    if mylist.last is None:
        return None
    temp=mylist.last.next
    result=[]
    while True:

        result.append(temp.item)
        temp=temp.next
        if temp!=mylist.last.next:
            break
    print("if list is palindrome", result==result[::-1])

mylist=cll()
mylist.insert_at_first(10)
mylist.insert_after(10,20)
mylist.insert_after(20,30)
mylist.insert_after(30,20)
mylist.insert_at_last(10)
mylist.print_list()
palindrome(mylist)