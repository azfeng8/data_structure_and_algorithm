# Hard

from typing import List

class MySolution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        counts = {}
        for n in nums:
            counts.setdefault(n, 0)
            counts[n] += 1

        diffs = {0: 0}    
        count_tuples = list((x,y) for x,y in counts.items())

        for i in range(len(count_tuples)):
            for j in range(i+1, len(count_tuples)):
                diff = abs(count_tuples[i][0] - count_tuples[j][0])
                diffs.setdefault(diff, 0)
                diffs[diff] += count_tuples[i][1] * count_tuples[j][1]
            if count_tuples[i][1] > 1:
                diffs[0] += count_tuples[i][1] * (count_tuples[i][1] - 1) / 2 

        sorted_diffs = sorted([(x,y ) for x,y in diffs.items()], key=lambda x: x[0])
        s = sum([x[1] for x in sorted_diffs])
        if s / 2 < k:
            count_backwards = s - k
            for val, count in sorted_diffs[::-1]:
                count_backwards -= count
                if count_backwards < 0:
                    return val
        else:
            for val, count in sorted_diffs:
                k -= count
                if k<=0:
                    return val