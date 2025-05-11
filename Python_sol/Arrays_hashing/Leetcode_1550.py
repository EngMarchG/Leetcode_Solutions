class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        counter = 0

        for num in arr:
            if num % 2 == 0:
                counter = 0
            else:
                counter += 1
            
            if counter == 3:
                return True
        
        return False