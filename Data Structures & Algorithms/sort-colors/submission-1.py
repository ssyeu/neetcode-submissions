class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        amount = Counter(nums)
        i = 0
        while i < len(nums):
            if amount[0] > 0:
                nums[i] = 0
                amount[0] -= 1
            elif amount[1] > 0:
                nums[i] = 1
                amount[1] -= 1
            else:
                nums[i] = 2
                amount[2] -= 1
            i += 1