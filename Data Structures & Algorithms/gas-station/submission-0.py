class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1

        total = 0
        result = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]

            # Reset if running total is negative
            if total < 0:
                total = 0
                result = i + 1

        return result