# Kth largest ele

```python
class Solution:
    def findKthLargest(self, nums, k):
        nums.sort()
        return nums[-k]
```

```python
class Solution:
    def findKthLargest(self, nums, k):

        def merge_sort(arr):
            # Base case
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            return merge(left, right)

        def merge(left, right):
            merged = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            # Append remaining elements
            while i < len(left):
                merged.append(left[i])
                i += 1

            while j < len(right):
                merged.append(right[j])
                j += 1

            return merged

        # Sort using merge sort
        sorted_nums = merge_sort(nums)

        # kth largest
        return sorted_nums[-k]

```

```python
class Solution:
    def findKthLargest(self, nums, k):
        OFFSET = 10000
        freq = [0] * 20001   # fixed range

        for num in nums:
            freq[num + OFFSET] += 1

        for i in range(20000, -1, -1):
            k = k - freq[i]
            if k <= 0:
                return i - OFFSET

```