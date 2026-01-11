# LC_19   Remove n th node from linked list

```python
class Solution:
    def removeNthFromEnd(self, head, n):
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next

        if count == n:
            head = head.next

        curr = head
        while curr:
            if count==n+1:
                curr.next = curr.next.next
                break
            curr = curr.next
            count -= 1
        return head
```
