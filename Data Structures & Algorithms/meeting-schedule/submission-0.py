"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        curr_time = 0
        intervals.sort(key=lambda interval: (interval.start, interval.end))
        for interval in intervals:
            if interval.start < curr_time:
                return False
            else:
                curr_time = interval.end
        return True
