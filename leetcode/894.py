"""894. All possible binary trees."""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 1st iteration: No memoization (no aid)

# 2nd iteration (hint: comment to use DP, so I memoized it)
class Solution(object):
    def allPossibleFBT(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def subtree(n, memo={}):
            if n in memo: return memo[n]
            trees = []
            if n == 1:
                trees =  [TreeNode()]
            else:
                trees = []
                for m in range(1, n-1, 2):
                    left_candidates = subtree(m, memo)
                    right_candidates = subtree(n - 1 - m, memo)
                    trees.extend(comb(left_candidates, right_candidates))
                memo[n] = trees
            return trees
        def comb(l, r):
            res = []
            for l_elt in l:
                for r_elt in r:
                    res.append(TreeNode(val=0, left=l_elt, right=r_elt))
            return res
        return subtree(n)

# Using memo as class static member rather than pass into the function (hint: from top solution)
class Solution(object):
    memo = {0: [], 1: [TreeNode()]}
    def allPossibleFBT(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def subtree(n):
            if n in Solution.memo: return Solution.memo[n]
            trees = []
            for m in range(1, n-1, 2):
                l = subtree(m)
                r = subtree(n - 1 - m)
                for l_elt in l:
                    for r_elt in r:
                        trees.append(TreeNode(val=0, left=l_elt, right=r_elt))
            Solution.memo[n] = trees
            return trees
        return subtree(n)