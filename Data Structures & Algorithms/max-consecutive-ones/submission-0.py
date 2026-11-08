class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        answer = 0
        temp = 0
        for num in nums:
            if num == 1:
                temp += 1
            else:
                if temp > answer:
                    answer = temp
                temp = 0
        if temp > answer:
                    answer = temp
        return answer