class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        x, y, z = 0, 0, 0
        temp1 = nums1[:m]
        temp2 = nums2[:n]
        while x < m and y < n:
            if temp1[x] <= temp2[y]:
                nums1[z] = temp1[x]
                x += 1
                z += 1
            else:
                nums1[z] = temp2[y]
                y += 1
                z += 1
        while x < m:
            nums1[z] = temp1[x]
            x += 1
            z += 1
        while y < n:
            nums1[z] = temp2[y]
            y += 1
            z += 1
        