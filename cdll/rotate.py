class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next

class cdll:
    def __init__(self, start=None):
        self.start = start

    def isempty(self):
        return self.start is None

    def insert(self, value):
        n = Node(item=value)
        if self.isempty():
            n.next = n.prev = n
            self.start = n
        else:
            current = self.start
            while current.next != self.start:
                current = current.next
            n.next = self.start
            self.start.prev = n
            current.next = n
            n.prev = current

    def display(self):
        if self.start is None:
            return None
        first = self.start
        while True:
            print(first.item, end=" ")
            first = first.next
            if first == self.start:
                break

    def Rotate(self, k):
        if self.start is None:
            return None

        # Count nodes
        count = 1
        temp = self.start
        while temp.next != self.start:
            count += 1
            temp = temp.next

        # Reduce unnecessary rotations
        k = k % count
        if k == 0:
            return self.start.item

        # Move start pointer k times
        for _ in range(k):
            self.start = self.start.next

        return self.start.item

# --- Testing ---
mycdll = cdll()
n = int(input("Enter number of nodes: "))
for _ in range(n):
    mycdll.insert(int(input("Enter node value: "))) 

print("Original list:")
mycdll.display()
print("\n")

k = int(input("Enter number of rotations: "))
print("New start element is:", mycdll.Rotate(k))
print("Rotated list:")
mycdll.display()