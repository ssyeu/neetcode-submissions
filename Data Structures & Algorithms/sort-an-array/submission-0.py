class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        answer = []
        for num in nums:
            i = 0
            if not answer:
                answer.append(num)
            else:
                while i < len(answer):
                    if num <= answer[i]:
                        answer.insert(i, num)
                        break
                    else:
                        i += 1
                if i == len(answer):
                    answer.append(num)
        return answer