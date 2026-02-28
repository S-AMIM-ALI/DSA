#Delete all occurrences of a given value
from q import dll

def delete_occurance(mylist, value):
    temp = mylist.start
    delete_count = 0

    while temp:
        next_node = temp.next   # save next before deletion

        if temp.item == value:
            # deleting first node
            if temp.prev is None:
                mylist.start = temp.next
                if mylist.start:
                    mylist.start.prev = None
            # deleting middle or last node
            else:
                if temp.next:
                    temp.next.prev = temp.prev
                temp.prev.next = temp.next

            mylist.item_count -= 1
            delete_count += 1

        temp = next_node

    print(f"{delete_count} is number of occurrences of {value}")

mylist=dll()
mylist.insert_at_first(10)
mylist.insert_at_last(20)
mylist.insert_at_last(30)
mylist.insert_after(mylist.search(20),25)
mylist.insert_after(mylist.search(25),10)
mylist.insert_after(mylist.search(30),10)

#mylist.delete_first()
mylist.insert_at_first(21)

mylist.insert_after(mylist.search(21),22)        
mylist.print_list()
print("\n")
delete_occurance(mylist,10)
mylist.print_list()




    


