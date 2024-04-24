class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        pointer = 1
        temp_min = intervals[0][0]
        temp_max = intervals[0][1]
        ans = []

        while pointer < len(intervals):
            if intervals[pointer][0] <= temp_max:
                temp_max = max(temp_max, intervals[pointer][1])
            else:
                ans.append([temp_min, temp_max])
                temp_min = intervals[pointer][0]
                temp_max = intervals[pointer][1]
            pointer += 1

        ans.append([temp_min, temp_max])

        return ans