class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        answer = set()
        result = 0
        for letter in s:
            if letter in answer:
                while letter in answer:
                    answer.remove(s[l])
                    l += 1
            answer.add(letter)
            if len(answer) > result:
                result = len(answer)
        return result