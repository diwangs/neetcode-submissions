class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        edfIntervals = sorted(intervals, key=lambda x: x[1])
        count = 0
        prevEnd = edfIntervals[0][1]

        for i in range(1, len(edfIntervals)):
            # Conflict
            if prevEnd > edfIntervals[i][0]:
                count += 1
            # No conflict, advance prevEnd
            else:
                prevEnd = edfIntervals[i][1]

        return count