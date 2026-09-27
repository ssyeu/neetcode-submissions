class Solution:
    def isValid(self, s: str) -> bool:
        seen = []
        pairs = {")":"(", "}":"{", "]":"["}
        for char in s:
            if char in pairs:
                if seen and pairs[char] == seen[-1]:
                    seen.pop()
                else:
                    return False
            else:
                seen.append(char)
        return len(seen) == 0