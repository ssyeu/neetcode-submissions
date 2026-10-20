class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        j = len(matrix) - 1
        while i <= j:
            m = (i + j) // 2
            if target < matrix[m][0]:
                j = m - 1
            elif target > matrix[m][0]:
                i = m + 1
            elif target == matrix[m][0]:
                return True
        l = 0
        r = len(matrix[m]) - 1
        while l <= r:
            x = (l + r) // 2
            if target < matrix[j][x]:
                r = x - 1
            elif target > matrix[j][x]:
                l = x + 1
            else:
                return True
        return False