class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        answer = r
        while l <= r:
            m = (l + r) // 2
            total = 0
            for pile in piles:
                total += -(-pile // m)
            if h >= total:
                answer = m
                r = m - 1  
            elif h < total:
                l = m + 1
        return answer