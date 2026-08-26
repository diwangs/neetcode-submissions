"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sortedIntervals = sorted(intervals, key=lambda x:x.start)

        for i in range(1, len(sortedIntervals)):
            a = sortedIntervals[i-1]
            b = sortedIntervals[i]

            if a.end > b.start:
                return False

        return True