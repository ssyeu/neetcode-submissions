class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = min(strs)
        for word in strs:
            i = 0
            while i < len(ans) and i < len(word):
                if word[i] != ans[i]:
                    ans = ans[: i] 
                i += 1
        return ans     

              