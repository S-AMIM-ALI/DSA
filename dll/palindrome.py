from q import dll,Node
#check whether given list is palindrome or not
def palindrome(mylist):
    if mylist.start is None or mylist.start.next is None:
        return mylist

    left=mylist.start
    right=mylist.start
    while right.next:
        right=right.next
   
    while left != right and left.prev!=right:
        if left.item!= right.item:
            print("list is not palindorm")
            return False
        left=left.next
        right=right.prev
    print("list is palindrome")
    return True

    
    
mylist=dll()
mylist.insert_at_first(10)
mylist.insert_after(mylist.search(10),20)
mylist.insert_after(mylist.search(20),30)
mylist.insert_after(mylist.search(30),20)
mylist.insert_at_last(10)
# mylist.insert_at_last(15)
mylist.print_list()
print('\n')
palindrome(mylist)
#mylist.print_list()





