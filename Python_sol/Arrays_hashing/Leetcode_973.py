class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        k_points = [[0,0]]*len(points)
        
        for i, num in enumerate(points):
            k_points[i] = [num[0]**2 + num[1]**2, i]

        k_points.sort()
        k_points = k_points[:k]

        for i in range(len(k_points)):
            k_points[i] = points[k_points[i][1]]

        return k_points