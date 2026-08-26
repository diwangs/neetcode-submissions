class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)

            diff = abs(stone1 - stone2)
            if diff > 0:
                heapq.heappush(stones, -diff)

        if len(stones) > 0:
            return -stones[0]
        else:
            return 0
