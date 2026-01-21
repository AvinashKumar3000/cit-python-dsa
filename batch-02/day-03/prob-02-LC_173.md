# LC_173 BST Iterator

```python
class BSTIterator:

    def __init__(self, root):
        self.arr = []
        self.index = 0
        self.inorder(root)

    def inorder(self, node):
        if not node:
            return
        self.inorder(node.left)
        self.arr.append(node.val)
        self.inorder(node.right)

    def next(self):
        val = self.arr[self.index]
        self.index += 1
        return val

    def hasNext(self):
        return self.index < len(self.arr)

```
