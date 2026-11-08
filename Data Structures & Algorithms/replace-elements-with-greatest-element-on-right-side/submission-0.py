class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l = 0
        answer = []
        while l < len(arr) - 1:
            answer.append(max(arr[l + 1:]))
            l += 1
        answer.append(-1)
        return answer 