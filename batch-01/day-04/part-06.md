# LC_100 same tree

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p, q) -> bool:
        
        def inorder(n1, n2):
            if n1 == None and n2 == None:
                return True
            if n1 == None or n2 == None:  
                # if any of them is None
                # other one is not none, 
                return False
            
            left_result = inorder(n1.left, n2.left)
            if n1.val != n2.val:
                return False
            right_result = inorder(n1.right, n2.right)

            if left_result and right_result:
                return True
            else:
                return False

        return inorder(p,q)
```
