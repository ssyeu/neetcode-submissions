class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        answer = []
        while nums:
            temp = nums[0]
            for num in nums:
                if num < temp:
                    temp = num
            answer.append(nums.pop(nums.index(temp)))
        return answer