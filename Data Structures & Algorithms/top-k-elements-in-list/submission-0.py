class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        return [x[0] for x in sorted(count.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)][:k]
        