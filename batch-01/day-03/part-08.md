# LC_203  remove item of match value

```python
class Solution:
    def removeElements(self, head, val):
      if head == None:
         return head

      while head and head.val == val:
         head = head.next

      curr = head
      
      while curr and curr.next:
         if curr.next.val == val:
            curr.next = curr.next.next
         else:   
            curr = curr.next
      return head
```
