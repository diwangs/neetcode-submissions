class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        edfIntervals = sorted(intervals, key=lambda x: x[1])
        removed = set()
        for i in range(len(edfIntervals)):
            for j in range(i+1, len(edfIntervals)):
                if not i in removed and edfIntervals[i][1] > edfIntervals[j][0]:
                    removed.add(j)

        return len(removed)