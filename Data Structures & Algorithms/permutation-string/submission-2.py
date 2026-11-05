class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = l + len(s1)
        set1 = dict(Counter(s1))
        while r <= len(s2):
            r = l + len(s1)
            set2 = dict(Counter(s2[l:r]))
            if set1 == set2:
                return True
            l += 1
        return False


                
        