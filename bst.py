class Node:
    def __init__(self, item=None, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None

    # ---------------- INSERT ----------------
    def insert(self, root, data):
        if root is None:
            return Node(data)

        if data < root.item:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)

        return root

    # ---------------- SEARCH ----------------
    def search(self, root, data):
        if root is None or root.item == data:
            return root

        if data < root.item:
            return self.search(root.left, data)
        else:
            return self.search(root.right, data)

    # ---------------- MIN VALUE ----------------
    def min(self, root):
        current = root
        while current.left:
            current = current.left
        return current.item

    # ---------------- MAX VALUE ----------------
    def max(self, root):
        current = root
        while current.right:
            current = current.right
        return current.item

    # ---------------- INORDER ----------------
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.item, end=' ')
            self.inorder(root.right)

    # ---------------- PREORDER ----------------
    def preorder(self, root):
        if root:
            print(root.item, end=' ')
            self.preorder(root.left)
            self.preorder(root.right)

    # ---------------- POSTORDER ----------------
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.item, end=' ')

    # ---------------- DELETE ----------------
    def delete(self, root, data):
        if root is None:
            return root

        if data < root.item:
            root.left = self.delete(root.left, data)
        elif data > root.item:
            root.right = self.delete(root.right, data)
        else:
            # Case 1: No child
            if root.left is None and root.right is None:
                return None

            # Case 2: One child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Case 3: Two children
            successor_value = self.min(root.right)
            root.item = successor_value
            root.right = self.delete(root.right, successor_value)

        return root
bst = BST()

values = [50, 30, 20, 40, 70, 60, 80]
for v in values:
    bst.root = bst.insert(bst.root, v)

print("Inorder traversal:")
bst.inorder(bst.root)

print("\nPreorder traversal:")
bst.preorder(bst.root)

print("\nPostorder traversal:")
bst.postorder(bst.root)

print("\nMin value:", bst.min(bst.root))
print("Max value:", bst.max(bst.root))

print("Search 40:", bst.search(bst.root, 40) is not None)

bst.root = bst.delete(bst.root, 50)
print("Inorder after deleting 50:")
bst.inorder(bst.root)
