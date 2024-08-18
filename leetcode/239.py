from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Intuitive solution that gets TLE
        # res = []
        # for i in range(0, len(nums) + 1 - k):
        #     res.append(max([nums[j] for j in range(i, i + k)]))
        # return res

        # Use a deque to maintain monotonically nonincreasing window of values
        # the deque tracks indices of the values
        res = []
        dq = deque()
        # initialize the window
        for i in range(0, k):
            # I also made a mistake here, dq[0] and dq.popleft().
            # If I did this, there could be lingering values on the right
            # b/c I was checking with the largest value first, instead of checking and removing increasingly larger values
            while len(dq) != 0 and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)
        # first number from initialized window
        res.append(nums[dq[0]])
        # shift the window
        for i in range(k, len(nums)):
            if dq[0] + k == i:
                dq.popleft()
            # This insight I missed: when find a largest value,
            # don't need to keep track of any previous values.
            # I thought may need to always keep track of top 2 values
            while len(dq) != 0 and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            res.append(nums[dq[0]])
        return res