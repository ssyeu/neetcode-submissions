class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        x, y = len(word1) - 1, len(word2) - 1
        a, b = 0, 0
        result = ""
        while a <= x and b <= y:
            result += word1[a]
            result += word2[b]
            a += 1
            b += 1
        if x > y:
            while a <= x:
                result += word1[a]
                a += 1
        elif y > x:
            while b <= y:
                result += word2[b]
                b += 1
        return result

