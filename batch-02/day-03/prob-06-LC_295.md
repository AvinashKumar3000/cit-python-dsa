# LC_295 Find Median from Data Stream


```python
class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        self.arr.sort()
        n = len(self.arr)

        if n % 2 == 1:
            return self.arr[n // 2]
        else:
            return (self.arr[n // 2 - 1] + self.arr[n // 2]) / 2

```

```python
import heapq

class MedianFinder:

    def __init__(self):
        self.min_heap = []  # Max heap (store negative values)
        self.max_heap = []  # Min heap

    def addNum(self, num: int) -> None:
        # Step 1: Add to max heap (small)
        heapq.heappush(self.min_heap, -num)

        # Step 2: Move largest of small to large heap
        heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

        # Step 3: Balance sizes
        if len(self.max_heap) > len(self.min_heap):
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

    def findMedian(self) -> float:
    
        if len(self.min_heap) > len(self.max_heap):
            return -self.min_heap[0]
        else:
            return (-self.min_heap[0] + self.max_heap[0]) / 2

```
