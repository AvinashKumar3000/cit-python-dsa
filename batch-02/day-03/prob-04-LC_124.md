# LC_124 Binary Tree Max Path Sum

```python
class Solution:
    def maxPathSum(self, root):
        max_sum = float('-inf')

        def dfs(node):
            nonlocal max_sum
            if not node:
                return 0

            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)

            curr_path_sum = node.val + left_gain + right_gain
            max_sum = max(max_sum, curr_path_sum)

            return node.val + max(left_gain, right_gain)

        dfs(root)
        return max_sum

```
