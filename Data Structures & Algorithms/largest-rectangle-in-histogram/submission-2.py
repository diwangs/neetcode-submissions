class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        result = 0
        stack = []

        for i in range(len(heights) + 1): # sentinel element where heights == 0
            while stack and (i == len(heights) or heights[i] < heights[stack[-1]]):
                height = heights[stack.pop()]
                width = (i - 1) - stack[-1] if stack else i
                result = max(result, height * width)
            stack.append(i)

        return result
        