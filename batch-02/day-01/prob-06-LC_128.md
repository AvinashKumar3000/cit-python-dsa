```python
class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        # Step 1: Create hashmap
        num_dict = {}
        for num in nums:
            num_dict[num] = True  # mark presence

        longest = 0

        # Step 2: iterate through keys
        for num in num_dict:
            # start sequence only if no left neighbor
            if num - 1 not in num_dict:
                current = num
                length = 1

                # expand sequence
                while current + 1 in num_dict:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest

```