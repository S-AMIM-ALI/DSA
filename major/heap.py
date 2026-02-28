class Heap:
    def __init__(self):
        self.heap=[]
    def creatheap(self,list1):
        for e in list1:
            self.insert(e)
    def insert(self,e):
        index=len(self.heap)
        parentindex=(index-1)//2
        while index>0 and self.heap[parentindex]<e:
            if index==len(self.heap):
                self.heap.append(self.heap[parentindex])
            else:
                self.heap[index]=self.heap[parentindex]
            index=parentindex
            parentindex=(index-1)//2
        if index==len(self.heap):
            self.heap.append(e)
        else:
            self.heap[index]=e
    def top(self):
        if len(self.heap)==0:
            raise EmptyHeapException()
        return self.heap[0]
    def heapsort(self,list1):
        self.creatheap(list1)
        list2=[]
        try:
            while True:
                list2.insert(0,self.delete())
        except EmptyHeapException:

            pass
        return list2
    def delete(self):
        if len(self.heap)==0:
            raise EmptyHeapException()
        if len(self.heap)==1:
            return self.heap.pop()
        max_value=self.heap[0]
        temp=self.heap.pop()
        index=0
        leftchildindex=2*index+1
        rightchildindex=2*index+2
        while leftchildindex<len(self.heap):
            if rightchildindex<len(self.heap):
                if self.heap[leftchildindex]>self.heap[rightchildindex]:
                    if self.heap[leftchildindex]>temp:
                        self.heap[index]=self.heap[leftchildindex]
                        index=leftchildindex
                    else:
                        break
                else:
                    if self.heap[rightchildindex]>temp:
                        self.heap[index]=self.heap[rightchildindex]
                        index=rightchildindex
                    else:
                        break
            else:
                if self.heap[leftchildindex]>temp:
                    self.heap[index]=self.heap[leftchildindex]
                    index=leftchildindex
                else:
        
                    break
            leftchildindex=2*index+1
            rightchildindex=2*index+2
        self.heap[index]=temp
        return max_value
class EmptyHeapException(Exception):
    def __init__(self,msg='empty heap'):
        self.msg=msg
    def __str__(self):
        return self.msg

    
h = Heap()

# Create heap from list
h.creatheap([10, 5, 20, 1, 15])
print("Heap:", h.heap)

# Insert new element
h.insert(25)
print("Heap after inserting 25:", h.heap)

# Top element
print("Max element:", h.top())

# Delete max element
print("Deleted max:", h.delete())
print("Heap after deletion:", h.heap)

# Heap sort
print("Heap sort:", h.heapsort([10, 5, 20, 1, 15]))
