# LC_234  palindrome

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        li = []

        curr = head
        while curr:
            li.append(curr.val)
            curr = curr.next
        
        return li==li[::-1]
```
