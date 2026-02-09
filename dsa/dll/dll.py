class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next
class dll:
    def __init__(self,start=None):
        self.start=start
    def isempty(self):
        return self.start is None
    def insert_at_first(self,data):
        n=Node(None,data,self.start)
        if not self.isempty():
            self.start.prev=n
        self.start=n
    def insert_at_last(self,data):
        n=Node(temp,data,None)
        if self.isempty():
            self.start=n
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=n
            n.prev=temp
    def insert_after(self,temp,data):
        if temp is not None:
        n=Node(temp,data,temp.next)
        if temp.next is not None:
            temp.next.prev=n
        temp.next=n
    def search(self,data):
       temp=self.start
       while temp is not None:
           if temp.item == data:
               return temp
           temp=temp.next
       return None
    def print_list(self):
       temp=self.start
       while temp is not None:
           print(temp.item,end=' ')
           temp=temp.next
           print()     

    def delete_first(self):
        if self.start is not None:
            self.start=self.start.next
            if self.start is not None:
                self.start.prev=None

    def delete_last(self):
        if self.start is None:
           pass
        elif self.start.next is not None:
            self.start=None
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.prev.next=None
    def delete_item(self,data):
        temp=self.start
        while temp is  not None:
            if temp.item==data:
                if temp.prev:
                    temp.prev.next=temp.next
                else:
                    self.start=temp.next
            if temp.next:
                temp.next.prev=temp.prev
                return
            temp=temp.next
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
        self.current=self.current.item
        return data
mylist=dll()
mylist.insert_at_first(10)
mylist.insert_at_last(20)
mylist.insert_at_last(30)
mylist.insert_after(mylist.search(20),25)
