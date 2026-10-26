class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a, b = 0, 0
        result = ""
        while a <= len(word1) - 1 and b <= len(word2) - 1:
            result += word1[a]
            result += word2[b]
            a += 1
            b += 1
        result += word1[a:]
        result += word2[b:]
        return result

