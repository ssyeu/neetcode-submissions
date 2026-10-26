class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while len(set(nums)) != len(nums):
            if nums[i] == nums[i + 1]:
                nums.pop(i)
            else:
                i += 1
        return len(set(nums))
