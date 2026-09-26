class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        sorted_counts = counts.most_common()
        return [num for num, count in sorted_counts[:k]]