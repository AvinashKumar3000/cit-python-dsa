# LC_98 validate binary search tree

```python
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        result = []

        def inorder(node):
            if node == None:
                return
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
        inorder(root)

        if len(set(result)) != len(result):
            return False

        if result == sorted(result):
            return True
        else:
            return False
```
