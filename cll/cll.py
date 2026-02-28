class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class cll:
    def __init__(self):
        self.last=None
        self.item_count=0

    def isempty(self):
        return self.last is None

    def insert_at_first(self,data):
        n=Node(data)
        if self.last is None:
            self.last=n
            n.next=n
        else:
            n.next=self.last.next
            self.last.next=n
        self.item_count+=1

    def insert_at_last(self,data):
        n=Node(data)
        if self.last is None:
            self.last=n
            n.next=n  
        else:
            n.next=self.last.next
            self.last.next=n
            self.last=n
        self.item_count+=1

    def search(self,data):
        if self.last is None:
            return None
        temp=self.last.next
        while True:
            if temp.item==data:
                return temp
            temp=temp.next
            if temp==self.last.next:
                break
        return None

    def insert_after(self,data,value):
        temp=self.search(data)
        if temp:
            n=Node(value,temp.next)
            temp.next=n
            if temp==self.last:
                self.last=n
        self.item_count+=1

    def delete_first(self):
        if self.last is None:
            return
        elif self.last==self.last.next:
            self.last=None
        else:
            self.last.next=self.last.next.next
        self.item_count-=1

    def delete_last(self):
        if self.last is None:
            return
        elif self.last==self.last.next:
            self.last=None
            return
        
        temp=self.last.next
        while temp.next!=self.last:
            temp=temp.next
        
        temp.next=self.last.next
        self.last=temp
        self.item_count-=1

    def delete_item(self,data):
        if self.last is None:
            return
        
        temp=self.last.next
        prev=self.last
        
        while True:
            if temp.item==data:
                if temp==self.last and temp.next==self.last:
                    self.last=None
                    return
                elif temp==self.last:
                    prev.next=temp.next
                    self.last=prev
                    return
                else:
                    prev.next=temp.next
                    return
            
            prev=temp
            temp=temp.next
            if temp==self.last.next:
                break
        self.item_count-=1

    def print_list(self):
        if self.last is None:
            return
        
        temp=self.last.next
        while True:
            print(temp.item,end=' ')
            temp=temp.next
            if temp==self.last.next:
                break
        print()
    def __len__(self):
        return self.item_count
mylist = cll()

# mylist.insert_at_first(5)
# mylist.insert_after(10, 5)
# mylist.insert_at_last(20)
# mylist.insert_after(15, 10)

# mylist.print_list()      # 10 15 5 20

# mylist.delete_first()
# mylist.print_list()      # 15 5 20

# mylist.delete_last()
# mylist.print_list()      # 15 5

# mylist.delete_item(5)
# mylist.print_list()      # 15
