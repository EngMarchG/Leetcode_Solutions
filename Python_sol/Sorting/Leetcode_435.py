class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        pointer = 1
        temp = popped = 0
        while pointer+temp < len(intervals):
            if intervals[pointer-1][1] > intervals[pointer+temp][0]:
                temp += 1
                if intervals[pointer-1][1]<=intervals[pointer+temp-1][1]:
                    continue

            pointer += temp + 1
            popped += temp
            temp = 0

        return popped+temp