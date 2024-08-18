# Medium

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            if not counts.get(n):
                counts[n] = 0
            counts[n] += 1
        most_frequent = sorted(counts.items(), key=lambda x: x[1])
        most_frequent.reverse()
        return [x for x,y in most_frequent[:k]]