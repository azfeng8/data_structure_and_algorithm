# Easy

class MySolution:
    # Runtime O(n**2) and space O(n) where n is the number of times called to the sum of squared digits; this call is O(m) with m being number of digits.
    #: O(n) to search if the number is in the set, at the time when the size of the set is n. Sum of squares 1^2, 2^2, 3^2 ... is O(n^2).
    def isHappy(self, n: int) -> bool:
        cycle = set()
        num = n
        while num not in cycle:
            if num == 1:
                return True 
            cycle.add(num)
            num = int(sum((int(i)**2) for i in str(num)))
        return False

# Floyd's Slow/Fast Two pointers solution:
# Worse runtime for better space complexity. O(n) and O(1)

class Solution:
    def sum(self, n: int):
        return sum(int(i)**2 for i in str(n))
    def isHappy(self, n: int) -> bool:
        slow, fast = self.sum(n), self.sum(self.sum(n))
        
        while slow != fast:
            slow = self.sum(slow)
            fast = self.sum(self.sum(fast))
        return fast == 1