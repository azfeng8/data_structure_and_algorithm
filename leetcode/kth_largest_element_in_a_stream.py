# Easy
from typing import List

class MySolution:

    def __init__(self, k: int, nums: List[int]):
        
        self.k = k
        self.kth_largest_idx = None
        self.nums = sorted(nums)

    def add(self, val: int) -> int:
        if len(self.nums) > 0:
            self.binary_search_insert(val)
        else:
            self.nums.append(val)

        # Get the Kth largest
        if len(self.nums) < self.k:
            return None
        else:
            return self.nums[-self.k]

    def binary_search_insert(self, val: int) -> int:
       # binary search on self.nums to insert: find the element directly to the left
        i = (len(self.nums)-1) // 2
        low = 0
        high = len(self.nums) - 1
        go1 = val >= self.nums[i] if i >= 0 else True
        go2 = val <= self.nums[i + 1] if i < len(self.nums) - 1 else True
        go = go1 and go2
        while not go:
            if self.nums[i] >= val:
                high = i
                i = (i + low) / 2
                # Clip
                i = int(i)
            else:
                low = i
                i = (i + high) / 2
                # Round up
                i = int(i) + 1
            if i > 0:
                go1 = val >= self.nums[i]
            else:
                go1 = True
            if i < len(self.nums) -1:
                go2 = val <= self.nums[i + 1]
            else:
                go2 = True
            go = go1 and go2

        if i == len(self.nums) - 1:
            if (self.nums[i] > val):
                self.nums.insert(max(0, i-1), val)
            else:
                self.nums.insert(i+1, val)
        elif i == 0:
            if (self.nums[i] > val):
                self.nums.insert(0, val)
            else:
                self.nums.insert(i+1, val)
        else:
            self.nums.insert(i+1, val)

# Best solution
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for n in nums:
            heapq.heappush(n) 
        self.heap = self.heap[len(nums) - k:]
    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)
        return self.heap[0]
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)