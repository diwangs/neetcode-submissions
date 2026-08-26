class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [-num for num in nums]
        heapq.heapify(self.heap)
        self.k = k
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, -val)

        buff = []
        for i in range(self.k - 1):
            buff.append(heapq.heappop(self.heap))
        result = self.heap[0]
        for num in buff:
            heapq.heappush(self.heap, num)

        return -result
        
