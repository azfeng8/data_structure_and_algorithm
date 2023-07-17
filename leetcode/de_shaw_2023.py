# Real code interview questions from D.E. Shaw: https://leetcode.com/discuss/interview-question/3769522/de-shaw-online-test-2023

# (no aid)
def Problem1_Solution(a, m):
    """Problem 1. Max length of subsequence with a special sum less than max sum"""
    n = len(a)
    def smallest_k(k):
        weighted_tuples = [(a[i], a[i] + i * k, i) for i in range(n)]
        weighted_tuples = sorted(weighted_tuples, key = lambda t: t[1])
        return sum((i[1] for i in weighted_tuples[:k])), weighted_tuples[:k]
    k = n//2
    converged = False
    left_ptr = (None, None) # subseq length, subseq:list of weighted tuples
    right_ptr = (None, None)
    while True:
        if left_ptr[0] is not None and right_ptr[0] is not None:
            converged = (right_ptr[0] == (left_ptr[0] + 1))

        if converged:
            return left_ptr[0]
        sum_, subseq = smallest_k(k)

        if sum_ <= m:
            if k == n:
                return k
            left_ptr = (k, subseq)
            k = (n + k + 1) // 2
        else:
            right_ptr = (k, subseq)
            if left_ptr is not None:
                k = left_ptr[0] + 1
            k = (k+1) // 2

import math
# Similar to #120
class Problem2_Solution():
    """Max weight path from top to bottom of triangle (array of arrays of increasing length)"""
    def maxTotal(self, arr):
        M = len(arr)
        N = int((-1 + math.sqrt(1+8*M)) / 2) # from M = (N+1)*N/2 and N has integer soln
        for i in range(N-2, -1, -1):
            for j in range(i+1):
                arr[int((i+1)*i/2) + j] += max(arr[int((i+1)*(i+2) / 2) + j], arr[int((i+1)*(i+2) / 2 + j+1)])
        return arr[0]
        
def Problem3_Solution(a, cost, k):
    """Divide array into subarrays to incur least total cost"""
    n = len(a)
    def divideSubarrays(i):
        if i == n:
            return (0,0) # total_cost, sum over (sum of cost[i] ... cost[j]) for each subarray
        prefix_sum = sum(a[:i])
        c = 0
        res = []
        for j in range(i, n - (i==0)): # the problem asks for "multiple" subarrays, so that's for the (n-(i==0))
            c += cost[j]
            prefix_sum += a[j]
            sub_arr_tc = (prefix_sum + k*1) * c

            forward_cost, costs_sum = divideSubarrays(j+1)
            res.append((sub_arr_tc + forward_cost + costs_sum * k, c + costs_sum)) # costs_sum * k is correction factor for moving subarray indices up by 1
        return min(res, key=lambda t: t[0])
    return divideSubarrays(0)[0]

a = [4,3,2,1]
m = 33
s = Problem1_Solution(a,m)
assert(s == 3)

test = [2, 3, 4, 6, 5, 7, 4, 1, 8, 3]
res = (Problem2_Solution().maxTotal(test))
print(res)
assert(res == 21)

res3 = Problem3_Solution([3,1,4],[2,3,3],1)
print(res3)
assert(res3 == 55)