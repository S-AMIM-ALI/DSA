# Implement a Doubly Linked List from scratch
# (insert at head/tail, delete node, traverse both ways)
class Node:
    def __init__(self,prev,item,next):
        self.prev=prev
        self.item=item
        self.next=next
class dll:
    def __init__(self):
        self.start=None
        self.item_count=0
    def isempty(self):
        return self.start is None
    def insert_at_first(self,data):
        n=Node(None,data,self.start)
        if not self.isempty() :
            self.start.prev=n
        self.start=n
        #print('\nelements is inserted ',data)
        self.item_count+=1
    def insert_at_last(self,data):
        if self.isempty():
            self.start=Node(None,data,None)
        else:
            temp=self.start
            while temp.next:
                temp=temp.next
            temp.next=Node(temp,data,None)
        self.item_count+=1
        #print(f"\nelements{data} is inserted at last")
    def insert_after(self,temp,data):
        
        if temp :
            n=Node(temp,data,temp.next)
            if temp.next :
                temp.next.prev=n
            temp.next=n
        self.item_count+=1
        #print(f"\nelements{data} is inserted after{temp.item}")
    def search(self,data):
        temp=self.start
        while temp:
            if temp.item==data:
                return temp
            temp=temp.next
        return None
    def print_list(self):
        temp=self.start
        while temp:
            print(temp.item,end=' ')
            temp=temp.next
    def delete_first(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None
        else:
            self.start=self.start.next
            self.start.prev=None
        self.item_count-=1
        #print(f"\nelements{self.start.item} is deleted at first")
    def delete_last(self):
        if self.isempty():
            pass
        elif self.start.next is None:
            self.start=None
        else:
            temp=self.start
            while temp.next.next:
                temp=temp.next
            temp.next=None
        self.item_count-=1
        #print(f"\nelements{temp.item} is deleted at last")
    def delete_item(self,data):
        temp =self.start
        while temp:
            new_node=temp.next
            if temp.item==data:
                if temp.prev:
                    if temp.next:
                        temp.prev.next=temp.next
                        temp.next.prev=temp.prev
                    else:
                        temp.prev.next=None   
                else:
                    self.start=temp.next
                    if self.start:
                        self.start.prev=None
            temp=new_node
        self.item_count-=1
        #print(f"\nelements{data} is deleted ")
    def __iter__(self):
        return dlliterator(self.start)
class dlliterator:
    def __init__(self,start):
        self.current=start
    def __iter__(self):
        return self
    def __next__(self):
        if self.current is None:
            raise StopIteration
        data=self.current.item
        self.current=self.current.next
        return data
# mylist=dll()
# mylist.insert_at_first(10)
# mylist.insert_at_last(20)
# mylist.insert_at_last(30)
# mylist.insert_after(mylist.search(20),25)
# print("\n elements",mylist.print_list())
# #mylist.delete_first()
# mylist.insert_at_first(21)
# print("\n elements",mylist.print_list())
# mylist.insert_after(mylist.search(21),22)
# print("\n elements",mylist.print_list())
# mylist.insert_at_last(55)
# print("\n elements",mylist.print_list())
# #mylist.delete_item(21)
# print("no of elements in list is ",mylist.item_count)
# #mylist.print_list()






            
    


    

        

            













# Pointer Manipulation (very common)

# 