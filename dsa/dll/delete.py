# Delete a node at a given position

from q import dll
def delete_at_pos(mylist,position):
    current=mylist.start
    if current is None:
        return {'list is empty'}
    elif position<0 or mylist.item_count<position:
        return {'invalid position'}
    else:
        if position==0:
            current=current.next
            if current:
                current.prev=None
            mylist.item_count-=1
            print(f"{current.item} elment")
        else:
            temp=mylist.start
            for i in range(position):
                temp=temp.next
            deleted=temp.item
            if temp.next:
                temp.next.prev=temp.prev
            temp.prev.next=temp.next
            print(f"{deleted} element ")
        mylist.item_count-=1
mylist=dll()
mylist.insert_at_first(10)
mylist.insert_at_last(20)
mylist.insert_at_last(30)
mylist.insert_after(mylist.search(20),25)

#mylist.delete_first()
mylist.insert_at_first(21)

mylist.insert_after(mylist.search(21),22)


print("\n elements",mylist.print_list())
delete_at_pos(mylist,4)

print("\n elements",mylist.print_list())

    

