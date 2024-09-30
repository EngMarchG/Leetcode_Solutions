class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxi = 0
        ans = -1
        for i, num in enumerate(nums):
            if num > maxi:
                print(num)
                if num / (maxi+0.00001) < 1.99:
                    ans = -1
                else:
                    ans = i
                maxi = num
            elif maxi / (num+0.00001) < 1.99:
                ans = -1

        return ans