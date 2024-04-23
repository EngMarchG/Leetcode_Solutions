class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Time complexity O(m+n) Space complexity O(1)
        for i in range(len(matrix)):
            if target <= matrix[i][-1]:
                if target in matrix[i]:
                    return True
                return False

"""Better Solution
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        
        # Time complexity O(m + logN) Space complexity O(1)
        while row < len(matrix):
            if matrix[row][-1] >= target:
                break
            else:
                row += 1
        if row >= len(matrix):
            return False
        
        left = 0
        right = len(matrix[0])
        while left < right:
            mid = int((left + right)/2)
            
            if matrix[row][mid] == target:
                return True
            
            elif matrix[row][mid] > target:
                right = mid 
            
            else:
                left = mid + 1
"""

"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[0] > target:
                break
            if row[-1] < target:
                continue

            for num in row:
                if target == num:
                    return 1

                if num > target:
                    return 0
            
            return 0
"""