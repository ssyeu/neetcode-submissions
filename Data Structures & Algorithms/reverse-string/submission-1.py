class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s) - 1
        while r > l:
            nl = s[r]
            nr = s[l]
            s[l] = nl
            s[r] = nr
            r -= 1
            l += 1