class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        result = 0
        stack = []

        for i in range(len(heights) + 1): # sentinel element where heights == 0
            while stack and (i == len(heights) or heights[stack[-1]] >= heights[i]):
                height = heights[stack.pop()]
                width = i - stack[-1] - 1 if stack else i
                result = max(result, height * width)
            stack.append(i)

        return result
        