"""120. Triangle: Min weight path top to bottom of array of arrays of increasing length"""

# My solution using memoization (no aid).
class Solution(object):

    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        M = len(triangle)
        def dfs_visit(m,n, memo={}):
            if (m,n) in memo: return memo[(m,n)]
            if m == M - 1:
                weight = triangle[m][n]
                memo[(m,n)] = weight
            else:
                weight = triangle[m][n] + min(dfs_visit(m+1,n, memo), dfs_visit(m+1,n+1, memo))
                memo[(m,n)] = weight
            return weight

        return dfs_visit(0, 0)

# hint: use tabulation form of DP
class Solution_Opt(object):
    """Tabulation bottom-up"""
    def minimumTotal(self, triangle):
        for i in range(len(triangle) - 2, -1, -1): # start on penultimate row
            for j in range(i+1):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]
    def maximumTotal(self, triangle):
        for i in range(len(triangle) - 2, -1, -1): # start on penultimate row
            for j in range(i+1):
                triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]

# hint: use tabulation form of DP
class Solution_Opt2(object):
    """Tabulation top-down"""
    def minimumTotal(self, triangle):
        for i in range(len(triangle)):
            if i == 0: continue # start on 2nd row
            for j in range(len(triangle[i])):
                if j == len(triangle[i]) - 1:
                    triangle[i][j] += triangle[i-1][j-1]
                elif j == 0:
                    triangle[i][j] += triangle[i-1][j]
                else:
                    triangle[i][j] += min(triangle[i-1][j], triangle[i-1][j-1])
        return min(triangle[-1])

print(Solution().minimumTotal([[-10]]))
print(Solution_Opt().maximumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))