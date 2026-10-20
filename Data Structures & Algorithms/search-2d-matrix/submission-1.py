class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        exists = any(target in sublist for sublist in matrix)
        return exists