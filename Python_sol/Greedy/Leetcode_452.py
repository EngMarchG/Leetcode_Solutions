class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # Consider a big time line with subsets inside it
        # When you encounter a smaller subset you have to shoot a ballon at its end
        # In order to ensure it is popped
        
        # Time complexity O(N + N) Space complexity O(1)
        count = 1
        points = sorted(points)
        
        end = 0
        start = 0
        while end < len(points):
            if points[start][1] < points[end][0]:
                count += 1
                start = end
            elif points[start][1] > points[end][1]:
                start = end
            end += 1
        return count