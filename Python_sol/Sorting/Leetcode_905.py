class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = []
        odd = []

        for num in nums:
            if num % 2:
                odd.append(num)
            else:
                even.append(num)
        
        return sorted(even) + sorted(odd, reverse=True)