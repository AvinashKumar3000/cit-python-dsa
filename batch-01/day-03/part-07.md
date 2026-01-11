# LC_142  cycle 2

```python
class Solution:
	def detectCycle(self, head):
		slow = head
		fast = head

		is_cycle = False

		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next
			if slow == fast:
				is_cycle = True
				break
		
		if not is_cycle:
			return None

		slow = head
		while slow != fast:
			slow = slow.next
			fast = fast.next

		return slow
```
