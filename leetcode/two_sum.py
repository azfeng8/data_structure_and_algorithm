# Easy

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(n) runtime solution with O(n) space
        good = {}
        for i, n in enumerate(nums):
            if n in good:
                return [i, good[n]]
            good[target-n]= i