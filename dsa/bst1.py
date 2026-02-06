class Node:
    def __init__(self,item=None,left=None,right=None):
        self.item=item
        self.left=left
        self.right=right
class BST:
    def __init__(self):
        self.root=None
    def insert(self,root,data):
        if root is None:
            return Node(data)
        if data<root.item:
            root.left=self.insert(root.left,data)
        else:
            root.right=self.insert(root.right,data)
        return root
    def search(self,root,data):
        if root is None or root.item==data:
            return root
        if data<root.item:
            return self.search(root.left,data)
        else:
            return self.search(root.right,data)
    def min_value(self,root):
        current=root
        while current.left is not None:
            current=current.left
        return current.item
    def max_value(self,root):
        current=root
        while current.right is not None:
            current=current.right
        return current.item
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.item,end=', ')
            self.inorder(root.right)
    def preorder(self,root):
        if root:
            print(root.item,end=', ')
            self.preorder(root.left)
            self.preorder(root.right)
    def postorder(self,root):
        if root:
            self.postorder(root.left)
            
            self.postorder(root.right)
            print(root.item,end=' ,')
    def delete(self,root,data):
        if root is None:
            return root
        if data<root.item:
            root.left=self.delete(root.left,data)
        elif data>root.item:
            root.right=self.delete(root.right,data)
        else:
            if root.left is None and root.right is None:
                return None
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            succ=self.max(root.left)
            root.item=succ
            root.left=self.delete(root.left,succ)
bst=BST()
values = [50, 30, 20, 40, 70, 60, 80]
for v in values:
    bst.root = bst.insert(bst.root, v)
bst.inorder(bst.root)
bst.preorder(bst.root)
bst.postorder(bst.root)
print(bst.min_value(bst.root))
bst.max_value(bst.root)
