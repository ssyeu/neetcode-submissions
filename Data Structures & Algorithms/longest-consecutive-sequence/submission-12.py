class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        answer = 0
        numsy = set(nums)
        for num in numsy:
            if num - 1 not in numsy:
                i = 0
                while num + i in numsy:
                    i += 1
                if i > answer:
                    answer = i
        return answer