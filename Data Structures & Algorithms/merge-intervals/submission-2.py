class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))
        
        result = []
        i = 1
        intervalBuffer = intervals[0]

        while i < len(intervals):
            if intervals[i][0] > intervalBuffer[1]:
                result.append(intervalBuffer[:])
                intervalBuffer = intervals[i]
            else:
                # intervalBuffer[0] = min(intervalBuffer[0], intervals[i][0])
                intervalBuffer[1] = max(intervalBuffer[1], intervals[i][1])

            i += 1

        result.append(intervalBuffer[:])
        return result
