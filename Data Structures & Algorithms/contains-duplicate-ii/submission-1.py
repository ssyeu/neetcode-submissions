class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0
        j = len(nums) - 1
        while i <= j:
            for x, val in enumerate(nums):
                if x != i and val == nums[i]:
                    if abs(i - x) <= k:
                        return True
            i += 1
        else:
            return False