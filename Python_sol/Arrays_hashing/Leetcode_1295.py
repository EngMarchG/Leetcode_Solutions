class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        arr = [10**i for i in range(7)]
        for num in nums:
            for i in range(6):
                if arr[i] <= num < arr[i+1]:
                    if not (i+1) % 2:
                        ans += 1
                    break
        return ans
            