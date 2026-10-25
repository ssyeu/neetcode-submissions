class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s) - 1
        rev = s.copy()
        while r > l:
            rev[l] = s[r]
            rev[r] = s[l]
            r -= 1
            l += 1
        s[:] = rev