class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x = (coordinates[1][1]-coordinates[0][1])
        y = (coordinates[1][0]-coordinates[0][0])
        for i in range(1, len(coordinates)):
            if x * (coordinates[i][0]-coordinates[i-1][0]) != y * (coordinates[i][1]-coordinates[i-1][1]):
                return False
        return True