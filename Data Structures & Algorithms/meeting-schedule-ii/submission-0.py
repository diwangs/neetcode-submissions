"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        combined = []
        for interval in intervals:
            combined.append((interval.start, 1))
            combined.append((interval.end, -1))

        combined.sort()

        countActiveJob = 0
        maxBuff = 0

        for event in combined:
            countActiveJob += event[1]
            maxBuff = max(maxBuff, countActiveJob)

        return maxBuff
            
                

            
