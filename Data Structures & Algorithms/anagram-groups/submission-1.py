class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = {}
        for word in strs:
            answer.setdefault("".join(sorted(word)), []).append(word)

        return list(answer.values())