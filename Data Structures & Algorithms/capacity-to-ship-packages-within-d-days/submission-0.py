class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        i = max(weights)
        j = sum(weights)
        answer = sum(weights)
        while i <= j:

            m = (i + j) // 2

            total = 0
            d = 1
            l = 0

            while l < len(weights):
                total += weights[l]
                if total <= m:
                    l += 1
                elif total > m:
                    d += 1
                    total = 0

            if days >= d:
                j = m - 1
                answer = m
            else:
                i = m + 1
        return answer
                
                