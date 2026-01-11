# LC_144 pre    order

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   def preorderTraversal(self, root) -> List[int]:
      if root == None:
         return []
      result = []
      stack = [root]
      while len(stack) != 0:
         curr = stack.pop()
         result.append(curr.val)

         if curr.right:
            stack.append(curr.right)
         if curr.left:
            stack.append(curr.left)

      return result
```
