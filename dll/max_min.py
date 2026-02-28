from q import dll,Node
def max_min(mylist):
    if mylist.start is None:
        return None,None
        
    temp=mylist.start
    maximum=minimum=mylist.start.item
    while temp:
        if temp.item>maximum:
            maximum=temp.item
        elif temp.item<minimum:
            minimum=temp.item
        
        temp=temp.next
    return maximum,minimum


    

        
mylist=dll()
mylist.insert_at_first(10)
mylist.insert_after(mylist.search(10),50)
mylist.insert_at_last(5)
mylist.insert_after(mylist.search(50),14)
mylist.insert_at_last(19)
mylist.print_list()

max,min=max_min(mylist)
print(f"maximum element is {max}")
print(f"maximum element is {min}")