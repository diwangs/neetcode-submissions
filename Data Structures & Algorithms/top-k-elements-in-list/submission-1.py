class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        freq = [[] for _ in range(len(nums) + 1)]
        for num, cnt in count.items():
            freq[cnt].append(num)

        # Flatten the freq matrix
        result = []
        for f in range(len(freq) - 1, 0, -1):
            for num in freq[f]:
                result.append(num)
                if len(result) == k:
                    return result
        