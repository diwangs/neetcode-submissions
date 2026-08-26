class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tempStack = []
        result = [0] * len(temperatures)
        
        for idx, temp in enumerate(temperatures):
            while len(tempStack) > 0 and temp > tempStack[-1][1]:
                sIdx, _ = tempStack.pop()
                result[sIdx] = idx - sIdx
            tempStack.append((idx, temp))

        return result
